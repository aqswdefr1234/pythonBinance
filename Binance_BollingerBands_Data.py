# -*- coding: utf-8 -*-
import ccxt
import pprint
import time

#주문조건식에 사용하기 위한 변수 선언
global trigger
global orderBtcPrice
global amt #포지션 크기
global ma_Trigger
global upperTrigger
global lowerTrigger
global btc
global startOrderType

global ma_20
global ma_120
global upperLimit
global lowerLimit
#global order_Id
startOrderType = -1
trigger = -1
ma_Trigger = -1
orderBtcPrice = 0
lowerTrigger = 1
upperTrigger = 1

#order_Id = ""
def StartOrder_else(market,binance_,positionSize):
    #upperTrigger,lowerTrigger 초기화
    global btc
    global ma_Trigger
    global trigger
    global orderBtcPrice
    
    global ma_20
    
    #주문 조건식
    if upperLimit - 30 < btc and upperLimit + 400 > btc :#상한선 근처에 왔을 때
        order = binance_.create_limit_sell_order(symbol = market, amount = positionSize, price = btc)
        pprint.pprint(order)
        orderBtcPrice = btc
        trigger = 0
    elif lowerLimit - 400 < btc and lowerLimit + 30 > btc :#하한선 근처에 왔을 때
        order = binance_.create_limit_buy_order(symbol = market, amount = positionSize, price = btc)
        pprint.pprint(order)
        orderBtcPrice = btc
        trigger = 1
    elif upperLimit + 440 < btc :#상한선보다 많이 넘어갔을 때
        order = binance_.create_limit_sell_order(symbol = market, amount = positionSize, price = btc)
        pprint.pprint(order)
        orderBtcPrice = btc
        trigger = 4
    elif lowerLimit - 440 > btc :#하한선보다 많이 내려왔을 때
        order = binance_.create_limit_buy_order(symbol = market, amount = positionSize, price = btc)
        pprint.pprint(order)
        orderBtcPrice = btc
        trigger = 5
    else:
        print("not order")
        
def StartOrder_elif2(market,binance_,positionSize):
    #upperTrigger,lowerTrigger 초기화
    global btc
    global trigger
    global orderBtcPrice
    
    #주문 조건식
    if upperLimit - 30 < btc and upperLimit > btc :#상한선 근처에 왔을 때
        order = binance_.create_limit_sell_order(symbol = market, amount = positionSize, price = btc)
        pprint.pprint(order)
        orderBtcPrice = btc
        trigger = 0
    elif lowerLimit < btc and lowerLimit + 30 > btc :#하한선 근처에 왔을 때
        order = binance_.create_limit_buy_order(symbol = market, amount = positionSize, price = btc)
        pprint.pprint(order)
        orderBtcPrice = btc
        trigger = 1
    elif upperLimit + 500 < btc :#상한선보다 많이 넘어갔을 때
        order = binance_.create_limit_sell_order(symbol = market, amount = positionSize, price = btc)
        pprint.pprint(order)
        orderBtcPrice = btc
        trigger = 4
    elif lowerLimit - 500 > btc :#하한선보다 많이 내려왔을 때
        order = binance_.create_limit_buy_order(symbol = market, amount = positionSize, price = btc)
        pprint.pprint(order)
        orderBtcPrice = btc
        trigger = 5
    else:
        print("not order")

def StartOrder_if(market,binance_,positionSize):
    #upperTrigger,lowerTrigger 초기화
    global btc
    global trigger
    global orderBtcPrice
    
    global ma_20
    global upperLimit
    global lowerLimit
    
    if lowerLimit - (25/1000)*btc < btc and lowerLimit + 50 > btc :#하한선 근처에 왔을 때
        order = binance_.create_limit_buy_order(symbol = market, amount = positionSize, price = btc)
        pprint.pprint(order)
        orderBtcPrice = btc
        trigger = 1
    elif ma_20 < btc and ma_20 + 20 >= btc : #현재가가 20일선보다 높은상태에서 20일선에 접근한다면
        order = binance_.create_limit_buy_order(symbol = market, amount = positionSize, price = btc)#20일선 보다 3원 높에 매수주문
        pprint.pprint(order)
        orderBtcPrice = btc
        trigger = 2
    elif lowerLimit - (25/1000)*btc > btc :#하한선보다 많이 내려왔을 때
        order = binance_.create_limit_buy_order(symbol = market, amount = positionSize, price = btc)
        pprint.pprint(order)
        orderBtcPrice = btc
        trigger = 5
    else:
        print("not order")

