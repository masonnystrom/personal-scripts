# script prints a chart of the btc price by year
# imports
import pandas as pd 
import plotly.express as px 


def btc_price():
    btc = pd.read_csv('https://raw.githubusercontent.com/coinmetrics-io/data/master/csv/btc.csv')

    # convert time
    btc['time'] = pd.to_datetime(btc['time'], infer_datetime_format=True)
    btc['year'] = btc['time'].dt.year 

    # plot btc chart
    gapminder = px.data.gapminder().query('year'=='2020')
    fig = px.line(btc, x="time", y="PriceUSD",)
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

if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script
    print(fig