from config import config
from userinput import userinput
from airplane import airplane
from amadeus import Client, ResponseError
import json

class main:
    def __init__(self):
        main = ""

    def runMain(self, event):
        start = config()
        baseURL = start.getBaseURL()
        amadeus = start.getClient()
        input = userinput()
        parseAir = airplane()

        inputInfo = []
        for (x, y) in event.items():
            inputInfo.append(str(y))

        input.setOrigin(inputInfo[0])
        input.setDestination(inputInfo[1])
        input.setArrivalDate(inputInfo[2])

        try:
            params = input.getOldParam()
            response = amadeus.analytics.itinerary_price_metrics.get(**params)
            olddata = parseAir.parseOld(response.data)

            params = input.getCurParam()
            response = amadeus.shopping.flight_offers_search.get(**params)
            newdata = parseAir.parseCur(response.data)
            
            data = {
                "oldValue": olddata,
                "newValue": newdata
            }
            return data

        except ResponseError as error:
            print("error! ")
            print (error)
