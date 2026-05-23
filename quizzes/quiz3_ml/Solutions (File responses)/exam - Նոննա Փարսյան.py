#Question 1 (Classification)
import pandas as pd 
import kagglehub
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import seaborn as sns
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,roc_auc_score,classification_report
import matplotlib.pyplot as plt 
from xgboost import plot_importance

path=kagglehub.dataset_download('johnsmith88/heart-disease-dataset')
data=pd.read_csv(f"{path}/heart.csv")
X=data.drop(columns=['target'])
y=data['target']



X.isnull().sum()


X.info()


X.describe()



X.columns 


sns.countplot(x='target',hue='sex',data=data);


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

param_grid={
    'n_estimators': [50, 100,150],
    'max_depth': [2, 3],
    'learning_rate': [0.01, 0.05, 0.1,0.08],
    'gamma': [0.5, 1,0.3],
    'subsample': [0.7, 0.8],
    'colsample_bytree': [0.7, 0.8]
}
grid_search=GridSearchCV(estimator=XGBClassifier(random_state=42),param_grid=param_grid,cv=5,n_jobs=-1)
grid_search.fit(X_train_scaled,y_train)
best_model=grid_search.best_estimator_

test_acc=accuracy_score(y_test,best_model.predict(X_test_scaled))
train_acc=accuracy_score(y_train,best_model.predict(X_train_scaled))
cv_score=grid_search.best_score_

print(f"Best Hyperparameters:{grid_search.best_params_}")
print(f"Mean cv Accuracy:{cv_score:.4f}")
print(f"Test Set Accuracy:{test_acc:.4f}")
print(f"Train Set Accuracy:{train_acc:.4f}")

train_pred_proba = best_model.predict_proba(X_train)[:, 1]
test_pred_proba = best_model.predict_proba(X_test)[:, 1]


train_roc_auc = roc_auc_score(y_train, train_pred_proba)
test_roc_auc = roc_auc_score(y_test, test_pred_proba)

print(f"Train Set ROC-AUC Score: {train_roc_auc:.4f}")
print(f"Test Set ROC-AUC Score: {test_roc_auc:.4f}")



cm=confusion_matrix(y_test,best_model.predict(X_test_scaled))

plt.figure(figsize=(6,6))
sns.heatmap(cm, annot=True,fmt='d',cmap='Blues')
plt.xlabel('Կանխատեսված')
plt.ylabel('Իրական')
plt.title('Confusion Matrix')
plt.show()



print(classification_report(y_test,best_model.predict(X_test_scaled)))


best_model.get_booster().feature_names = list(X_train.columns)
plt.figure(figsize=(10, 12)) 
plot_importance(best_model)
plt.show();


#Question 2 (Clustering)

import kagglehub
import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


path=kagglehub.dataset_download('arjunbhasin2013/ccdata')
credits=pd.read_csv(f"{path}/CC GENERAL.csv")
credits.head()


credits.isnull().sum()

credits.describe()


mean_value=credits['CREDIT_LIMIT'].mean()
most_common=credits['MINIMUM_PAYMENTS'].mode()[0]

credits['CREDIT_LIMIT']=credits['CREDIT_LIMIT'].fillna(mean_value)
credits['MINIMUM_PAYMENTS']=credits['MINIMUM_PAYMENTS'].fillna(most_common)

X=credits[['PURCHASES','PURCHASES_TRX']]
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)


wcss=[]

for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8,6))
plt.plot(range(1,11),wcss,marker='o',linestyle='--')

plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()



optimal_k=5
kmeans=KMeans(n_clusters=optimal_k,init='k-means++',random_state=42)
y=kmeans.fit_predict(X_scaled)
credits['Cluster']=y



plt.figure(figsize=(10,7))

colors=['red','green','blue','pink','yellow']
for i in range(optimal_k):
    plt.scatter(
        X.iloc[y==i,0],
        X.iloc[y==i,1],
        c=colors[i],
        s=50,
        label=f"Cluster{i}"
    )
    
original_centroids=scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(
    original_centroids[:, 0], 
    original_centroids[:, 1], 
    s=200, 
    c='black', 
    marker='X', 
    label='Centroids'
)

plt.title('K-Means Clustering')
plt.legend()
plt.grid(True)
plt.show()



result=credits.groupby('Cluster')['BALANCE'].mean()
result.round()