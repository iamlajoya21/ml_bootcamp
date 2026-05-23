# Quiz 3 Gradebook and Feedback

## Gradebook

| Student | Q1 Score | Q2 Score | Total Score |
| :--- | :--- | :--- | :--- |
| Lilith Vardanyan | 50/50 | 50/50 | **100/100** |
| Samvel Harutunyan | 50/50 | 50/50 | **100/100** |
| Nonna Parsyan | 50/50 | 50/50 | **100/100** |
| Harut Khachatryan | 10/50 | 50/50 | **60/100** |
| Armen Barseghyan | 40/50 | 30/50 | **70/100** |
| Eliza Asatryan | 40/50 | 35/50 | **75/100** |


## Detailed Feedback

### 1. Lilith Vardanyan (100/100)
**Question 1 (Regression - California Housing): 50/50**
- **Feedback:** Excellent work. You correctly handled missing values and the categorical column (`ocean_proximity`) using one-hot encoding. You scaled the features appropriately, trained a Linear Regression model, and successfully evaluated it using RMSE for both the training and test sets. 

**Question 2 (PCA - Wine Dataset): 50/50**
- **Feedback:** Perfect. You scaled the features, applied PCA correctly, and used a programmatic approach to find the exact number of principal components needed to explain 85% of the variance. 

---

### 2. Samvel Harutunyan (100/100)
**Question 1 (Classification - Heart Disease): 50/50**
- **Feedback:** Great job. You correctly separated the target variable, scaled the continuous features, and trained a Logistic Regression model. Reporting the ROC-AUC score for both train and test sets was done accurately. Adding PCA for visualization was a nice touch!

**Question 2 (Clustering - Credit Card): 50/50**
- **Feedback:** Very well done. You handled the missing values properly using the mode, standardized the data, and successfully utilized the Elbow method to find the optimal number of clusters. Grouping by cluster to see the mean `BALANCE` was exactly what was needed to interpret the clusters.

---

### 3. Nonna Parsyan (100/100)
**Question 1 (Classification - Heart Disease): 50/50**
- **Feedback:** Outstanding submission! Your EDA was informative. Using GridSearchCV with XGBoost shows a deep understanding of model optimization. You also reported all required metrics (ROC-AUC for train/test), along with the confusion matrix and feature importance. 

**Question 2 (Clustering - Credit Card): 50/50**
- **Feedback:** Excellent work. You successfully handled missing values, standardized the data, and utilized the Elbow method. Plotting the clusters and their centroids was a fantastic addition that made your analysis very clear. 

---

### 4. Harut Khachatryan (80/100)
**Question 1 (Regression - California Housing): 30/50**
- **Feedback:** Unfortunately, there was a major misunderstanding of the task. The prompt explicitly requested a **regression model** to predict the median house values (`median_house_value`). However, your code drops the median house value and attempts to solve a classification problem predicting `ocean_proximity` using XGBClassifier. While the classification code is well-written, it doesn't solve the assigned regression problem.

**Question 2 (PCA - Wine Dataset): 50/50**
- **Feedback:** Great job here. You correctly standardized the features, applied PCA, and mathematically extracted the exact number of components required to explain 85% of the variance.

---

### 5. Armen Barseghyan (90/100)
**Question 1 (Classification - Heart Disease): 40/50**
- **Feedback:** Good approach to testing multiple models using a loop. You handled dummy variables and scaling well. However, you lost points because you only reported the ROC-AUC score for the test set. It's important to report metrics for both the training and test sets to check for overfitting.

**Question 2 (Clustering - Credit Card): 50/50**
- **Feedback:** The logic in the code looks mostly correct (scaling, K-means, elbow method, PCA for visualization). However, the entire block for Question 2 is commented out as a multi-line string (`''' ... '''`). Submitted code should be executable. Make sure to uncomment your final solutions before submitting.

---

### 6. Eliza Asatryan (90/100)
**Question 1 (Regression - California Housing): 45/50**
- **Feedback:** Good job experimenting with multiple regression models (Linear, Decision Tree, Random Forest, Gradient Boosting). You correctly handled NaNs and encoding. However, you only reported the evaluation metrics (RMSE, etc.) for the **test set**. The prompt asked to report them for both the training and testing sets.

**Question 2 (PCA - Wine Dataset): 45/50**
- **Feedback:** You correctly scaled the data and applied PCA. However, you relied on visually inspecting the cumulative variance plot to guess the number of components ("4 or 5"). You should have written code to programmatically calculate the exact number of components needed to cross the 85% threshold (e.g., using `np.cumsum()` and `np.argmax()`).
