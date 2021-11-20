import requests
from requests import auth
#import argparse

def main():
    print("Welcome to the Zendesk API coding assesment! Enter your credentials to begin:")
    email = str(input("Input your email: "))
    authKey = "insert_auth_key_here"
    if email == "Y":                    #TEMPORARY BYPASS FOR TESTING PURPOSES (TODO: DELETE)
        email = "insert_email_here"
    else:
        authKey = str(input("Input your auth token: "))

    url = "https://zccelijah.zendesk.com/api/v2/tickets.json"
    response = requests.get(url, auth=(email+"/token", authKey))
    
    if response:
        print('Response OK')
    else:
        print('Response Failed with error ' + str(response.status_code))

main()