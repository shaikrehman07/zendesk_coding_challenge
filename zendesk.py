from requests.auth import HTTPBasicAuth
import requests
import credentials
from exceptions import AuthorizeException, ForbiddenException, ValueNotFoundException

url = 'https://' + credentials.subdomain + '.zendesk.com/api/v2/tickets/'

def getData(url: str):
    
    raw_request = requests.get(url, auth = HTTPBasicAuth(credentials.email, credentials.password))
    
    
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
    per_page = 25
    limit_per_page = url + '?page=' + str(page) + '&per_page=' + str(per_page) 
    all_tickets = getData(limit_per_page)
    return all_tickets
    
def getTicketById(ticket_id : int):
    final_url = url + str(ticket_id) 
    ticket_by_id = getData(final_url)
    #parsing_data = model.parseSingleTicket(ticket_by_id)
    return ticket_by_id
