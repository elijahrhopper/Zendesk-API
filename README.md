# Zendesk-API
Welcome to the Zendesk coding challenge to implement an interface that interacts with Zendesk's ticket viewer API!

I created a command line interface (CLI) that interacts with the Zendesk API. It pulls tickets from the user's account and displays them either on pages of 25 tickets each, or in a more detailed view of each one. The "list" command lists 25 at a time on pages, and the "find" command can pull up any one ticket with more detail. At any point in the interface, the user can type "exit" to exit the current command, or to terminate the entire interface. The interface also provides feedback messages for invalid commands, unsuccessful server connections, out of bound indices (for the find command), among other messages.

To run this interface, you will need to have python installed, and the requests library for python. To install requests, simply type "python -m pip install requests" into your terminal.

To run unit tests, use pytest by typing "pytest test_ZendeskTicketViewer.py" into the current directory terminal
