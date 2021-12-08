import json

class airplane:

    def __init__(self):
        self = ""

    def parseCur(self, param):
        data = ""
        for i in range(len(param)):
            if i<1:
                data = (param[0]['price']['grandTotal'])
        return data

    def parseOld(self, param):
        data = ""
        data = param[0]['priceMetrics'][0]['amount']
        return data
        
    def parseOldAvg(self, param):
        data = ""
        data = param[0]['priceMetrics'][0]['amount']
        return data
        
    def parseAvg(self, param):
        data = ""
        tempdata = param[0]['priceMetrics'][1]['amount']
        tempans = (float(tempdata)/7)
        data = str('{0:.2f}'.format(tempans))
        return data
