import colorama
from colorama import Fore
import os
import time

colorama.init()

print(Fore.RED + """

 /$$$$$$ /$$$$$$$        /$$$$$$$  /$$$$$$ /$$   /$$  /$$$$$$  /$$$$$$$$ /$$$$$$$ 
|_  $$_/| $$__  $$      | $$__  $$|_  $$_/| $$$ | $$ /$$__  $$| $$_____/| $$__  $$
  | $$  | $$  \ $$      | $$  \ $$  | $$  | $$$$| $$| $$  \__/| $$      | $$  \ $$
  | $$  | $$$$$$$/      | $$$$$$$/  | $$  | $$ $$ $$| $$ /$$$$| $$$$$   | $$$$$$$/
  | $$  | $$____/       | $$____/   | $$  | $$  $$$$| $$|_  $$| $$__/   | $$__  $$
  | $$  | $$            | $$        | $$  | $$\  $$$| $$  \ $$| $$      | $$  \ $$
 /$$$$$$| $$            | $$       /$$$$$$| $$ \  $$|  $$$$$$/| $$$$$$$$| $$  | $$
|______/|__/            |__/      |______/|__/  \__/ \______/ |________/|__/  |__/
                                                                                  
                                                                                  
                                                                                  
""")

# os.system('cls')

def ping():
    while True:
        ping_response = os.system(f'ping -n 1 {IP} > nul')
        if ping_response == 0:
            print(logo)
            time.sleep(0.1)
        else:
            print(logo)
            time.sleep(0.1)

print(logo)
IP = input('Enter IP: ')
ping()
