# transform.py

def normalize_df(df):
    """
    Normaliza un DataFrame (renombra columnas, tipado, etc.).
    """
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df
