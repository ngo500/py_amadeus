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

        input.setOrigin(event.get('originIataCode'))
        input.setDestination(event.get('destinationIataCode'))
        input.setArrivalDate(event.get('departureDate'))

        try:
            params = input.getCurParam()
            response = amadeus.shopping.flight_offers_search.get(**params)
            currentPrice = parseAir.parseCur(response.data)
            
            input.adjustMonth()
            params = input.getOldParam()
            response = amadeus.analytics.itinerary_price_metrics.get(**params)
            avg1MonthAgo = parseAir.parseAvg(response.data)
            
            input.adjustMonth()
            params = input.getOldParam()
            response = amadeus.analytics.itinerary_price_metrics.get(**params)
            avg2MonthAgo = parseAir.parseAvg(response.data)
            
            input.adjustMonth()
            params = input.getOldParam()
            response = amadeus.analytics.itinerary_price_metrics.get(**params)
            avg3MonthAgo = parseAir.parseAvg(response.data)
            
            input.adjustMonth()
            params = input.getOldParam()
            response = amadeus.analytics.itinerary_price_metrics.get(**params)
            avg4MonthAgo = parseAir.parseAvg(response.data)
            
            input.adjustMonth()
            params = input.getOldParam()
            response = amadeus.analytics.itinerary_price_metrics.get(**params)
            avg5MonthAgo = parseAir.parseAvg(response.data)
            
            input.setArrivalDate(event.get('departureDate'))
            input.adjustYear()
            params = input.getOldParam()
            response = amadeus.analytics.itinerary_price_metrics.get(**params)
            price1YearAgo = parseAir.parseOld(response.data)
            
            input.adjustMonth()
            input.adjustDay()
            params = input.getOldParam()
            response = amadeus.analytics.itinerary_price_metrics.get(**params)
            avg1year1MonthAgo = parseAir.parseOldAvg(response.data)
            
            input.adjustMonth()
            params = input.getOldParam()
            response = amadeus.analytics.itinerary_price_metrics.get(**params)
            avg1year2MonthAgo = parseAir.parseOldAvg(response.data)
            
            input.adjustMonth()
            params = input.getOldParam()
            response = amadeus.analytics.itinerary_price_metrics.get(**params)
            avg1year3MonthAgo = parseAir.parseOldAvg(response.data)
            
            input.adjustMonth()
            params = input.getOldParam()
            response = amadeus.analytics.itinerary_price_metrics.get(**params)
            avg1year4MonthAgo = parseAir.parseOldAvg(response.data)
            
            input.adjustMonth()
            params = input.getOldParam()
            response = amadeus.analytics.itinerary_price_metrics.get(**params)
            avg1year5MonthAgo = parseAir.parseOldAvg(response.data)
            
            
            data = {
                "currentPrice": currentPrice,
                "avg1MonthAgo": avg1MonthAgo,
                "avg2MonthAgo": avg2MonthAgo,
                "avg3MonthAgo": avg3MonthAgo,
                "avg4MonthAgo": avg4MonthAgo,
                "avg5MonthAgo": avg5MonthAgo,
                "price1YearAgo": price1YearAgo,
                "avg1year1MonthAgo": avg1year1MonthAgo,
                "avg1year2MonthAgo": avg1year2MonthAgo,
                "avg1year3MonthAgo": avg1year3MonthAgo,
                "avg1year4MonthAgo": avg1year4MonthAgo,
                "avg1year5MonthAgo": avg1year5MonthAgo,
            }
            
            return data

        except ResponseError as error:
            return (error)
