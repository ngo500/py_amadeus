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
            if (input.getDate() > input.getToday()):
                if(input.getDate().month == input.getToday().month):
                    response = amadeus.shopping.flight_offers_search.get(**params)
                    currentPrice = parseAir.parseCur(response.data)
                else:
                    currentPrice = -1
            else:
                response = amadeus.shopping.flight_offers_search.get(**params)
                currentPrice = parseAir.parseCur(response.data)
            
            input.adjustMonth()
            params = input.getOldParam()
            if(input.getDate() > input.getToday()):
                avg1MonthAgo = -1
            else:
                response = amadeus.analytics.itinerary_price_metrics.get(**params)
                avg1MonthAgo = parseAir.parseAvg(response.data)
            
            input.adjustMonth()
            params = input.getOldParam()
            if(input.getDate() > input.getToday()):
                avg2MonthAgo = -1
            else:
                response = amadeus.analytics.itinerary_price_metrics.get(**params)
                avg2MonthAgo = parseAir.parseAvg(response.data)
                
            input.adjustMonth()
            params = input.getOldParam()
            if(input.getDate() > input.getToday()):
                avg3MonthAgo = -1
            else:
                response = amadeus.analytics.itinerary_price_metrics.get(**params)
                avg3MonthAgo = parseAir.parseAvg(response.data)
                
            input.adjustMonth()
            params = input.getOldParam()
            if(input.getDate() > input.getToday()):
                avg4MonthAgo = -1
            else:
                response = amadeus.analytics.itinerary_price_metrics.get(**params)
                avg4MonthAgo = parseAir.parseAvg(response.data)
                
            input.adjustMonth()
            params = input.getOldParam()
            if(input.getDate() > input.getToday()):
                avg5MonthAgo = -1
            else:
                response = amadeus.analytics.itinerary_price_metrics.get(**params)
                avg5MonthAgo = parseAir.parseAvg(response.data)
                
            input.adjustMonth()
            params = input.getOldParam()
            if(input.getDate() > input.getToday()):
                avg6MonthAgo = -1
            else:
                response = amadeus.analytics.itinerary_price_metrics.get(**params)
                avg6MonthAgo = parseAir.parseAvg(response.data)    
                
            input.adjustMonth()
            params = input.getOldParam()
            if(input.getDate() > input.getToday()):
                avg7MonthAgo = -1
            else:
                response = amadeus.analytics.itinerary_price_metrics.get(**params)
                avg7MonthAgo = parseAir.parseAvg(response.data)   
                
            input.adjustMonth()
            params = input.getOldParam()
            if(input.getDate() > input.getToday()):
                avg8MonthAgo = -1
            else:
                response = amadeus.analytics.itinerary_price_metrics.get(**params)
                avg8MonthAgo = parseAir.parseAvg(response.data)   
                
            input.adjustMonth()
            params = input.getOldParam()
            if(input.getDate() > input.getToday()):
                avg9MonthAgo = -1
            else:
                response = amadeus.analytics.itinerary_price_metrics.get(**params)
                avg9MonthAgo = parseAir.parseAvg(response.data)   
            
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
            
            input.adjustMonth()
            params = input.getOldParam()
            response = amadeus.analytics.itinerary_price_metrics.get(**params)
            avg1year6MonthAgo = parseAir.parseOldAvg(response.data)
            
            input.adjustMonth()
            params = input.getOldParam()
            response = amadeus.analytics.itinerary_price_metrics.get(**params)
            avg1year7MonthAgo = parseAir.parseOldAvg(response.data)
            
            input.adjustMonth()
            params = input.getOldParam()
            response = amadeus.analytics.itinerary_price_metrics.get(**params)
            avg1year8MonthAgo = parseAir.parseOldAvg(response.data)
            
            input.adjustMonth()
            params = input.getOldParam()
            response = amadeus.analytics.itinerary_price_metrics.get(**params)
            avg1year9MonthAgo = parseAir.parseOldAvg(response.data)
            
            data = {}
            currentPriceHistory = "currentPriceHistory"
            previousPriceHistory = "previousPriceHistory"
            data[currentPriceHistory] = [currentPrice, avg1MonthAgo, avg2MonthAgo, avg3MonthAgo, avg4MonthAgo, avg5MonthAgo, avg6MonthAgo, avg7MonthAgo, avg8MonthAgo, avg9MonthAgo]
            data[previousPriceHistory] = [price1YearAgo, avg1year1MonthAgo, avg1year2MonthAgo, avg1year3MonthAgo, avg1year4MonthAgo, avg1year5MonthAgo, avg1year6MonthAgo, avg1year7MonthAgo, avg1year8MonthAgo, avg1year9MonthAgo]
            
            return data

        except Exception as e:
            print(e)
            return("ERROR- The date " + event.get('departureDate') +  " is not accepted. Please enter a different date.")
