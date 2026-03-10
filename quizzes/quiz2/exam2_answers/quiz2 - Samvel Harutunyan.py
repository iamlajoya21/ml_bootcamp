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
df.columns = df.columns.str.strip()

#-----------------------------------

ans_1 = np.percentile(df['Infant mortality (per 1000 births)'].dropna(),10)
print(ans_1)

#-----------------------------------------------------

df['Birth_Category']= np.where(df['Birthrate'] > 30, 'High','Normal')

#------------------------------------------------------

ans_3 = df[(df['Phones (per 1000)'] > 100) & (df['Region'] == 'SUB-SAHARAN AFRICA')]
print(ans_3)

#------------------------------------------------------

ans_4 = df.groupby('Region')['Service'].mean()
print(ans_4)

#-----------------------------------------------------



plt.figure(figsize=(10,6))

scat = plt.scatter(
    df['Area (sq. mi.)'],
    df['Population'],
    c = df['GDP ($ per capita)'],
    cmap='viridis'
    )
plt.colorbar(scat,label = 'GDP per capita')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Area (sq. mi.)')
plt.ylabel('Population')
plt.title('Area vs Population')

ch = df[df['Country']=='China ']
plt.annotate(
    'China',
    xy=(ch['Area (sq. mi.)'].values[0] , ch['Population'].values[0]),
    xytext=(50,50),
    textcoords='offset points',
    arrowprops=dict(facecolor = 'black')
    )
plt.show()
