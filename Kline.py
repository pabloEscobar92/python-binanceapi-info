import pandas as pd

class Kline:
    """Clase para representar una vela (candlestick) típica del formato Kline u OHLCV extendido"""

    def __init__(self, open_time, open_price, high_price, low_price, close_price,
                 volume, close_time, quote_asset_volume, number_of_trades,
                 taker_buy_base_asset_volume, taker_buy_quote_asset_volume, ignore=0.0):
        self.open_time = open_time
        self.open_price = float(open_price)
        self.high_price = float(high_price)
        self.low_price = float(low_price)
        self.close_price = float(close_price)
        self.volume = float(volume)
        self.close_time = close_time
        self.quote_asset_volume = float(quote_asset_volume)
        self.number_of_trades = int(number_of_trades)
        self.taker_buy_base_asset_volume = float(taker_buy_base_asset_volume)
        self.taker_buy_quote_asset_volume = float(taker_buy_quote_asset_volume)
        self.ignore = float(ignore)

    def to_dict(self) -> dict:
        return {
            "open_time": self.open_time,
            "open_price": self.open_price,
            "high_price": self.high_price,
            "low_price": self.low_price,
            "close_price": self.close_price,
            "volume": self.volume,
            "close_time": self.close_time,
            "quote_asset_volume": self.quote_asset_volume,
            "number_of_trades": self.number_of_trades,
            "taker_buy_base_asset_volume": self.taker_buy_base_asset_volume,
            "taker_buy_quote_asset_volume": self.taker_buy_quote_asset_volume,
            "ignore": self.ignore
        }

    @staticmethod
    def to_dataframe(klines_list):
        """Convierte una lista de objetos Kline en un DataFrame de pandas."""
        return pd.DataFrame([k.to_dict() for k in klines_list])

    def __repr__(self):
        return (
            f"Kline(open_time={self.open_time}, open={self.open_price}, "
            f"high={self.high_price}, low={self.low_price}, close={self.close_price}, "
            f"volume={self.volume}, trades={self.number_of_trades})"
        )