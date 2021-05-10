import pyupbit

krw_tickers = pyupbit.get_tickers(fiat="KRW")

prices = pyupbit.get_current_price(krw_tickers)

for k, v in prices.items(): # 딕셔너리를 for문으로 돌리려면 .items()를 이용하면 됨
    print(k, v)