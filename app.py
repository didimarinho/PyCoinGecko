# import numpy as np
# import matplotlib.pyplot as plt

import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc
print('\n')

# instância de classe CoinGeckoAPI
cg = CoinGeckoAPI()


'''
!pegando os valores de bicoins dos últimos 30 dias com instância cg da classe CoinGeckoAPI
!É um dicionário contendo uma matriz bi-dimmensional com colunas 0 e 1
'''
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='brl', days=30)


# separando somente pela coluna 'prices'
bitcoin_price_data = bitcoin_data['prices']


# transformando em um dataframe e organizando com as colunas 'TimeStamp' e 'price'
data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])


data['date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))



candlestick_data = data.groupby(data.date, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})


    # usando ploty através da instância go
fig = go.Figure(data=[go.Candlestick(x=candlestick_data['date'],
                open=candlestick_data['Price']['first'], 
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'], 
                close=candlestick_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()



























