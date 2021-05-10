import pyupbit
import pandas as pd # 월봉의 거래량이 너무 커서 지수형식으로 나오는 것을 보기 좋게 바꿔주기 위해

df1 = pyupbit.get_ohlcv("KRW-BTC", "minute1",5)     # 세 번째 인자를 생략하면 최대 200 개의 정보를 가져옴
print(df1)                                          # 분봉: 1,3,5,10,15,30,60,240 가능

df2 = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="day", count=5)  # 일봉
print(df2)

df3 = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="week", count=5) # 주봉
# df3.to_excel("week_btc.xlsx")   # 결과를 엑셀로 저장
print(df3)

pd.options.display.float_format = "{:.1f}".format   # 소수점 이하 한자리까지만 출력
df4 = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="month", count=5)    # 월봉
print(df4)