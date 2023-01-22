
import pandas as pd
import matplotlib as plt
import plotly as py
from pycoingecko import CoinGeckoAPI
print('\n')



# criando uma instância do pycoingecko
cg = CoinGeckoAPI()

# solicitando os valores da moeda em reais dos últimos 30 dias
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency ='brl',days = 30)

# printando a lista de valores pela coluna 'preços'
data = pd.DataFrame(bitcoin_data['prices'], columns= ['timestamp','price'])

data['Date'] = pd.to_datetime(data['timestamp'], unit = 'ms')

candlestick_data = data.groupby(data.Date.dt.date).agg({'price': ['min', 'max', 'first', 'last']})

fig = go.Figure(data = [go.Candlestick(x = candlestick_data.index, open = candlestick_data['price']['first'],
                                       high = candlestick_data['price']['max'],
                                       low = candlestick_data['price']['min'],
                                       close = candlestick_data['price']['last'])])

fig.update_layout(xaxis_rangerslider_visible = False, xaxis_title = 'Date', yaxis_title = 'price (BRL)',
                  title = 'Bitcoin Price')

py.plot(fig, filename = 'bitcoin_price.html')

