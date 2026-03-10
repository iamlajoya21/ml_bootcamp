# Grading Feedback: Ashot Klekchyan

**Total Score: 67/100**

## Task Breakdown
### Task 1
- **Score:** 10/20
- **Feedback:** The core logic of using `np.percentile` is present and conceptually correct. However, for real-world datasets that often contain missing values (NaNs), it's crucial to use `np.nanpercentile` to correctly calculate the percentile by ignoring these NaNs. Your current implementation would return `NaN` (as happens in this dataset for this column due to missing values), thus not providing a useful numerical result. Points were deducted for this critical oversight in handling missing data robustly.

### Task 2
- **Score:** 20/20
- **Feedback:** Excellent! Your implementation for conditional labeling using `np.where` is perfectly correct and efficient. The new 'Birth_Category' column is created as expected.

### Task 3
- **Score:** 18/20
- **Feedback:** Your multi-condition filtering is spot on and correctly identifies the countries meeting both criteria. The use of parentheses and the '&' operator is correct for combining conditions. To fully match the golden answer's demonstration, you could also print the count of filtered countries, which is a common and useful follow-up after filtering.

### Task 4
- **Score:** 19/20
- **Feedback:** Your `groupby()` and `mean()` aggregation is perfectly correct and efficiently calculates the mean 'Service' sector by 'Region'. A useful addition, as shown in the golden answer, would be to sort the results by the mean service value (e.g., `.sort_values(ascending=False)`) to easily identify regions with the highest or lowest service sector contributions, improving readability and insight.

### Task 5
- **Score:** 0/20
- **Feedback:** This task was not attempted. It required creating a scatter plot with log scales for both axes, coloring data points by 'GDP ($ per capita)', adding appropriate labels, a title, a colorbar, and specifically annotating 'China' on the plot. Note that the initial data cleaning was missing 'GDP ($ per capita)' from the `cols_to_fix` list, which would have caused issues if the task had been attempted as GDP would not have been correctly converted to a float.

## Overall Feedback
Ashot demonstrated a solid understanding of fundamental Pandas and NumPy operations in the tasks attempted. Tasks 2, 3, and 4 were largely correct, showcasing proficiency in conditional logic, multi-condition filtering, and data aggregation. However, there are key areas for improvement: (1) Robustness in NumPy: For Task 1, overlooking the importance of `np.nanpercentile` for handling missing data is a critical flaw in a data science context. (2) Completeness and Detail: While the core logic was correct for Tasks 3 and 4, pay attention to fully addressing the implicit or explicit requirements of the task, such as displaying counts or sorting results for better insights and readability. (3) Matplotlib: Task 5 was not attempted, which means a significant portion of the visualization skills could not be assessed. Additionally, ensure all relevant columns for subsequent tasks (like 'GDP ($ per capita)' and stripping 'Country' names) are correctly preprocessed during the initial data cleaning phase to avoid potential errors later on.
