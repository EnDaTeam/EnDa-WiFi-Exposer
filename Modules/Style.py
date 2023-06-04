#Import needed modules
try:
    import os
    from colorama import Fore
    from pystyle import Colors,Colorate
    import sys
    import time
    from pyfiglet import *
    import art
    import random
    import socket
except:
    raise ModuleNotFoundError("Please install all needed modules!")

#Define an space function (enter)
def enter(lines=1):
    for i in range(lines):
        print("")

#Define a clearconsole function
def clearConsole():
    command = "clear"
    if os.name in ("dos","nt"):
        command = "cls"
    os.system(command)

#Define a slow printing function
def slowPrint(text:str,times=0.2):
    for i in text + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(times)

#Define an error output 
def error(text:str,option:int=1,slowprinting:bool=False):
    try:
        int(option)
    except:
        raise ValueError("The option from error function is not an integer! [ENDA CAPP]")
    if slowprinting:
        if int(option) == 1:
            slowprinting(Fore.RED + "[ERROR]" + Fore.WHITE + " >> " + Fore.LIGHTRED_EX + str(text) + Fore.RESET)
        elif int(option) == 2:
            slowPrint(Fore.RED + "ERROR" + Fore.WHITE + " >> " + Fore.LIGHTRED_EX + str(text) + Fore.RESET)
        elif int(option) == 3:
            slowPrint(Fore.RED + """       
    ▒█▀▀▀ █▀▀█ █▀▀█ █▀▀█ █▀▀█ 
    ▒█▀▀▀ █▄▄▀ █▄▄▀ █░░█ █▄▄▀ 
    ▒█▄▄▄ ▀░▀▀ ▀░▀▀ ▀▀▀▀ ▀░▀▀
            """ + Fore.LIGHTRED_EX)
            enter()
            slowPrint(str(text) + Fore.RESET) 
        elif int(option) == 4:
            slowPrint(Colorate.Horizontal(Colors.white_to_red,"""
        (    (        )   (     
        )\ ) )\ )  ( /(   )\ )  
    (   (()/((()/(  )\()) (()/(  
    )\   /(_))/(_))((_)\   /(_)) 
    ((_) (_)) (_))    ((_) (_))   
    | __|| _ \| _ \  / _ \ | _ \  
    | _| |   /|   / | (_) ||   /  
    |___||_|_\|_|_\  \___/ |_|_\                                                                  
        """,1 + Fore.LIGHTRED_EX))
            enter()
            slowPrint(str(text) + Fore.RESET) 
        elif int(option) == 5:
            slowPrint(Colorate.Horizontal(Colors.white_to_red,r"""
    ___ ___ ___  ___  ___ 
    | __| _ \ _ \/ _ \| _ \
    | _||   /   / (_) |   /
    |___|_|_\_|_\\___/|_|_\                                                          
        """, 1))
            enter()
            slowPrint(str(text) + Fore.RESET) 
    else:
        if int(option) == 1:
            print(Fore.RED + "[ERROR]" + Fore.WHITE + " >> " + Fore.LIGHTRED_EX + str(text) + Fore.RESET)
        elif int(option) == 2:
            print(Fore.RED + "ERROR" + Fore.WHITE + " >> " + Fore.LIGHTRED_EX + str(text) + Fore.RESET)
        elif int(option) == 3:
            print(Fore.RED + """       
    ▒█▀▀▀ █▀▀█ █▀▀█ █▀▀█ █▀▀█ 
    ▒█▀▀▀ █▄▄▀ █▄▄▀ █░░█ █▄▄▀ 
    ▒█▄▄▄ ▀░▀▀ ▀░▀▀ ▀▀▀▀ ▀░▀▀
            """ + Fore.LIGHTRED_EX)
            enter()
            print(str(text) + Fore.RESET)
        elif int(option) == 4:
            print(Colorate.Horizontal(Colors.white_to_red,"""
      (    (        )   (     
      )\ ) )\ )  ( /(   )\ )  
     (   (()/((()/(  )\()) (()/(  
     )\   /(_))/(_))((_)\   /(_)) 
    ((_) (_)) (_))    ((_) (_))   
    | __|| _ \| _ \  / _ \ | _ \  
    | _| |   /|   / | (_) ||   /  
    |___||_|_\|_|_\  \___/ |_|_\                                                                  
        """,1 + Fore.LIGHTRED_EX))
            enter()
            print(str(text) + Fore.RESET)
        elif int(option) == 5:
            print(Colorate.Horizontal(Colors.white_to_red,r"""
    ___ ___ ___  ___  ___ 
    | __| _ \ _ \/ _ \| _ \
    | _||   /   / (_) |   /
    |___|_|_\_|_\\___/|_|_\                                                          
        """, 1))
            enter()
            print(Fore.LIGHTRED_EX + str(text) + Fore.RESET)
    if int(option) not in (1,2,3,4,5):
        raise ValueError("The option from error function is not an integer (1,2,3,4,5) ! [ENDA CAPP]")

