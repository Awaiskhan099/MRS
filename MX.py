#coding=utf-8
import sys,time
from platform import uname
from os import path,system
arch=uname().machine.lower()
if "aarch" in arch:
    arch="aarch"
    print('\033[1;32m\nCongratulatings! Your Deviec Support This Tools');time.sleep(1)
else:
    print('\033[1;31m\nSorry System not support this tools');sys.exit()

try:
    if sys.argv[1]=='update':
        system('cd $HOME && cd AKING && rm -f *')
        system("curl -L https://raw.githubusercontent.com/AKING110/AKING/main/AKING.py -o AKING.py && python AKING.py")
except:
    pass
   
banner=("""\033[1;37m    β€οΈπ₯Ί

[+]βββββββββββββββββββββββββββββββββββββββββ
[+] Author    : RAMZAM-TALHAπ³π
[+] Github    : AKING110
[+] Facebook  : IMTIAZ.FUCK
[+] Tool Type : FREE
[+] Version   : 1.3.6
[+] this massage for haters : \033[1;31mjust feel me π₯
\033[1;37m[+]βββββββββββββββββββββββββββββββββββββββββ""")

def main():
    if path.isfile("dz.so"):
        pass
    else:
        system("curl -L https://raw.githubusercontent.com/AKING110/Data/main/dz.so -o dz.so")
    system('clear')
    print(banner)
    print('[1] Version : 1.3.6\n[2] Version : 1.3.5\n[3] Version : 1.3.4\n[4] Random Cloning\n\033[1;37m[+]βββββββββββββββββββββββββββββββββββββββββ')
    vs=input('[β’] Choice : ')
    if vs in ['1','01']:
        if path.isfile('AKING.so'):
            import AKING
        else:
            system("curl -L https://raw.githubusercontent.com/AKING110/Data/main/AKING.so -o AKING.so")
            import AKING
    elif vs in ['2','02']:
        if path.isfile("File.so"):
            import File
        else:
            system("curl -L https://raw.githubusercontent.com/AKING110/Data/main/File.so -o File.so")
            import File
    elif vs in ['3','03']:
        if path.isfile("AKINGG.so"):
            import AKINGG
        else:
            system("curl -L https://raw.githubusercontent.com/AKING110/Data/main/AKINGG.so -o AKINGG.so")
            import AKINGG
   
    elif vs in ['4','04']:
        if path.isfile("Rndm.so"):
            import Rndm
        else:
            system("curl -L https://raw.githubusercontent.com/AKING110/Data/main/Rndm.so -o Rndm.so")
            import Rndm
    else:
        if path.isfile("AKING.so"):
            import AKING
        else:
            system("curl -L https://raw.githubusercontent.com/AKING110/Data/main/AKING.so -o AKING.so")
            import AKING
main()
