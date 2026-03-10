# Grading Feedback: Samvel Harutunyan

**Total Score: 74/100**

## Task Breakdown
### Task 1
- **Score:** 18/20
- **Feedback:** Your solution correctly calculates the 10th percentile for 'Infant mortality (per 1000 births)'. You correctly handled NaN values using `.dropna()` before `np.percentile()`. While effective, the golden answer utilized `np.nanpercentile()`, which is often a more direct way to achieve the same result by ignoring NaNs directly. A minor point is the lack of formatted printing as seen in the golden answer.

### Task 2
- **Score:** 19/20
- **Feedback:** Your implementation for creating the 'Birth_Category' column using `np.where()` is perfectly correct and follows the prompt's logic. The only minor point of difference is that the golden answer included a print statement to display the first few rows of the new column, which was omitted here.

### Task 3
- **Score:** 17/20
- **Feedback:** Your multi-condition filtering to find countries in 'SUB-SAHARAN AFRICA' with 'Phones (per 1000)' greater than 100 is logically sound and correctly implemented. However, the golden answer specifically asked for and printed the *number* of countries found, whereas your solution prints the entire filtered DataFrame. While the data is correct, returning a count is more concise when asked for such a specific metric.

### Task 4
- **Score:** 15/20
- **Feedback:** You correctly calculated the mean 'Service' sector value grouped by 'Region'. The fundamental aggregation is accurate. The primary deduction here is that your result was not sorted in descending order as demonstrated in the golden answer's output, which helps in quickly identifying regions with higher or lower service sector contributions.

### Task 5
- **Score:** 5/20
- **Feedback:** This task had several critical issues:
1.  **Data Cleaning Omission:** The most significant issue is that 'GDP ($ per capita)' was not included in your initial `cols_to_fix` list. This column contains commas in the raw data, meaning it was likely read as a string/object type. Attempting to use a non-numeric column for `c` in `plt.scatter()` for color mapping would either fail or produce incorrect/meaningless results.
2.  **Country Column Not Stripped:** You stripped the 'Region' column but not the 'Country' column. This led to issues in annotating 'China', as the country name in the DataFrame is 'China ' (with a trailing space). The golden answer explicitly strips the 'Country' column to ensure robust matching.
3.  **Missing Plot Details:** Several aesthetic details were missing from the scatter plot, such as `alpha` and `edgecolors` for the scatter points, and the more descriptive labels for axes (e.g., 'Area (sq. mi.) - Log Scale') and title ('Global Scale: Area vs. Population (Colored by GDP)').
4.  **Annotation Details:** The arrow properties for the 'China' annotation were less detailed than in the golden answer (missing `arrowstyle`, `color`, `lw`, `fontsize`, `fontweight`).
5.  **Missing Grid:** The plot also missed the addition of a grid, which aids readability for log-scale plots.

## Overall Feedback
Samvel, your submission demonstrates a good understanding of NumPy for basic operations and Pandas for filtering and grouping. Tasks 1, 2, and 3 showed strong core logic, with only minor deviations in presentation or specific method choice. Task 4 was very close, missing only a sorting step. 

However, Task 5 revealed significant challenges, particularly concerning robust data cleaning and attention to detail in visualization requirements. The omission of 'GDP ($ per capita)' from the initial data cleaning meant that the core 'coloring' aspect of the scatter plot would likely not function as intended, which is a critical error. Similarly, not stripping the 'Country' column introduces brittleness to your code when trying to match specific country names. 

To improve, focus on:
1.  **Comprehensive Data Cleaning:** Ensure all columns used in calculations or visualizations are in the correct data type, especially after reading CSVs with non-standard delimiters (like commas in numbers).
2.  **Attention to Detail:** Carefully review all requirements for each task, including specific output formats (e.g., printing count vs. full DataFrame, sorting results).
3.  **Robustness:** Consider edge cases and data inconsistencies (like leading/trailing spaces in string columns) and implement cleaning steps to handle them proactively, as shown in the golden answer for the 'Country' column.

Keep up the good work on the conceptual understanding, and pay closer attention to the finer details and robustness of your implementations!
