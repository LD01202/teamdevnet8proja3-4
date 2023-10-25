"""
This source code was made by
Fajardo, Cill Tristan
Feliciano, Bernard Angeliko
Galang, Lorenzo Daniel
Segundo, Mellicent
4ITA

In fulfillment of project activity 3
given on Oct 23 2023
for IT26210 - System Integration

API used is from ipapi.co

"""

from termcolor import colored, cprint
from datetime import datetime
from requests import get
import json
import os

choice=0
again=True

print_yellow_on_black = lambda x: cprint(x, "yellow", "on_black")
print_red_on_black = lambda x: cprint(x,"red", "on_black")
print_magenta_on_black = lambda x: cprint(x,"magenta","on_black")
print_cyan_on_black_bold = lambda x: cprint(x,"cyan","on_black",attrs=["bold"])

print_magenta_on_black("=================================================================")
print_magenta_on_black("Project Activity 4 - October 23 2023")
print_magenta_on_black("Python Application to Get IP Information \nof Current Machine")
print_magenta_on_black("By Team Devnet 8 - 4ITA\n")
print_magenta_on_black("Fajardo, Cill Tristan")
print_magenta_on_black("Feliciano, Bernard Angeliko")
print_magenta_on_black("Galang, Lorenzo Daniel")
print_magenta_on_black("Segundo, Mellicent\n")
print_magenta_on_black("========================START OF PROGRAM=========================")

def case_1():
    logC=False
    info = get('https://ipapi.co/json/')
    report = json.dumps(info.json(), indent=4)
    print_yellow_on_black (report)
    print_cyan_on_black_bold("\nDone printing complete IP and location information of current machine.")
    
    mkFile(report)
    logC=True
    return logC

def case_2():
    logC2 = False
    info = get('https://ipapi.co/ip/').text
    print_yellow_on_black("IP Address of current machine: " + info)
    
    info = get('https://ipapi.co/asn/').text
    print_yellow_on_black("ASN (Autonomous System Number): " +info)
    
    info = get('https://ipapi.co/org/').text
    print_yellow_on_black("ISP (Internet Service Provider): " +info)
    print_cyan_on_black_bold("\nDone printing public IP address and ISP of current machine.")

    logC2 = True
    return logC2

def case_3():
    logC3 = False
    info = get('https://ipapi.co/country_name/').text
    print_yellow_on_black("Country: "+info)

    info = get('https://ipapi.co/country_capital/').text
    print_yellow_on_black("Country Capital: "+info)

    info = get('https://ipapi.co/country_calling_code/').text
    print_yellow_on_black("Country Calling Code: "+info)

    info = get('https://ipapi.co/country/').text
    print_yellow_on_black("Country Code (2 letter, ISO 3166-1 alpha-2): "+info)

    info = get('https://ipapi.co/country_code/').text
    print_yellow_on_black("Country Code (2 letter, ISO 3166-1 alpha-2): "+info)
    
    info = get('https://ipapi.co/country_code_iso3/').text
    print_yellow_on_black("Country Code (3-Letter, ISO 3166-1 alpha-3): "+info)

    info = get('https://ipapi.co/country_tld/').text
    print_yellow_on_black("Country TLD: "+info)

    info = get('https://ipapi.co/country_area/').text
    print_yellow_on_black("Country Area: "+info)

    info = get('https://ipapi.co/country_population/').text
    print_yellow_on_black("Country Population: "+info)
    
    info = get('https://ipapi.co/region/').text
    print_yellow_on_black("Region "+info)
    
    info = get('https://ipapi.co/region_code/').text
    print_yellow_on_black("Region Code: "+info)
    
    info = get('https://ipapi.co/city/').text
    print_yellow_on_black("City: "+info)
    
    info = get('https://ipapi.co/postal/').text
    print_yellow_on_black("Postal Code: "+info)

    info = get('https://ipapi.co/continent_code/').text
    print_yellow_on_black("Continent Code: "+info)

    info = get('https://ipapi.co/in_eu/').text
    print_yellow_on_black("inside EU?: "+info)

    print_cyan_on_black_bold("\nDone printing locale information information of current machine.")
    logC3=True
    return logC3

def case_4():
    logC4 = False
    info = get('https://ipapi.co/timezone/').text
    print_yellow_on_black("Timezone: " + info)

    info = get('https://ipapi.co/utc_offset/').text
    print_yellow_on_black("UTC Offset: " + info)

    info = get('https://ipapi.co/latlong/').text
    print_yellow_on_black("Latitude/Longitude: " +info)

    print_cyan_on_black_bold("\nDone printing timezone and coordinates information of current machine.")
    logC4 = True
    return logC4

def case_5():
    logC5 = False
    info = get('https://ipapi.co/currency_name/').text
    print_yellow_on_black("Currency: " +info)

    info = get('https://ipapi.co/currency/').text
    print_yellow_on_black("Currency Code: " +info)

    info = get('https://ipapi.co/languages/').text
    print_yellow_on_black("Languages: " + info)

    print_cyan_on_black_bold("\nDone printing currency and languages information of current machine.")
    logC5=True
    return logC5

def inv_case():
    inv = False
    print_red_on_black("Not a valid option")
    inv = True
    return inv

def mkFile(reportout):
    ver = True
    now = datetime.now()
    dateString = now.strftime("%Y") + "-" + now.strftime("%m") + "-" + now.strftime("%d") + " " + now.strftime("%H%M%S")
    logName = "LOGFILE "+dateString+".txt"
    try:
        f = open(os.path.join("log_ipinfogetter",logName), "x")
        f.write(reportout)
        print_cyan_on_black_bold("log file located in log_ipinfogetter/" + logName)
    except FileExistsError:
        print_red_on_black("\nDirectory log does not exist. Please check current working directory")
        ver = False  
    return ver  

while(again):
    print(colored("[1] Complete IP Address and Location Information","green",attrs=["bold"]))
    print(colored("[2] Public IP Address ASN/ISP Information","green",attrs=["bold"]))
    print(colored("[3] Country Information","green",attrs=["bold"]))
    print(colored("[4] Timezone and Coordinates Information","green",attrs=["bold"]))
    print(colored("[5] Currency and Languages Information","green",attrs=["bold"]))
    choice = input ( colored("Please choose which information set to get:","cyan",attrs=["bold"]))
    match choice:
        case "1":
            case_1()
        case "2":
            case_2()
        case "3":
            case_3()
        case "4":
            case_4() 
        case "5":
            case_5()
        case _:
            inv_case()
    
    loop2 = True
    while(loop2):
        choice = input(colored("\nWould you like to run the program again?[Y/N]: ","cyan",attrs=["bold"]))
        if(choice.lower() == "y"):
            again = True
            loop2=False
        elif(choice.lower() == "n"):
            again = False
            print_yellow_on_black("Exitting")
            break
        else:
            again = False
            print_red_on_black("Unknown Command. Please input Y or N only.")
