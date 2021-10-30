from amadeus import Client

class config:

    def __init__(self):
        self.url = "http://test.api.amadeus.com/v2"
        self.api = "shopping/flight-offers?"
        self.c_id = 'X'
        self.c_se = 'X'

    def getBaseURL(self):
        return self.url + self.api

    def getClient(self):
        amadeus = Client(
            client_id=self.c_id,
            client_secret=self.c_se
        )
        return amadeus
