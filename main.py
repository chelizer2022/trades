from pybit import inverse_perpetual
import csv 
from pybit import usdt_perpetual
from pybit import spot
from _datetime import datetime
from pybit import inverse_perpetual
from scipy.optimize._optimize import bracket

fecha_inicial = '2019/01/18'
fecha_final= '2022/11/19'
fecha_inicio = datetime.strptime(fecha_inicial, '%Y/%m/%d')
fecha_fin = datetime.strptime(fecha_final, '%Y/%m/%d')

fecha_inicio=fecha_inicio.timestamp()
fecha_fin=fecha_fin.timestamp()
print(fecha_fin)
just_now=datetime.now()
just_now=just_now.timestamp()
seg_por_dia=24+60+60

session_auth = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key="vqUcOnIiqHC3yW9i34",
    api_secret="xrqc27FjR83HSiZKCI3GAsJkQocAyN2x3kPV"
)
count=0
cuenta=0
i=1
data_file = open('data_file_bybit.csv', 'w') 
csv_writer = csv.writer(data_file) 
infoBTCUSDT=""

#BTCUSDT pages 9   total trades 1663
#GMTUSDT pages 3   total trades 480
#ETHUSDT page 3    ""    ""     542
#SOLUSDT page 2                 296
#APEUSDT page 1                 7
#DOTUSDT page 1                 9
#BNBUSDT page 1                 34
#BANDUSDT page 1                4
#BAKEUSDT page 1                23
#AVAXUSDT page 1                85
#ALICEUSDT page 1               13
#XRPUSDT   page 1               79
#TRXUSDT   page 3               519
#STGUSDT   page 1               14
#OPUSDT    page 1               14
#ONTUSDT   page 1               44
#NEARUSDT  page 1               57
#MATICUSDT page 1               35
#MASKUSDT  page 1               5
#GRTUSDT   page 1               4
#total:                        3.927

while i<=9:
 infoBTCUSDT=session_auth.user_trade_records(
    symbol="BTCUSDT",
    page=i,
    limit=200
 )
 if infoBTCUSDT['result']['data']!=None:
  trade_data_BTCUSDT = infoBTCUSDT['result']['data']
  for trade_ in trade_data_BTCUSDT: 
     if count == 0: 
  
        
        header = trade_.keys() 
        csv_writer.writerow(header) 
        count += 1
  
     cuenta+=1
     csv_writer.writerow(trade_.values()) 
  i+=1
 else:
     break

i=1
while i<=3:
 infoBTCUSDT=session_auth.user_trade_records(
    symbol="GMTUSDT",
    page=i,
    limit=200
 )
 if infoBTCUSDT['result']['data']!=None:
  trade_data_BTCUSDT = infoBTCUSDT['result']['data']
  for trade_ in trade_data_BTCUSDT: 
     if count == 0: 
  
        
        header = trade_.keys() 
        csv_writer.writerow(header) 
        count += 1
  
     cuenta+=1
     csv_writer.writerow(trade_.values()) 
  i+=1
 else:
     break


i=1
while i<=3:
 infoBTCUSDT=session_auth.user_trade_records(
    symbol="ETHUSDT",
    page=i,
    limit=200
 )
 if infoBTCUSDT['result']['data']!=None:
  trade_data_BTCUSDT = infoBTCUSDT['result']['data']
  for trade_ in trade_data_BTCUSDT: 
     if count == 0: 
  
        
        header = trade_.keys() 
        csv_writer.writerow(header) 
        count += 1
  
     cuenta+=1
     csv_writer.writerow(trade_.values()) 
  i+=1
 else:
     break
  

i=1
while i<=2:
 infoBTCUSDT=session_auth.user_trade_records(
    symbol="SOLUSDT",
    page=i,
    limit=200
 )
 if infoBTCUSDT['result']['data']!=None:
  trade_data_BTCUSDT = infoBTCUSDT['result']['data']
  for trade_ in trade_data_BTCUSDT: 
     if count == 0: 
  
        
        header = trade_.keys() 
        csv_writer.writerow(header) 
        count += 1
  
     cuenta+=1
     csv_writer.writerow(trade_.values()) 
  i+=1
 else:
     break 
 
i=1
while i<=1:
 infoBTCUSDT=session_auth.user_trade_records(
    symbol="APEUSDT",
    page=i,
    limit=200
 )
 if infoBTCUSDT['result']['data']!=None:
  trade_data_BTCUSDT = infoBTCUSDT['result']['data']
  for trade_ in trade_data_BTCUSDT: 
     if count == 0: 
  
        
        header = trade_.keys() 
        csv_writer.writerow(header) 
        count += 1
  
     cuenta+=1
     csv_writer.writerow(trade_.values()) 
  i+=1
 else:
     break 
 
