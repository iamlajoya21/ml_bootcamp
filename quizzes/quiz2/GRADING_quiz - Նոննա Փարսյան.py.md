# Grading Feedback: Նոննա Փարսյան

**Total Score: 83/100**

## Task Breakdown
### Task 1
- **Score:** 20/20
- **Feedback:** Excellent work! You correctly calculated the 10th percentile of 'Infant mortality (per 1000 births)'. Using `.dropna()` before `np.percentile` is a perfectly valid and effective way to handle missing values, achieving the same correct result as `np.nanpercentile`.

### Task 2
- **Score:** 20/20
- **Feedback:** Perfect implementation! You've correctly used `np.where` to create the 'Birth_Category' column based on the specified condition. The logic is sound and produces the expected output.

### Task 3
- **Score:** 20/20
- **Feedback:** Great job! Your multi-condition filtering using Pandas boolean indexing with the `&` operator is spot on. You successfully identified the countries meeting both criteria.

### Task 4
- **Score:** 18/20
- **Feedback:** Your calculation of the mean 'Service' sector by 'Region' using `groupby()` is correct. To make the output even more insightful and easier to interpret, consider sorting the results (e.g., `sort_values(ascending=False)`) as demonstrated in the golden answer. This helps quickly identify regions with the highest or lowest mean service percentages.

### Task 5
- **Score:** 5/20
- **Feedback:** You correctly identified the need for a scatter plot, applied log scales to both axes, and correctly set up the labels, title, and colorbar. The annotation for 'China' was also implemented well, including finding its coordinates and using appropriate `annotate` parameters.

However, there is a critical error in data preparation for the plot. The 'GDP ($ per capita)' column was not converted to a numeric type (float) in your initial data cleaning step. This column contains commas as decimal separators (e.g., '30,800') and was treated as an 'object' (string) type by Pandas. As a result, when you tried to use `c=df['GDP ($ per capita)']` for coloring the scatter points, Matplotlib would raise a `ValueError` because it expects a numeric array for colormapping. This means the plot as intended (colored by GDP) would not render correctly.

Remember to ensure all columns intended for numerical operations or visual encoding (like color intensity) are properly cleaned and converted to numeric types before plotting.

## Overall Feedback
Նոննա, your submission demonstrates a strong understanding of NumPy and Pandas for data manipulation, as evidenced by your excellent performance in Tasks 1, 2, and 3. You correctly applied percentiles, conditional labeling, and multi-condition filtering.

In Task 4, your grouped aggregation was correct, but a minor improvement would be to sort the results for better readability.

Task 5, the visualization task, highlighted a critical area for improvement: thorough data preparation. While your plotting setup (log scales, labels, title, annotation) was largely correct, the omission of converting 'GDP ($ per capita)' to a numeric type during the initial cleaning caused a functional error in the scatter plot's coloring. Data cleaning is a foundational step, especially when preparing data for numerical operations or visualizations.

Overall, a very good effort! Focus on robust data type handling in your preprocessing steps, particularly for visualization, and continue practicing with sorting grouped results for enhanced presentation.
