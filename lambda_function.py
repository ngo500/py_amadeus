import json
from main import *

def lambda_handler(event, context):
    start = main()
    data = start.runMain(event)
    return data
