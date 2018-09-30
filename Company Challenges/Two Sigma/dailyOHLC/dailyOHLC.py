import pandas as pd
from datetime import datetime
from operator import itemgetter
def dailyOHLC(timestamp, instrument, side, price, size):
    data_df = pd.DataFrame({"timestamp": timestamp,
                            "instrument": instrument,
                            "side": side,
                            "price": price,
                            "size": size})
    # change timestamp to `datetime` object
    data_df.timestamp = data_df.timestamp.map(datetime.utcfromtimestamp)
    # create empty list for ohlc data
    ohlc_data = []
    # generate ohlc data
    for symbol, cluster in data_df[['timestamp', 'instrument', 'price']].groupby('instrument'):
        prices = cluster.set_index('timestamp')['price'].resample('D',
                                                                  how=[lambda x: symbol,
                                                                       'first',
                                                                       'max',
                                                                       'min',
                                                                       'last'])
        prices = prices.dropna()
        # append each row to ohlc data list in specified format
        for index, row in prices.iterrows():
            line = [index.strftime('%Y-%m-%d')]
            for column in row:
                try: line.append('%.2f' % column)
                except: line.append(column)
            ohlc_data.append(line)
    # return ohlc data list sorted by date and instrument
    return sorted(ohlc_data, key=itemgetter(0,1))