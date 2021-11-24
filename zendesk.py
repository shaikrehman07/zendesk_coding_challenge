from requests.auth import HTTPBasicAuth
import requests
import credentials
from exceptions import AuthorizeException, ForbiddenException, ValueNotFoundException

# our main url for fetching tickets endpoint
url = 'https://' + credentials.subdomain + '.zendesk.com/api/v2/tickets/'

def getData(url: str):
    """
    this funtions takes url as input and fetch the data from endpoint url with basic authorization details
    """
    raw_request = requests.get(url, auth = HTTPBasicAuth(credentials.email, credentials.password))
    
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
    limit_per_page = url + '?page=' + str(page) + '&per_page=' + str(per_page) 
    all_tickets = getData(limit_per_page)
    return all_tickets
    
def getTicketById(ticket_id : int):
    """
    function returns raw data collected from url endpoint passed with ticket id
    """
    final_url = url + str(ticket_id) 
    ticket_by_id = getData(final_url)
    #parsing_data = model.parseSingleTicket(ticket_by_id)
    return ticket_by_id
