import colorama
from colorama import Fore
import os
import time

logo = f"""
{Fore.RED}       IP Pinger
{Fore.RED}       This shit needs a better logo        
"""

os.system('cls')

def ping():
    while True:
        ping_response = os.system(f'ping -n 1 {IP} >null')
        if ping_response == 0:
            os.system('cls')
            print(logo)
            time.sleep(0.1)
        else:
            os.system('cls')
            print(logo)
            time.sleep(0.1)

os.system('😎')

print(logo)
IP = input('Enter IP : ')
ping() # really simple
