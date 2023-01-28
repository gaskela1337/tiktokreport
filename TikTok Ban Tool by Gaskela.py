import requests
from requests.sessions import session
import json
import time
import colorama
from colorama import Fore, Back, Style

colorama.init()

session = requests.session()

print(Fore.RED + """ 
  ▄████  ▄▄▄        ██████  ██ ▄█▀▓█████  ██▓     ▄▄▄         
 ██▒ ▀█▒▒████▄    ▒██    ▒  ██▄█▒ ▓█   ▀ ▓██▒    ▒████▄       
▒██░▄▄▄░▒██  ▀█▄  ░ ▓██▄   ▓███▄░ ▒███   ▒██░    ▒██  ▀█▄     
░▓█  ██▓░██▄▄▄▄██   ▒   ██▒▓██ █▄ ▒▓█  ▄ ▒██░    ░██▄▄▄▄██    
░▒▓███▀▒ ▓█   ▓██▒▒██████▒▒▒██▒ █▄░▒████▒░██████▒ ▓█   ▓██▒   
 ░▒   ▒  ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░▓  ░ ▒▒   ▓▒█░   
  ░   ░   ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒ ▒░ ░ ░  ░░ ░ ▒  ░  ▒   ▒▒ ░   
░ ░   ░   ░   ▒   ░  ░  ░  ░ ░░ ░    ░     ░ ░     ░   ▒      
      ░       ░  ░      ░  ░  ░      ░  ░    ░  ░      ░  ░   
                                                                    ░                                                             """
      )
print("")
print("")
print("Gaskela TikTok Ban Tool | @gasiich instagram <3")

print("")
print("")

x = input('Report Link: ')
print("")
print("")

print('brrrrrrr reportanje krece.....')
print('')
print('')

while True:
  req = session.post(x)

  print(req.text)
  print('ufff :D')

  time.sleep(1)

input()










































































##### all credits to @gasiich!