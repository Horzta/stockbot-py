import http.client
import json

class PhisixConnectionService:

    def __init__(self):
        self.conn = http.client.HTTPSConnection("phisix-api3.appspot.com")


    def get_stock_info(self, stock_code):
        self.conn.request("GET", "/stocks/{}.json".format(stock_code))
        res = self.conn.getresponse()
        data = res.read()
        print(data)
        json_data = json.loads(data.decode("utf-8"))

        return json_data