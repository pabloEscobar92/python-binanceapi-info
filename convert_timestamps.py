"""Convertir timestamps en milisegundos a fechas legibles dentro de un JSON.

Este script:
- hace un backup del archivo original (añade sufijo .bak)
- detecta claves que contienen 'time' o terminan en '_time' y cuyo valor parece ser un timestamp en ms
- convierte esos valores a ISO 8601 UTC (YYYY-MM-DDTHH:MM:SSZ)
- sobrescribe el archivo original con el JSON modificado

Uso:
    python convert_timestamps.py [ruta_al_json]

Por defecto usa: Binance_BTCUSDT_30m_1512086400000-1546300800000.json
"""
import sys
import json
import shutil
from datetime import datetime
from pathlib import Path


def looks_like_ms_timestamp(value):
    # detecta enteros/float grandes que representen ms desde epoch
    try:
        if isinstance(value, (int, float)):
            # en ms típicamente >= 10^11 (aprox 1973-03-03 en ms)
            return value > 1e11
    except Exception:
        return False
    return False


def ms_to_iso(ms):
    # convierte ms a ISO 8601 UTC sin milisegundos
    return datetime.utcfromtimestamp(int(ms) / 1000).strftime("%Y-%m-%dT%H:%M:%SZ")


def convert_file(path: Path):
    if not path.exists():
        print(f"Archivo no encontrado: {path}")
        return 1

    backup = path.with_suffix(path.suffix + ".bak")
    print(f"Creando backup: {backup}")
    shutil.copy2(path, backup)

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    modified = 0

    # Si es una lista de objetos
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                for k, v in list(item.items()):
                    # detecta claves relacionadas con tiempo
                    if ("time" in k.lower() or k.lower().endswith("_time")) and looks_like_ms_timestamp(v):
                        item[k] = ms_to_iso(v)
                        modified += 1
    elif isinstance(data, dict):
        # recorrer recursivamente si es un dict
        def recurse(obj):
            nonlocal modified
            if isinstance(obj, dict):
                for k, v in list(obj.items()):
                    if ("time" in k.lower() or k.lower().endswith("_time")) and looks_like_ms_timestamp(v):
                        obj[k] = ms_to_iso(v)
                        modified += 1
                    else:
                        recurse(v)
            elif isinstance(obj, list):
                for e in obj:
                    recurse(e)

        recurse(data)

    # escribir de vuelta (sobrescribir)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Conversión completada. Campos convertidos: {modified}")
    print(f"Archivo sobreescrito: {path}\nBackup en: {backup}")
    return 0


def main():
    default = "Binance_BTCUSDT_30m_1512086400000-1546300800000.json"
    p = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(default)
    return convert_file(p)


if __name__ == "__main__":
    sys.exit(main())
