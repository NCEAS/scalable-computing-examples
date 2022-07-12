import pandas as pd
import os

files = snakemake.input
print(files)
df_out = pd.DataFrame()
for i in range(len(files)):
    df = pd.read_csv(files[i], na_values = [-999.9])
    df['date'] = pd.to_datetime(df.numYear, format='%Y') + pd.to_timedelta(df.numJulian - 1, unit='d')
    daily_data = df.groupby('date', as_index = False).mean()

    df_out = pd.concat([df_out, daily_data], axis = 0)

df_out.to_csv(snakemake.output[0])   

