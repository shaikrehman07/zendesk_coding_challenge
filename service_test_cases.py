import unittest as test
from exceptions import ValueNotFoundException
from service import parseMultipleTickets, parseSingleTicket

from zendesk import getTicketById


class TestService(test.TestCase):

    def test_parseSingleTicket_1(self):
        #this test will pass only if ticket is present with id 1 and actual_data contains same data as ticket details
        ticket_id = 1
        actual_data = "Ticket is opened by '422051396791' with subject 'Sample ticket: Meet the ticket' on '19 Nov 2021' with status 'open'"
        expected_data = parseSingleTicket(ticket_id)
        self.assertEqual(actual_data, expected_data)

    def test_parseSingleTicket_2(self):
        ticket_id = 1000
        try:
            parseSingleTicket(ticket_id)
        except ValueNotFoundException as e:
            self.assertEqual(type(e), ValueNotFoundException)

    def test_parseMultipleTickets_1(self):
        actual_output = 25
        expected_output, count, next, prev, limit= parseMultipleTickets(1)
        self.assertEqual(actual_output, limit)

if __name__ == '__main__':
    test.main()