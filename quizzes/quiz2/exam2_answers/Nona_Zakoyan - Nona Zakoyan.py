#%%
from tokenize import group

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
#%%
df.info()
#%% md
# N1
# English: Use NumPy to calculate the 10th percentile of 'Infant mortality (per 1000 births)'.
# Հայերեն: Օգտագործեք NumPy-ը՝ հաշվելու 'Infant mortality (per 1000 births)'-ի 10-րդ պերցենտիլը:
#%%
np.percentile(df['Infant mortality (per 1000 births)'].dropna(),10)
#%% md
# N2 English: Create a new column 'Birth_Category' using np.where. If 'Birthrate' > 30, label it 'High', otherwise 'Normal'.
# Հայերեն: Ստեղծեք նոր 'Birth_Category' սյունակ՝ օգտագործելով np.where: Եթե 'Birthrate' > 30, նշեք 'High', հակառակ դեպքում՝ 'Normal':
#%%
df['Birth_Category'] = np.where(df['Birthrate']>30, 'High', 'Normal')
#%% md
# N3
# English: Filter for countries in 'SUB-SAHARAN AFRICA' with 'Phones (per 1000)' > 100.
# Հայերեն: Զտեք այն երկրները 'SUB-SAHARAN AFRICA' տարածաշրջանում, որոնք ունեն 100-ից ավել 'Phones (per 1000)':
#%%
filtered_df = df[(df['Region'].str.strip() == "SUB-SAHARAN AFRICA") & (df['Phones (per 1000)'] > 100)]
filtered_df
#%% md
# N4
# English: Group by 'Region' and calculate the mean 'Service' (economic sector) for each region.
# Հայերեն: Խմբավորեք ըստ 'Region'-ի և հաշվեք յուրաքանչյուր տարածաշրջանի 'Service' (տնտեսական ոլորտ) միջինը:
#%%
grouped_df = df.groupby('Region')['Service'].mean()
grouped_df
#%% md
# N5
# English: Create a scatter plot of 'Area (sq. mi.)' vs 'Population'
# 1 Use log scales for both axes (plt.xscale('log'), plt.yscale('log')).
# 2 Color points by 'GDP ($ per capita)'.
# 3 Use plt.annotate to label 'China'.
# Հայերեն:
# 1 Ստեղծեք 'Area (sq. mi.)'-ի և 'Population'-ի scatter plot:1. Օգտագործեք լոգարիթմական սանդղակներ երկու առանցքների համար:
# 2 Գունավորեք կետերը ըստ 'GDP ($ per capita)'-ի:
# 3 Օգտագործեք plt.annotate՝ «China»-ն պիտակավորելու համար:
#%%
plt.scatter(x=df['Area (sq. mi.)'], y=df['Population'], c=df['GDP ($ per capita)'], cmap='magma', alpha=0.5)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Area (sq. mi.)')
plt.ylabel('Population')
china_data = df[df['Country'].str.strip() == 'China']
plt.annotate(xy=(china_data['Area (sq. mi.)'].values[0], china_data['Population'].values[0]), arrowprops=dict(arrowstyle="->"), text='China')
plt.colorbar()
plt.show()
#%%
