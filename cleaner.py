import pandas as pd

def clean_data(df):

    df.drop_duplicates(inplace=True)

    df.fillna("Unknown", inplace=True)

    return df