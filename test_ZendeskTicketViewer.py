import ZendeskTicketViewer

def test_welcome(capsys):
    tempJson = {}
    expectedOut = "\n|---------------------------------------|\n"
    expectedOut += "|\tThis is the help guide!\t\t|\n"
    expectedOut += "| \'exit\' - quits the program            |\n"
    expectedOut += "| \'list\' - lists all tickets            |\n"
    expectedOut += "| \'find\' - finds one specific ticket    |\n"
    expectedOut += "|---------------------------------------|\n\n"

    ZendeskTicketViewer.help(tempJson)

    out, err = capsys.readouterr()
    assert out == expectedOut
    assert err == ''

def test_ticketPrinter(capsys):
    expectedOutput = "Ticket " + "1" + " with subject \"" + "testTicket" + "\"\n"
    expectedOutput += "Created at: " + "home\n"
    expectedOutput += "Requester ID: " + "eli\n"
    expectedOutput += "Assignee ID: " + "shoo\n"

    testerJson = {"tickets": [{"subject": "testTicket", "created_at": "home", "requester_id": "eli", "assignee_id": "shoo"}]}


    ZendeskTicketViewer.printTicket(testerJson, 0)

    out, err = capsys.readouterr()
    assert out == expectedOutput
    assert err == ''

def test_ticketDetailPrinter(capsys):
    expectedOutput = "\n------------------------------------------------------------\n"
    expectedOutput += "Ticket 1\n"
    expectedOutput += "Subject: \"" + "testTicket" + "\"\n"
    expectedOutput += "Created at: " + "home\n"
    expectedOutput += "Requester ID: " + "eli\n"
    expectedOutput += "Assignee ID: " + "shoo\n"
    expectedOutput += "Tags: " + "[\'apple\', \'orange\']\n"
    expectedOutput += "\nDescription: " + "this is a ticket to test the CLI\n"
    expectedOutput += "------------------------------------------------------------\n\n"

    testerJson = {"tickets": [{"subject": "testTicket", "created_at": "home", "requester_id": "eli", "assignee_id": "shoo", "tags": ["apple", "orange"], "description": "this is a ticket to test the CLI"}]}


    ZendeskTicketViewer.printTicketDetails(testerJson, 0)

    out, err = capsys.readouterr()
    assert out == expectedOutput
    assert err == ''