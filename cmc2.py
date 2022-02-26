from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError

cmc = CoinMarketCapAPI('14b8bd8f-3b8d-466d-914d-a038dbfec958')

#r = cmc.cryptocurrency_info(symbol='BTC')

#cmc = CoinMarketCapAPI(debug=True)
#cmc.cryptocurrency_info(symbol='BTC')

target = ['BTC', 'ETH', 'XRP', 'USDT', 'BNB', 'SOL', 'DOT', 'DOGE', 'ATOM', 'LTC']

if __name__ == '__main__':
    try:
        r = cmc.cryptocurrency_quotes_latest(symbol="BTC,ETH,XRP,USDT,BNB,SOL,DOT,DOGE,ATOM,LTC",convert='USD')
    except CoinMarketCapAPIError as e:
        r = e.rep

    print(repr(r.status['timestamp']))
    #print(repr(r.data))
    #print(repr(r.data))
    #print(repr(r.data['BTC']['quote']['USD']['last_updated']))
    #print(repr(r.data['BTC']['quote']['USD']['price']))
    #print(repr(r.data['BTC']['quote']['ADA']['price']))
    print(repr(r.data))
    #print(repr(r.data))
"""{'BTC': 
     {'id': 1, 
      'name': 'Bitcoin',
      'symbol': 'BTC',
      'slug': 'bitcoin',
      'num_market_pairs': 9123,
      'date_added': '2013-04-28T00:00:00.000Z',
      'tags': ['mineable', 'pow', 'sha-256', 'store-of-value', 'state-channel', 'coinbase-ventures-portfolio', 'three-arrows-capital-portfolio', 'polychain-capital-portfolio', 'binance-labs-portfolio', 'blockchain-capital-portfolio', 'boostvc-portfolio', 'cms-holdings-portfolio', 'dcg-portfolio', 'dragonfly-capital-portfolio', 'electric-capital-portfolio', 'fabric-ventures-portfolio', 'framework-ventures-portfolio', 'galaxy-digital-portfolio', 'huobi-capital-portfolio', 'alameda-research-portfolio', 'a16z-portfolio', '1confirmation-portfolio', 'winklevoss-capital-portfolio', 'usv-portfolio', 'placeholder-ventures-portfolio', 'pantera-capital-portfolio', 'multicoin-capital-portfolio', 'paradigm-portfolio'], 
      'max_supply': 21000000, 
      'circulating_supply': 18949081, 
      'total_supply': 18949081,
      'is_active': 1, 
      'platform': None, 
      'cmc_rank': 1, 
      'is_fiat': 0, 
      'self_reported_circulating_supply': None, 
      'self_reported_market_cap': None,
      'last_updated': '2022-02-05T04:02:00.000Z',
      'quote': 
          {'USD': 
               {'price': 41433.714774999135, 
                'volume_24h': 30948439710.6353, 
                'volume_change_24h': 60.1234, 
                'percent_change_1h': 0.11098879, 
                'percent_change_24h': 10.94146791, 
                'percent_change_7d': 9.80534843, 
                'percent_change_30d': -3.52522474,
                'percent_change_60d': -18.89787769, 
                'percent_change_90d': -33.46180326, 
                'market_cap': 785130817402.3553, 
                'market_cap_dominance': 41.5485, 
                'fully_diluted_market_cap': 870108010274.98, 
                'last_updated': '2022-02-05T04:02:00.000Z'}
           }
      }
 }"""