i=1
while i<=1:
 infoBTCUSDT=session_auth.user_trade_records(
    symbol="DOTUSDT",
    page=i,
    limit=200
 )
 if infoBTCUSDT['result']['data']!=None:
  trade_data_BTCUSDT = infoBTCUSDT['result']['data']
  for trade_ in trade_data_BTCUSDT: 
     if count == 0: 
  
        
        header = trade_.keys() 
        csv_writer.writerow(header) 
        count += 1
  
     cuenta+=1
     csv_writer.writerow(trade_.values()) 
  i+=1
 else:
     break 
 
i=1
while i<=1:
 infoBTCUSDT=session_auth.user_trade_records(
    symbol="BNBUSDT",
    page=i,
    limit=200
 )
 if infoBTCUSDT['result']['data']!=None:
  trade_data_BTCUSDT = infoBTCUSDT['result']['data']
  for trade_ in trade_data_BTCUSDT: 
     if count == 0: 
  
        
        header = trade_.keys() 
        csv_writer.writerow(header) 
        count += 1
  
     cuenta+=1
     csv_writer.writerow(trade_.values()) 
  i+=1
 else:
     break 
 
i=1
while i<=1:
 infoBTCUSDT=session_auth.user_trade_records(
    symbol="BANDUSDT",
    page=i,
    limit=200
 )
 if infoBTCUSDT['result']['data']!=None:
  trade_data_BTCUSDT = infoBTCUSDT['result']['data']
  for trade_ in trade_data_BTCUSDT: 
     if count == 0: 
  
        
        header = trade_.keys() 
        csv_writer.writerow(header) 
        count += 1
  
     cuenta+=1
     csv_writer.writerow(trade_.values()) 
  i+=1
 else:
     break 
 
i=1
while i<=1:
 infoBTCUSDT=session_auth.user_trade_records(
    symbol="BAKEUSDT",
    page=i,
    limit=200
 )
 if infoBTCUSDT['result']['data']!=None:
  trade_data_BTCUSDT = infoBTCUSDT['result']['data']
  for trade_ in trade_data_BTCUSDT: 
     if count == 0: 
  
        
        header = trade_.keys() 
        csv_writer.writerow(header) 
        count += 1
  
     cuenta+=1
     csv_writer.writerow(trade_.values()) 
  i+=1
 else:
     break 
 
i=1
while i<=1:
 infoBTCUSDT=session_auth.user_trade_records(
    symbol="AVAXUSDT",
    page=i,
    limit=200
 )
 if infoBTCUSDT['result']['data']!=None:
  trade_data_BTCUSDT = infoBTCUSDT['result']['data']
  for trade_ in trade_data_BTCUSDT: 
     if count == 0: 
  
        
        header = trade_.keys() 
        csv_writer.writerow(header) 
        count += 1
  
     cuenta+=1
     csv_writer.writerow(trade_.values()) 
  i+=1
 else:
     break 
 
i=1
while i<=1:
 infoBTCUSDT=session_auth.user_trade_records(
    symbol="ALICEUSDT",
    page=i,
    limit=200
 )
 if infoBTCUSDT['result']['data']!=None:
  trade_data_BTCUSDT = infoBTCUSDT['result']['data']
  for trade_ in trade_data_BTCUSDT: 
     if count == 0: 
  
        
        header = trade_.keys() 
        csv_writer.writerow(header) 
        count += 1
  
     cuenta+=1
     csv_writer.writerow(trade_.values()) 
  i+=1
 else:
     break 
 
i=1
while i<=1:
 infoBTCUSDT=session_auth.user_trade_records(
    symbol="XRPUSDT",
    page=i,
    limit=200
 )
 if infoBTCUSDT['result']['data']!=None:
  trade_data_BTCUSDT = infoBTCUSDT['result']['data']
  for trade_ in trade_data_BTCUSDT: 
     if count == 0: 
  
        
        header = trade_.keys() 
        csv_writer.writerow(header) 
        count += 1
  
     cuenta+=1
     csv_writer.writerow(trade_.values()) 
  i+=1
 else:
     break 
 
