# crypto/btc_price 

# imports
import pandas as pd 
import plotly.express as px 

from crypto import btc_price


def btc_price():
    btc = pd.read_csv('https://raw.githubusercontent.com/coinmetrics-io/data/master/csv/btc.csv')

    # convert time
    btc['time'] = pd.to_datetime(btc['time'], infer_datetime_format=True)
    btc['year'] = btc['time'].dt.year 

    # plot btc chart
    gapminder = px.data.gapminder()
    fig = px.line(btc, x="time", y="PriceUSD")
    fig.update_layout(
        xaxis_title="year",
        yaxis_title="Price in USD",
        font=dict( family="Open Sans", size=16)
        ),
    fig.update_layout(
    title={
        'text': "Bitcoin Price",
        'y':0.97,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
    
    return fig
