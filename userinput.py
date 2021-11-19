
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
        
    def adjustYear(self):
        date = self.arr
        tempyear = date.split("-")
        date = ""
        temp = int(tempyear[0][3])
    
        if(temp == 0):
            temp2 = int(tempyear[0][2])
            temp2 -= 1
            date = tempyear[0][0] + tempyear[0][1] + str(temp2) + '9' + '-' + tempyear[1] + '-' + tempyear[2]
        else:
            temp -= 1
            date = tempyear[0][0] + tempyear[0][1] + tempyear[0][2] + str(temp) + '-' + tempyear[1] + '-' + tempyear[2]
    
        self.arr = date
        
    def adjustMonth(self):
        date = self.arr
        tempmonth = date.split("-")
        date = ""
        temp = tempmonth[1]
        
        if(temp == '01'):
            date = tempmonth[0] + '-' + '12' + '-' + tempmonth[2]
        elif(temp == '02'):
            date = tempmonth[0] + '-' + '01' + '-' + tempmonth[2]
        elif(temp == '03'):
            date = tempmonth[0] + '-' + '02' + '-' + tempmonth[2]
        elif(temp == '04'):
            date = tempmonth[0] + '-' + '03' + '-' + tempmonth[2]
        elif(temp == '05'):
            date = tempmonth[0] + '-' + '04' + '-' + tempmonth[2]
        elif(temp == '06'):
            date = tempmonth[0] + '-' + '05' + '-' + tempmonth[2]
        elif(temp == '07'):
            date = tempmonth[0] + '-' + '06' + '-' + tempmonth[2]
        elif(temp == '08'):
            date = tempmonth[0] + '-' + '07' + '-' + tempmonth[2]
        elif(temp == '09'):
            date = tempmonth[0] + '-' + '08' + '-' + tempmonth[2]
        elif(temp == '10'):
            date = tempmonth[0] + '-' + '09' + '-' + tempmonth[2]
        elif(temp == '11'):
            date = tempmonth[0] + '-' + '10' + '-' + tempmonth[2]
        elif(temp == '12'):
            date = tempmonth[0] + '-' + '11' + '-' + tempmonth[2]
        else:
            date = "error"
        
        self.arr = date
        
    def adjustDay(self):
        date = self.arr
        tempday = date.split("-")
        date = ""
        if(tempday[2] == '01'):
            date = tempday[0] + '-' + tempday[1] + '-' + '02'
        else:
            date = tempday[0] + '-' + tempday[1] + '-' + '01'
            
        self.arr = date

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
