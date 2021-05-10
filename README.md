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



### 사이트

> https://docs.upbit.com/reference					<- 개발자 가이드
>
> https://wikidocs.net/book/1665						<- 파이썬을 이용한 비트코인 자동매매(개정판)
>
> https://github.com/sharebook-kr/pyupbit	 <- pyupbit github

