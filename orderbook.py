import time
import requests
import datetime
import pandas as pd

previous_date = None

while True:
    timestamp = datetime.datetime.now()
    current_date = timestamp.strftime('%Y-%m-%d')
    current_time = timestamp.strftime('%Y-%m-%d %H:%M:%S')

    file_name = f"data_{current_date}.csv"

    if current_date != previous_date:
        print(f"새로운 파일 생성: {file_name}")
        previous_date = current_date

        with open(file_name, 'w') as file:
            file.write("price   | quantitiy | type | timestamp\n")

    response = requests.get('https://api.bithumb.com/public/orderbook/BTC_KRW/?count=5')
    book = response.json()
    data = book['data']
    bids = pd.DataFrame(data['bids']).apply(pd.to_numeric, errors='coerce')
    bids.sort_values('price', ascending=False, inplace=True)
    bids['type'] = 0
    asks = pd.DataFrame(data['asks']).apply(pd.to_numeric, errors='coerce')
    asks.sort_values('price', ascending=True, inplace=True)
    asks['type'] = 1
    df = bids.append(asks)
    df['timestamp'] = current_time
    df.to_csv(file_name, index=False, header=False, mode='a', sep='|')
    time.sleep(4.9)
