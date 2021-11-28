from datetime import datetime
from exceptions import AuthorizeException, ValueNotFoundException, ForbiddenException
import sys

from zendesk import getAllTicketswithPaging, getTicketById

def parsingFunction(data):
    """
    this function takes data from api which includes all fields and parse into the string which is easy to read.
    """
    #Extracting data from raw api endpoint data we get from zendest api for ticket
    id = data["id"]
    subject = data["subject"]
    requester_id = data["requester_id"]
    created_at = data["created_at"]
    status = data["status"]
    #Formatting the date to be read easily by others in "date Month(shortest form) Year" format
    created_date = datetime.fromisoformat(created_at.replace("Z",""))
    format_date = created_date.strftime("%d %b %Y")
    #Simple string shown to end user after formatting the raw data
    parsedData = f"Ticket with id '{id}' is opened by '{requester_id}' with subject '{subject}' on '{format_date}' with status '{status}'"
    return parsedData

def parseSingleTicket(ticket_id):
    """
    this function helps to parse the details of ticket by id coming from zendesk api and handles any exceptions if present.
    returns: single parsed ticket data
    """
    parsedData = ""
    try:
        # get ticket details from zendesk api
        data = getTicketById(ticket_id)
        parsedData = parsingFunction(data)
    except ValueNotFoundException:
        print(f"value with id {ticket_id} is not found.....")
    except AuthorizeException:
        print("Could not authorize you.....Please check credentials")
        sys.exit()
    except Exception:
        print("Something went wrong.....Please check url and credentials once...")
        sys.exit()
    return parsedData

def printSingleTicket(ticket_id):
    """
    this function just prints the data received from below used function "parseSingleTicket"
    """
    data = parseSingleTicket(ticket_id)
    print("\n" + data, end = "\n")
    
def parseMultipleTickets(page):
    """
    this function helps to parse the details of mutliple tickets coming from zendesk api with given page limit
    returns: list of parsed tickets, total tickets count in all pages, next page details, previous page details, limit per page
    """
    #list of parsed tickets with limit given as requirement i.e., 25
    full_parsed_data = []
    #next page details
    next = ""
    #previous page details
    previous = ""
    #total tickets count in all pages
    total_tickets_count = 0
    try:
        data, count, next_page, prev_page, limit_per_page = getAllTicketswithPaging(page)
        # get tickets details from zendesk api only if atleast 1 ticket is present else return empty list of tickets
        if(len(data) > 0):
            for i in range(0,len(data)):
                #Extracting data from raw api endpoint data we get from zendest api for tickets
                parsedData = parsingFunction(data[i])
                full_parsed_data.append(parsedData)
                #next page details
                next = next_page
                #previous page details
                previous = prev_page
                #get all tickets count
                total_tickets_count = count
    except AuthorizeException:
        print("Could not authorize you.....Please check credentials")
        sys.exit()
    except Exception:
        print("Something went wrong.....Please check url and credentials once...")
        sys.exit()
    return full_parsed_data, total_tickets_count, next, previous, limit_per_page

def printMultipleticketswithPaging(page):
    """
    this function just prints the data received from below used function "parseMultipleTickets"
    input param : taking input param as "page" to display content of particular page if more than 25 tickets are returned from api
    """
    data, count, next_page, previous_page, limit_per_page = parseMultipleTickets(page)
    # if data is present then only we need to print otherwise no data
    if(len(data) > 0):
        #to count total number of pages with limit 25 per page
        if(count%limit_per_page == 0):
            total_pages = count/limit_per_page;
        else:
            total_pages = int(count/limit_per_page) + 1;
        #print the data in 25 and page label with next and prev page details
        for i in range(0,len(data)):
            print("\n" + data[i])
        print(f"\n========== Page {page} of {total_pages} ==========")
        print(f"\nNext page = {next_page}\nPrevious page = {previous_page}")
        #Based on next page and prev page details multiple options are made available to end user to procedd further or quit or go to previous list
        if next_page != None and previous_page == None:
            print("\nType 'next' for Next 25 Tickets or 'q' to quit")
            #funtion that handles the inputs given by the user when this method call happens. Inputs should be entered as it suggested by above print statement  in cli 
            inputs_for_next_prev_quit_for_pages(page, next_page, previous_page)
        elif next_page != None and previous_page != None:
            print("\nType 'next' for Next 25 Tickets or 'prev' for previous 25 Tickets or 'q' to quit")
            #funtion that handles the inputs given by the user when this method call happens. Inputs should be entered as it suggested by above print statement in cli 
            inputs_for_next_prev_quit_for_pages(page, next_page, previous_page)
        elif previous_page != None and next_page == None:
            print("\n\tAll tickets printed.....")
            print("\nType 'prev' for previous 25 Tickets or 'q' to quit")
            #funtion that handles the inputs given by the user when this method call happens. Inputs should be entered as it suggested by above print statement  in cli 
            inputs_for_next_prev_quit_for_pages(page, next_page, previous_page)
        else:
            print("\n\tThese are the tickets available to print.....")
    else:
        print("No data to print..")

def inputs_for_next_prev_quit_for_pages(page, next_page, previous_page):
    """
    this function just asks input for next, prev or quit
    """
    option = input("Enter your option: ")
    if option == "next" and next_page != None:
        printMultipleticketswithPaging(page+1)
    elif option == "prev" and previous_page != None:
        printMultipleticketswithPaging(page-1)
    elif option == "q":
        print("quit")
    else:
        print("wrong input entered..please try again..")
        inputs_for_next_prev_quit_for_pages(page, next_page, previous_page)

