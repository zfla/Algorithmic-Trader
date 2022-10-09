from curses import meta
from wsgiref.handlers import format_date_time
import requests
import pandas as pd
import yfinance as yf
from bs4 import BeautifulSoup
import datetime

def get_sp500_instruments():
    res = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    soup = BeautifulSoup(res.content,"lxml")
    table = soup.find_all("table")[0] 
    df = pd.read_html(str(table))
    return list(df[0]["Symbol"])

def get_sp500_df():
    symbols = get_sp500_instruments()
    symbols = symbols[:30]
    ohlcvs = {}
    for symbol in symbols:
        symbol_df = yf.Ticker(symbol).history(period="10y") # ohlcv, dividends, stock splits (only interested in ohlch)
        ohlcvs[symbol] = symbol_df[["Open", "High", "Low", "Close", "Volume"]].rename(
            columns={
                "Open" : "open",
                "High" : "high",
                "Low" : "low",
                "Close" : "close",
                "Volume" : "volume"
            }
        )
        print(ohlcvs[symbol])
    # moving into a single DF

    df = pd.DataFrame(index=ohlcvs["GOOGL"].index)
    df.index.name = "date"
    instruments = list(ohlcvs.keys())

    for inst in instruments:
        inst_df = ohlcvs[inst]
        columns = list(map(lambda x: "{} {}".format(inst, x), inst_df.columns)) # open -> AAPL open
        df[columns] = inst_df

    return df, instruments

# taking ohlcv and adding other statistics
def extend_dataframe(traded, df):
    df.index = pd.Series(df.index).apply(lambda x: format_date(x))
    open_cols = list(map(lambda x: str(x) + " open", traded))
    high_cols = list(map(lambda x: str(x) + " high", traded))
    low_cols = list(map(lambda x: str(x) + " low", traded))
    close_cols = list(map(lambda x: str(x) + " close", traded))
    volume_cols = list(map(lambda x: str(x) + " volume", traded))
    historical_data = df.copy()
    historical_data = historical_data[open_cols + high_cols + low_cols + close_cols + volume_cols]
    historical_data.fillna(method="ffill", inplace=True)
    historical_data.fillna(method="bfill", inplace=True)
    
    for inst in traded:
        historical_data["{} % ret".format(inst)] = historical_data["{} close".format(inst)] / historical_data["{} close".format(inst)].shift(1) - 1 # close to close return statistic
        historical_data["{} % ret vol".format(inst)] =  historical_data["{} % ret".format(inst)].rolling(25).std() # historical rolling sd of returns as realised volatility proxy
        historical_data["{} active".format(inst)] = historical_data["{} close".format(inst)] != historical_data["{} close".format(inst)].shift(1) # checks to see if stock is still trading
    return historical_data

def format_date(date):
    yymmdd = list(map(lambda x: int(x), str(date).split(" ")[0].split("-")))
    return datetime.date(yymmdd[0], yymmdd[1], yymmdd[2])

df = pd.read_excel("./Data/hist.xlsx").set_index("date")
