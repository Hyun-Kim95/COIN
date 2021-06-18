import pyupbit
import pprint

f = open("key.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()
upbit = pyupbit.Upbit(access,secret)

# 시장가 매수
resp = upbit.buy_market_order("KRW-BTC", 10000) # 티커, 주문가격
pprint.pprint(resp)

# 잔고 조회
btc_balance = upbit.get_balance("KRW-BTC")

# 시장가 매도
upbit.sell_market_order("KRW-BTC", btc_balance)
