import json

class airplane:

    def __init__(self):
        self = ""

    def parse(self, param):
        for i in range(len(param)):
            if i<5:
                print (param[i]['price'])
        return self
