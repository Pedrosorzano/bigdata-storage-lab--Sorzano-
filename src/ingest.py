# ingest.py

def ingest_csv(path):
    """
    Ingesta un archivo CSV desde una ruta local.
    """
    import pandas as pd
    return pd.read_csv(path)
