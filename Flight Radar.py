"""
Author: @new92
Flight Radar is a program which contains many useful tools for airplanes, airports, departures, arrivals etc.
"""

#Imports
try:
    import sys
    import os
    import requests
    import sniffer
    import http
    import socket
    import cryptography
    import crypto
    import instagrapi
    import pyfiglet
    import time
    import smtplib
    import geocoder
    import json
    import getpass
    import locale
    import random
    import subprocess
    import platform
    import datetime
    import scapy
    import Cryptodome
    import time
    import pyflightdata
    from FlightRadar24.api import FlightRadar24API
    from pyflightdata import FlightData
    from os import system
except ImportError as imp:
    print("[!] WARNING: Not all modules used in this program have been installed !")
    time.sleep(1)
    print("[+] Ignoring Warning...")
    time.sleep(1)
    if platform.system == "Windows":
        system("pip3 install -r requirements.txt")
    else:
        system("sudo pip3 install -r requirements.txt")

#End of Imports

#LOGO
radar=pyfiglet.figlet_format("FLIGHT RADAR")
print(radar)
#

#Main program
print("[+] Program for Fligh")
print("\n")
print("[+] Github: @new92")
print("\n")
print("[01] Airports")
print("[02] Airlines")
print("[03] Flights")
print("[04] Airline Logo")
print("[05] Country Flags")
print("[06] Information for Specific Flights")
print("[07] Information for Specific Airports")
print("[08] Arrivals of an Airport")
print("[09] Departures of an Airport")
print("[10] Weather of an Airport")
print("[11] Airport Reviews")
print("[12] Airport Stats")
print("[13] Zones")
print("[14] Current Flight(s)")
print("[15] Exit")
print("\n")
option=input("[::] Choose an option: ")
FRadar = FlightRadar24API()
FData = FlightData()
while option != "01" and option != "1" and option != "02" and option != "2" and option != "03" and option != "3" and option != "04" and option != "4" and option != "05" and option != "5" and option != "06" and option != "6" and option != "07" and option != "7" and option != "08" and option != "8" and option != "09" and option != "10" and option != "11" and option != "12" and option != "13" and option != "14" and option != "15":
    time.sleep(1)
    print("[!] Invalid option !")
    time.sleep(1)
    option=input("[+] Please enter again: ")
if option == "01" or option == "1":
    time.sleep(1)
    airports=FRadar.get_airports()
    time.sleep(2)
    print("[+] Airports: "+str(airports))
elif option == "02" or option == "2":
    time.sleep(1)
    airlines=FRadar.get_airlines()
    time.sleep(2)
    print("[+] Airlines: "+str(airlines))
elif option == "03" or option == "3":
    time.sleep(1)
    flights=FRadar.get_flights()
    time.sleep(2)
    print("[+] Flights: "+str(flights))
elif option == "04" or option == "4":
    time.sleep(1)
    IATA=input("[+] Please enter the IATA of the airline: ")
    time.sleep(2)
    IATAU1=IATA.upper()
    ICAO=input("[+] Please enter the ICAO of the airline: ")
    time.sleep(2)
    ICAO1=ICAO.upper()
    logo=FRadar.get_airline_logo(IATAU1,ICAO1)
    time.sleep(1)
    print("[+] The logo is available in this link: "+str(logo))
elif option == "05" or option == "5":
    time.sleep(1)
    country_name=input("[+] Please enter the name of the country: ")
    time.sleep(1)
    FRadar.get_country_flag(country_name)
    time.sleep(2)
    print("[+] The flag of the given country is available in this link: "+str(country_name))
elif option == "06" or option == "6":
    time.sleep(1)
    FID=input("[+] Please enter the flight ID: ")
    time.sleep(1)
    dets=FRadar.get_flight_details(FID)
    time.sleep(2)
    print("[+] Details of the flight: "+str(dets))
elif option == "07" or option == "7":
    time.sleep(1)
    IATA1=input("[+] Please enter the IATA of the airport: ")
    time.sleep(1)
    IATAU=IATA1.upper()
    airport_dets=FData.get_airport_details(IATAU)
    time.sleep(2)
    print("[+] Details of the given airport: "+str(airport_dets))
elif option == "08" or option == "8":
    time.sleep(1)
    IATA2=input("[+] Please enter the IATA of the airport: ")
    time.sleep(1)
    IATAU2=IATA2.upper()
    arrivals=FData.get_airport_arrivals(IATAU2)
    time.sleep(2)
    print("[+] Arrivals of the given airport: "+str(arrivals))
elif option == "09" or option == "9":
    time.sleep(1)
    IATA3=input("[+] Please enter the IATA of the airport: ")
    time.sleep(1)
    IATAU3=IATA3.upper()
    departures=FData.get_airport_departures(IATAU3)
    time.sleep(2)
    print("[+] Departures of the given airport: "+str(departures))
elif option == "10":
    time.sleep(1)
    IATA4=input("[+] Please enter the IATA of the airport: ")
    time.sleep(1)
    IATAU4=IATA4.upper()
    weather=FData.get_airport_weather(IATAU4)
    time.sleep(2)
    print("[+] The weather of the given airport: "+str(weather))
elif option == "11":
    time.sleep(1)
    IATA5=input("[+] Please enter the IATA of the airport: ")
    time.sleep(1)
    IATAU5=IATA5.upper()
    reviews=FData.get_airport_reviews(IATAU5)
    time.sleep(2)
    print("[+] Reviews for the given airport: "+str(reviews))
elif option == "12":
    time.sleep(1)
    IATA6=input("[+] Please enter the IATA of the airport: ")
    time.sleep(1)
    IATAU6=IATA6.upper()
    stats=FData.get_airport_stats()
    time.sleep(2)
    print("[+] Stats for the given airport: "+str(stats))
elif option == "13":
    time.sleep(1)
    zones=FRadar.get_zones()
    time.sleep(2)
    print("[+] Zones: "+str(zones))
elif option == "14":
    time.sleep(1)
    flight=FRadar.get_real_time_flight_tracker_config()
    time.sleep(2)
    print("[+] Current Flight: "+str(flight))
else:
    print("[!] Exiting...")
    exit(0)
#End of the Program
