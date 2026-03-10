import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- DATA SETUP ---
url = "https://raw.githubusercontent.com/bnokoro/Data-Science/master/countries%20of%20the%20world.csv"
df = pd.read_csv(url)

# Cleaning: Fix decimal commas and strip strings
cols_to_fix = ['Infant mortality (per 1000 births)', 'Birthrate', 'Phones (per 1000)', 'Service', 'Area (sq. mi.)', 'Population']
for col in cols_to_fix:
    df[col] = df[col].astype(str).str.replace(',', '.').astype(float)
df['Region'] = df['Region'].str.strip()

#Problem 1
ans_1 = np.nanpercentile(df['Infant mortality (per 1000 births)'], 10)
ans_1

#Problem 2
ans_2 = df.copy()
high_birthrate = df['Birthrate'] > 30

ans_2['Birth_Category'] = np.where(high_birthrate, 'High', 'Normal')
ans_2

#Problem 3                                   
ans_3 = df[(df['Region'] == 'SUB-SAHARAN AFRICA') & (df['Phones (per 1000)'] > 100)]
ans_3

#Problem 4
ans_4 = df.groupby('Region').agg(economic_secrtor=('Service', 'mean'))
ans_4

#Problem 5
fig = plt.figure(figsize=(12, 5))

plt.scatter(df['Area (sq. mi.)'], df['Population'], c=df['GDP ($ per capita)'])
plt.xscale('log')
plt.yscale('log')

china = df[df['Country'] == 'China '].iloc[0]


plt.annotate(china['Country'],
             xy=(china['Area (sq. mi.)'], china['Population']),
             xytext=(20, 20), 
             textcoords='offset points', 
             arrowprops=dict(arrowstyle='->'))


plt.xlabel('Area (sq. mi.) log Scale')
plt.ylabel('Population log Scale')
plt.title('Global Scale Area vs Popilation (Colored by GDP)')
plt.colorbar(label='GDP ($ per capita)')
plt.show();