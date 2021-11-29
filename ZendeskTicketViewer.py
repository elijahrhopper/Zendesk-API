import requests

def printTicket(ticketsArr, index):
    print("Ticket " + str(index + 1) + " with subject \"" + ticketsArr["tickets"][index]["subject"] + "\"")
    print("Created at: " + ticketsArr["tickets"][index]["created_at"])
    print("Requester ID: " + str(ticketsArr["tickets"][index]["requester_id"]))
    print("Assignee ID: " + str(ticketsArr["tickets"][index]["assignee_id"]))

def printTicketDetails(ticketsArr, index):
    print("\n------------------------------------------------------------")
    print("Ticket " + str(index + 1))
    print("Subject: \"" + ticketsArr["tickets"][index]["subject"] + "\"")
    print("Created at: " + ticketsArr["tickets"][index]["created_at"])
    print("Requester ID: " + str(ticketsArr["tickets"][index]["requester_id"]))
    print("Assignee ID: " + str(ticketsArr["tickets"][index]["assignee_id"]))
    print("Tags: " + str(ticketsArr["tickets"][index]["tags"]))

    print("\nDescription: " + ticketsArr["tickets"][index]["description"])
    print("------------------------------------------------------------\n")

def login():
    while (True):
        email = str(input("Input your email: "))
        authKey = "TEMP"
        if email == "Y":
            email = "TEMP"
        elif email == "exit":
            print("Thank you for using the Zendesk API ticket viewer! Goodbye!")
            exitCLI()
        else:
            authKey = str(input("Input your auth token: "))
        
        url = "https://zccelijah.zendesk.com/api/v2/tickets.json"

        try:
            response = requests.get(url, auth=(email+"/token", authKey))
        except:
            print("API is not avaliable at this time, please try again later!")
            continue
        if response:
            print("Access granted!")
            return response
        else:
            errorCode = response.status_code
            if errorCode == 401:
                print("Credentials not authorized to access server! Please try again or type \'exit\' to close the program")
            else:
                print("Error " + str(errorCode) + ". Please try again.")

def help(tickets):
    print("\n|---------------------------------------|")
    print("|\tThis is the help guide!\t\t|")
    print("| \'exit\' - quits the program            |")
    print("| \'list\' - lists all tickets            |")
    print("| \'find\' - finds one specific ticket    |")
    print("|---------------------------------------|\n")

def exitCLI(tickets):
    print("Thank you for using the Zendesk API ticket viewer! Have a nice day.")
    exit()

def listTickets(tickets):
    numOfTickets = len(tickets["tickets"])
    min = 0
    max = 25
    newPage = True
    currentFunc = ""
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
            min += 25
            max += 25
            newPage = True
        elif currentFunc == "prev" and min != 0:
            min -= 25
            max = min + 25
            newPage = True
        elif currentFunc != "exit":
            print("Please enter a valid command!")
            newPage = False

def findTicket(tickets):
    numOfTickets = len(tickets["tickets"])
    currentFunc = ""
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

def main():
    print("Hello and welcome to the Zendesk API ticket viewer coding assesment! Enter your credentials to begin:")

    response = login()
    tickets = response.json()

    functions = {"help": help, "exit": exitCLI, "list": listTickets, "find": findTicket}

    while True:
        print("------------------------------------------------------------------------------------")
        print("Type \'list\' or \'find\' to view tickets, or type \'help\' for help, and \'exit\' to quit")
        currentFunc = str(input())
        if currentFunc in functions:
            functions[currentFunc](tickets)
        else:
            print("Please enter a valid command!")

main()