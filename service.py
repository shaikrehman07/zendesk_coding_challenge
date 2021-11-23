from datetime import datetime
from exceptions import AuthorizeException, ValueNotFoundException, ForbiddenException
import sys

from zendesk import getAllTicketswithPaging, getTicketById

def parseSingleTicket(ticket_id):
    parsedData = ""
    try:
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
        print("Something went wrong.....Please check url once...")
        sys.exit()
    return parsedData
    
def parseMultipleTickets(page):
    full_parsed_data = []
    next = ""
    previous = ""
    try:
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
    
                parsedData = f"Ticket {id} is opened by '{requester_id}' with subject '{subject}' on '{format_date}' with status '{status}'"
                full_parsed_data.append(parsedData)
                next = data["next_page"]
                previous = data["previous_page"]
    except AuthorizeException:
        print("Could not authorize you.....Please check credentials")
        sys.exit()
    except Exception:
        print("Something went wrong.....Please check url once...")
        sys.exit()
    return full_parsed_data, next, previous

def printSingleTicket(ticket_id):
    data = parseSingleTicket(ticket_id)
    print("\n" + data, end = "\n\n")

def printMultipleticketswithPaging(page):
    data, next_page, previous_page = parseMultipleTickets(page)
    if(len(data) > 0):
        for i in range(0,len(data)):
            print("\n" + data[i])
        print(f"\nNext page = {next_page}\nPrevious page = {previous_page}")
    else:
       print("No data to print..")
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
    elif previous_page != None:
        print("\n\tAll tickets are printed.......")
        print("\nType 'prev' for previous 25 Tickets or 'q' to quit")
        next_input = input("Enter your option: ")
        if(next_input == "next"):
            printMultipleticketswithPaging(page-1)
        elif(next_input == "q"):
            print('quit')
    else:
        print("\nType 'q' to quit")
        next_input = input("Enter your option: ")
        if(next_input == 'q'):
            print("quit")
    
