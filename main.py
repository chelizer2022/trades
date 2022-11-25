from binance import Client,AsyncClient, ThreadedWebsocketManager, ThreadedDepthCacheManager
import config, time
import csv
from _ast import Await
import asyncio
import threading




api_key= 'uMTIBnTFmfxYV73LmDVa1TEd5wJJjbXIN8A02tPzyjfHjLQu8j9maD395kJV92pP'
api_secret= '1btmNRVAUwuZjibZTj4V4lASWv5WYsWaeQ41PIR0wY3DpKJhosDqImbmVL7MxNp7'

client = Client(api_key, api_secret)
cuenta=0
global count
data_file = open('data_file_binance.csv', 'w') 
csv_writer = csv.writer(data_file) 
#prices = client.futures_historical_trades(symbol='BTCUSDT',page=23,limit=1000)
#print(prices)

#cuenta=client.get_account();


def  getAllTickers(client):

    # Get all available exchange tickers
    exchangeInfo = client.get_exchange_info()

    # Extract the tickers general info
    exchangeSymbols = []

    for i in exchangeInfo['symbols']:
        exchangeSymbols.append(i)

    return exchangeSymbols

def  getTrade(symbol):
  trade= client.get_my_trades(symbol=symbol)
  if trade :
     for i in trade:
     
  
      csv_writer.writerow(i.values())
     
def  getAllTrades(tickers):
 trade= client.get_my_trades(symbol="ETHBTC")
 if trade :
     for i in trade:       
        header = i.keys() 
        csv_writer.writerow(header)
        break   
 for i in tickers:
    trade=threading.Thread(getTrade(i['symbol']))
    trade.start()
    time.sleep(0.3)
    print(trade)
    #trade= client.getTrade(symbol=i['symbol'])
   
    #traded.append(trade)
  
    
tickers=getAllTickers(client)
contador=0
getAllTrades(tickers) 
print("csv generado con éxito")
