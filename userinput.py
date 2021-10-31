class userinput:

    def __init__(self):
        self.origin = 'SFO'
        self.dest = 'JFK'
        self.arr = '12-01-21'
        self.ad = 1
        
    def setOrigin(self, param):
        self.origin = param

    def setDestination(self, param):
        self.dest = param

    def setArrivalDate(self, param):
        self.arr = param

    def setAdults(self, param):
        self.ad = param

    def getOrigin(self):
        return self.origin

    def getDestination(self):
        return self.dest

    def getArrivalDate(self):
        return self.arr

    def getAdults(self):
        return self.ad

    def getParam(self):
        params = {}
        originLocationCode = self.origin
        destinationLocationCode = self.dest
        departureDate = self.arr
        adults = self.ad

        for var in ["originLocationCode", "destinationLocationCode", "departureDate", "adults"]:
            params[var] = eval(var)
        return params
