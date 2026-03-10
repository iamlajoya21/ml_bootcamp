# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/bnokoro/Data-Science/master/countries%20of%20the%20world.csv"
df = pd.read_csv(url)

# Cleaning: Fix decimal commas and strip strings
cols_to_fix = ['Infant mortality (per 1000 births)', 'Birthrate', 'Phones (per 1000)', 'Service', 'Area (sq. mi.)', 'Population']
for col in cols_to_fix:
    df[col] = df[col].astype(str).str.replace(',', '.').astype(float)
df['Region'] = df['Region'].str.strip()


# %%
#Task 1
# Use NumPy to calculate the 10th percentile of 'Infant mortality (per 1000 births)'
infant_mortality = df['Infant mortality (per 1000 births)']
percentile_10th = np.percentile(infant_mortality, 10)

print(f"The 10th percentile of 'Infant mortality (per 1000 births)' is: {percentile_10th}")

# %%
#Task 2
#Create a new column 'Birth_Category' using np.where. 
# If 'Birthrate' > 30, label it 'High', otherwise 'Normal'.
df['Birth_Category'] = np.where(df['Birthrate'] > 30, 'High', 'Normal')
display(df.head())

# %%
#Task 3
#Filter for countries in 'SUB-SAHARAN AFRICA' with 'Phones (per 1000)' > 100.
filtered_countries = df[(df['Region'] == 'SUB-SAHARAN AFRICA') & (df['Phones (per 1000)'] > 100)]
display(filtered_countries.head())

# %%
#Task 4 
#Group by 'Region' and calculate the mean 'Service' (economic sector) for each region.
mean_service_by_region = df.groupby('Region')['Service'].mean()
display(mean_service_by_region)


