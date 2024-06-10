import os
import pandas as pd

# 파일 경로 설정
input_file_path = os.path.expanduser('~/ai-crypto-project-3-live-btc-krw.csv')

# 파일 존재 여부 확인
if not os.path.exists(input_file_path):
    print(f"Error: The file {input_file_path} does not exist.")
else:
    # CSV 파일 읽기
    df = pd.read_csv(input_file_path)
    
    # PnL 계산
    sell_pnl = df[df['side'] == 1].apply(lambda row: row['amount'] - row['fee'], axis=1).sum()
    buy_pnl = df[df['side'] == 0].apply(lambda row: -row['amount'] - row['fee'], axis=1).sum()
    
    # 총 PnL 계산
    total_pnl = sell_pnl + buy_pnl
    
    # 결과 출력
    print(f"Total PnL: {total_pnl}") 
