from models.StockModel import StockModel
from plyer import notification

class StockService:

    def __init__(self, stock_code, conn_service, config_service):
        self.stock_code     = stock_code
        self.conn_service   = conn_service
        self.config_service = config_service
        self.stock          = None


    def initialize_stock(self):
        self.stock = StockModel(self.conn_service.get_stock_info(self.stock_code))


    def update(self):
        self.stock.update(self.conn_service.get_stock_info(self.stock_code))


    def notify(self):
        if self.stock is None:
            self.initialize_stock()
        else:
            self.update()

        notification.notify(
            title = "[{}] {} stock data".format(self.stock.symbol, self.stock.name),
            message = "Current Price: {} {} \n".format(self.stock.currency, self.stock.current_price)
                + "Previous Price: {} {} \n".format(self.stock.currency, self.stock.previous_price)
                + "As of {}".format(self.stock.updated_at),  
            app_name = "AkiBot",
            app_icon = "",
            timeout  = int(self.config_service.get('NOTIFICATION', 'timeout'))
        )
