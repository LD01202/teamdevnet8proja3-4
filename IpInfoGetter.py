"""
This source code was made by
Fajardo, Cill Tristan
Feliciano, Bernard Angeliko
Galang, Lorenzo Daniel
Segundo, Mellicent
4ITA

In fulfillment of project activity 3
given on Sept 25 2023
for IT26210 - System Integration

"""


from requests import get
import json

print("Project Activity 3 - September 25 2023")
print("Python Application to Get IP Information \nof Current Machine")
print("By Team Devnet 8 - 4ITA\n")
print("Fajardo, Cill Tristan")
print("Feliciano, Bernard Angeliko")
print("Galang, Lorenzo Daniel")
print("Segundo, Mellicent\n\n")


choice=0
again=True
while(again):
    print("[1] Complete Location Information")
    print("[2] Public IP Address ASN / ISP")
    print("[3] Country/Country Code/Region/Region Code/City/Postal Code")
    print("[4] Timezone/UTC Offset/Latitude/Longitude")
    print("[5] Currency / Languages")
    choice = input ("Please choose what information to get:")
    match choice:
        case "1":
            info = get('https://ipapi.co/json/')
            print (json.dumps(info.json(), indent=4))
            print("Done printing complete location information of current machine.")
            
        case "2":
            info = get('https://ipapi.co/ip/').text
            print("IP Address of current machine: " + info)
            
            info = get('https://ipapi.co/asn/').text
            print("ASN (Autonomous System Number): " +info)
            
            info = get('https://ipapi.co/org/').text
            print("ISP (Internet Service Provider): " +info)
        
        case "3":
            info = get('https://ipapi.co/country_name/').text
            print("Country: "+info)
            
            info = get('https://ipapi.co/country_code_iso3/').text
            print("Country Code "+info)
            
            info = get('https://ipapi.co/region/').text
            print("Region "+info)
            
            info = get('https://ipapi.co/region_code/').text
            print("Region Code: "+info)
            
            info = get('https://ipapi.co/city/').text
            print("City: "+info)
            
            info = get('https://ipapi.co/postal/').text
            print("Postal Code: "+info)
        
        case "4":
            info = get('https://ipapi.co/timezone/').text
            print("Timezone: " + info)
            
            info = get('https://ipapi.co/utc_offset/').text
            print("UTC Offset: " + info)
            
            info = get('https://ipapi.co/latlong/').text
            print("Latitude/Longitude: " +info)
        
        case "5":
            info = get('https://ipapi.co/currency_name/').text
            print("Currency: " +info)
            
            info = get('https://ipapi.co/currency/').text
            print("Currency Code: " +info)
            
            info = get('https://ipapi.co/languages/').text
            print("Languages: " + info)
        
        case _:
            print("Not a valid option")
            
    choice = input("\n\nWould you like to try again?[Y/N]: ")
    if(choice.lower() == "y"):
        again = True
    elif(choice.lower() == "n"):
        again = False
        print("Exitting")
    else:
        again = False
        print("Exitting")
