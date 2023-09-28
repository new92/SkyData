# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
Leetcode: @new92

Python script which displays information about airplanes, airlines, airports but it can also be used to track a specific flight !
"""

try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[!] Error ! SkyData requires Python version 3.X ! ")
        sleep(2)
        print("""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[*] Please install Python 3 and then use SkyData ✅")
        sleep(2)
        print("[+] Exiting...")
        sleep(1)
        quit(0)
    from tqdm import tqdm
    total_mods = 9
    bar = tqdm(total=total_mods, desc='Loading modules', unit='module')
    for _ in range(total_mods):
        sleep(0.75)
        bar.update(1)
    bar.close()
    import platform
    import string
    import json
    from os import system
    import os
    import webbrowser
    from FlightRadar24 import FlightRadar24API
    from pyflightdata import FlightData
except ImportError or ModuleNotFoundError:
    print("[!] WARNING: Not all packages used in SkyData have been installed !")
    sleep(2)
    print("[+] Ignoring warning...")
    sleep(1)
    if sys.platform.startswith('linux'):
        if os.geteuid() != 0:
            print("[!] Root user not detected !")
            sleep(2)
            print("[+] Trying to enable root user...")
            sleep(1)
            system("sudo su")
            try:
                system("sudo pip install -r requirements.txt")
            except Exception as ex:
                print("[!] Error ! Cannot install the required modules !")
                sleep(1)
                print(f"[=] Error message ==> {ex}")
                sleep(2)
                print("[1] Uninstall script")
                print("[2] Exit")
                opt=int(input("[>] Please enter a number (from the above ones): "))
                while opt < 1 or opt > 2 or opt == None:
                    if opt == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid number !")
                        sleep(1)
                        print("[+] Acceptable numbers: [1,2]")
                    sleep(1)
                    print("[1] Uninstall script")
                    print("[2] Exit")
                    opt=int(input("[>] Please enter again a number (from the above ones): "))
                if opt == 1:
                    def fpath(fname: str):
                        for root, dirs, files in os.walk('/'):
                            if fname in files:
                                return os.path.abspath(os.path.join(root, fname))
                        return None
                    def rmdir(dire):
                        DIRS = []
                        for root, dirs, files in os.walk(dire):
                            for file in files:
                                os.remove(os.path.join(root,file))
                            for dir in dirs:
                                DIRS.append(os.path.join(root,dir))
                        for i in range(len(DIRS)):
                            os.rmdir(DIRS[i])
                        os.rmdir(dire)
                    rmdir(fpath('SkyData'))
                    print("[✓] Files and dependencies uninstalled successfully !")
                else:
                    print("[+] Exiting...")
                    sleep(1)
                    print("[+] See you next time 👋")
                    quit(0)
        else:
            system("sudo pip install -r requirements.txt")
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
    elif platform.system() == 'Windows':
        system("pip install -r requirements.txt")

print("[✓] Successfully loaded modules !")
sleep(1)

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))
    return None

UPPERS = list(string.ascii_uppercase)
DIGS = list(string.digits)

def ScriptInfo():
    with open('config.json') as config:
        conf = json.load(config)
    f = conf['name'] + '.py'
    fsize = 0 if not os.path.exists(fpath(f)) else os.stat(fpath(f)).st_size
    print(f"[+] Author: {conf['author']}")
    print(f"[+] Github: @{conf['author']}")
    print(f"[+] Leetcode: @{conf['author']}")
    print(f"[+] License: {conf['lice']}")
    print(f"[+] Natural language: {conf['lang']}")
    print(f"[+] Programming language(s) used: {conf['language']}")
    print(f"[+] Number of lines: {conf['lines']}")
    print(f"[+] Script's name: {conf['name']}")
    print(f"[+] API(s) used: {conf['api']}")
    print(f"[+] File size: {fsize} bytes")
    print(f"[+] File path: {fpath(f)}")
    print(f"|======|GITHUB REPO INFO|======|")
    print(f"[+] Stars: {conf['stars']}")
    print(f"[+] Forks: {conf['forks']}")
    print(f"[+] Open issues: {conf['issues']}")
    print(f"[+] Closed issues: {conf['clissues']}")
    print(f"[+] Open pull requests: {conf['prs']}")
    print(f"[+] Closed pull requests: {conf['clprs']}")
    print(f"[+] Discussions: {conf['discs']}")

