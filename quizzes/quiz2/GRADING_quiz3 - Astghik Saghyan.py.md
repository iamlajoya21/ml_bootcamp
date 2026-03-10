# Grading Feedback: Astghik Saghyan

**Total Score: 100/100**

## Task Breakdown
### Task 1
- **Score:** 20/20
- **Feedback:** Excellent work. You correctly calculated the 10th percentile for 'Infant mortality (per 1000 births)'. Using `.dropna()` before `np.percentile` is a valid and robust approach to handle missing values, achieving the same correct result as `np.nanpercentile`.

### Task 2
- **Score:** 20/20
- **Feedback:** Perfect implementation of conditional labeling using `np.where`. The new 'Birth_Category' column is correctly assigned based on the 'Birthrate' condition.

### Task 3
- **Score:** 20/20
- **Feedback:** Outstanding use of Pandas for multi-condition filtering. Your approach of creating a boolean mask first is clear, readable, and functionally identical to the golden answer, correctly identifying countries in 'SUB-SAHARAN AFRICA' with more than 100 'Phones (per 1000)'.

### Task 4
- **Score:** 20/20
- **Feedback:** Very good. You correctly grouped the DataFrame by 'Region' and calculated the mean 'Service' for each region using `groupby()` and `mean()`. While the golden answer included sorting for presentation, your core aggregation is completely accurate as per the task requirements.

### Task 5
- **Score:** 20/20
- **Feedback:** A comprehensive and accurate visualization. You successfully created the scatter plot, applied log scales to both axes, colored the points by 'GDP ($ per capita)', and correctly annotated 'China'. Your method for finding 'China' using `.str.contains()` is robust. Minor stylistic differences (like `alpha` and `edgecolors` for scatter, or arrow color/size for annotation) do not detract from the functional correctness and clarity of the visualization.

## Overall Feedback
Astghik, your submission is excellent! You demonstrated a strong understanding of NumPy, Pandas, and Matplotlib across all tasks. Your solutions are correct, robust, and well-implemented. Keep up the great work!
