# Grading Feedback: Հար Խաչատրյան

**Total Score: 74/100**

## Task Breakdown
### Task 1
- **Score:** 15/20
- **Feedback:** The calculation of the 10th percentile is correct. However, using `np.percentile` instead of `np.nanpercentile` is less robust if NaNs were present (though `dropna` might mitigate this here). The variable name `percentile_90` is confusing as it represents the 10th percentile. Additionally, the result should be printed with a descriptive message rather than just outputting the variable.

### Task 2
- **Score:** 18/20
- **Feedback:** The implementation of `np.where` to create the `Birth_Category` column is perfectly correct. A minor improvement would be to display a sample of the DataFrame (e.g., using `.head()`) to clearly show the newly added column and its values, as demonstrated in the golden answer.

### Task 3
- **Score:** 17/20
- **Feedback:** The multi-condition filtering logic is correct and effectively identifies the countries meeting the criteria. While `.str.strip()` on `df['Region']` within the filter is functionally correct, it's redundant if the column was already stripped during the initial data cleaning. The primary deduction is for displaying `filtered_df.head()` instead of providing the requested *number* or *count* of countries that satisfy the conditions.

### Task 4
- **Score:** 14/20
- **Feedback:** The core grouping by 'Region' and calculating the mean of 'Service' is correct. However, `reset_index()` is generally not needed for displaying aggregated results as a Series is often clearer. More importantly, the results were not sorted, which is a common practice for grouped aggregations to easily identify patterns (e.g., highest/lowest regions). A descriptive print statement for the result is also missing.

### Task 5
- **Score:** 10/20
- **Feedback:** While the overall structure of the plot is present (scatter plot, log scales, colorbar, basic annotation), there are several critical omissions and areas for improvement. **Crucially, 'GDP ($ per capita)' was not included in your `cols_to_fix` list during data setup, meaning it was likely not converted to a proper float type from strings with commas, which is a fundamental data preparation step for numerical plotting.** Other missing elements include `edgecolors` for the scatter points, the grid, and more detailed styling for the annotation arrow (`color`, `lw`, `fontsize`, `fontweight`). The axis labels and title could also be more descriptive by explicitly mentioning 'Log Scale'.

## Overall Feedback
Հար, your submission demonstrates a good understanding of the core concepts in NumPy, Pandas, and Matplotlib. You've correctly applied `np.where`, multi-condition filtering, and basic grouping. The plotting structure for Task 5 is also largely there.

However, there are recurring themes for improvement:
1.  **Robust Data Cleaning:** The most significant issue was the oversight in Task 5 where the 'GDP ($ per capita)' column was not properly converted to a numerical type during the initial data cleaning, which is essential for accurate plotting. Similarly, using `np.nanpercentile` in Task 1 is generally more robust than `np.percentile` when dealing with potential missing data.
2.  **Completeness of Output/Demonstration:** For several tasks (1, 2, 3, 4), you provided the direct output of a variable or a `.head()` view instead of a clear, descriptive print statement or the specific summary (like a count) that the task implied. Always aim to present your results clearly and completely.
3.  **Attention to Detail in Visualization:** For Matplotlib, pay close attention to all requested details – this includes descriptive labels, specific plot elements (like `edgecolors` or a `grid`), and comprehensive annotation styling.

Keep practicing these details, especially robust data preparation and clear result presentation, to elevate your data science skills!
