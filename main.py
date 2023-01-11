"""
Author: new92
Github: @new92
SkyData: Is a program which displays information about airplanes, airports, airlines but it can also be used to track a specific flight !
"""

#Imports
try:
    import sys
    import platform
    from os import system
    from time import sleep
    import os
    import json
    import pyflightdata
    import webbrowser
    from FlightRadar24.api import FlightRadar24API
    from pyflightdata import FlightData
except ImportError as imp:
    print("[!] WARNING: Not all packages used in this program have been installed !")
    sleep(1)
    print("[+] Ignoring Warning...")
    sleep(1)
    if sys.platform.startswith('linux') == True:
        system("sudo pip install -r requirements.txt")
        pass
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
        pass
    elif platform.system() == 'Windows':
        system("pip install -r requirements.txt")
        pass

#LOGO

print("""
░██████╗██╗░░██╗██╗░░░██╗      ██████╗░░█████╗░████████╗░█████╗░
██╔════╝██║░██╔╝╚██╗░██╔╝      ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
╚█████╗░█████═╝░░╚████╔╝░      ██║░░██║███████║░░░██║░░░███████║
░╚═══██╗██╔═██╗░░░╚██╔╝░░      ██║░░██║██╔══██║░░░██║░░░██╔══██║
██████╔╝██║░╚██╗░░░██║░░░      ██████╔╝██║░░██║░░░██║░░░██║░░██║
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░      ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝
""")

#Main program

print("\n")
print("[+] Program which display's information about airports, airplanes, airlines etc.")
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
option=int(input("[::] Please enter the number of the action to make: "))
while option < 1 or option > 16 or option == None:
    sleep(1)
    print("[!] Invalid option !")
    sleep(1)
    option=int(input("[::] Please enter again the number of the action to make: "))

FRadar = FlightRadar24API()
FData = FlightData()

if option == 1:
    try:
        airports==FRadar.get_airports()
        sleep(2)
        print("[+] Airports: "+str(airports))
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Quiting...")
        quit(0)

elif option == 2:
    try:
        airlines=FRadar.get_airlines()
        sleep(2)
        print("[+] Airlines: "+str(airlines))
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Quiting...")
        quit(0)

elif option == 3:
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
        print(ex)
        sleep(2)
        print("[+] Quiting...")
        quit(0)

elif option == 4:
    try:
        IATA=str(input("[::] Please enter the IATA of the airline: "))
        while IATA == None or len(IATA) > 3:
            print("[!] Invalid IATA !")
            sleep(1)
            IATA=str(input("[::] Please enter again the IATA of the airline: "))
        sleep(2)
        IATA=IATA.upper()
        ICAO=str(input("[::] Please enter the ICAO of the airline: "))
        while ICAO == None or len(ICAO) > 4:
            print("[!] Invalid ICAO !")
            sleep(1)
            ICAO=str(input("[::] Please enter again the ICAO of the airline: "))
        sleep(2)
        ICAO=ICAO.upper()
        logo=FRadar.get_airline_logo(IATA,ICAO)
        sleep(1)
        print("[+] The logo is available in this link: "+str(logo))
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Quiting...")
        quit(0)

elif option == 5:
    try:
        country_name=str(input("[::] Please enter the name of the country: "))
        while country_name == None:
            print("[!] Invalid Name !")
            sleep(1)
            country_name=str(input("[::] Please enter again the name of the country: "))
        sleep(1)
        FRadar.get_country_flag(country_name)
        sleep(2)
        print("[+] The flag of the country is available in this link: "+str(country_name))
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Quiting...")
        quit(0)
elif option == 6:
    try:
        FID=int(input("[::] Please enter the flight ID: "))
        while FID == None or FID <= 0:
            print("[!] Invalid Flight ID !")
            sleep(1)
            FID=int(input("[::] Please enter again the flight ID: "))
        sleep(1)
        dets=FRadar.get_flight_details(FID)
        sleep(2)
        print("[+] Details of the flight: "+str(dets))
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Quiting...")
        quit(0)

elif option == 7:
    try:
        IATA=str(input("[::] Please enter the IATA of the airport: "))
        while IATA == None or len(IATA) > 3:
            print("[!] Invalid IATA !")
            sleep(1)
            IATA=str(input("[::] Please enter again the IATA of the airport: "))
        sleep(1)
        IATA=IATA.upper()
        airport_dets=FData.get_airport_details(IATA)
        sleep(2)
        print("[+] Information about the airport: "+str(airport_dets))
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Quiting...")
        quit(0)

elif option == 8:
    try:
        IATA=str(input("[::] Please enter the IATA of the airport: "))
        while IATA == None or len(IATA) > 3:
            print("[!] Invalid IATA !")
            sleep(1)
            IATA=str(input("[::] Please enter again the IATA of the airport: "))
        sleep(1)
        IATA=IATA.upper()
        arrivals=FData.get_airport_arrivals(IATA)
        sleep(2)
        print("[+] The arrivals at the airport: "+str(arrivals))
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Quiting...")
        quit(0)

elif option == 9:
    try:
        IATA=str(input("[::] Please enter the IATA of the airport: "))
        while IATA == None or len(IATA) > 3:
            print("[!] Invalid IATA !")
            sleep(1)
            IATA=str(input("[::] Please enter again the IATA of the airport: "))
        sleep(1)
        IATA=IATA.upper()
        departures=FData.get_airport_departures(IATA)
        sleep(2)
        print("[+] The departures of the airport: "+str(departures))
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Quiting...")
        quit(0)

elif option == 10:
    try:
        IATA=str(input("[::] Please enter the IATA of the airport: "))
        while IATA == None or len(IATA) > 3:
            print("[!] Invalid IATA !")
            sleep(1)
            IATA=str(input("[::] Please enter again the IATA of the airport: "))
        sleep(1)
        IATA=IATA.upper()
        weather=FData.get_airport_weather(IATA)
        sleep(2)
        print("[+] The weather at the airport: "+str(weather))
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Quiting...")
        quit(0)

elif option == 11:
    try:
        IATA=str(input("[::] Please enter the IATA of the airport: "))
        while IATA == None or len(IATA) > 3:
            print("[!] Invalid IATA !")
            sleep(1)
            IATA=str(input("[::] Please enter again the IATA of the airport: "))
        sleep(1)
        IATA=IATA.upper()
        reviews=FData.get_airport_reviews(IATA)
        sleep(2)
        print("[+] Reviews for the airport: "+str(reviews))
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Quiting...")
        quit(0)

elif option == 12:
    try:
        IATA=str(input("[::] Please enter the IATA of the airport: "))
        while IATA == None or len(IATA) > 3:
            print("[!] Invalid IATA !")
            sleep(1)
            IATA=str(input("[::] Please enter again the IATA of the airport: "))
        sleep(1)
        IATA=IATA.upper()
        stats=FData.get_airport_stats(IATA)
        sleep(2)
        print("[+] Stats for the requested airport: "+str(stats))
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Quiting...")
        quit(0)

elif option == 13:
    try:
        zones=FRadar.get_zones()
        sleep(2)
        print("[+] Zones: "+str(zones))
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Quiting...")
        quit(0)

elif option == 14:
    try:
        flight=FRadar.get_real_time_flight_tracker_config()
        sleep(2)
        print("[+] Current Flight: "+str(flight))
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Quiting...")
        quit(0)

elif option == 15:
    webbrowser.open("https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:_A")
    quit(0)

else:
    print("[+] Quiting...")
    quit(0)
