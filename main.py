from helper_methods import select_menu_option
import sys

def menu(option):
    """
    displays menu options and ask inputs from user
    """
    if(option == "menu"):
        while True:
            print("\n\t*Select any of the following options")
            print("\tPress 1 to view all tickets")
            print("\tPress 2 to view specific ticket")
            print("\tPress 3 to quit", end = "\n\n")
            #method will return other inputs based on input provided above
            select_menu_option()
    elif option == "q":
        print("Thanks for using Zendesk ticket viewer....Bye")
        sys.exit()
    else:
        print("please enter valid option....\n")
        option_again = input("Enter your option: ")
        menu(option_again)

if __name__ == "__main__":
    print("Welcome to Zendesk ticket viewer....", end="\n\n")
    print("Type menu for options or 'q' to quit")
    option = input("Enter your option: ")
    menu(option)
