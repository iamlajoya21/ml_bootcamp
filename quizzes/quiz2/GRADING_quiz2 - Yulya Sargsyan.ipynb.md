# Grading Feedback: Yulya Sargsyan

**Total Score: 88/100**

## Task Breakdown
### Task 1
- **Score:** 20/20
- **Feedback:** Excellent work. You correctly used `np.percentile` and handled missing values using `.dropna()` before calculation, which is a valid approach. The result is accurate.

### Task 2
- **Score:** 20/20
- **Feedback:** Correctly implemented `np.where` to create the 'Birth_Category' column based on the specified condition. The logic is sound.

### Task 3
- **Score:** 20/20
- **Feedback:** You successfully filtered the DataFrame using multiple conditions with Pandas. The use of parentheses for conditions and `&` for logical AND is correct. Printing the filtered countries by name is a good way to show the result.

### Task 4
- **Score:** 20/20
- **Feedback:** You correctly grouped the DataFrame by 'Region' and calculated the mean of the 'Service' column using Pandas `groupby()` and `mean()`. This is an accurate aggregation.

### Task 5
- **Score:** 8/20
- **Feedback:** This task had several critical issues and missing components:
1.  **Data Cleaning Omission (Critical)**: The `GDP ($ per capita)` column was not included in your initial `cols_to_fix` list. This means if the raw data contained commas as decimal separators (which it does), this column would remain as a string/object type. As a result, using `c=df["GDP ($ per capita)"]` in `plt.scatter` would likely fail to color the points correctly or at all, rendering a core part of the visualization non-functional.
2.  **Colorbar Usage**: Your `plt.colorbar(label="GDP ($ per capita)")` call is not explicitly linked to the `scatter` plot object. While it might sometimes work, the robust way is `plt.colorbar(scatter_object, label=...)` after `scatter_object = plt.scatter(...)`. Given the GDP cleaning issue, the colorbar would also be incorrect or absent.
3.  **Annotation Placement (Critical)**: For the China annotation, `xytext=(100000000,9000000000)` sets an *absolute* coordinate that is extremely far from the actual data point and likely off-plot, rendering the annotation useless. The correct approach for offsetting text relative to the point is to use `textcoords='offset points'` with smaller `xytext` values, as demonstrated in the Golden Answer.
4.  **Missing `plt.show()`**: While plots may display in some interactive environments without it, `plt.show()` is essential for scripts and good practice.
5.  **Missing Aesthetics**: Several aesthetic elements like `plt.figure(figsize=...)`, `cmap`, `alpha`, `edgecolors` for the scatter plot, and `fontsize`, `fontweight`, `color` for annotation, and `plt.grid()` were missing. These significantly enhance plot readability and professionalism. You did correctly apply log scales and set the main labels and title.

## Overall Feedback
Yulya, you demonstrated excellent proficiency in the NumPy and Pandas tasks (Tasks 1-4), providing accurate and efficient solutions. Your understanding of data manipulation, filtering, and aggregation is strong.

However, your submission for the Matplotlib visualization task (Task 5) had several critical functional errors. The most significant was overlooking the cleaning of the 'GDP ($ per capita)' column, which directly impacted the coloring of your scatter plot and the subsequent colorbar. Furthermore, the method used for annotating 'China' led to the annotation being placed incorrectly, making it ineffective.

To improve, pay close attention to the entire data pipeline, including all necessary cleaning steps for columns used in visualization. For Matplotlib, practice the precise usage of functions like `plt.annotate`'s `xytext` and `textcoords` parameters, and ensure your `colorbar` is correctly linked. Also, consider incorporating more aesthetic choices (like `figsize`, `cmap`, `alpha`, and `grid`) to make your visualizations more informative and visually appealing. Reviewing the Golden Answer for Task 5 thoroughly will be beneficial for understanding these nuances.
