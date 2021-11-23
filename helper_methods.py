from service import parseMultipleTickets, parseSingleTicket, printMultipleticketswithPaging, printSingleTicket
from zendesk import getAllTicketswithPaging, getTicketById
import sys

def select_menu_option():
    try:
        option1 = input("Enter your option: ")
    except ValueError:
        option1 = None
    if option1 == '1':
        #function to display first 25 tickets
        page = 1
        printMultipleticketswithPaging(page)
    elif option1 == '2':
        #function to dispaly ticket by id
        option2 = input("\nEnter ticket id: ")
        printSingleTicket(option2)
    elif option1 == '3':
        print("Thanks for using ticket viewer...Bye")
        sys.exit()
    elif option1 == "":
        print("\n\toption is not entered....")
        print("\tPlease try again....\n")
        select_menu_option()
    else:
        print("\n\toption entered is wrong....")
        print("\tPlease try again....\n")
        select_menu_option()