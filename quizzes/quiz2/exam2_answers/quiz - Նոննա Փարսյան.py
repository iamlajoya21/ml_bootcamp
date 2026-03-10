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

# TASK 1 (NumPy): Percentiles
# English: Use NumPy to calculate the 10th percentile of 'Infant mortality (per 1000 births)'.
# Հայերեն: Օգտագործեք NumPy-ը՝ հաշվելու 'Infant mortality (per 1000 births)'-ի 10-րդ պերցենտիլը:
ans1=df['Infant mortality (per 1000 births)'].dropna()
print(np.percentile(ans1.values,10))

# TASK 2 (NumPy): Conditional Labeling
# English: Create a new column 'Birth_Category' using np.where. 
# If 'Birthrate' > 30, label it 'High', otherwise 'Normal'.
# Հայերեն: Ստեղծեք նոր 'Birth_Category' սյունակ՝ օգտագործելով np.where: 
# Եթե 'Birthrate' > 30, նշեք 'High', հակառակ դեպքում՝ 'Normal':


df['Birth_Category']=np.where(df['Birthrate']>30,'High','Normal')
print(df.head())


# TASK 3 (Pandas): Multi-Condition Filtering
# English: Filter for countries in 'SUB-SAHARAN AFRICA' with 'Phones (per 1000)' > 100.
# Հայերեն: Զտեք այն երկրները 'SUB-SAHARAN AFRICA' տարածաշրջանում, որոնք ունեն 100-ից ավել 'Phones (per 1000)':

ans3=df[(df['Region']=='SUB-SAHARAN AFRICA')&(df['Phones (per 1000)']>100)]
print(ans3['Country'].values.tolist())



#TASK 4 (Pandas): Grouped Aggregation
# English: Group by 'Region' and calculate the mean 'Service' (economic sector) for each region.
# Հայերեն: Խմբավորեք ըստ 'Region'-ի և հաշվեք յուրաքանչյուր տարածաշրջանի 'Service' (տնտեսական ոլորտ) միջինը:

print(df.groupby("Region")['Service'].mean())


# TASK 5 (Matplotlib): Visualization & Annotation
# English: Create a scatter plot of 'Area (sq. mi.)' vs 'Population'.
# 1. Use log scales for both axes (plt.xscale('log'), plt.yscale('log')).
# 2. Color points by 'GDP ($ per capita)'.
# 3. Use plt.annotate to label 'China'.
# Հայերեն: Ստեղծեք 'Area (sq. mi.)'-ի և 'Population'-ի scatter plot:
# 1. Օգտագործեք լոգարիթմական սանդղակներ երկու առանցքների համար:
# 2. Գունավորեք կետերը ըստ 'GDP ($ per capita)'-ի:
# 3. Օգտագործեք plt.annotate՝ «China»-ն պիտակավորելու համար:

fig=plt.figure(figsize=(12,7))

x=df['Area (sq. mi.)']
y=df['Population']
plt.scatter(x,y,c=df['GDP ($ per capita)'],cmap='viridis',marker='^',alpha=0.8)
plt.xscale('log')
plt.yscale('log')
df['Country'] = df['Country'].str.strip()
China=df[df['Country']=='China']
x_val=China['Area (sq. mi.)'].iloc[0]
y_val=China['Population'].iloc[0]

plt.annotate(
    text="China",
    xy=(x_val,y_val),
    xytext=(20,20),
    textcoords="offset points",
    arrowprops=dict(arrowstyle='->',color='red',lw=2),
    fontsize=15,
    fontweight='bold'
)

plt.title("Global Scale:Area vs. Population (Colored by GDP)")
plt.xlabel('Area (sq. mi.)-Log Scale')
plt.ylabel('Population-Log Scale')

plt.colorbar(label='GDP ($ per capita)');
