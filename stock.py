import json
import urllib.request
import random
QUERY = "https://api.example.com/stock-quotes?random={}"

def getDataPoint(quote):
    """ Produce all of the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])

    # Calculate the average price using bid and ask prices
    price = (bid_price + ask_price) / 2

    return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
    """ Calculate the ratio of price_a to price_b """
    if (price_b == 0):
        # To avoid division by zero error
        return
    return price_a / price_b

if __name__ == "__main__":
    # Query the price once every N seconds.
    N=10
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        # Update to get the ratio
        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

        # Calculate and print the ratio for the specified stocks
        print("Ratio %s" % getRatio(prices["ABC"], prices["DEF"]))





