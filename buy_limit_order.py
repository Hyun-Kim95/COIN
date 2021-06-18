import pyupbit
import pprint

f = open("key.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()
upbit = pyupbit.Upbit(access, secret)

# xrp limit order buy
xrp_price = pyupbit.get_current_price("KRW-XRP")
print(xrp_price)  # 일단 금액 확인

# 지정가 주문을 통해서 매매 금액보다 낮게 주문 넣기
resp = upbit.buy_limit_order("KRW-XRP", 200, 100) # buy_limit_order(티커, 주문가격, 주문량) : 최소수량은 홈페이지에서 확인해야 함
pprint.pprint(resp)