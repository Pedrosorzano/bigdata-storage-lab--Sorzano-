import pandas as pd
from datetime import datetime, timezone
from typing import List

def tag_lineage(df: pd.DataFrame, source_name: str) -> pd.DataFrame:
    """
    Añade columnas de linaje:
    - source_file: nombre del archivo de origen
    - ingested_at: timestamp UTC en formato ISO 8601
    """
    df = df.copy()
    df['source_file'] = source_name
    df['ingested_at'] = datetime.now(timezone.utc).isoformat()
    return df


def concat_bronze(frames: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Concatena una lista de DataFrames al esquema canónico extendido:
    - Campos esperados: date, partner, amount, source_file, ingested_at
    """
    expected_cols = ['date', 'partner', 'amount', 'source_file', 'ingested_at']
    unified = pd.concat(frames, ignore_index=True)
    unified = unified[expected_cols]  # asegura el orden y esquema
    return unified
