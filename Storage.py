import pandas as pd
import json
from datetime import datetime
import os

class Storage:
    @staticmethod
    def save_to_json(data, symbol, interval, start, end):
        """
        Escribe directamente nuevos datos en un archivo JSON distinto por llamada
        (cada iteración del bucle generará un fichero nuevo). Si el archivo no
        existe, lo crea.

        :param data: Lista de datos a escribir.
        :param symbol: Símbolo del par de trading (e.g., BTCUSDT).
        :param interval: Intervalo de tiempo (e.g., 30m).
        :param start: Fecha de inicio en formato timestamp (milisegundos desde epoch).
        :param end: Fecha de fin en formato timestamp (milisegundos desde epoch).
        """
        # Convertir las fechas de inicio y fin de timestamp a formato legible
        start_readable = datetime.utcfromtimestamp(start / 1000).strftime("%Y-%m-%d")
        end_readable = datetime.utcfromtimestamp(end / 1000).strftime("%Y-%m-%d")

        # Crear el nombre del archivo
        filename = "Binance_{}_{}_{}-{}.json".format(symbol, interval, start_readable, end_readable)

        # Crear el directorio 'output' si no existe
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)

        # Ruta completa del archivo
        filepath = os.path.join(output_dir, filename)

        # Guardar los datos en el archivo JSON
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"Datos guardados en {filepath}")

    @staticmethod
    def create_json_file(symbol, interval, start, end):
        """
        Crea un archivo JSON vacío en el directorio 'output'.

        :param symbol: Símbolo del par de trading (e.g., BTCUSDT).
        :param interval: Intervalo de tiempo (e.g., 30m).
        :param start: Fecha de inicio en formato timestamp (milisegundos desde epoch).
        :param end: Fecha de fin en formato timestamp (milisegundos desde epoch).
        """
        # Convertir las fechas de inicio y fin de timestamp a formato legible
        start_readable = datetime.utcfromtimestamp(start / 1000).strftime("%Y-%m-%d")
        end_readable = datetime.utcfromtimestamp(end / 1000).strftime("%Y-%m-%d")

        # Crear el nombre del archivo
        filename = "Binance_{}_{}_{}-{}.json".format(symbol, interval, start_readable, end_readable)

        # Crear el directorio 'output' si no existe
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)

        # Ruta completa del archivo
        filepath = os.path.join(output_dir, filename)

        # Crear un archivo JSON vacío si no existe
        if not os.path.exists(filepath):
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=2)

        return filepath
