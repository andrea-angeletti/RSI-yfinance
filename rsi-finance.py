# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time
start_time = time.time()
import yfinance as yf

from datetime import datetime, timedelta

from datetime import datetime, timedelta

now = datetime.now()
today=now.strftime('%Y-%m-%d')

period=14

before=now-timedelta(period+95)

then=before.strftime('%Y-%m-%d')  

def rsi(df, periods = 14):
    """
    Returns a pd.Series with the relative strength index.
    """
    close_delta = df['Close'].diff()

    # Make two series: one for lower closes and one for higher closes
    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)
    
    # Use exponential moving average
    ma_up = up.ewm(com = periods - 1, adjust=True, min_periods = periods).mean()
    ma_down = down.ewm(com = periods - 1, adjust=True, min_periods = periods).mean()
 
    rsi = ma_up / ma_down
    rsi = 100 - (100/(1 + rsi))
    return rsi

def notify (lista):
    promising=[]
    for i in lista:
        data = yf.download(i, start=then, end=today)
        a=rsi(data)
        if a[-1]>67 or a[-1]<33:
            #print(i)
            #print(a[-1])
            promising.append(i)
            promising.append(a[-1])
    for i in promising:
        #st.write(i)      
        print(i)
def test ():
   
  
        data = yf.download("AAPL", start=then, end=today)
        a=rsi(data)
        print(a[-1])

test()

indexes=[
"^NYA",
"^XAX",
"^BUK100P",
"^RUT",
"^VIX",
"^FTSE",
"^GDAXI",
"^FCHI",

"^N100",
"^BFX",
"IMOEX.ME",
"^N225",
"^HSI",
"000001.SS",
"399001.SZ",
#"^STI",
"^AXJO",
"^AORD",
"^BSESN",
#"^JKSE",
"^KLSE",
"^NZ50",
"^KS11",
#"^TWII",
"^GSPTSE",
"^BVSP",
#"^MXX",
#"^MERV",

#"^CASE30",
#"^JN0U.JO"
]

currencies = [
"EURUSD=X",
"JPY=X",
"GBPUSD=X",
"AUDUSD=X",
"NZDUSD=X",
"EURJPY=X",
"GBPJPY=X",
"EURGBP=X",
"EURCAD=X",
"EURSEK=X",
"EURCHF=X",
"EURHUF=X",
"EURJPY=X",
"CNY=X",
"HKD=X",
"SGD=X",
"INR=X",
"MXN=X",
#"PHP=X",
"IDR=X",
#"THB=X",
#"MYR=X",
"ZAR=X",
"RUB=X",
"CADJPY=X",
"CADCHF=X"
]


commodities = [
"ES=F",
#"YM=F",
"NQ=F",
"RTY=F",
"ZB=F",
"ZN=F",
"ZF=F",
"ZT=F",
"GC=F",
"MGC=F",
"SI=F",
"SIL=F",
"PL=F",
"HG=F",
"PA=F",
"CL=F",
"HO=F",
"NG=F",
"RB=F",
"BZ=F",
"B0=F",
"ZC=F",
"ZO=F",
"KE=F", #wheat
#"ZR=F",
"ZM=F",
#"ZL=F", soybeans oil future
"ZS=F",
"GF=F",
"HE=F",
"LE=F",
"CC=F",
"KC=F",
"CT=F",
#"LBS=F",
"OJ=F",
"SB=F",
]

lista=indexes+currencies+commodities


notify(lista)



print("--- %s seconds ---" % (time.time() - start_time))
