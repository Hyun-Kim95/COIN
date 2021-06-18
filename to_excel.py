import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC")
# print(df.head())   # 일봉확인
df.to_excel("btc.xlsx")