def StartOrder_elif(market,binance_,positionSize):
    #upperTrigger,lowerTrigger 초기화
    global btc
    global trigger
    global orderBtcPrice
    
    global ma_20
    global upperLimit
    global lowerLimit
    
    if upperLimit - 50 < btc and upperLimit + (25/1000)*btc > btc :#상한선 근처에 왔을 때
        order = binance_.create_limit_sell_order(symbol = market, amount = positionSize, price = btc)
        pprint.pprint(order)
        orderBtcPrice = btc
        trigger = 0
    elif ma_20 > btc and ma_20 -20 <= btc : #현재가가 20일선보다 낮은상태에서 20일선에 접근한다면
        order = binance_.create_limit_sell_order(symbol = market, amount = positionSize, price = btc)#20일선 보다 3원 낮게 매도주문
        pprint.pprint(order)
        orderBtcPrice = btc
        trigger = 3
    elif upperLimit + (25/1000)*btc < btc :#상한선보다 많이 넘어갔을 때
        order = binance_.create_limit_sell_order(symbol = market, amount = positionSize, price = btc)
        pprint.pprint(order)
        orderBtcPrice = btc
        trigger = 4
    else:
        print("not order")

def SellOrBuy(binance_,market,orderBtcPrice_,positionSize):#포지션이 열렸을 때 판매 리미트 걸기
    global startOrderType
    global trigger
    
    if startOrderType == 0:
        if trigger == 1:#하한선 근처에서 매수 포지션 열렸을 때
            order = binance_.create_limit_sell_order(symbol = market, amount = positionSize, price = orderBtcPrice_*(1015/1000))
            pprint.pprint(order)
        elif trigger == 2:#20일선 근처에서 매수 포지션 열렸을 때
            order = binance_.create_limit_sell_order(symbol = market, amount = positionSize, price = orderBtcPrice_*(101/100))
            pprint.pprint(order)
        elif trigger == 5:#하한선 넘어가 매수 포지션 열렸을 때
            order = binance_.create_limit_sell_order(symbol = market, amount = positionSize, price = orderBtcPrice_*(102/100))
            pprint.pprint(order)
            
    elif startOrderType == 1:
        if trigger == 0:#상한선 근처에서 매도 포지션 열렸을 때. 1퍼센트 높은값
            order = binance_.create_limit_buy_order(symbol = market, amount = positionSize, price = orderBtcPrice_*(985/1000))
            pprint.pprint(order)
        elif trigger == 3:#20일선 근처에서 매도 포지션 열렸을 때
            order = binance_.create_limit_buy_order(symbol = market, amount = positionSize, price = orderBtcPrice_*(99/100))
            pprint.pprint(order)
        elif trigger == 4:#상한선 넘어가 매도 포지션 열렸을 때. 1퍼센트 높은값
            order = binance_.create_limit_buy_order(symbol = market, amount = positionSize, price = orderBtcPrice_*(98/100))
            pprint.pprint(order)
            
    elif startOrderType == 3:
        if trigger == 0:#상한선 근처에서 매도 포지션 열렸을 때. 1퍼센트 높은값
            order = binance_.create_limit_buy_order(symbol = market, amount = positionSize, price = orderBtcPrice_*(99/100))
            pprint.pprint(order)
        elif trigger == 1:#하한선 근처에서 매수 포지션 열렸을 때
            order = binance_.create_limit_sell_order(symbol = market, amount = positionSize, price = orderBtcPrice_*(101/100))
            pprint.pprint(order)
        elif trigger == 4:#상한선 넘어가 매도 포지션 열렸을 때. 1퍼센트 높은값
            order = binance_.create_limit_buy_order(symbol = market, amount = positionSize, price = orderBtcPrice_*(99/100))
            pprint.pprint(order)
        elif trigger == 5:#하한선 넘어가 매수 포지션 열렸을 때
            order = binance_.create_limit_sell_order(symbol = market, amount = positionSize, price = orderBtcPrice_*(101/100))
            pprint.pprint(order)
            
    else:
        if trigger == 0:#상한선 근처에서 매도 포지션 열렸을 때. 1퍼센트 높은값
            order = binance_.create_limit_buy_order(symbol = market, amount = positionSize, price = orderBtcPrice_*(98/100))
            pprint.pprint(order)
        elif trigger == 1:#하한선 근처에서 매수 포지션 열렸을 때
            order = binance_.create_limit_sell_order(symbol = market, amount = positionSize, price = orderBtcPrice_*(102/100))
            pprint.pprint(order)
        elif trigger == 2:#20일선 근처에서 매수 포지션 열렸을 때
            order = binance_.create_limit_sell_order(symbol = market, amount = positionSize, price = orderBtcPrice_*(1005/1000))
            pprint.pprint(order)
        elif trigger == 3:#20일선 근처에서 매도 포지션 열렸을 때
            order = binance_.create_limit_buy_order(symbol = market, amount = positionSize, price = orderBtcPrice_*(995/1000))
            pprint.pprint(order)
        elif trigger == 4:#상한선 넘어가 매도 포지션 열렸을 때. 1퍼센트 높은값
            order = binance_.create_limit_buy_order(symbol = market, amount = positionSize, price = orderBtcPrice_*(98/100))
            pprint.pprint(order)
        elif trigger == 5:#하한선 넘어가 매수 포지션 열렸을 때
            order = binance_.create_limit_sell_order(symbol = market, amount = positionSize, price = orderBtcPrice_*(102/100))
            pprint.pprint(order)
        
