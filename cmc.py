from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
    'symbol': 'BTC',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '14b8bd8f-3b8d-466d-914d-a038dbfec958',
}

session = Session()
session.headers.update(headers)

def current_price():
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        price = data['data']['BTC']['quote']['USD']
        return price
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

"""if __name__ == '__main__':
    d = cmctest()
    #print(repr(r.status['timestamp']))
    #print(repr(d.data['quote']))
    d = d['data']['BTC']['quote']['USD']
    print(d)"""
