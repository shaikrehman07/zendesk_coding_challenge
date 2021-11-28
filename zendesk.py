from requests.auth import HTTPBasicAuth
import requests
import credentials
from exceptions import AuthorizeException, ForbiddenException, ValueNotFoundException

# our main url for fetching tickets endpoint
url = 'https://' + credentials.subdomain + '.zendesk.com/api/v2/tickets/'

def getData(url, user_email, user_password):
    """
    this funtions takes url, zendesk account email and password as input and fetch the data from endpoint url with basic authorization
    """
    raw_request = requests.get(url, auth = HTTPBasicAuth(user_email, user_password))
    
    # based on response code the conditions are seperated, 200 if success, 404 if value not found, 401 if not authorized else url is not correct then request forbidden error
    if(raw_request.status_code == 200):
        #converting request object to python dictionary
        data = raw_request.json()
        return data
    elif(raw_request.status_code == 404):
        raise ValueNotFoundException()
    elif(raw_request.status_code == 401):
        raise AuthorizeException()
    else:
        raise ForbiddenException()

def getAllTicketswithPaging(page = 1):
    """
    function returns raw data collected from url endpoint passed with page and limit per page details
    """
    per_page = 25
    limit_per_page_url = url + '?page=' + str(page) + '&per_page=' + str(per_page) 
    #passing url for all tickets with paging with email and password to fetch the data
    all_tickets = getData(limit_per_page_url, credentials.email, credentials.password)
    #getting all details such as tickets in list, total tickets count, next page details, prev page details which are used for parsing as per page
    tickets_list, count, next_page, prev_page = all_tickets["tickets"], all_tickets["count"], all_tickets["next_page"], all_tickets["previous_page"]
    return tickets_list, count, next_page, prev_page, per_page
    
def getTicketById(ticket_id : int):
    """
    function returns raw data collected from url endpoint passed with ticket id
    """
    final_url = url + str(ticket_id)
    #passing url for ticket by id with email and password to fetch the data 
    ticket_by_id = getData(final_url, credentials.email, credentials.password)
    #getting only ticket detail for parsing
    ticket_details = ticket_by_id["ticket"]
    return ticket_details
