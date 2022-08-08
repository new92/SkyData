"""
Author: @new92
Flight Radar is a program which display's information about airplanes, airports, airlines etc.
"""

#Imports

try:
    import time
    import platform
    from os import system
    import sys
    import os
    import requests
    import sniffer
    import http
    import socket
    import geocoder
    import json
    import locale
    import webbrowser as browser
    import pyflightdata
    import art
    from art import tprint
    from FlightRadar24.api import FlightRadar24API
    from pyflightdata import FlightData
except ImportError as imp:
    print("[!] WARNING: Not all modules used in this program have been installed !")
    time.sleep(1)
    print("[+] Ignoring Warning...")
    time.sleep(1)
    if platform.system() == "Windows":
        system("pip3 install -r requirements.txt")
    else:
        system("sudo pip3 install -r requirements.txt")

#LOGO

tprint("FLIGHT    DATA",font="tarty1")

#Main program

print("\n")
print("[+] Program which display's information about airports, airplanes, airlines etc.")
print("\n")
print("[+] Github: @new92")
print("\n")
print("[1] Airports")
print("[2] Airlines")
print("[3] Flights")
print("[4] Airline Logo")
print("[5] Country Flags")
print("[6] Information for Specific Flights")
print("[7] Information for Specific Airports")
print("[8] Arrivals of an Airport")
print("[9] Departures of an Airport")
print("[10] Weather of an Airport")
print("[11] Airport Reviews")
print("[12] Airport Stats")
print("[13] Zones")
print("[14] Current Flight(s)")
print("[15] Exit")
print("\n")
option=int(input("[::] Please enter the number of the action to make: "))
while option <= 0 or option > 15 or option == None:
    time.sleep(1)
    print("[!] Invalid option !")
    time.sleep(1)
    option=int(input("[::] Please enter again the number of the action to make: "))
FRadar = FlightRadar24API()
FData = FlightData()
if option == 1:
    time.sleep(1)
    airports=FRadar.get_airports()
    time.sleep(2)
    print("[+] Airports: "+str(airports))
elif option == 2:
    time.sleep(1)
    airlines=FRadar.get_airlines()
    time.sleep(2)
    print("[+] Airlines: "+str(airlines))
elif option == 3:
    time.sleep(1)
    flights=FRadar.get_flights()
    time.sleep(2)
    print("[+] Flights: "+str(flights))
elif option == 4:
    time.sleep(1)
    IATA=input("[::] Please enter the IATA of the airline: ")
    while IATA == None:
        print("[!] Invalid IATA !")
        time.sleep(1)
        IATA=input("[::] Please enter again the IATA of the airline: ")
    time.sleep(2)
    IATA=IATA.upper()
    ICAO=input("[::] Please enter the ICAO of the airline: ")
    while ICAO == None:
        print("[!] Invalid ICAO !")
        time.sleep(1)
        ICAO=input("[::] Please enter again the ICAO of the airline: ")
    time.sleep(2)
    ICAO=ICAO.upper()
    logo=FRadar.get_airline_logo(IATA,ICAO)
    time.sleep(1)
    print("[+] The logo is available in this link: "+str(logo))
elif option == 5:
    time.sleep(1)
    country_name=input("[::] Please enter the name of the country: ")
    while country_name == None:
        print("[!] Invalid Name !")
        time.sleep(1)
        country_name=input("[::] Please enter again the name of the country: ")
    time.sleep(1)
    FRadar.get_country_flag(country_name)
    time.sleep(2)
    print("[+] The flag of the country is available in this link: "+str(country_name))
elif option == 6:
    time.sleep(1)
    FID=input("[::] Please enter the flight ID: ")
    while FID == None:
        print("[!] Invalid Flight ID !")
        time.sleep(1)
        FID=input("[::] Please enter again the flight ID: ")
    time.sleep(1)
    dets=FRadar.get_flight_details(FID)
    time.sleep(2)
    print("[+] Details of the flight: "+str(dets))
elif option == 7:
    time.sleep(1)
    IATA=input("[::] Please enter the IATA of the airport: ")
    while IATA == None:
        print("[!] Invalid IATA !")
        time.sleep(1)
        IATA=input("[::] Please enter again the IATA of the airport: ")
    time.sleep(1)
    IATA=IATA.upper()
    airport_dets=FData.get_airport_details(IATA)
    time.sleep(2)
    print("[+] Information about the airport: "+str(airport_dets))
elif option == 8:
    time.sleep(1)
    IATA=input("[::] Please enter the IATA of the airport: ")
    while IATA == None:
        print("[!] Invalid IATA !")
        time.sleep(1)
        IATA=input("[::] Please enter again the IATA of the airport: ")
    time.sleep(1)
    IATA=IATA.upper()
    arrivals=FData.get_airport_arrivals(IATA)
    time.sleep(2)
    print("[+] The arrivals at the airport: "+str(arrivals))
elif option == 9:
    time.sleep(1)
    IATA=input("[::] Please enter the IATA of the airport: ")
    while IATA == None:
        print("[!] Invalid IATA !")
        time.sleep(1)
        IATA=input("[::] Please enter again the IATA of the airport: ")
    time.sleep(1)
    IATA=IATA.upper()
    departures=FData.get_airport_departures(IATA)
    time.sleep(2)
    print("[+] The departures of the airport: "+str(departures))
elif option == 10:
    time.sleep(1)
    IATA=input("[::] Please enter the IATA of the airport: ")
    while IATA == None:
        print("[!] Invalid IATA !")
        time.sleep(1)
        IATA=input("[::] Please enter again the IATA of the airport: ")
    time.sleep(1)
    IATA=IATA.upper()
    weather=FData.get_airport_weather(IATA)
    time.sleep(2)
    print("[+] The weather at the airport: "+str(weather))
elif option == 11:
    time.sleep(1)
    IATA=input("[::] Please enter the IATA of the airport: ")
    while IATA == None:
        print("[!] Invalid IATA !")
        time.sleep(1)
        IATA=input("[::] Please enter again the IATA of the airport: ")
    time.sleep(1)
    IATA=IATA.upper()
    reviews=FData.get_airport_reviews(IATA)
    time.sleep(2)
    print("[+] Reviews for the airport: "+str(reviews))
elif option == 12:
    time.sleep(1)
    IATA=input("[::] Please enter the IATA of the airport: ")
    while IATA == None:
        print("[!] Invalid IATA !")
        time.sleep(1)
        IATA=input("[::] Please enter again the IATA of the airport: ")
    time.sleep(1)
    IATA=IATA.upper()
    stats=FData.get_airport_stats()
    time.sleep(2)
    print("[+] Stats for the requested airport: "+str(stats))
elif option == 13:
    time.sleep(1)
    zones=FRadar.get_zones()
    time.sleep(2)
    print("[+] Zones: "+str(zones))
elif option == 14:
    time.sleep(1)
    flight=FRadar.get_real_time_flight_tracker_config()
    time.sleep(2)
    print("[+] Current Flight: "+str(flight))
else:
    print("[+] Exiting...")
    exit(0)
