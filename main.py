from binance.client import Client
import Exchange
import json
from datetime import datetime
import locale
from Kline import Kline
from Storage import Storage

symbol = "BTCUSDT"
start = "1 Jan, 2024"
end = "1 Jan, 2025"
interval = Client.KLINE_INTERVAL_30MINUTE

Exchange.get_exchange_symbols()

klines = Exchange.get_historical_klines(symbol, interval, start, end)

'''
# Convertir cada array en un Kline para escribir cada kline como un dict
temp_klines: list[Kline] = [Kline(*array) for array in klines]

# Guardar los datos en un archivo JSON usando la clase Storage
Storage.save_to_json(
    data=[k.to_dict() for k in temp_klines],
    symbol=symbol,
    interval=interval,
    start=start,
    end=end
)
'''


