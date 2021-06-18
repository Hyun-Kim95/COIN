# 코인 자동 매매

## pyupbit(import pyupbit)

### 마켓 코드 조회

* `tickers = pyupbit.get_tickers(fiat="KRW")`

  > get_tickers: 마켓 코드를 파이썬 리스트 타입으로 리턴
  >
  > fiat="KRW": 원화시장의 목록만 불러옴

### 시세 캔들 조회

> o: open 시가
>
> h: high 고가
>
> l: low 저가
>
> c: close 종가
>
> v: volume 거래량

#### * 분봉

* `df = pyupbit.get_ohlcv("KRW=BTC", "minute1", 5)`
  * 세 번째 인자를 생략하면 최대 200 개의 정보를 가져옴
  * 분봉: 1,3,5,10,15,30,60,240 가능

#### * 일봉

* `df = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="day", count=5)`
  * count를 생략하면 최대 200 개의 정보를 가져옴

#### * 주봉

* `df = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="week", count=5)`
  * count를 생략하면 최대 200 개의 정보를 가져옴

#### * 월봉

* `df = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="month", count=5)`

  * count를 생략하면 최대 200 개의 정보를 가져옴

  * 거래량이 너무 커서 지수 형식으로 출력됨

    * ```python
      import pandas as pd
      pd.options.display.float_format = "{:.1f}".format
      ```

      > 지수 형식이 보기 힘드니, 소수점 첫째 자리까지만 출력하도록 함

### 현재가 정보

* ```python
  import pyupbit
  tickers = ["KRW-BTC", "KRW-XRP"]
  price = pyupbit.get_current_price(tickers)
  ```

### 호가 정보

* ```python
  import pyupbit
  import pprint
  
  orderbooks = pyupbit.get_orderbook("KRW-BTC")
  pprint.pprint(orderbooks)
  ```

  > pprint: 보기 좋게 프린트

  * 위에서 부터 1호가 ~ 15호가 까지 제공
  * ask: 매도 호가
    * total_ask_size: 매도 호가의 총 잔량
  * bid: 매수 호가
    * total_bid_size: 매수 호가의 총 잔량

* 총 잔량만 확인하는 법

* ```python
  import pyupbit
  
  orderbooks = pyupbit.get_orderbook("KRW-BTC")
  orderbook = orderbooks[0]       # KRW-BTC 만 주었으므로 첫번째 인덱스
  
  total_ask_size = orderbook['total_ask_size']
  total_bid_size = orderbook['total_bid_size']
  
  print("매도 호가의 총 잔량: ", total_ask_size)
  print("매수 호가의 총 잔량: ", total_bid_size)
  ```

### 로그인 및 자동화 준비

* 업비트 홈페이지 하단 오른쪽에 Open API 들어가서 신청을 해야 함
  * 인증 4단계까지 마쳐야 함
* Open API 사용하기 클릭
* 입금하기, 출금하기 는 보안상 위험할 수 있으니 체크하지 않음
* '접속관리'의 아이피주소를 확인하여 '특정 IP에서만 실행' 칸에 적어주고 키 발급을 클릭
* Access key, Secret key 발급 완료(메모장에 붙혀넣어 놓기)

### 잔고 확인

```python
import pyupbit

f = open("key.txt")
lines = f.readline()
access = lines[0].strip()       # access key
secret = lines[1].strip()       # secret key 를 파이썬 문자열로 가져옴
f.close()

upbit = pyupbit.Upbit(access, secret)   	# class instance
balance = upbit.get_balance("KRW-BTC")      # 원화 잔고조회 ex) "KRW-BTC"
print(balance)
```

### 지정가 주문

#### 매수

```python
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
resp = upbit.buy_limit_order("KRW-XRP", 200, 100)
# buy_limit_order(티커, 주문가격, 주문량) : 최소수량은 홈페이지에서 확인해야 함
pprint.pprint(resp)
```

#### 매도

* xrp_balance = upbit.get_balance("KRW-SRP")
  * 보유 수량 확인
* resp = upbit.sell_limit_order("KRW-XRP", 265, xrp_balance)
* print(resp)

### 사이트

> https://docs.upbit.com/reference					<- 개발자 가이드
>
> https://wikidocs.net/book/1665						<- 파이썬을 이용한 비트코인 자동매매(개정판)
>
> https://github.com/sharebook-kr/pyupbit	 <- pyupbit github

