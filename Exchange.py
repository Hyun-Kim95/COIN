import pyupbit

f = open("key.txt")
lines = f.readline()
access = lines[0].strip()       # access key
secret = lines[1].strip()       # secret key 를 파이썬 문자열로 가져옴
f.close()

upbit = pyupbit.Upbit(access, secret)       # class instance
balance = upbit.get_balance("KRW-BTC")      # 원화 잔고조회 ex) "KRW-BTC"
print(balance)