i=1
while i<=3:
 infoBTCUSDT=session_auth.user_trade_records(
    symbol="TRXUSDT",
    page=i,
    limit=200
 )
 if infoBTCUSDT['result']['data']!=None:
  trade_data_BTCUSDT = infoBTCUSDT['result']['data']
  for trade_ in trade_data_BTCUSDT: 
     if count == 0: 
  
        
        header = trade_.keys() 
        csv_writer.writerow(header) 
        count += 1
  
     cuenta+=1
     csv_writer.writerow(trade_.values()) 
  i+=1
 else:
     break 
 
i=1
while i<=1:
 infoBTCUSDT=session_auth.user_trade_records(
    symbol="STGUSDT",
    page=i,
    limit=200
 )
 if infoBTCUSDT['result']['data']!=None:
  trade_data_BTCUSDT = infoBTCUSDT['result']['data']
  for trade_ in trade_data_BTCUSDT: 
     if count == 0: 
  
        
        header = trade_.keys() 
        csv_writer.writerow(header) 
        count += 1
  
     cuenta+=1
     csv_writer.writerow(trade_.values()) 
  i+=1
 else:
     break 
 
i=1
while i<=1:
 infoBTCUSDT=session_auth.user_trade_records(
    symbol="OPUSDT",
    page=i,
    limit=200
 )
 if infoBTCUSDT['result']['data']!=None:
  trade_data_BTCUSDT = infoBTCUSDT['result']['data']
  for trade_ in trade_data_BTCUSDT: 
     if count == 0: 
  
        
        header = trade_.keys() 
        csv_writer.writerow(header) 
        count += 1
  
     cuenta+=1
     csv_writer.writerow(trade_.values()) 
  i+=1
 else:
     break 
 
i=1
while i<=1:
 infoBTCUSDT=session_auth.user_trade_records(
    symbol="ONTUSDT",
    page=i,
    limit=200
 )
 if infoBTCUSDT['result']['data']!=None:
  trade_data_BTCUSDT = infoBTCUSDT['result']['data']
  for trade_ in trade_data_BTCUSDT: 
     if count == 0: 
  
        
        header = trade_.keys() 
        csv_writer.writerow(header) 
        count += 1
  
     cuenta+=1
     csv_writer.writerow(trade_.values()) 
  i+=1
 else:
     break 
 
i=1
while i<=1:
 infoBTCUSDT=session_auth.user_trade_records(
    symbol="NEARUSDT",
    page=i,
    limit=200
 )
 if infoBTCUSDT['result']['data']!=None:
  trade_data_BTCUSDT = infoBTCUSDT['result']['data']
  for trade_ in trade_data_BTCUSDT: 
     if count == 0: 
  
        
        header = trade_.keys() 
        csv_writer.writerow(header) 
        count += 1
  
     cuenta+=1
     csv_writer.writerow(trade_.values()) 
  i+=1
 else:
     break 
 
i=1
while i<=1:
 infoBTCUSDT=session_auth.user_trade_records(
    symbol="MATICUSDT",
    page=i,
    limit=200
 )
 if infoBTCUSDT['result']['data']!=None:
  trade_data_BTCUSDT = infoBTCUSDT['result']['data']
  for trade_ in trade_data_BTCUSDT: 
     if count == 0: 
  
        
        header = trade_.keys() 
        csv_writer.writerow(header) 
        count += 1
  
     cuenta+=1
     csv_writer.writerow(trade_.values()) 
  i+=1
 else:
     break 
 
i=1
while i<=1:
 infoBTCUSDT=session_auth.user_trade_records(
    symbol="MASKUSDT",
    page=i,
    limit=200
 )
 if infoBTCUSDT['result']['data']!=None:
  trade_data_BTCUSDT = infoBTCUSDT['result']['data']
  for trade_ in trade_data_BTCUSDT: 
     if count == 0: 
  
        
        header = trade_.keys() 
        csv_writer.writerow(header) 
        count += 1
  
     cuenta+=1
     csv_writer.writerow(trade_.values()) 
  i+=1
 else:
     break 
 
i=1
while i<=1:
 infoBTCUSDT=session_auth.user_trade_records(
    symbol="GRTUSDT",
    page=i,
    limit=200
 )
 if infoBTCUSDT['result']['data']!=None:
  trade_data_BTCUSDT = infoBTCUSDT['result']['data']
  for trade_ in trade_data_BTCUSDT: 
     if count == 0: 
  
        
        header = trade_.keys() 
        csv_writer.writerow(header) 
        count += 1
  
     cuenta+=1
     csv_writer.writerow(trade_.values()) 
  i+=1
 else:
     break 
 
 
data_file.close() 
print("csv generado con éxito")
print(cuenta)