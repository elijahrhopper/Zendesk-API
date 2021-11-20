import requests

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
    print("Type \'help\' for a list of avaliable functions. Type \'exit\' to end the program.")
    currentFunc = str(input())
    response = None
    while (currentFunc != "exit"):
        if currentFunc == "help":
            print("\n|---------------------------------------|")
            print("|\tThis is the help guide!\t\t|")
            print("| \'exit\' - quits the program            |")
            print("| \'list\' - lists all tickets            |")
            print("| \'find\' - finds one specific ticket    |")
            print("|---------------------------------------|\n")
        elif currentFunc == "list":
            print("list")
        elif currentFunc == "find":
            print("find")
        else:
            print("Please enter a valid command!")
        currentFunc = str(input("Input your next command (\'help\' for help, \'exit\' to quit):\n"))

    print("Thank you for using the Zendesk API ticket viewer! Have a nice day.")

main()