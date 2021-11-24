import unittest as test

from exceptions import ValueNotFoundException
from zendesk import *
import credentials
import requests
from requests.auth import HTTPBasicAuth

class TestZendesk(test.TestCase):

    tickets = [1,2,3,4]

    def test_getAllTicketsWithPaging_1(self):
        value = getAllTicketswithPaging(page=1)
        self.assertNotEqual(self.tickets, value)

    def test_getAllTicketsWithPaging_2(self):
        expected_length_of_data = 25
        page = 3
        value = getAllTicketswithPaging(page)
        self.assertEqual(expected_length_of_data, len(value["tickets"]))

    def test_getTicketByID_1(self):
        id = 1
        actual_value = 1
        value = getTicketById(id)
        self.assertEqual(actual_value, value["ticket"]["id"])

    def test_getData_1(self):
        id = 32324323
        url = 'https://' + credentials.subdomain + '.zendesk.com/api/v2/tickets/' + str(id)
        self.assertRaises(ValueNotFoundException, getData, url, credentials.email, credentials.password)

    def test_getData_2(self):
        url = 'https://' + credentials.subdomain + '.zendesk.com/api/v2/tickets/'
        self.assertRaises(AuthorizeException, getData, url, "abc@gmail.com", "1234")
    
    def test_getData_3(self):
        #url is wrong here
        url = 'https://' + credentials.subdomain + '.zendesk.com/api/tickets/'
        self.assertRaises(ForbiddenException, getData, url, credentials.email, credentials.password)

if __name__ == '__main__':
    test.main()