def PositionSize():
    global amt
    #현재 포지션 값
    balance = binance.fetch_balance(params = {"type":"future"})
    print("선물 지갑",balance["USDT"]["free"])
    print("선물 지갑",balance["USDT"])
    for posi in balance["info"]["positions"]:
        if posi["symbol"]=="BTCUSDT" :
            amt = float(posi["positionAmt"])

def BollingerBands(market,standardTime,binance_,btc_ohlcv_):#스탠다드 타임은 무슨 봉 기준으로 볼린저 밴드를 계산 할 것이냐
    global ma_20
    global upperLimit
    global lowerLimit
    standardDeviation = 0 #표준편차
    
    #표준편차로 상한선 하한선 구하기
    standardDeviation = float(Dispersion(btc_ohlcv_)) #표준편차를 구하는 함수
    upperLimit = ma_20 + standardDeviation*2
    lowerLimit = ma_20 - standardDeviation*2
    #실제보다 상한선이 12원정도 더 높게나옴
    #실제보다 상한선이 12원정도 더 낮게나옴
    
def Dispersion(ohlcv): #표준편차를 구하는 함수이다.
    dispersion = [0]*20 # 요소값 - 평균값
    variance = 0 #분산
    sumOfSquares = 0 #제곱합
    for i in range(20):
        dispersion[i] = float(ohlcv[i][4] - ma_20) #분산
    for i in range(20):
        sumOfSquares = float(sumOfSquares) + float(dispersion[i])**2 #제곱
    variance = float(sumOfSquares/19) #제곱의 합을 나누기 (20개 - 1)
    return float(variance**(1/2)) #분산의 제곱근이 표준편차이다.

def MA20(btc_ohlcv_):
    global ma_20
    sum = 0
    #20일 평균 구하기
    for i in range(20):
        sum = sum + btc_ohlcv_[i][4] #종가 20개 봉 더하기
    ma_20 = sum/20
    
def MA120(binance_):
    global ma_120
    btc_ohlcv = binance_.fetch_ohlcv(symbol = "BTC/USDT", timeframe = "4h", since = None, limit = 120)
    sum = 0
    #120일 평균 구하기
    for i in range(120):
        sum = sum + btc_ohlcv[i][4] #종가 20개 봉 더하기
    ma_120 = sum/120
    
#api키 가져오기
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

#볼린저 밴드 함수 실행
PositionSize()#거래전 포지션 크기값
while True:
    ini_amt = amt#초기 포지션크기 읽기
    print(ini_amt)
    while True:
        btc_ohlcv = binance.fetch_ohlcv(symbol = "BTC/USDT", timeframe = "4h", since = None, limit = 20)
        MA20(btc_ohlcv)
        MA120(binance)
        BollingerBands("BTC/USDT","4h",binance,btc_ohlcv)
        print(ma_20)
        print(ma_120)
        print(upperLimit)
        print(lowerLimit)
        btc = binance.fetch_ticker("BTC/USDT")["last"]
        print(btc)
        if btc > ma_120 and (upperLimit-lowerLimit) > (3/100)*ma_20:#120 선 위에 있고 볼린저 밴드 간격이 넓어질 때
            StartOrder_if("BTC/USDT",binance,0.01)
            startOrderType = 0
        elif btc < ma_120 and (upperLimit-lowerLimit) > (3/100)*ma_20:#120 선 아래에 있고 볼린저 밴드 간격이 넓어질 때
            StartOrder_elif("BTC/USDT",binance,0.01)
            startOrderType = 1
        elif (upperLimit-lowerLimit) < (203/10000)*ma_20:
            StartOrder_elif2("BTC/USDT",binance,0.01)
            startOrderType = 3
        else:
            StartOrder_else("BTC/USDT",binance,0.01)
            startOrderType = 2
            
        time.sleep(2)
        if trigger != -1:
            break

    while True:
        time.sleep(5)
        PositionSize()#포지션 
        print(amt)
        print(ini_amt)
        if ini_amt == amt:
            print("true")
        if ini_amt != amt:
            break
        
    SellOrBuy(binance,"BTC/USDT",orderBtcPrice,0.01)
    print("구매 후 리미트 설정 완료")
    
    if(trigger == 4 or trigger == 5):
        time.sleep(3600)
    else:
        time.sleep(1800)
    if amt == 0 : #포지션이 닫혔으면 ma트리거값을 초기화한다. 남아 있는 미체결 주문을 취소한다.
        ma_Trigger = -1
        binance.cancel_all_orders(symbol = "BTC/USDT")
    while True: #0.01 개 이상 살 수 있을 만큼 돈이 있으면break
        time.sleep(20)
        balance = binance.fetch_balance(params = {"type":"future"})
        if float(balance["USDT"]["free"]) > btc/1000 + 0.5:
            break
    trigger = -1
#break후 trigger값 읽어와 대응

