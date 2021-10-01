from services.ConfigurationService import ConfigurationService
from services.PhisixConnectionService import PhisixConnectionService
from services.StockService import StockService
import time

# Basic Services
config_service = ConfigurationService()
conn_service  = PhisixConnectionService()


# Initialize Stock Services
stock_codes = config_service.get('DEFAULT', 'stocks').split(',')
stock_services = []

for code in stock_codes:
    stock_services.append(StockService(code, conn_service, config_service))


# Run
while True:
    for stock_service in stock_services:
        stock_service.notify()
    
    time.sleep(int(config_service.get('NOTIFICATION', 'interval')))