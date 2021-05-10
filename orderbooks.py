import pyupbit
import pprint   

orderbooks = pyupbit.get_orderbook("KRW-BTC")
# pprint.pprint(orderbooks)     # 보기 좋게 프린트
orderbook = orderbooks[0]       # KRW-BTC 만 주었으므로 첫번째 인덱스

total_ask_size = orderbook['total_ask_size']
total_bid_size = orderbook['total_bid_size']

print("매도 호가의 총 잔량: ", total_ask_size)
print("매수 호가의 총 잔량: ", total_bid_size)