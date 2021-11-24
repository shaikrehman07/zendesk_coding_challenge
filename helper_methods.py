from service import parseMultipleTickets, parseSingleTicket, printMultipleticketswithPaging, printSingleTicket
from zendesk import getAllTicketswithPaging, getTicketById
import sys

def select_menu_option():
    """
    function to provide further options based on earlier options provided bu user
    """
    try:
        option1 = input("Enter your option: ")
    except ValueError:
        option1 = None
    if option1 == '1':
        #function to display first 25 tickets
        page = 1
        #this method prints the first page data by default and ask for next instructions to print next page or previous page details
        printMultipleticketswithPaging(page)
    elif option1 == '2':
        #function to dispaly ticket by id
        option2 = input("\nEnter ticket id: ")
        #this method prints the data with ticket id provided
        printSingleTicket(option2)
    elif option1 == '3':
        print("Thanks for using ticket viewer...Bye")
        sys.exit()
    elif option1 == "":
        print("\n\toption is not entered....")
        print("\tPlease try again....\n")
        # ask input again if not entered correctly
        select_menu_option()
    else:
        print("\n\toption entered is wrong....")
        print("\tPlease try again....\n")
        # ask input again if not entered correctly
        select_menu_option()