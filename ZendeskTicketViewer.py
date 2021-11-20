import requests
from requests.sessions import TooManyRedirects

def printTicket(ticketsArr, index):
    print("Ticket " + str(index + 1) + " with subject \"" + ticketsArr["tickets"][index]["subject"] + "\"")
    print("Created at: " + ticketsArr["tickets"][index]["created_at"])
    print("Requester ID: " + str(ticketsArr["tickets"][index]["requester_id"]))
    print("Assignee ID: " + str(ticketsArr["tickets"][index]["assignee_id"]))

def printTicketDetails(ticketsArr, index):
    print("------------------------------------------------------------")
    print("Ticket " + str(index + 1))
    print("Subject: \"" + ticketsArr["tickets"][index]["subject"] + "\"")
    print("Created at: " + ticketsArr["tickets"][index]["created_at"])
    print("Requester ID: " + str(ticketsArr["tickets"][index]["requester_id"]))
    print("Assignee ID: " + str(ticketsArr["tickets"][index]["assignee_id"]))
    print("Tags: " + str(ticketsArr["tickets"][index]["tags"]))

    print("\nDescription: " + ticketsArr["tickets"][index]["description"])
    print("------------------------------------------------------------")

def main():
    print("Hello and welcome to the Zendesk API ticket viewer coding assesment! Enter your credentials to begin:")

    accessGranted = False
    while (not accessGranted):
        email = str(input("Input your email: "))
        authKey = "TEMP"
        if email == "Y":
            email = "TEMP"
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
    print("Type \'list\' or \'find\' to view tickets, or type \'help\' for help, and \'exit\' to quit")
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
            newPage = True
            while currentFunc != "exit":
                if max > numOfTickets:
                    max = numOfTickets
                if newPage:
                    print("---------------------------------------")
                    for i in range(min, max):
                        printTicket(tickets, i)
                        print("---------------------------------------")
                if (min == 0 and max == numOfTickets):
                    currentFunc = "exit"
                elif min == 0:
                    currentFunc = input("Enter a command: \'next\' for next page, \'exit\' to exit list view\n")
                elif max == numOfTickets:
                    currentFunc = input("Enter a command: \'prev\' for previous page, \'exit\' to exit list view\n")
                else:
                    currentFunc = input("Enter a command: \'next\' for next page, \'prev\' for previous page, \'exit\' to leave list view\n")
                if currentFunc == "next" and max != numOfTickets:
                    min += 15
                    max += 15
                    newPage = True
                elif currentFunc == "prev" and min != 0:
                    min -= 15
                    max = min + 15
                    newPage = True
                elif currentFunc != "exit":
                    print("Please enter a valid command!")
                    newPage = False
            
        elif currentFunc == "find":
            numOfTickets = len(tickets["tickets"])
            while currentFunc != "exit":
                currentFunc = input("What ticket number would you like to lookup? Or type \'exit\' to leave find view\n")
                if currentFunc == "exit":
                    break
                index = -1
                try:
                    index = int(currentFunc)
                    if index >= 1 and index <= numOfTickets:
                        printTicketDetails(tickets, index - 1)
                    else:
                        print("Please enter a valid index (1 - # of tickets)! Or type \'exit\' to leave find view.")
                except:
                    print("Please enter an integer value index or type \'exit\' to leave find view!")
                
        else:
            print("Please enter a valid command!")
        currentFunc = str(input("Type \'list\' or \'find\' to view tickets, or type \'help\' for help, and \'exit\' to quit\n"))

    print("Thank you for using the Zendesk API ticket viewer! Have a nice day.")

main()