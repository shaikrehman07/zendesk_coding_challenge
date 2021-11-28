# zendesk_coding_challenge
- The challenge has been implemented completely using python and the mode of usage of application is CLI.
- To run the program:
  1. Edit the credentials.py file with data as per your need to test the program (details asked are zendesk's: email, password and subdomain) as I have used basic        authorization for connecting to Zendesk API.
  2. Run main.py to start the program
- Implementation:
  1. Ticket can be viewed by entering id.
  2. All tickets can be viewed in number of 25 with pagination if more than 25 tickets are present. It will ask options as 'next' or 'prev' or 'q'(quit) to navigate      through the tickets because the code was written keeping in mind that only fetch the details from respected page not more than that.
  3. Exceptions are also handled.
