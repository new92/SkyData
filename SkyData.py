# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92

SkyData: Is a Python script which displays information about airplanes, airlines, airports but it can also be used to track a specific flight !
"""

try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[!] Error ! This script requires Python version 3.X ! ")
        print("""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        print("[*] Please install the Python 3 and then use this script ✅")
        sleep(2)
        print("[+] Exiting...")
        sleep(1)
        quit(0)
    import platform
    from os import system
    import os
    import webbrowser
    from FlightRadar24.api import FlightRadar24API
    from pyflightdata import FlightData
except ImportError:
    print("[!] WARNING: Not all packages used in Researcher have been installed !")
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
                    rmdir(os.path.abspath('SkyData'))
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

def ProgInfo():
    author = 'new92'
    lice = 'MIT'
    lang = 'Python'
    language = 'en-US'
    name = 'Sky Data'
    desc = 'Script which displays information about airplanes, airlines, airports but it can also be used to track a specific flight !'
    f = '/SkyData/SkyData.py'
    if os.path.exists(os.path.abspath(f)):
        fsize = (os.stat(f)).st_size
    else:
        fsize = 0
    api = None
    lns = 461
    stars = 8
    forks = 2
    print(f"[+] Author: {author}")
    print(f"[+] License: {lice}")
    print(f"[+] Programming language used: {lang}")
    print(f"[+] Natural language: {language}")
    print(f"[+] Script's name: {name}")
    print(f"[+] Script's description: {desc}")
    print(f"[+] File size: {fsize}")
    print(f"[+] Path to the script: {os.path.abspath(f)}")
    print(f"[+] Lines of code: {lns}")
    print(f"[+] API(s) used: {api}")
    print(f"[+] Github repo stars: {stars}")
    print(f"[+] Github repo forks: {forks}")
    
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
    print("[+] Script which display's information about airports, airplanes, airlines etc.")
    print("\n")
    print("[+] Author: new92")
    print("[+] Github: @new92")
    print("\n")
    print("[1] Airports")
    print("[2] Airlines")
    print("[3] Flights")
    print("[4] Airline Logo")
    print("[5] Country Flags")
    print("[6] Information for specific flights")
    print("[7] Information for specific airports")
    print("[8] Arrivals of an airport")
    print("[9] Departures of an airport")
    print("[10] Weather of an airport")
    print("[11] Airport reviews")
    print("[12] Airport stats")
    print("[13] Zones")
    print("[14] Current Flight(s)")
    print("[15] Display IATA and ICAO codes for airports")
    print("[16] Exit")
    print("\n")
    option=int(input("[::] Please enter a number (from the above ones): "))
    while option < 1 or option > 16 or option == None:
        sleep(1)
        print("[!] Invalid option !")
        sleep(1)
        option=int(input("[::] Please enter again a number (from the above ones): "))

    FRadar = FlightRadar24API()
    FData = FlightData()

    if option == 1:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        try:
            print(f"[+] Airports: {FRadar.get_airports()}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 2:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        try:
            print(f"[+] Airlines: {FRadar.get_airlines()}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 3:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        ICAO=str(input("[::] Please enter the ICAO code of the airport: "))
        while ICAO == None or len(ICAO) > 4:
            print("[!] Invalid ICAO code !")
            sleep(1)
            ICAO=str(input("[::] Please enter again the ICAO code of the airport: "))
        try:
            flights=FRadar.get_flights(ICAO)
            sleep(2)
            print("[+] Flights: "+str(flights))
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 4:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        IATA=str(input("[::] Please enter the IATA code of the airline: "))
        while IATA == None or len(IATA) > 3:
            print("[!] Invalid IATA code !")
            sleep(1)
            IATA=str(input("[::] Please enter again the IATA code of the airline: "))
        sleep(2)
        IATA = IATA.upper()
        ICAO=str(input("[::] Please enter the ICAO code of the airline: "))
        while ICAO == None or len(ICAO) > 4:
            print("[!] Invalid ICAO !")
            sleep(1)
            ICAO=str(input("[::] Please enter again the ICAO code of the airline: "))
        sleep(2)
        ICAO=ICAO.upper()
        try:
            print(f"[+] The logo is available in this url: {FRadar.get_airline_logo(IATA,ICAO)}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 5:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        try:
            country_name=str(input("[::] Please enter the name of the country: "))
            while country_name == None:
                print("[!] Invalid name !")
                sleep(1)
                country_name=str(input("[::] Please enter again the name of the country: "))
            sleep(1)
            print(f"[+] The flag of the country is available in this url: {FRadar.get_country_flag(country_name)}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 6:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        FID=int(input("[::] Please enter the flight ID: "))
        while FID == None or FID <= 0:
            print("[!] Invalid flight ID !")
            sleep(1)
            FID=int(input("[::] Please enter again the flight ID: "))
        try:
            sleep(1)
            print(f"[+] Details of the flight: {FRadar.get_flight_details(FID)}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 7:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        IATA=str(input("[::] Please enter the IATA code of the airport: "))
        while IATA == None or len(IATA) > 3:
            print("[!] Invalid IATA code !")
            sleep(1)
            IATA=str(input("[::] Please enter again the IATA code of the airport: "))
        sleep(1)
        IATA = IATA.upper()
        try:
            print(f"[+] Information about the airport: {FData.get_airport_details(IATA)}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 8:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        IATA=str(input("[::] Please enter the IATA code of the airport: "))
        while IATA == None or len(IATA) > 3:
            print("[!] Invalid IATA code !")
            sleep(1)
            IATA=str(input("[::] Please enter again the IATA code of the airport: "))
        sleep(1)
        IATA=IATA.upper()
        try:
            print(f"[+] The arrivals at the airport: {FData.get_airport_arrivals(IATA)}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 9:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        IATA=str(input("[::] Please enter the IATA code of the airport: "))
        while IATA == None or len(IATA) > 3:
            print("[!] Invalid IATA code !")
            sleep(1)
            IATA=str(input("[::] Please enter again the IATA code of the airport: "))
        sleep(1)
        IATA=IATA.upper()
        try:
            print(f"[+] The departures of the airport: {FData.get_airport_departures(IATA)}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 10:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        IATA=str(input("[::] Please enter the IATA code of the airport: "))
        while IATA == None or len(IATA) > 3:
            print("[!] Invalid IATA code !")
            sleep(1)
            IATA=str(input("[::] Please enter again the IATA code of the airport: "))
        sleep(1)
        IATA=IATA.upper()
        try:
            print(f"[+] The weather at the airport: {FData.get_airport_weather(IATA)}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 11:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        IATA=str(input("[::] Please enter the IATA code of the airport: "))
        while IATA == None or len(IATA) > 3:
            print("[!] Invalid IATA code !")
            sleep(1)
            IATA=str(input("[::] Please enter again the IATA code of the airport: "))
        sleep(1)
        IATA=IATA.upper()
        try:
            print(f"[+] Reviews for the airport: {FData.get_airport_reviews(IATA)}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 12:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        IATA=str(input("[::] Please enter the IATA code of the airport: "))
        while IATA == None or len(IATA) > 3:
            print("[!] Invalid IATA code !")
            sleep(1)
            IATA=str(input("[::] Please enter again the IATA code of the airport: "))
        sleep(1)
        IATA=IATA.upper()
        try:
            print(f"[+] Stats for the requested airport: {FData.get_airport_stats(IATA)}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 13:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        try:
            print(f"[+] Zones: {FRadar.get_zones()}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 14:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        try:
            print(f"[+] Current Flight: {FRadar.get_real_time_flight_tracker_config()}")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 15:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        webbrowser.open("https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:_A")
        quit(0)

    else:
        print("[+] Thank you for using my script 😁")
        sleep(2)
        print("[+] See you next time 👋")
        sleep(1)
        quit(0)

if __name__ == '__main__':
    main()
