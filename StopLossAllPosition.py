# -*- coding: utf-8 -*-
import ccxt
import time

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

while True :
    btc = binance.fetch_ticker("BTC/USDT")["last"]
    balance = binance.fetch_balance(params = {"type":"future"})
    for posi in balance["info"]["positions"]:
        if posi["symbol"]=="BTCUSDT" :
            entryPrice = float(posi["entryPrice"])
            unrealizedProfit = float((posi["unrealizedProfit"]))
            positionAmt = float(posi["positionAmt"])
            print(entryPrice)
            print(unrealizedProfit)
            print(positionAmt)
    if btc < entryPrice*(97/100) and positionAmt > 0:#롱포지션으로 -35퍼 되면(두개의 조건을 조합하여 어느방향 포지션인지 알수 있음)
        binance.create_limit_sell_order(symbol = "BTC/USDT", amount = abs(positionAmt), price = btc-10)
        binance.cancel_all_orders(symbol = "BTC/USDT")
    elif btc > entryPrice*(103/100) and positionAmt < 0:#숏포지션 -35퍼
        print(abs(positionAmt))
        binance.create_limit_buy_order(symbol = "BTC/USDT", amount = abs(positionAmt), price = btc+10)
        binance.cancel_all_orders(symbol = "BTC/USDT")
    time.sleep(10)