# %%
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

# %%
# problem 1
# Հայերեն: Օգտագործեք NumPy-ը՝ հաշվելու 'Infant mortality (per 1000 births)'-ի 10-րդ պերցենտիլը:
print(np.percentile(df["Infant mortality (per 1000 births)"].dropna(),10))

# %%
# problem 2
# Հայերեն: Ստեղծեք նոր 'Birth_Category' սյունակ՝ օգտագործելով np.where: 
# Եթե 'Birthrate' > 30, նշեք 'High', հակառակ դեպքում՝ 'Normal':
df["Birth_Category"]=np.where(df["Birthrate"]>30,"High","Normal")
print(df["Birth_Category"])

# %%
# problem 3
# Հայերեն: Զտեք այն երկրները 'SUB-SAHARAN AFRICA' տարածաշրջանում, որոնք ունեն 100-ից ավել 'Phones (per 1000)':
more_100=df[(df["Region"]=="SUB-SAHARAN AFRICA") & (df["Phones (per 1000)"]>100)]
print(more_100["Country"])

# %%
# problem 4
# Հայերեն: Խմբավորեք ըստ 'Region'-ի և հաշվեք յուրաքանչյուր տարածաշրջանի 'Service' (տնտեսական ոլորտ) միջինը:
grouped=df.groupby("Region")["Service"].mean()
print(grouped)

# %%
# probelm 5
# Հայերեն: Ստեղծեք 'Area (sq. mi.)'-ի և 'Population'-ի scatter plot:
# 1. Օգտագործեք լոգարիթմական սանդղակներ երկու առանցքների համար:
# 2. Գունավորեք կետերը ըստ 'GDP ($ per capita)'-ի:
# 3. Օգտագործեք plt.annotate՝ «China»-ն պիտակավորելու համար:
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Area (sq. mi.) log-Scale")
plt.ylabel("Population log-Scale")
plt.title("Global Scale:Area vs Population(Colored by GDP)")
plt.scatter(df["Area (sq. mi.)"],df["Population"],c=df["GDP ($ per capita)"])
plt.colorbar(label="GDP ($ per capita)")
china=df[df['Country'].str.contains('China')]
plt.annotate("China",
          xy=(china["Area (sq. mi.)"].values[0],
              china["Population"].values[0]),
        xytext=(100000000,9000000000),
        arrowprops=dict(arrowstyle="->")
)


