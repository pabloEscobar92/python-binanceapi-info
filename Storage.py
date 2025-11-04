import pandas as pd

class Storage:
    """ Almacena los datos OHLC del par y el estado de las opreaciones"""

    def __init__(self):
        self.status: str = 'NONE' # ['LONG', 'SHORT', 'NONE']
        self.ohcl_data: pd.DataFrame = pd.DataFrame(columns=['ts',
                                                             'open',
                                                             'close',
                                                             'low',
                                                             'high',
                                                             'volume'])
        self.max_data: int = 300
    
    def push(self, ohcl_list: List[dict], frequency: str):
        """ Almacena uno o varios datos obtenidos del exchange"""
        pass

    def pop(self):
        """Quita datos antiguos cuando se alcanza el limite max_data"""
        pass

    def get(self, idx: int= -1) -> pd.DataFrame:
        return self.ohcl_data.loc[self.ohcl_data.index[idx]]
    
    def _check_ts(self, df: pd.DataFrame, interval: str) -> None:
        """Comprueba la frecuencia de los timstamp de un DataFrame, que
        no esta repetido y que no falta ningún valor, Errores como excepciones"""
        pass