def clear():
    system('cls') if platform.system() == 'Windows' else system('clear')

def checkID(fid:str) -> bool:
    return fid == None or fid == '' or len(fid) < 1 or len(fid) > 7 or fid[:2] not in UPPERS or len([i for i in fid[3:] if i in DIGS]) != len(fid[3:])

def checkIATA(iata: str) -> bool:
    return iata == None or iata == '' or len(iata) != 3 or len([i for i in range(len(iata)) if i in UPPERS]) != len(iata)

def checkICAO(icao: str) -> bool:
    return icao == None or icao == '' or len(icao) != 4 or len([i for i in range(len(icao)) if i in UPPERS]) != len(icao)

def banner() -> str:
    return """
    ░██████╗██╗░░██╗██╗░░░██╗      ██████╗░░█████╗░████████╗░█████╗░
    ██╔════╝██║░██╔╝╚██╗░██╔╝      ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
    ╚█████╗░█████═╝░░╚████╔╝░      ██║░░██║███████║░░░██║░░░███████║
    ░╚═══██╗██╔═██╗░░░╚██╔╝░░      ██║░░██║██╔══██║░░░██║░░░██╔══██║
    ██████╔╝██║░╚██╗░░░██║░░░      ██████╔╝██║░░██║░░░██║░░░██║░░██║
    ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░      ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝
    """
    
