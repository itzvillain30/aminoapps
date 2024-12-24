_A='info.json'
import os
os.system('pip install pycryptodome')
os.system('pip install requests')
os.system('pip install tqdm')
os.system('pip install colorama')
os.system('pip install websockets')
os.system('pip install websocket-client==1.3.1')
os.system('pip install json_minify')
try:os.system('pip install aiohttp')
except:pass
os.system('cls'if os.name=='nt'else'clear')
from colorama import Fore
from json import load
from json import dump
data=load(open(_A))
print(Fore.GREEN+'INSTALLATION DONE OF ALL REQUIRED PYTHON PACKAGE')
print(Fore.RED+"CHOOSE A OPTION \n1.YES, I HAVE A KEY \n2.NO, I DON'T HAVEA KEY")
ch=int(input(Fore.GREEN+'ENTER A OPTION HERE : '))
if ch==1:
	key=input(Fore.GREEN+'ENTER KEY HERE : ');data['keys']=key
	with open(_A,'w')as file:dump(data,file,indent=4)
	os.system('cls'if os.name=='nt'else'clear');print(Fore.GREEN+'KEY IS ADDED SUCESSFULLY !!');print(Fore.CYAN+'YOUR SCRIPT IS READY TO USE NOW !!')
else:print(Fore.CYAN+'YOUR SCRIPT IS READY TO USE NOW BUT YOU NEED KEY FOR THE SCRIPT FROM OWNER')
