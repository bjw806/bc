import fetch_data
import cmc
from numpy import genfromtxt

data_csv = genfromtxt('./historical_data/history.csv', delimiter=',', dtype=str)

def search_historical_data(base, target, start, end):
    for x in range(1):
        if(float(data_csv[x][0]) == 'start'):
            start_price = float(data_csv[x][4])

    return 0


def convert_price(base, target, when):

    if(when == 'now'):
        pass
    return 0


if __name__ == '__main__':
    # example

    print("\r1: Search historical data")
    print("2: Convert price")
    print("3: Fetch historical data")
    command = input("Enter what you want: ")

    if (command == 1):
        base = input("base currency: ")
        target = input("target currency: ")
        start = input("starting at: ")
        end = input("ending at: ")
        search_historical_data(base, target, start, end)

    elif (command == 2):
        base = input("from: ")
        target = input("to: ")
        when = input("at: ")
        convert_price(base, target, when)

    elif (command == 3):
        fetch_data.fetchData("BTCUSDT", 10)
