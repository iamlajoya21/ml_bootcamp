import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests
from io import StringIO

# --- DATA SETUP ---
url = "https://raw.githubusercontent.com/bnokoro/Data-Science/master/countries%20of%20the%20world.csv"

response = requests.get(url)
data = StringIO(response.text)
df = pd.read_csv(data)

# Cleaning: Fix decimal commas and strip strings
cols_to_fix = ['Infant mortality (per 1000 births)', 'Birthrate', 'Phones (per 1000)', 'Service', 'Area (sq. mi.)', 'Population']
for col in cols_to_fix:
    df[col] = df[col].astype(str).str.replace(',', '.').astype(float)
df['Region'] = df['Region'].str.strip()



#Task 1
cleaned_df = df.dropna(subset=['Infant mortality (per 1000 births)'])
percentile_10 = np.percentile(cleaned_df['Infant mortality (per 1000 births)'],10)
print(f"10th percentile of Infant mortality (per 1000 births): {percentile_10}")

#Task 2
birth_category = np.where(df['Birthrate'] > 30, 'High', "Normal")
print(birth_category)

#Task 3
df_africa = df[df['Region'] == 'SUB-SAHARAN AFRICA']
df_africa_phones = df_africa[df_africa['Phones (per 1000)'] > 100]
print(df_africa_phones)

#Task 4
grouped_region = df.groupby('Region')['Service'].mean()
print(grouped_region)

#Task 5
scatter_plotted = plt.scatter(df['Area (sq. mi.)'], df['Population'], c=df['GDP ($ per capita)'], cmap='viridis')
bar = plt.colorbar(scatter_plotted, label='GDP ($ per capita)')
plt.xlabel('Area (sq. mi.) - Log Scale')
plt.ylabel('Population - Log Scale')
plt.title('Area vs Population')
plt.xscale('log')
plt.yscale('log')
china = df[df['Country'] == 'China']
plt.annotate('China', xy= (1, 1), arrowprops=dict(arrowstyle='->'))
plt.show()