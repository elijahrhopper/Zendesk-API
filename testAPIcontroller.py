import json
import requests
from requests import auth
#import argparse

def main():
    print("Welcome to the Zendesk API coding assesment! Enter your credentials to begin:")
    email = str(input("Input your email: "))
    authKey = "0TGCws2yIfaZrcIAmdUzuOAGaPkhYozJJZS0UG9u"
    if email == "Y":
        email = "ehopper3@gatech.edu"
    else:
        authKey = str(input("Input your auth token: "))

    url = "https://zccelijah.zendesk.com/api/v2/tickets.json"
    response = requests.get(url, auth=(email+"/token", authKey))

    

    tickets = response.json()
    for i in range(100):
        print(str(i) + ": " + tickets["tickets"][i]["subject"])
    
    if response:
        print('Response OK')
    else:
        print('Response Failed with error ' + str(response.status_code))

main()