#Define a tip output
def tip(text:str,option:int=1,slowprinting:bool=False):
    try:
        int(option)
    except:
        raise ValueError("The option from tip function is not an integer (1,2,3,4,5) ! [ENDA CAPP]")
    if slowprinting:
        if int(option) == 1:
            slowprinting(Fore.LIGHTYELLOW_EX + "[TIP]" + Fore.WHITE + " >> " + Fore.LIGHTYELLOW_EX + str(text) + Fore.RESET)
        elif int(option) == 2:
            slowPrint(Fore.LIGHTYELLOW_EX + "TIP" + Fore.WHITE + " >> " + Fore.LIGHTYELLOW_EX + str(text) + Fore.RESET)
        elif int(option) == 3:
            slowPrint(Fore.LIGHTYELLOW_EX + """       
    ▀▀█▀▀ ▀█▀ ▒█▀▀█ 
    ░▒█░░ ▒█░ ▒█▄▄█ 
    ░▒█░░ ▄█▄ ▒█░░░
            """ + Fore.LIGHTYELLOW_EX)
            enter()
            slowPrint(str(text) + Fore.RESET) 
        elif int(option) == 4:
            slowPrint(Colorate.Horizontal(Colors.red_to_yellow,"""
            (    (     
      *   ) )\ ) )\ )  
    ` )  /((()/((()/(  
     ( )(_))/(_))/(_)) 
    (_(_())(_)) (_))   
    |_   _||_ _|| _ \  
      | |   | | |  _/  
      |_|  |___||_|                                                                   
        """,1 + Fore.LIGHTYELLOW_EX))
            enter()
            slowPrint(str(text) + Fore.RESET) 
        elif int(option) == 5:
            slowPrint(Colorate.Horizontal(Colors.yellow,r"""
      _____ ___ ___ 
     |_   _|_ _| _ \
       | |  | ||  _/
       |_| |___|_|                                                                    
        """, 1))
            enter()
            slowPrint(Fore.LIGHTYELLOW_EX + str(text) + Fore.RESET) 
    else:
        if int(option) == 1:
            print(Fore.LIGHTYELLOW_EX + "[TIP]" + Fore.WHITE + " >> " + Fore.LIGHTYELLOW_EX + str(text) + Fore.RESET)
        elif int(option) == 2:
            print(Fore.LIGHTYELLOW_EX + "TIP" + Fore.WHITE + " >> " + Fore.LIGHTYELLOW_EX + str(text) + Fore.RESET)
        elif int(option) == 3:
            print(Fore.LIGHTYELLOW_EX + """       
    ▀▀█▀▀ ▀█▀ ▒█▀▀█ 
    ░▒█░░ ▒█░ ▒█▄▄█ 
    ░▒█░░ ▄█▄ ▒█░░░
            """ + Fore.LIGHTYELLOW_EX)
            enter()
            print(str(text) + Fore.RESET) 
        elif int(option) == 4:
            print(Colorate.Horizontal(Colors.red_to_yellow,"""
            (    (     
      *   ) )\ ) )\ )  
    ` )  /((()/((()/(  
     ( )(_))/(_))/(_)) 
    (_(_())(_)) (_))   
    |_   _||_ _|| _ \  
      | |   | | |  _/  
      |_|  |___||_|                                                                   
        """,1 + Fore.LIGHTYELLOW_EX))
            enter()
            print(str(text) + Fore.RESET) 
        elif int(option) == 5:
            print(Colorate.Horizontal(Colors.yellow,r"""
      _____ ___ ___ 
     |_   _|_ _| _ \
       | |  | ||  _/
       |_| |___|_|                                                                    
        """, 1))
            enter()
            print(Fore.LIGHTYELLOW_EX + str(text) + Fore.RESET) 
    if int(option) not in (1,2,3,4,5):
        raise ValueError("The option from tip function is not an integer (1,2,3,4,5) ! [ENDA CAPP]")

#Define a banner generator
def generate_banner(text:str):
    return art.text2art(text)
    
#Define a banner coloration
def banner_color(text):
    option = random.randint(1,5)
    if option == 1:
        return Colorate.Horizontal(Colors.green_to_white,text,1)
    elif option == 2:
        return Colorate.Horizontal(Colors.purple_to_blue,text,1)
    elif option == 3:
        return Colorate.Horizontal(Colors.blue_to_white,text,1)
    elif option == 4:
        return Colorate.Horizontal(Colors.white_to_red,text,1)
    elif option == 5:
        return Colorate.Vertical(Colors.red_to_yellow,text,1)

#Define an outro for the program
def outro(text:str,option:int=1,slowPrinting:bool=0,times:float=3,exiting:bool=1):
    try:
        int(option)
    except:
        raise ValueError("The option from outro is not avaible! [ENDA CAPP]")
    if slowPrinting:
        if int(option) == 1:
            slowPrint(Fore.BLUE + "[*] " + str(text) + Fore.RESET)
        elif int(option) == 2:
            slowPrint(Fore.MAGENTA + str(text) + Fore.RESET)
    else:
        if int(option) == 1:
            print(Fore.BLUE + "[*] " + str(text) + Fore.RESET)
        elif int(option) == 2:
            print(Fore.MAGENTA + str(text) + Fore.RESET)
    if int(option) not in (1,2):
        raise ValueError("The value of option is not avaible on outro! [ENDA CAPP]")
    if exiting:
        print(Fore.RESET)
        time.sleep(times)
        exit()
        