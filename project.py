import pyupbit
import time
import datetime

def cal_target(ticker):                 # 목표 매수가 구하는 함수
    df = pyupbit.get_ohlcv(ticker, "day")
    yesterday = df.iloc[-2]
    today = df.iloc[-1]
    yesterday_range = yesterday['high']-yesterday['low']
    target = today['open'] + yesterday_range * 0.5
    return target

# 객체 생성
f = open("key.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()
upbit = pyupbit.Upbit(access,secret)

# 변수 설정
target = cal_target("KRW-BTC")
op_mode = False         # 매도 후 다음 목표가 생성 전까지 매수 금지를 위한 체크
hold = False            # 코인을 보유 중인지 체크

while True:
    now = datetime.datetime.now()   # 현재 시간 정보

    # 매도 시도
    if now.hour == 8 and now.minute == 59 and 50 <= now.second <= 59:
        if op_mode is True and hold is True:
            btc_balance = upbit.get_balance("KRW-BTC")
            upbit.sell_market_order("KRW-BTC", btc_balance)     # 가진 전량을 시장가로 매도
            hold = False

        op_mode = False
        time.sleep(10)

    # 09:00:00 목표가 갱신
    if now.hour == 9 and now.minute == 0 and 20 <= now.second <= 30:
        target = cal_target("KRW-BTC")
        op_mode = True
        time.sleep(10)

    price = pyupbit.get_current_price("KRW-BTC")    # 현재가

    # 매초마다 조건을 확인한 후 매수 시도
    if op_mode is True and price is not None and hold is False and price >= target:     # 예외 발생 시 price 가 None이 나옴
        # 매수
        krw_balance = upbit.get_balance("KRW")
        upbit.buy_market_order("KRW-BTC", krw_balance)
        hold = True

    # 상태 출력 (약 1초에 한번 현재가 출력)
    print(f"현재시간: {now} 목표가: {target} 현재가: {price} 보유상태: {hold} 동작상태: {op_mode}")

    time.sleep(1)
