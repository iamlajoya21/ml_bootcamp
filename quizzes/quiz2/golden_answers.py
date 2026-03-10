import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- DATA SETUP (Provided in prompt) ---
url = "https://raw.githubusercontent.com/bnokoro/Data-Science/master/countries%20of%20the%20world.csv"
df = pd.read_csv(url)

# Cleaning: Fix decimal commas and strip strings
cols_to_fix = ['Infant mortality (per 1000 births)', 'Birthrate', 'Phones (per 1000)', 
               'Service', 'Area (sq. mi.)', 'Population', 'GDP ($ per capita)'] # Added GDP for Task 5
for col in cols_to_fix:
    df[col] = df[col].astype(str).str.replace(',', '.').astype(float)

df['Region'] = df['Region'].str.strip()
df['Country'] = df['Country'].str.strip() # Crucial for Task 5 matching

# ==========================================
# TASK 1 (NumPy): Percentiles
# ------------------------------------------
# We use np.nanpercentile to ignore any missing (NaN) values in the column
infant_10th = np.nanpercentile(df['Infant mortality (per 1000 births)'], 10)

print(f"The 10th percentile for Infant Mortality is: {infant_10th:.2f}")

# ==========================================
# TASK 2 (NumPy): Conditional Labeling
# ------------------------------------------
df['Birth_Category'] = np.where(df['Birthrate'] > 30, 'High', 'Normal')

print("\nFirst 5 rows with Birth_Category:")
print(df[['Country', 'Birthrate', 'Birth_Category']].head())

# ==========================================
# TASK 3 (Pandas): Multi-Condition Filtering
# ------------------------------------------
# Use () to separate conditions and & for logical AND
africa_phones = df[(df['Region'] == 'SUB-SAHARAN AFRICA') & (df['Phones (per 1000)'] > 100)]

print(f"\nNumber of Sub-Saharan countries with > 100 phones: {len(africa_phones)}")

# ==========================================
# TASK 4 (Pandas): Grouped Aggregation
# ------------------------------------------
service_mean = df.groupby('Region')['Service'].mean().sort_values(ascending=False)

print("\nMean Service Sector by Region:")
print(service_mean)

# ==========================================
# TASK 5 (Matplotlib): Visualization & Annotation
# ------------------------------------------
plt.figure(figsize=(10, 6))

# 1. Create the scatter plot
# We use a colormap (cmap) to visualize GDP wealth
scatter = plt.scatter(df['Area (sq. mi.)'], df['Population'], 
                     c=df['GDP ($ per capita)'], cmap='viridis', 
                     alpha=0.6, edgecolors='white')

# 2. Set Log Scales
plt.xscale('log')
plt.yscale('log')

# 3. Add Labels and Titles
plt.xlabel('Area (sq. mi.) - Log Scale')
plt.ylabel('Population - Log Scale')
plt.title('Global Scale: Area vs. Population (Colored by GDP)')
plt.colorbar(scatter, label='GDP ($ per capita)')

# 4. Annotation for China
# We locate China's coordinates
china_data = df[df['Country'] == 'China']

if not china_data.empty:
    china_x = china_data['Area (sq. mi.)'].values[0]
    china_y = china_data['Population'].values[0]
    
    plt.annotate('China', 
                 xy=(china_x, china_y),          # Point to annotate
                 xytext=(30, 30),                # Text position offset
                 textcoords='offset points', 
                 arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
                 fontsize=12, fontweight='bold')

plt.grid(True, which="both", ls="-", alpha=0.2)
plt.show()