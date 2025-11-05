import json
import matplotlib.pyplot as plt
from Kline import Kline
import pandas as pd

#Paso 2: cargar el archivo JSON y crear objetos Kline
# Cargar el archivo JSON
with open("Binance_BTCUSDT_30m_1512086400000-1514764800000.json", "r") as f:
    data = json.load(f)

# Crear una lista de objetos Kline
klines = [Kline(**item) for item in data]

#Paso 3: convertir la lista en un DataFrame
df = Kline.to_dataframe(klines)

#Paso 4: convertir las fechas a formato legible
df["open_time"] = pd.to_datetim./e(df["open_time"], unit="ms")

# Crear gráfico
plt.figure(figsize=(12,6))
plt.plot(df["open_time"], df["high_price"], label="High Price", linewidth=1.5)
plt.plot(df["open_time"], df["low_price"], label="Low Price", linewidth=1.5)

# Personalizar
plt.title("BTC/USDT High & Low Prices (30m candles)")
plt.xlabel("Fecha")
plt.ylabel("Precio (BTC)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Mostrar gráfico
plt.show()