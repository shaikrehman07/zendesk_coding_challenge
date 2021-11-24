import unittest as test
from exceptions import ValueNotFoundException
from service import parseMultipleTickets, parseSingleTicket

from zendesk import getTicketById


class TestService(test.TestCase):

    def test_parseSingleTicket_1(self):
        ticket_id = 1
        actual_data = "Ticket is opened by '422051396791' with subject 'Sample ticket: Meet the ticket' on '19 Nov 2021' with status 'open'"
        expected_data = parseSingleTicket(ticket_id)
        self.assertEqual(actual_data, expected_data)

    def test_parseSingleTicket_2(self):
        ticket_id = 1000
        expected_output = parseSingleTicket(ticket_id)
        self.assertEqual("", expected_output)

    def test_parseMultipleTickets_1(self):
        page = 1
        actual_output = 25
        expected_output = parseMultipleTickets(page)
        self.assertEqual(actual_output, len(expected_output[0]))

if __name__ == '__main__':
    test.main()