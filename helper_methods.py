from service import parseMultipleTickets, parseSingleTicket, printMultipleticketswithPaging, printSingleTicket
from zendesk import getAllTicketswithPaging, getTicketById
import sys

def select_menu_option():
    """
    function to provide further options based on earlier options provided bu user
    """
    option1 = input("Enter your option: ")
    if option1 == '1':
        page = 1
        #this method prints the first page data by default and ask for next instructions to print next page or previous page details
        printMultipleticketswithPaging(page)
    elif option1 == '2':
        #valids and print the ticket details if the provided ticket id is valid input
        ticket_id_input()
    elif option1 == '3':
        #if 3 entered it quits the program
        print("Thanks for using ticket viewer...Bye")
        sys.exit()
    elif option1 == "":
        #if no option entered
        print("\n\toption is not entered....")
        print("\tPlease try again....\n")
        # ask input again if not entered correctly
        select_menu_option()
    else:
        #if entered wrong input then it will ask the input again
        print("\n\toption entered is wrong....")
        print("\tPlease try again....\n")
        # ask input again if not entered correctly
        select_menu_option()

def ticket_id_input():
        ticket_option = input("\nEnter ticket id: ")
        #prints the data with ticket id provided if it is valid input
        if(ticket_option.isdecimal()):
            printSingleTicket(ticket_option)
        else:
            print("wrong ticket id typed....")
            ticket_id_input()