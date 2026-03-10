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
#Task1 
np.percentile(df['Infant mortality (per 1000 births)'].dropna(), 10)


#Task 2
df['Birth_Category']  = np.where(df['Birthrate']>30, 'High', 'Normal')
df['Birth_Category']

#Task3
df[(df['Region']== 'SUB-SAHARAN AFRICA') & (df['Phones (per 1000)']>100)]

#Task4
df.groupby('Region')['Service'].agg('mean')

#Task5
plt.scatter(df['Area (sq. mi.)'], df['Population'], c=df['GDP ($ per capita)'], cmap='viridis')
plt.xscale('log')
plt.yscale('log')
plt.annotate('China', xy=(df['Area (sq. mi.)'][42], df['Population'][42]))
plt.xlabel('Area (sq. mi.)')
plt.ylabel('Population')
plt.colorbar()
