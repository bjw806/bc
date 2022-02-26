import sqlite3
import datetime


def search(source, target, when):
    if (when == 'NOW' or when == 'now'):
        date = datetime.datetime.now()
        when = date.strftime('%Y-%m-%d %H:%M')

    conn = sqlite3.connect("cryptodata.db", isolation_level=None)
    c = conn.cursor()

    c.execute("SELECT * FROM 'cryptodata' WHERE source=:idn1 AND target=:idn2 AND timestamp=:idn3",
              {"idn1": source, "idn2": target, "idn3": when})
    found = c.fetchone() # ('2022-02-05 19:34', 'ATOM', 'XRP', 46.607)
    conn.close()

    if (found == None):
        print("*not found")
        return -1

    return found

def search_historical_data(source, target, start, end):
    try:
        ret1 = search(source, target, start)
        index_start = ret1[0]
        ret2 = search(source, target, end)
        index_end = ret2[0]

        conn = sqlite3.connect("cryptodata.db", isolation_level=None)
        c = conn.cursor()

        c.execute("SELECT * FROM 'cryptodata' WHERE id BETWEEN ? AND ? AND source=? AND target=?",
                  [index_start, index_end, source, target])

        found = c.fetchall()
        conn.close()

        return found
    except:
        print("*Input format is invalid.")
        return -1

def convert_price(source, target, when):
    try:
        ret = search(source, target, when)
        ratio = ret[4]
        return ratio
    except:
        print("*Input format is invalid.")
        return -1

def print_historical_data(source, target, start, end):
    found = search_historical_data(source, target, start, end)
    if(found == -1):
        return
    for x in range(len(found)):
        print(found[x][1], "[1 " + target + " = " + str(found[x][4]) + " " + source + "]")

def print_converted_price(source, target, when):
    ratio = convert_price(source, target, when)
    if(ratio == -1):
        return
    print("[1 " + target + " = " + str(ratio) + " " + source + "]")
