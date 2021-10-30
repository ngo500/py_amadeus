class userinput:

    def __init__(self):
        self.origin = 'SFO'
        self.dest = 'JFK'
        self.arr = '12-01-21'
        self.ad = 1

    def getOrigin(self):
        return self.origin

    def getDestination(self):
        return self.dest

    def getArrivalDate(self):
        return self.arr

    def getAdults(self):
        return self.ad

    def getParam(self):
        params = {"originLocationCode" : 'SFO',
        "destinationLocationCode" : 'JFK',
        "departureDate" : '2021-12-01',
        "adults" : 1}
        return params
