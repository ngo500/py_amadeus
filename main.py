from config import config
from userinput import userinput
#from airplane import airplane
from amadeus import Client, ResponseError

start = config()
baseURL = start.getBaseURL()
amadeus = start.getClient()
input = userinput()
params = input.getParam()


try:
    response = amadeus.shopping.flight_offers_search.get(**params)
    print(response.data)

except ResponseError as error:
    print("error! ")
    print (error)
