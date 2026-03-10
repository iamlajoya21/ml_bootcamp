# Grading Feedback: Narek Stepanyan

**Total Score: 75/100**

## Task Breakdown
### Task 1
- **Score:** 15/20
- **Feedback:** Your solution correctly calculates the 10th percentile. However, instead of using `df.dropna(subset=['Infant mortality (per 1000 births)'])`, which modifies the entire DataFrame in-place, it is generally better practice to use `np.nanpercentile()`. This function directly ignores NaN values in the calculation without altering the original DataFrame, thus preventing unintended side effects on subsequent tasks. If you absolutely need to drop NaNs, consider doing so on a copy of the specific column or DataFrame slice to maintain the integrity of your main `df` for later operations.

### Task 2
- **Score:** 20/20
- **Feedback:** Excellent work! You have correctly implemented the conditional labeling using `np.where` to create the 'Birth_Category' column exactly as requested. The logic is sound and efficient.

### Task 3
- **Score:** 20/20
- **Feedback:** Perfectly done! Your multi-condition filtering for countries in 'SUB-SAHARAN AFRICA' with 'Phones (per 1000)' > 100 is accurate and uses the correct Pandas syntax. You effectively combined the conditions using the logical AND operator `&`.

### Task 4
- **Score:** 15/20
- **Feedback:** Your implementation correctly groups the DataFrame by 'Region' and calculates the mean of the 'Service' column. However, the result of `df.groupby('Region')['Service'].mean()` was not assigned to a variable or printed to the console. In a script, this means the computation is performed, but its output is lost. Always ensure to either assign the result to a variable for future use or print it to make it visible. Adding `.sort_values(ascending=False)` would also improve readability of the output.

### Task 5
- **Score:** 5/20
- **Feedback:** This task requires significant improvement due to several critical issues:
1.  **Data Cleaning Error (Critical):** You omitted `'GDP ($ per capita)'` from your initial `cols_to_fix` list. This means the GDP column was never converted to a numeric type (float) and remained as strings (e.g., '1,234.5'). As a result, `plt.scatter` cannot properly color the points based on a continuous numerical scale, leading to an incorrect or non-functional plot coloring.
2.  **Data Cleaning Error (Critical):** You also missed stripping the `Country` column (`df['Country'] = df['Country'].str.strip()`) during data setup. If country names had leading/trailing spaces (which is common in raw data), your `df[df['Country'] == 'China']` filter would likely return an empty DataFrame, causing an error when trying to access `.iloc[0]` for annotation coordinates.
3.  **Missing Plot Elements:** Your plot is missing an essential title (`plt.title()`) and a colorbar (`plt.colorbar()`), which are crucial for interpreting the colored points representing GDP.
4.  **Annotation Enhancements:** While you attempted the annotation for 'China', it lacked stylistic details like `color`, `lw` (linewidth), `fontsize`, and `fontweight` for the arrow and text, which make the annotation more visible and professional.
5.  **Axis Labels:** While present, the `xlabel` and `ylabel` could be more descriptive by adding ' - Log Scale' to clearly indicate the transformation.

## Overall Feedback
Narek, your submission demonstrates a good understanding of core NumPy and Pandas operations for Tasks 2 and 3, which were executed perfectly. For Task 1 and 4, the logic was mostly correct, but there were minor functional omissions or less ideal practices (like `dropna` modifying the DataFrame or not printing/storing results). The main area for improvement is Task 5, where critical omissions in the initial data cleaning directly impacted the functionality and correctness of the Matplotlib visualization. Pay close attention to ensuring all relevant columns are correctly prepared (e.g., stripped, converted to numeric types) before attempting advanced operations or visualizations. Thorough data preparation is the foundation of successful data analysis and visualization. Keep practicing!
