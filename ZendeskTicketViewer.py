import requests
from requests.sessions import TooManyRedirects

def printTicket(ticketsArr, index):
    print(str(index + 1) + ": " + ticketsArr["tickets"][index]["subject"])

def main():
    print("Hello and welcome to the Zendesk API ticket viewer coding assesment! Enter your credentials to begin:")

    accessGranted = False
    while (not accessGranted):
        email = str(input("Input your email: "))
        authKey = "0TGCws2yIfaZrcIAmdUzuOAGaPkhYozJJZS0UG9u"
        if email == "Y":
            email = "ehopper3@gatech.edu"
        else:
            authKey = str(input("Input your auth token: "))
        
        url = "https://zccelijah.zendesk.com/api/v2/tickets.json"

        try:
            response = requests.get(url, auth=(email+"/token", authKey))
            if response:
                print("Access granted!")
                accessGranted = True
            else:
                print("Error " + str(response.status_code + ". Please try again."))
        except:
            print("Unknown error!")

    print("------------------------------------------------------------------------------------")
    print("Type \'help\' for a list of avaliable functions. Type \'exit\' to end the program.")
    currentFunc = str(input())
    tickets = response.json()
    while (currentFunc != "exit"):
        if currentFunc == "help":
            print("\n|---------------------------------------|")
            print("|\tThis is the help guide!\t\t|")
            print("| \'exit\' - quits the program            |")
            print("| \'list\' - lists all tickets            |")
            print("| \'find\' - finds one specific ticket    |")
            print("|---------------------------------------|\n")
        elif currentFunc == "list":
            numOfTickets = len(tickets["tickets"])
            min = 0
            max = 15
            while currentFunc != "exit":
                if max > numOfTickets:
                    max = numOfTickets
                print("---------------------------------------")
                for i in range(min, max):
                    printTicket(tickets, i)
                print("---------------------------------------")
                if (min == 0 and max == numOfTickets):
                    currentFunc = "exit"
                elif min == 0:
                    currentFunc = input("Enter a command: \'next\' for next page, \'exit\' to exit\n")
                elif max == numOfTickets:
                    currentFunc = input("Enter a command: \'prev\' for previous page, \'exit\' to exit\n")
                else:
                    currentFunc = input("Enter a command: \'next\' for next page, \'prev\' for previous page, \'exit\' to exit\n")
                if currentFunc == "next" and max != numOfTickets:
                    min += 15
                    max += 15
                elif currentFunc == "prev" and min != 0:
                    min -= 15
                    max = min + 15
                elif currentFunc != "exit":
                    print("Please enter a valid command!")
            
        elif currentFunc == "find":
            indexToFind = -1
            while currentFunc != "exit":
                currentFunc = input("What ticket number would you like to lookup?\n")
                if currentFunc == "exit":
                    break
                index = -1
                try:
                    index = int(currentFunc)
                    if index >= 1 and index <= numOfTickets:
                        printTicket(tickets, index - 1)
                    else:
                        print("Please enter a valid index! (1 - # of tickets)")
                except:
                    print("Please enter an integer value index or type \'exit\' to exit!")
                
        else:
            print("Please enter a valid command!")
        currentFunc = str(input("Input your next command (\'help\' for help, \'exit\' to quit):\n"))

    print("Thank you for using the Zendesk API ticket viewer! Have a nice day.")

main()