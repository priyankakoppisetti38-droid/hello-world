import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('stock_data.csv')
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'], high=df['High'],
                low=df['Low'], close=df['Close'])])
fig.show()
