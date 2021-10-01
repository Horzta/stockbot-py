class StockModel:

    def __init__(self, payload):
        self.name           = payload['stock'][0]['name']
        self.symbol         = payload['stock'][0]['symbol']
        self.current_price  = payload['stock'][0]['price']['amount']
        self.currency       = payload['stock'][0]['price']['currency']
        self.percent_change = payload['stock'][0]['percent_change']
        self.previous_price = 0
        self.updated_at     = payload['as_of']
        self.price_history  = [{
                'datetime' : payload['as_of'],
                'price'    : payload['stock'][0]['price']['amount']
            }]


    def update(self, payload):
        self.previous_price = self.current_price
        self.current_price  = payload['stock'][0]['price']['amount']
        self.percent_change = payload['stock'][0]['percent_change']
        self.updated_ad     = payload['as_of']
        self.price_history.append({
                    'datetime' : payload['as_of'],
                    'price'    : payload['stock'][0]['price']['amount']
                }
            )
