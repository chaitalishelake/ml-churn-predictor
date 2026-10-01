import pandas as pd
def clean_data(filepath):
df = pd.read_csv(filepath)
df = df.dropna()
return df
