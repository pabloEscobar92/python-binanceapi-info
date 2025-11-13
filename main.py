
from binance.client import Client
import Exchange
import json

from Kline import Kline


symbol = "BTCUSDT"
start = "1 Dec, 2017"
end = "1 Jan, 2019"
interval = Client.KLINE_INTERVAL_30MINUTE

Exchange.get_exchange_symbols()

klines = Exchange.get_historical_klines(symbol, interval, start, end)

#init Klines
temp_klines: list[Kline] = []

# Convierto cada array en un Kline para escribir cada kline como un dict
for array in klines:
    temp_klines.append(Kline(*array))

# open a file with filename including symbol, interval and start and end converted to milliseconds
with open(
    "Binance_{}_{}_{}-{}.json".format(
        symbol, interval, Exchange.date_to_milliseconds(start), Exchange.date_to_milliseconds(end)
    ),
    "w",  # set file write mode
) as f:
    f.write(json.dumps([k.to_dict() for k in temp_klines], indent=2))
    


