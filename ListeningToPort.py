import asyncio
from JihadLibrary import JihadLibrary
import socket
from subprocess import check_output

# Main function
async def main():
    JihadLibrary().copyRight()
    ip = "localhost"
    port = JihadLibrary().port()
    print(ip,port)
    print("____________________________________________")
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s = JihadLibrary().connectToSocket(socket, ip, port)
    #     JihadLibrary().listeningToPort(s)
    check_output("ncat -nvlp " + str(port), shell=True)
    print("____________________________________________")

# Calling the main function
asyncio.run(main())