import pyupbit

tickers = pyupbit.get_tickers(fiat="KRW")       # get_tickers 함수: 마켓 코드를 파이썬 리스트 타입으로 리턴함
print(tickers)                                  # fiat = "KRW": 원화시장의 목록만 불러옴
print(len(tickers))