# Grading Feedback: Yulya Sargsyan

**Total Score: 80/100**

## Task Breakdown
### Task 1
- **Score:** 18/20
- **Feedback:** The calculation of the 10th percentile is correct, and using `.dropna()` effectively handles missing values, achieving the desired result. For conciseness and idiomatic NumPy, `np.nanpercentile` is often preferred as it handles NaNs internally without needing an explicit `.dropna()` call. Additionally, the output was not formatted as demonstrated in the golden answer (e.g., using an f-string with formatting).

### Task 2
- **Score:** 19/20
- **Feedback:** The implementation of conditional labeling using `np.where` is perfectly correct. The new `Birth_Category` column is created accurately based on the specified condition. The only minor deduction is for printing the entire `Birth_Category` series instead of a representative sample (like `head()`) or a subset, which is generally better for output presentation in notebooks or scripts.

### Task 3
- **Score:** 19/20
- **Feedback:** The multi-condition filtering using Pandas is correctly applied. The student accurately identifies countries in 'SUB-SAHARAN AFRICA' with more than 100 'Phones (per 1000)'. The golden answer, however, printed the *count* of these countries, whereas the student printed the list of `Country` names. While technically showing the filtered data, providing the count was the implicit objective for this problem statement.

### Task 4
- **Score:** 19/20
- **Feedback:** The grouped aggregation to calculate the mean 'Service' sector by 'Region' is correctly implemented using `groupby()` and `mean()`. The result is accurate. A minor enhancement, as shown in the golden answer, would be to sort the results (e.g., `sort_values(ascending=False)`) for better readability and easier comparison of regions.

### Task 5
- **Score:** 5/20
- **Feedback:** This task has several significant issues:
1.  **Critical Data Cleaning Oversight:** The 'GDP ($ per capita)' column was not included in the initial `cols_to_fix` list, meaning it likely remained as an `object` (string with commas) instead of being converted to a `float`. This is a critical functional error, as `plt.scatter` cannot use a string column for numerical coloring, rendering the `c=df["GDP ($ per capita)"]` part of the plot ineffective or causing an error.
2.  **Colorbar Linkage:** The `plt.colorbar()` call was not correctly linked to the scatter plot object (e.g., `plt.colorbar(scatter_object, ...) `). This can lead to an unassociated or improperly scaled colorbar.
3.  **Annotation `xytext` Misuse:** The `xytext` parameter for `plt.annotate` was specified using absolute data coordinates (`(100000000, 9000000000)`), which is generally incorrect. `xytext` is typically used to specify an offset in points from the annotated point, often in conjunction with `textcoords='offset points'`, or relative to the figure. This misuse makes the annotation text placement problematic, likely placing it far from the arrow or off-screen.
4.  **Incomplete Cleaning for Country:** The 'Country' column was not stripped of whitespace during initial cleaning, which could affect precise country matching (though `str.contains('China')` is forgiving here).
5.  **Missing Visual Enhancements:** The plot lacks several details from the golden answer, such as explicit `figsize` for the figure, `alpha` and `edgecolors` for the scatter points, and a grid (`plt.grid()`). Also, `plt.show()` was omitted.

## Overall Feedback
Yulya demonstrates a strong grasp of fundamental NumPy and Pandas operations as shown in Tasks 1-4. The logic for these tasks is largely correct, with minor deductions related to output formatting or opportunities for slightly more idiomatic/readability-focused solutions. However, Task 5 on Matplotlib visualization and annotation has significant functional and conceptual issues. The most critical problem is the oversight in data cleaning for the 'GDP ($ per capita)' column, which directly impacts the ability to color the scatter plot correctly. Additionally, the approach to annotating 'China' using `xytext` with absolute coordinates indicates a misunderstanding of how to properly position annotation text. To improve, Yulya should pay closer attention to comprehensive data preparation (especially when a column's data type is crucial for subsequent operations), and thoroughly review advanced Matplotlib features like `plt.annotate` and `plt.colorbar` to understand their parameters and best practices.
