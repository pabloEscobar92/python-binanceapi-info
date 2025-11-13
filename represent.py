import json
import matplotlib.pyplot as plt
from Kline import Kline
import pandas as pd

#Paso 2: cargar el archivo JSON y crear objetos Kline
# Cargar el archivo JSON
with open("Binance_BTCUSDT_30m_1512086400000-1546300800000.json", "r") as f:
    data = json.load(f)

# Crear una lista de objetos Kline
klines = [Kline(**item) for item in data]

#Paso 3: convertir la lista en un DataFrame
df = Kline.to_dataframe(klines)

#Paso 4: convertir las fechas a formato legible (soporta timestamps en ms o cadenas ISO)

def _parse_time_series(series):
    """Detecta si la serie es numérica (ms) o cadenas y la convierte a datetime UTC.

    - Si la serie es numérica se interpreta como milisegundos desde epoch.
    - Si la serie contiene cadenas, se intenta parsear como ISO u otros formatos.
    - Si falla la conversión de cadenas, se intenta convertir a numérico y usar ms.
    """
    # Si pandas ya reconoce un tipo datetime, devolver tal cual
    if pd.api.types.is_datetime64_any_dtype(series):
        return pd.to_datetime(series, utc=True)

    # Serie numérica -> interpretar como ms
    if pd.api.types.is_numeric_dtype(series):
        return pd.to_datetime(series, unit="ms", utc=True)

    # Intentar parsear cadenas
    parsed = pd.to_datetime(series, utc=True, errors="coerce", infer_datetime_format=True)
    if parsed.notna().any():
        return parsed

    # Si no se pudo parsear, intentar convertir a número (por si vienen como string de ms)
    numeric = pd.to_numeric(series, errors="coerce")
    if numeric.notna().any():
        return pd.to_datetime(numeric, unit="ms", utc=True)

    # Si todo falla, devolver la serie original como datetime (coerce)
    return pd.to_datetime(series, utc=True, errors="coerce")


df["open_time"] = _parse_time_series(df["open_time"]) 
# also parse close_time if present
if "close_time" in df.columns:
    df["close_time"] = _parse_time_series(df["close_time"])

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