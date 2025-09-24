# validate.py

def validate_df(df):
    """
    Realiza validaciones básicas sobre un DataFrame.
    """
    report = {
        "shape": df.shape,
        "missing_values": df.isnull().sum().to_dict(),
        "duplicated_rows": df.duplicated().sum()
    }
    return report
