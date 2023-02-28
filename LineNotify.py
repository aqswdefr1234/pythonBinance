# -*- coding: utf-8 -*-
import ccxt
import time
import requests

global ma_20
global ma_10
global ma_5
global past_ma_20
global past_ma_10
global past_ma_5

def MA(time_frame, period):#종가 평균
    global ma_20
    global ma_10
    global ma_5
    global past_ma_20
    global past_ma_10
    global past_ma_5
    
    sum = 0
    #조사할 기간보다 이틀을 더 가져와 이전 봉에서의 n일선을 구한다.
    btc_ohlcv = binance.fetch_ohlcv(symbol = "BTC/USDT", timeframe = time_frame, since = None, limit = period + 1)
    #20일 평균 구하기
    if period == 20:
        for i in range(1, 21):#최근 봉 기준 인덱스 1에서 20까지
            sum = sum + btc_ohlcv[i][4]
        ma_20 = sum/period
        sum = 0
        for i in range(0, 20):#최근 봉 기준 인덱스 0에서 19까지
            sum = sum + btc_ohlcv[i][4]
        past_ma_20 = sum/period
        sum = 0
    elif period == 10:
        for i in range(1, 11):#최근 봉 기준 인덱스 1에서 20까지
            sum = sum + btc_ohlcv[i][4]
        ma_10 = sum/period
        sum = 0
        for i in range(0, 10):#최근 봉 기준 인덱스 0에서 19까지
            sum = sum + btc_ohlcv[i][4]
        past_ma_10 = sum/period
        sum = 0
    elif period == 5:
        for i in range(1, 6):#최근 봉 기준 인덱스 1에서 20까지
            sum = sum + btc_ohlcv[i][4]
        ma_5 = sum/period
        sum = 0
        for i in range(0, 5):#최근 봉 기준 인덱스 0에서 19까지
            sum = sum + btc_ohlcv[i][4]
        past_ma_5 = sum/period
        sum = 0
            
        
path = "C:/Users/KIM/Desktop/Python/Binance_API_Key.txt"
lines = open(path, "r").readlines()
api_key = lines[1].strip()#스트립은 공백제거
secret_key = lines[3].strip()

print(api_key)
print(secret_key)

#바이낸스 객체생성 선물
binance = ccxt.binance(config = {
    "apiKey":api_key,
    "secret":secret_key,
    "enableRateLimit":True,
    "options":{
        "defaultType":"future"
        }
    })
#라인 메시징
url = "https://notify-api.line.me/api/notify"
token = "" #Issue a token in the Line app and enter the token value here
headers = {'Authorization':'Bearer '+token}

while True:
    MA("1h", 10)
    MA("1h", 5)
    #10일선 위로 5일선이 돌파할때
    if ma_5 > ma_10 and past_ma_5 < past_ma_10:
        message = {"message" : "5가 10 위로"}
        requests.post(url, headers= headers , data = message)
        time.sleep(1800)#30분
    #10일선 아래로 5일선 돌파
    elif ma_5 < ma_10 and past_ma_5 > past_ma_10:
        message = {"message" : "5가 10 아래로"}
        requests.post(url, headers= headers , data = message)
        time.sleep(1800)#30분
    time.sleep(10)
    print(ma_5)
    print(ma_10)
    print(past_ma_5)
    print(past_ma_10)
    print("감시 중")
    
"""
url = "https://notify-api.line.me/api/notify"
token = "tVVrHYxUi5VnwUDZ5xapeVmpzFu6P5XHLnvX7nSEPd1"

headers = {'Authorization':'Bearer '+token}

message = {
    "message" : "Hello world"
}

requests.post(url, headers= headers , data = message)
"""
