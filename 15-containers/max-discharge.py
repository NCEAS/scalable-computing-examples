#!env python
import pandas as pd
import matplotlib.pyplot as plt

# Read and subset our input data
discharge = pd.read_csv("/var/data/input/discharge-data.csv")
rivers = ['Yukon', 'Mackenzie', 'Lena']
discharge_subset = discharge[discharge.river.isin(rivers)]
discharge_max = discharge_subset.groupby('river', as_index=False).max(numeric_only=True)

# Create and save a barplot to the output directory
plt.bar(discharge_max['river'], discharge_max['discharge'], color='maroon', width=0.4)
plt.xlabel("River")
plt.ylabel("Max discharge")
plt.savefig("/var/data/output/max-discharge.png")
