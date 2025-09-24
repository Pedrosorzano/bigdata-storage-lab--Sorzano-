import pandas as pd
from typing import List

def basic_checks(df: pd.DataFrame) -> List[str]:
    """
    Realiza validaciones básicas sobre el DataFrame:
    - Verifica presencia de columnas canónicas.
    - Chequea que amount sea numérico y ≥ 0.
    - Chequea que date esté en formato datetime.
    Retorna una lista de errores encontrados.
    """
    errors = []

    required_columns = ['date', 'partner', 'amount']
    for col in required_columns:
        if col not in df.columns:
            errors.append(f"Falta la columna requerida: {col}")

    if 'amount' in df.columns:
        if not pd.api.types.is_numeric_dtype(df['amount']):
            errors.append("La columna 'amount' no es numérica.")
        elif (df['amount'] < 0).any():
            errors.append("Existen valores negativos en 'amount'.")

    if 'date' in df.columns:
        if not pd.api.types.is_datetime64_any_dtype(df['date']):
            errors.append("La columna 'date' no es datetime.")

    return errors
