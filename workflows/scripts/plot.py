import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(snakemake.input[0])
df['date'] = pd.to_datetime(df.date)

var = 'numTempT'
var_labs = {'numTempT': 'Temperature (deg C)'}

fig, ax = plt.subplots(figsize=(7, 7))
plt.style.use("seaborn-talk")
plt.plot(df['date'], df[var]);
plt.xticks(rotation = 45);
ax.set_ylabel(var_labs.get('numTempT'));

plt.savefig(snakemake.output[0])