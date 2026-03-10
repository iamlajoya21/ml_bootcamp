import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# --- DATA SETUP ---
url = "https://raw.githubusercontent.com/bnokoro/Data-Science/master/countries%20of%20the%20world.csv"
df = pd.read_csv(url)

# Cleaning: Fix decimal commas and strip strings
cols_to_fix = [
    'Infant mortality (per 1000 births)',
    'Birthrate',
    'Phones (per 1000)',
    'Service',
    'Area (sq. mi.)',
    'Population',
    'GDP ($ per capita)'
]
for col in cols_to_fix:
    df[col] = df[col].astype(str).str.replace(',', '.').astype(float)
df['Region'] = df['Region'].str.strip()

# ==========================================
# TASK 1 (NumPy): Percentiles
# English: Use NumPy to calculate the 10th percentile of 'Infant mortality (per 1000 births)'.
# Հայերեն: Օգտագործեք NumPy-ը՝ հաշվելու 'Infant mortality (per 1000 births)'-ի 10-րդ պերցենտիլը:
# ------------------------------------------

infant_mortality_perc_10 = np.percentile(df["Infant mortality (per 1000 births)"].dropna(), 10)

print("Infant mortality percentile 10\n", infant_mortality_perc_10, "\n")

# ==========================================
# TASK 2 (NumPy): Conditional Labeling
# English: Create a new column 'Birth_Category' using np.where. 
# If 'Birthrate' > 30, label it 'High', otherwise 'Normal'.
# Հայերեն: Ստեղծեք նոր 'Birth_Category' սյունակ՝ օգտագործելով np.where: 
# Եթե 'Birthrate' > 30, նշեք 'High', հակառակ դեպքում՝ 'Normal':
# ------------------------------------------

df["Birth_Category"] = np.where(df["Birthrate"] > 30, "High", "Normal")

print("Birth category\n", df["Birth_Category"].head(), "\n")

# ==========================================
# TASK 3 (Pandas): Multi-Condition Filtering
# English: Filter for countries in 'SUB-SAHARAN AFRICA' with 'Phones (per 1000)' > 100.
# Հայերեն: Զտեք այն երկրները 'SUB-SAHARAN AFRICA' տարածաշրջանում, որոնք ունեն 100-ից ավել 
# 'Phones (per 1000)':
# ------------------------------------------

mask = (df['Region'] == 'SUB-SAHARAN AFRICA') & (df['Phones (per 1000)'] > 100)
df_filtered = df[mask]

print("High phone using countries in Africa\n", df_filtered["Country"], "\n")

# ==========================================
# TASK 4 (Pandas): Grouped Aggregation
# English: Group by 'Region' and calculate the mean 'Service' (economic sector) for each region.
# Հայերեն: Խմբավորեք ըստ 'Region'-ի և հաշվեք յուրաքանչյուր տարածաշրջանի 'Service' 
# (տնտեսական ոլորտ) միջինը:
# ------------------------------------------

service_mean = df.groupby("Region")["Service"].mean()

print("Service mean by region\n", service_mean, "\n")

# ==========================================
# TASK 5 (Matplotlib): Visualization & Annotation
# English: Create a scatter plot of 'Area (sq. mi.)' vs 'Population'.
# 1. Use log scales for both axes (plt.xscale('log'), plt.yscale('log')).
# 2. Color points by 'GDP ($ per capita)'.
# 3. Use plt.annotate to label 'China'.
# Հայերեն: Ստեղծեք 'Area (sq. mi.)'-ի և 'Population'-ի scatter plot:
# 1. Օգտագործեք լոգարիթմական սանդղակներ երկու առանցքների համար:
# 2. Գունավորեք կետերը ըստ 'GDP ($ per capita)'-ի:
# 3. Օգտագործեք plt.annotate՝ «China»-ն պիտակավորելու համար:
# ------------------------------------------

plt.figure(figsize=(10, 6))
plt.scatter(df["Area (sq. mi.)"], df["Population"], c=df["GDP ($ per capita)"], cmap="viridis") 
plt.colorbar(label='GDP ($ per capita)')
plt.xlabel('Area (sq. mi.)')
plt.ylabel('Population')
plt.title('Relationship between area, population and GDP')
plt.grid(True, linestyle='--', alpha=0.5)
plt.xscale('log')
plt.yscale('log')

mask = df['Country'].str.contains("China", case=False, na=False)
row = df[mask]
x_val = row['Area (sq. mi.)'].iloc[0]
y_val = row['Population'].iloc[0]
        
plt.annotate("China", 
                xy=(x_val, y_val),           # Point to the data
                xytext=(20, 20),             # Offset the text
                textcoords='offset points',  # How to interpret the offset
                arrowprops=dict(arrowstyle='->', color='black', lw=1),
                fontsize=10, 
                fontweight='bold')

plt.show();



