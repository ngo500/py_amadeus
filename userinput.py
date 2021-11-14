
class userinput:

    def __init__(self):
        self.origin = 'MAD'
        self.dest = 'BOS'
        self.arr = '2021-12-31'
        self.ad = 0

    def setOrigin(self, param):
        self.origin = param

    def setDestination(self, param):
        self.dest = param

    def setArrivalDate(self, param):
        self.arr = param

    def setAdults(self, param):
        self.ad = param

    def getOldParam(self):
        params = {}
        originIataCode = self.origin
        destinationIataCode = self.dest
        departureDate = self.arr
        currencyCode = "USD"

        for var in ["originIataCode", "destinationIataCode", "departureDate", "currencyCode"]:
            params[var] = eval(var)

        return params

    def getCurParam(self):
        params = {}
        originLocationCode = self.origin
        destinationLocationCode = self.dest
        departureDate = self.arr
        adults = 1
        currencyCode = "USD"

        for var in ["originLocationCode", "destinationLocationCode", "departureDate", "adults", "currencyCode"]:
            params[var] = eval(var)

        return params
