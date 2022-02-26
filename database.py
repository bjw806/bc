import sqlite3
import datetime
import time as TIME
import sys
from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError

symbol_str = "BTC,ETH,USDT,BNB,USDC,ADA,SOL,XRP,LUNA,DOT," \
          "DOGE,AVAX,BUSD,MATIC,SHIB,UST,CRO,WBTC,DAI,ATOM," \
          "LTC,LINK,NEAR,UNI,ALGO,TRX,FTT,BCH,MANA,FTM"

symbol_list = ["BTC","ETH","USDT","BNB","USDC","ADA","SOL","XRP","LUNA","DOT",
          "DOGE","AVAX","BUSD","MATIC","SHIB","UST","CRO","WBTC","DAI","ATOM",
          "LTC","LINK","NEAR","UNI","ALGO","TRX","FTT","BCH","MANA","FTM"]

cmc = CoinMarketCapAPI('14b8bd8f-3b8d-466d-914d-a038dbfec958')


def current_price(source):
    try:
        r = cmc.cryptocurrency_quotes_latest(symbol=symbol_str, convert=source)
    except CoinMarketCapAPIError as e:
        r = e.rep

    date = datetime.datetime.now()
    time = date.strftime('%Y-%m-%d %H:%M')  #:%S

    for x in range(len(symbol_list)):
        t_price = repr(r.data[symbol_list[x]]['quote'][source]['price'])
        data.append((time, symbol_list[x], source, round(float(t_price), 5)))
    return data


def create_database():
    conn = sqlite3.connect("cryptodata.db", isolation_level=None)
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS cryptodata \
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp DATETIME DEFAULT (DATETIME('now', 'localtime')), target name, source name, price real)")

    for x in range(30):
        data = current_price(symbol_list[x])

    c.executemany("INSERT INTO cryptodata(timestamp, target, source, price) VALUES(?,?,?,?)", data)
    c.execute("CREATE INDEX IF NOT EXISTS time ON cryptodata(timestamp)")
    c.execute("CREATE INDEX IF NOT EXISTS target_currency ON cryptodata(target)")

    conn.close()


def run_database():
    while (1):
        date = datetime.datetime.now()
        time = date.strftime('%H:%M:%S')
        sys.stdout.write("\r{0}".format(time))
        sys.stdout.flush()
        sec = (str(time).split(':'))[2]
        global data
        data = []
        if (sec == '00'):
            create_database()
        else:
            TIME.sleep(1)


if __name__ == '__main__':
    run_database()