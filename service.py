from datetime import datetime
from exceptions import AuthorizeException, ValueNotFoundException, ForbiddenException
import sys

from zendesk import getAllTicketswithPaging, getTicketById

def parseSingleTicket(ticket_id):
    """
    this function helps to parse the details of ticket by id coming from zendesk api as per programmer requirement
    returns: single parsed ticket data
    """
    parsedData = ""
    try:
        # get ticket details from zendesk api
        data = getTicketById(ticket_id)
        #Extracting data from raw api endpoint data we get from zendest api for ticket by id
        subject = data["ticket"]["subject"]
        requester_id = data["ticket"]["requester_id"]
        created_at = data["ticket"]["created_at"]
        status = data["ticket"]["status"]
        #Formatting the date to be read easily by others in "date Month(shortest form) Year" format
        created_date = datetime.fromisoformat(created_at.replace("Z",""))
        format_date = created_date.strftime("%d %b %Y")
        #Simple string shown to end user after formatting the raw data
        parsedData = f"Ticket is opened by '{requester_id}' with subject '{subject}' on '{format_date}' with status '{status}'"
    except ValueNotFoundException:
        print(f"value with id {ticket_id} is not found.....")
    except AuthorizeException:
        print("Could not authorize you.....Please check credentials")
        sys.exit()
    except Exception:
        print("Something went wrong.....Please check url and credentials once...")
        sys.exit()
    return parsedData
    
def parseMultipleTickets(page):
    """
    this function helps to parse the details of mutliple tickets coming from zendesk api with given page as per programmer requirement
    returns: list of parsed tickets, next page details, previous page details
    """
    full_parsed_data = []
    next = ""
    previous = ""
    try:
        # get tickets details from zendesk api only if atleast 1 ticket is present else return empty list of tickets
        data = getAllTicketswithPaging(page)
        if(len(data["tickets"]) > 0):
            for i in range(0,len(data["tickets"])):
                #Extracting data from raw api endpoint data we get from zendest api for tickets
                id = data["tickets"][i]["id"]
                subject = data["tickets"][i]["subject"]
                requester_id = data["tickets"][i]["requester_id"]
                created_at = data["tickets"][i]["created_at"]
                status = data["tickets"][i]["status"]
                #Formatting the date to be read easily by others in "date Month(shortest form) Year" format
                created_date = datetime.fromisoformat(created_at.replace("Z",""))
                format_date = created_date.strftime("%d %b %Y")
                #Simple string shown to end user after formatting the raw data
                parsedData = f"Ticket {id} is opened by '{requester_id}' with subject '{subject}' on '{format_date}' with status '{status}'"
                full_parsed_data.append(parsedData)
                #next page details
                next = data["next_page"]
                #previous page details
                previous = data["previous_page"]
    except AuthorizeException:
        print("Could not authorize you.....Please check credentials")
        sys.exit()
    except Exception:
        print("Something went wrong.....Please check url and credentials once...")
        sys.exit()
    return full_parsed_data, next, previous

def printSingleTicket(ticket_id):
    """
    this function just prints the data received from below used function "parseSingleTicket"
    """
    data = parseSingleTicket(ticket_id)
    print("\n" + data, end = "\n\n")

def printMultipleticketswithPaging(page):
    """
    this function just prints the data received from below used function "parseMultipleTickets"
    input param : taking input param as "page" to display content of particular page if more than 25 tickets are returned from api
    """
    data, next_page, previous_page = parseMultipleTickets(page)
    # if data is present then only we need to print otherwise no data
    if(len(data) > 0):
        for i in range(0,len(data)):
            print("\n" + data[i])
        print(f"\nNext page = {next_page}\nPrevious page = {previous_page}")
    else:
       print("No data to print..")
    #Based on next page and prev page details multiple options are made available to end user to procedd further or quit or go to previous list
    if next_page != None and previous_page == None:
        print("\nType 'next' for Next 25 Tickets or 'q' to quit")
        next_input = input("Enter your option: ")
        if(next_input == "next"):
            printMultipleticketswithPaging(page+1)
        elif(next_input == "q"):
            print('quit')
    elif next_page != None and previous_page != None:
        print("\nType 'next' for Next 25 Tickets or 'prev' for previous 25 Tickets or 'q' to quit")
        next_input = input("Enter your option: ")
        if(next_input == "next"):
            printMultipleticketswithPaging(page+1)
        elif(next_input == "prev"):
            printMultipleticketswithPaging(page-1)
        elif(next_input == "q"):
            print('quit')
    elif previous_page != None and next_page == None:
        print("\n\tAll tickets are printed.......")
        print("\nType 'prev' for previous 25 Tickets or 'q' to quit")
        next_input = input("Enter your option: ")
        if(next_input == "prev"):
            printMultipleticketswithPaging(page-1)
        elif(next_input == "q"):
            print('quit')
    else:
        print("\nType 'q' to quit")
        next_input = input("Enter your option: ")
        if(next_input == 'q'):
            print("quit")
    
