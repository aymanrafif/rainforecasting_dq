import pandas as pd

def remove_outliers_iqr(df, columns_to_check=None, factor=1.5):
    if columns_to_check is None:
        columns_to_check = df.columns

    Q1 = df[columns_to_check].quantile(0.25)
    Q3 = df[columns_to_check].quantile(0.75)
    IQR = Q3 - Q1

    mask = ~((df[columns_to_check] < (Q1 - factor * IQR)) | (df[columns_to_check] > (Q3 + factor * IQR))).any(axis=1)

    df_filtered = df[mask]

    return df_filtered