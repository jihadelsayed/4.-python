import os
import struct
os.system('color')


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
        #s.send(bytes(buffer + "\r\n", "latin-1"))
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
        while True:
            seeMore = input(colors.WARNING + "Receive more(y/n)(default:n): " + colors.END) or "n"
            if seeMore =="y":
                print(colors.WARNING + "Received: " + colors.END)
                data = s.recv(1024)
                data = data.decode()
                print(f"{colors.OkCyan}       {data} {colors.END}")
                time.sleep(0.5)
            else:
                break

    def sendToSocket(self,s,message):
        #s.send(message)
        isString = isinstance(message, str)
        if isString:
            s.sendall(message.encode('ascii'))
        else:
            s.send(message)
        print(colors.OkGreen + "This message:" + message + "\n has been send successfully" + colors.END)
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

        eIP = input("enter the EIP(1234567A): ") or "0x31704330"
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
        isAllRandom =  input("is all the character are random (yes): ") or "yes"
        if isAllRandom == "yes":
            payload = JihadLibrary().createPattern(totalCharacter) 
        else:
            payload = (character * totalCharacter).encode('ascii') 
               
        return payload, totalCharacter
    def generateMessage(self,payload):
        payload = input(colors.WARNING + "What is your message(default:anonymessage): " + colors.END) or "anonymessage"
        return payload
    
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
