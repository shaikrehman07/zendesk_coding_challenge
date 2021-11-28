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
        #length will be 25 only if it contains more data when I tested I have more data in my account
        expected_length_of_data = 25
        page = 2
        value = getAllTicketswithPaging(page)
        self.assertEqual(expected_length_of_data, len(value))

    def test_getTicketByID_1(self):
        #give input for id which is present in zendesk
        id = 1
        #same as id value should be kept to test
        actual_value = 1
        value = getTicketById(id)
        self.assertEqual(actual_value, value["id"])

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