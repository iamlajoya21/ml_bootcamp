#1
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA




df = pd.read_csv(r"\Users\aharu\Downloads\exam1\heart.csv")


X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()

features = ['age', 'oldpeak', 'trestbps', 'chol']
X_train_scaled = X_train.copy()
X_test_scaled = X_test.copy()

X_train_scaled[features] = scaler.fit_transform(X_train[features])
X_test_scaled[features] = scaler.transform(X_test[features])

model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train_scaled, y_train)

pca = PCA(n_components=2, random_state=42)
X_test_pca = pca.fit_transform(X_test_scaled) 


plt.figure(figsize=(9, 6))

scatter = plt.scatter(X_test_pca[:, 0], X_test_pca[:, 1], c=y_test, cmap='coolwarm', s=60, alpha=0.85, edgecolors='k')
plt.legend(handles=scatter.legend_elements()[0], labels=['Healthy (0)', 'Sick (1)'])
plt.title('PCA for heart disease', fontsize=14)

plt.show()

y_test_proba = model.predict_proba(X_test_scaled)[:,1]
y_train_proba = model.predict_proba(X_train_scaled)[:,1]

train_roc_auc = roc_auc_score(y_train, y_train_proba)
test_roc_auc = roc_auc_score(y_test, y_test_proba)

print(f"Train ROC-AUC  {train_roc_auc:.2f}")
print(f"Test ROC-AUC  {test_roc_auc:.2f}")

#-------------------------------------------------------
#2
from sklearn.cluster import KMeans

df_cc = pd.read_csv(r"\Users\aharu\Downloads\Credit card\CC GENERAL.csv")


X_cc = df_cc.drop(['CUST_ID','BALANCE_FREQUENCY','PURCHASES','ONEOFF_PURCHASES','INSTALLMENTS_PURCHASES'], axis=1)
X_cc['CREDIT_LIMIT'] = X_cc['CREDIT_LIMIT'].fillna(X_cc['CREDIT_LIMIT'].mode()[0])
X_cc['MINIMUM_PAYMENTS'] = X_cc['MINIMUM_PAYMENTS'].fillna(X_cc['MINIMUM_PAYMENTS'].mode()[0])

scaler_cc = StandardScaler()
X_cc_scaled = scaler_cc.fit_transform(X_cc)


wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_cc)
    wcss.append(kmeans.inertia_)


plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

kmeans = KMeans(n_clusters=4, init='k-means++', random_state=42)
clusters_lbl = kmeans.fit_predict(X_cc)

X_cc['cluster'] = clusters_lbl

res = X_cc.groupby('cluster')['BALANCE'].mean()
print(res)