def main():
    print(banner())
    print("\n")
    print("[+] SkyData is a python script which display's information about airports, flights, airlines etc.")
    print("\n")
    print("[+] Author: new92")
    print("[+] Github: @new92")
    print("\n")
    print("[1] Display airports")
    print("[2] Display airlines")
    print("[3] Display flights")
    print("[4] Get aircraft info")
    print("[5] Display countries")
    print("[6] Show information for specific flights    [<--]")
    print("[7] Show information for specific airports")
    print("[8] Show arrivals of an airport")
    print("[9] Show departures of an airport")
    print("[10] Show weather conditions of an airport")
    print("[11] Display airport reviews")
    print("[12] Display airport stats")
    print("[13] Show zones  [<--]")
    print("[14] Display current flight(s)   [<--]")
    print("[15] Display IATA and ICAO codes for airports")
    print("[16] Display the landed aircrafts on a specific airport")
    print("[17] Get history of aircraft by flight number")
    print("[18] Exit")
    print("\n")
    option=int(input("[::] Please enter a number (from the above ones): "))
    while option < 1 or option > 18 or option == None:
        sleep(1)
        print("[!] Invalid option !")
        sleep(1)
        option=int(input("[::] Please enter again a number (from the above ones): "))

    fr = FlightRadar24API()
    fdata = FlightData()

    if option == 1:
        clear()
        country=str(input("[::] Country >>> "))
        while country == None or country == '':
            print("[!] This field can't be blank !")
            sleep(1)
            country=str(input("[::] Country >>> "))
        country = country.capitalize().strip()
        try:
            airports = fdata.get_airports(country=country)
            print(f"[+] Airports:")
            print("-"*10)
            print("\n")
            for i in range(len(airports)):
                if 'name' in airports[i]:
                    print(f"[+] Name: {airports[i]['name']}")
                if 'iata' in airports[i]:
                    print(f"[+] IATA: {airports[i]['iata']}")
                if 'lat' in airports[i]:
                    print(f"[+] Latitude: {airports[i]['lat']}")
                if 'lon' in airports[i]:
                    print(f"[+] Longitude: {airports[i]['lon']}")
                print("-"*15)
                sleep(0.75)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[>] Please enter a number (from the above ones): "))
            while num < 1 or num > 2 or num == None:
                if num == None:
                    print("[!] This field can't be empty !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[*] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                num=int(input("[>] Please enter again a number (from the above ones): "))
            if num == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        fdata.clear_last_request()

    elif option == 2:
        clear()
        try:
            airlines = fdata.get_airlines()
            print(f"[+] Airlines:")
            print("-"*10)
            print("\n")
            for i in range(len(airlines)):
                if 'title' in airlines[i]:
                    print(f"[+] Name: {airlines[i]['title']}")
                if 'airline-code' in airlines[i]:
                    print(f"[+] Airline code: {airlines[i]['airline-code']}")
                if 'img' in airlines[i]:
                    print(f"[+] Image: {airlines[i]['img']}")
                if 'callsign' in airlines[i]:
                    print(f"[+] Call sing: {airlines[i]['callsign']}")
                if 'fleet-size' in airlines[i]:
                    print(f"[+] Fleet size: {airlines[i]['fleet-size']}")
                print("-"*15)
                sleep(0.75)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[>] Please enter a number (from the above ones): "))
            while num < 1 or num > 2 or num == None:
                if num == None:
                    print("[!] This field can't be empty !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[*] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                num=int(input("[>] Please enter again a number (from the above ones): "))
            if num == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        fdata.clear_last_request()

    elif option == 3:
        clear()
        key=str(input("[::] Flight number >>> "))
        while key == None or key == '':
            print("[!] This field can't be blank !")
            sleep(1)
            key=str(input("[::] Flight number >>> "))
        try:
            flights = fdata.get_flights(key)
            if len(flights) == 0:
                print("[!] No flights related to specific airline found !")
                sleep(1)
                print(f"[+] Searched using flight number > {key}")
            else:
                print(f"[+] Flights:")
                for i in range(len(flights)):
                    print(f"[>] {flights[i]}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[>] Please enter a number (from the above ones): "))
            while num < 1 or num > 2 or num == None:
                if num == None:
                    print("[!] This field can't be empty !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[*] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                num=int(input("[>] Please enter again a number (from the above ones): "))
            if num == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        fdata.clear_last_request()

    elif option == 4:
        clear()
        tnum=str(input("[::] Aircraft tail number >>> "))
        while tnum == None or tnum == '':
            print("[!] This field can't be blank !")
            sleep(1)
            tnum=str(input("[::] Aircraft tail number >>> "))
        tnum = tnum.lower().strip()
        try:
            data = fdata.get_info_by_tail_number(tnum)
            if len(data) == 0:
                print("[!] No data found for specific aircraft !")
                sleep(1)
                print(f"[+] Searched using tail number: {tnum}")
            else:
                print("[+] Aircraft data:")
                for i in range(len(data)):
                    print(f"[>] {data[i]}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[>] Please enter a number (from the above ones): "))
            while num < 1 or num > 2 or num == None:
                if num == None:
                    print("[!] This field can't be empty !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[*] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                num=int(input("[>] Please enter again a number (from the above ones): "))
            if num == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        fdata.clear_last_request()

    elif option == 5:
        clear()
        countries = fdata.get_countries()
        try:
            print("[+] Countries:")
            for i in range(len(countries)):
                print(f"[>] {countries[i]}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[>] Please enter a number (from the above ones): "))
            while num < 1 or num > 2 or num == None:
                if num == None:
                    print("[!] This field can't be empty !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[*] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                num=int(input("[>] Please enter again a number (from the above ones): "))
            if num == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        fdata.clear_last_request()

    elif option == 6:
        clear()
        FID=str(input("[::] Flight ID >>> "))
        while checkID(FID):
            if FID == None or FID == '':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid flight ID !")
                sleep(1)
                print("[+] Acceptable flight ID format --> XX 1234")
            sleep(1)
            FID=str(input("[::] Flight ID >>> "))
        try:
            sleep(1)
            print(f"[+] Flight details >>> {fr.get_flight_details(FID)}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[>] Please enter a number (from the above ones): "))
            while num < 1 or num > 2 or num == None:
                if num == None:
                    print("[!] This field can't be empty !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[*] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                num=int(input("[>] Please enter again a number (from the above ones): "))
            if num == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        fdata.clear_last_request()

    elif option == 7:
        clear()
        IATA=str(input("[::] Airport IATA code >>> "))
        while checkIATA(IATA):
            if IATA == None or IATA == '':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid IATA code !")
                sleep(1)
                print("[+] Acceptable IATA code format --> XXX")
            sleep(1)
            IATA=str(input("[::] Airport IATA code >>> "))
        sleep(1)
        IATA = IATA.upper().strip()
        try:
            print(f"[+] Airport info >>> {fdata.get_airport_details(IATA)}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[>] Please enter a number (from the above ones): "))
            while num < 1 or num > 2 or num == None:
                if num == None:
                    print("[!] This field can't be empty !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[*] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                num=int(input("[>] Please enter again a number (from the above ones): "))
            if num == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        fdata.clear_last_request()

    elif option == 8:
        clear()
        IATA=str(input("[::] Airport IATA code >>> "))
        while checkIATA(IATA):
            if IATA == None or IATA == '':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid IATA code !")
                sleep(1)
                print("[+] Acceptable IATA code format --> XXX")
            sleep(1)
            IATA=str(input("[::] Airport IATA code >>> "))
        sleep(1)
        IATA = IATA.upper().strip()
        try:
            print(f"[+] Airport arrivals >>> {fdata.get_airport_arrivals(IATA)}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[>] Please enter a number (from the above ones): "))
            while num < 1 or num > 2 or num == None:
                if num == None:
                    print("[!] This field can't be empty !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[*] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                num=int(input("[>] Please enter again a number (from the above ones): "))
            if num == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        fdata.clear_last_request()

    elif option == 9:
        clear()
        IATA=str(input("[::] Airport IATA code >>> "))
        while checkIATA(IATA):
            if IATA == None or IATA == '':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid IATA code !")
                sleep(1)
                print("[+] Acceptable IATA code format --> XXX")
            sleep(1)
            IATA=str(input("[::] Airport IATA code >>> "))
        sleep(1)
        IATA = IATA.upper().strip()
        try:
            print(f"[+] Airport's departures >>> {fdata.get_airport_departures(IATA)}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[>] Please enter a number (from the above ones): "))
            while num < 1 or num > 2 or num == None:
                if num == None:
                    print("[!] This field can't be empty !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[*] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                num=int(input("[>] Please enter again a number (from the above ones): "))
            if num == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        fdata.clear_last_request()

    elif option == 10:
        clear()
        IATA=str(input("[::] Airport IATA code >>> "))
        while checkIATA(IATA):
            if IATA == None or IATA == '':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid IATA code !")
                sleep(1)
                print("[+] Acceptable IATA code format --> XXX")
            sleep(1)
            IATA=str(input("[::] Airport IATA code >>> "))
        sleep(1)
        IATA = IATA.upper().strip()
        try:
            print(f"[+] Airport weather >>> {fdata.get_airport_weather(IATA)}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[>] Please enter a number (from the above ones): "))
            while num < 1 or num > 2 or num == None:
                if num == None:
                    print("[!] This field can't be empty !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[*] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                num=int(input("[>] Please enter again a number (from the above ones): "))
            if num == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        fdata.clear_last_request()

    elif option == 11:
        clear()
        IATA=str(input("[::] Airport IATA code >>> "))
        while checkIATA(IATA):
            if IATA == None or IATA == '':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid IATA code !")
                sleep(1)
                print("[+] Acceptable IATA code format --> XXX")
            sleep(1)
            IATA=str(input("[::] Airport IATA code >>> "))
        sleep(1)
        IATA = IATA.upper().strip()
        try:
            print(f"[+] Reviews for the airport: {fdata.get_airport_reviews(IATA)}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[>] Please enter a number (from the above ones): "))
            while num < 1 or num > 2 or num == None:
                if num == None:
                    print("[!] This field can't be empty !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[*] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                num=int(input("[>] Please enter again a number (from the above ones): "))
            if num == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        fdata.clear_last_request()

    elif option == 12:
        clear()
        IATA=str(input("[::] Airport IATA code >>> "))
        while checkIATA(IATA):
            if IATA == None or IATA == '':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid IATA code !")
                sleep(1)
                print("[+] Acceptable IATA code format --> XXX")
            sleep(1)
            IATA=str(input("[::] Airport IATA code >>> "))
        sleep(1)
        IATA = IATA.upper().strip()
        try:
            print(f"[+] Airport stats >>> {fdata.get_airport_stats(IATA)}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[>] Please enter a number (from the above ones): "))
            while num < 1 or num > 2 or num == None:
                if num == None:
                    print("[!] This field can't be empty !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[*] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                num=int(input("[>] Please enter again a number (from the above ones): "))
            if num == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        fdata.clear_last_request()

    elif option == 13:
        clear()
        try:
            sleep(1)
            print(f"[+] Zones: {fr.get_zones()}")
        except Exception as ex: 
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[>] Please enter a number (from the above ones): "))
            while num < 1 or num > 2 or num == None:
                if num == None:
                    print("[!] This field can't be empty !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[*] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                num=int(input("[>] Please enter again a number (from the above ones): "))
            if num == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        fdata.clear_last_request()

    elif option == 14:
        clear()
        try:
            fconf = fr.get_flight_tracker_config()
            lim=int(input("[::] Enter flights limit: "))
            while lim < 1 or lim > 100 or lim == None:
                print("[!] Invalid limit !")
                sleep(1)
                print("[+] Acceptable range: [1-100]")
            lim=int(input("[::] Enter flights limit: "))
            fconf.limit = lim
            fr.set_flight_tracker_config(fconf)
            print(f"[+] Flights >>> {fr.get_flights}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[>] Please enter a number (from the above ones): "))
            while num < 1 or num > 2 or num == None:
                if num == None:
                    print("[!] This field can't be empty !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[*] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                num=int(input("[>] Please enter again a number (from the above ones): "))
            if num == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        fdata.clear_last_request()

    elif option == 15:
        clear()
        sleep(1)
        webbrowser.open("https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:_A")
        print("[1] Return to menu")
        print("[2] Exit")
        num=int(input("[>] Please enter a number (from the above ones): "))
        while num < 1 or num > 2 or num == None:
            if num == None:
                print("[!] This field can't be empty !")
            else:
                print("[!] Invalid number !")
                sleep(1)
                print("[*] Acceptable numbers: [1/2]")
            sleep(1)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[>] Please enter again a number (from the above ones): "))
        if num == 1:
            clear()
            main()
        else:
            clear()
            print("[+] Exiting...")
            sleep(1)
            print("[+] See you next time 👋")
            sleep(1)
            quit(0)
        fdata.clear_last_request()

    elif option == 16:
        clear()
        IATA=str(input("[::] Airport IATA code >>> "))
        while checkIATA(IATA):
            if IATA == None or IATA == '':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid IATA code !")
                sleep(1)
                print("[+] Acceptable IATA code format --> XXX")
            sleep(1)
            IATA=str(input("[::] Airport IATA code >>> "))
        IATA = IATA.upper().strip()
        try:
            print(f"[+] Aircrafts on airport >>> {fdata.get_airport_metars(IATA)}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[>] Please enter a number (from the above ones): "))
            while num < 1 or num > 2 or num == None:
                if num == None:
                    print("[!] This field can't be empty !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[*] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                num=int(input("[>] Please enter again a number (from the above ones): "))
            if num == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        fdata.clear_last_request()

    elif option == 17:
        clear()
        fnum=str(input("[::] Flight number >>> "))
        while fnum == None or fnum == '':
            if fnum == None or fnum == '':
                print("[!] This field can't be blank !")
            sleep(1)
            fnum=str(input("[::] Flight number >>> "))
        fnum = fnum.upper().strip()
        try:
            print(f"[+] Aircraft history >>> {fdata.get_all_available_history_by_flight_number(fnum)}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[>] Please enter a number (from the above ones): "))
            while num < 1 or num > 2 or num == None:
                if num == None:
                    print("[!] This field can't be empty !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[*] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                num=int(input("[>] Please enter again a number (from the above ones): "))
            if num == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        fdata.clear_last_request()

    else:
        print("[+] Thank you for using SkyData 😁")
        sleep(2)
        print("[+] See you next time 👋")
        sleep(1)
        quit(0)

    print("\n\n")
    print("[1] Return to menu")
    print("[2] Exit")
    num=int(input("[>] Please enter a number (from the above ones): "))
    while num < 1 or num > 2 or num == None:
        if num == None:
            print("[!] This field can't be empty !")
        else:
            print("[!] Invalid number !")
            sleep(1)
            print("[*] Acceptable numbers: [1/2]")
        sleep(1)
        print("[1] Return to menu")
        print("[2] Exit")
        num=int(input("[>] Please enter again a number (from the above ones): "))
    if num == 1:
        clear()
        main()
    else:
        clear()
        print("[+] Exiting...")
        sleep(1)
        print("[+] See you next time 👋")
        sleep(1)
        quit(0)

if __name__ == '__main__':
    main()
