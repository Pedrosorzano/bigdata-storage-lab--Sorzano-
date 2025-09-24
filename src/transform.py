import pandas as pd

def normalize_columns(df: pd.DataFrame, mapping: dict) -> pd.DataFrame:
    """
    Renombra columnas según mapping y normaliza los valores:
    - Convierte fechas a formato datetime (ISO).
    - Limpia y formatea el campo amount (quita €, cambia , por .).
    - Elimina espacios en el campo partner.
    """
    df = df.rename(columns=mapping)

    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

    if 'amount' in df.columns:
        df['amount'] = (
            df['amount']
            .astype(str)
            .str.replace("€", "", regex=False)
            .str.replace(",", ".", regex=False)
            .str.strip()
        )
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

    if 'partner' in df.columns:
        df['partner'] = df['partner'].astype(str).str.strip()

    return df


def to_silver(bronze: pd.DataFrame) -> pd.DataFrame:
    """
    Agrega los datos a nivel de partner y mes calendario.
    Retorna un DataFrame con columnas: month, partner, amount.
    """
    bronze = bronze.copy()
    bronze['month'] = bronze['date'].dt.to_period('M').dt.to_timestamp()
    
    silver = (
        bronze
        .groupby(['month', 'partner'], as_index=False)
        .agg({'amount': 'sum'})
    )
    
    return silver
