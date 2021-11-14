import json

class airplane:

    def __init__(self):
        self = ""

    def parseCur(self, param):
        data = ""
        for i in range(len(param)):
            if i<1:
                data = (param[i]['price']['grandTotal'])
        return data

    def parseOld(self, param):
        data = ""
        data = param[0]['priceMetrics'][0]['amount']
        return data
