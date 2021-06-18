# REST API
import requests                             # pip install requests

url = "https://api.upbit.com/v1/market/all" # 스크렙 해올 주소
params = {                                  # 이 부분이 없어도 기본은 false 로 돼있음
    "isDetails":"false"                     # true: 유의 종목 여부를 볼 수 있음
}                                           # NONE: 해당 사항 없음, CAUTION: 투자유의
resp = requests.get(url, params=params)     # requests 모듈의 get 함수에 url을 준 결과를 갖고 있는 어떤 클래스의 개체
data = resp.json()                          # json 매소드: javascript 언어를 python의 리스트나 딕셔너리로 바꿔줌

원화목록 = []
for i in data:
    a = i['market']                         # i: 딕셔너리, market: 종목이름 키값
    if a.startswith("KRW"):                 # "KRW-BTC"와 같이 원화일때
        원화목록.append(a)
        print(a)
print(len(원화목록))                        # 원화목록의 갯수
