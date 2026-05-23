#%%
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
from catboost import CatBoostClassifier
from xgboost import XGBClassifier
#%%
1
'''
cp
thalach
exang
oldpeak
slope
ca
thal
'''
#categorical cp,fbs,slope,ca,thal,
Data=pd.read_csv('data//heart.csv')
Data.isna().sum()
categoricall=['cp','fbs','slope','ca','thal']
X=Data.drop(columns=['target'])
Y=Data['target']
X=pd.get_dummies(X,columns=categoricall,drop_first=True)
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2, random_state=9)
scaler=StandardScaler()
x_train_scaled=scaler.fit_transform(x_train)
x_test_scaled=scaler.transform(x_test)
models={
"logmodel":LogisticRegression(),
"knn":KNeighborsClassifier(n_neighbors=5),
"treemodel":DecisionTreeClassifier(),
"fmodel":RandomForestClassifier(),
}

for name,model in models.items():
    model.fit(x_train_scaled,y_train)
    y_pred=model.predict(x_test_scaled)
    y_prob=model.predict_proba(x_test_scaled)
    y_prob=y_prob[:,1]

    print(name)
    #print(classification_report(y_test,y_pred))
    print("roc auc",roc_auc_score(y_test,y_prob))
'''
modelss={
    "cmodel":CatBoostClassifier(),
    "xmodel":XGBClassifier()
}

for name,model in modelss.items():
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)

    print(name)
    print(classification_report(y_test,y_pred))
    print("roc auc",roc_auc_score(y_test,y_pred))
'''

2
'''
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

fData=pd.read_csv('data//CC GENERAL.csv')
Data.head()
Data.isna().sum()
originaldata=Data.copy()
X=Data.drop(columns=['CUST_ID'])
X=X.fillna(X.mean())
X.isna().sum()
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

inertias=[]
k_range=range(1,11)
for k in k_range:
    kmeans=KMeans(n_clusters=k,random_state=0)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)
plt.plot(k_range,inertias)
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()
#k=5
final_kmeans=KMeans(n_clusters=5, random_state=0)
clusters=final_kmeans.fit_predict(X_scaled)
originaldata['cluster']=clusters
print(originaldata['cluster'].value_counts())
mean_balance=originaldata.groupby('cluster')['BALANCE'].mean()
print(mean_balance)
pca=PCA(n_components=2)
X_pca=pca.fit_transform(X_scaled)
plt.scatter(X_pca[:,0],X_pca[:,1],c=clusters)
plt.show()
'''
#%%
