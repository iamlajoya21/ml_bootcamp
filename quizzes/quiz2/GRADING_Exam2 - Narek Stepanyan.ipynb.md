# Grading Feedback: Narek Stepanyan

**Total Score: 67/100**

## Task Breakdown
### Task 1
- **Score:** 15/20
- **Feedback:** The calculation for the 10th percentile is correct, and you successfully print the result. However, it's generally better practice to use `np.nanpercentile()` when dealing with potential NaN values, as it allows you to calculate the percentile while ignoring NaNs without modifying the original DataFrame. Your approach of using `df.dropna(subset=...)` modifies the DataFrame, which could have unintended side effects on subsequent tasks if other columns from those dropped rows were needed.

### Task 2
- **Score:** 20/20
- **Feedback:** Excellent work! You correctly used `np.where()` to create the 'Birth_Category' column based on the specified condition. The preview of the DataFrame with the new column is also well done.

### Task 3
- **Score:** 20/20
- **Feedback:** Perfect! You successfully applied multi-condition filtering using Pandas to select countries in 'SUB-SAHARAN AFRICA' with 'Phones (per 1000)' greater than 100. Displaying the head of the filtered DataFrame is appropriate.

### Task 4
- **Score:** 12/20
- **Feedback:** You correctly identified the grouping and aggregation needed to calculate the mean 'Service' by 'Region'. However, there are two points for improvement: 
1. The result of `df.groupby(...).mean()` was computed but not stored in a variable or printed, so the output for this task is not displayed.
2. The golden answer also included `sort_values(ascending=False)` to order the regions by their mean 'Service', which is a good practice for presenting grouped data clearly.

### Task 5
- **Score:** 0/20
- **Feedback:** This task has several critical issues:
1.  **Critical Data Cleaning Error:** The `GDP ($ per capita)` column was not included in your initial `cols_to_fix` list. This means it remained a string type (likely containing commas). `plt.scatter`'s `c` argument expects numeric data for color mapping; therefore, this fundamental error prevents the plot from correctly coloring points by GDP, likely leading to an error or an incorrect visualization without color mapping.
2.  **Missing `Country` Column Cleaning:** You did not strip whitespace from the `Country` column (`df['Country'] = df['Country'].str.strip()`). While 'China' might not have leading/trailing spaces in this specific dataset, this is a crucial step for robust data matching and can lead to annotation failures.
3.  **Incomplete Plot Elements:** You correctly used log scales and basic x/y labels. However, you missed adding a title (`plt.title`) and, critically, a color bar (`plt.colorbar`), which is essential for interpreting what the colors (GDP) represent.
4.  **Basic Annotation:** While you attempted to annotate 'China', your annotation is very basic. The golden answer demonstrated more complete annotation styling (e.g., `xytext`, `arrowprops`, `fontsize`, `fontweight`) to make the label clearer and more professional.

Due to the critical data type error for the color mapping, the core requirement of coloring by GDP could not be correctly fulfilled, leading to a score of 0 for this task.

## Overall Feedback
Narek, your submission demonstrates a solid understanding of basic NumPy and Pandas operations for Tasks 2 and 3, which were executed perfectly. You also correctly grasped the core logic for percentiles (Task 1) and grouped aggregation (Task 4).

However, there are crucial areas for improvement. For Task 1 and 4, pay close attention to best practices (like using `np.nanpercentile` to avoid modifying the DataFrame) and ensuring all computed results are explicitly displayed or stored. The most significant area for improvement is Task 5. A fundamental error in data cleaning (not converting 'GDP ($ per capita)' to a numeric type) prevented the core visualization requirement from being met. Additionally, robust data preparation (stripping `Country` names) and comprehensive plot elements (title, colorbar, detailed annotation styling) are essential for effective data visualization. Focus on these details and dependencies between data cleaning and visualization for future assignments.
