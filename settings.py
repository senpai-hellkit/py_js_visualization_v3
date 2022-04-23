import os
import pandas as pd


def get_data_to_json():
    path_to_data: str = os.path.join(os.getcwd(), 'data', 'USDCB_210131_220131.csv')
    df: pd.DataFrame = pd.read_csv(path_to_data, sep='\t')
    df = df.rename(columns=dict(map(lambda x: (x, x.replace('<', '').replace('>', '').lower()), df.columns)))
    df['date'] = pd.to_datetime(df['date'].astype(str).apply(lambda x: f'{x[:4]}-{x[4:6]}-{x[6:]}'))
    df.sort_values(by='date', inplace=True)
    df['close'] = df['close'].apply(lambda x: x.replace(',', '.') if isinstance(x, str) else x).astype(float)
    df['date'] = df['date'].astype(str)
    data: pd.DataFrame = df.tail(10).loc[:, ['date', 'close']]

    return data
