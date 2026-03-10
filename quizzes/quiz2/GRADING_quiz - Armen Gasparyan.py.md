# Grading Feedback: Armen Gasparyan

**Total Score: 45/100**

## Task Breakdown
### Task 1
- **Score:** 10/20
- **Feedback:** Armen correctly identified how to calculate the 10th percentile for 'Infant mortality' and handled missing values using `.dropna()` before `np.percentile()`. While effective, `np.nanpercentile()` is generally more direct for this purpose. The primary deduction is for not assigning the result to a variable and not printing the calculated value, making the code's output unclear and the result inaccessible for further use.

### Task 2
- **Score:** 15/20
- **Feedback:** The implementation for creating the 'Birth_Category' column using `np.where()` is correct and follows best practices. The logic for categorizing 'High' or 'Normal' based on a birthrate greater than 30 is also accurate. The only deduction is for not explicitly showing a sample of the updated DataFrame (e.g., using `.head()`) to confirm the new column's creation and its values in the output.

### Task 3
- **Score:** 10/20
- **Feedback:** Armen correctly applied multi-condition filtering using Pandas to select countries in 'SUB-SAHARAN AFRICA' with 'Phones (per 1000)' greater than 100. The use of parentheses and the `&` operator is correct. However, similar to Task 1 and 4, the filtered DataFrame is not assigned to a variable, nor is any output (like the number of filtered countries or a sample of the DataFrame) printed, making the code's effect unclear without manual inspection.

### Task 4
- **Score:** 10/20
- **Feedback:** The grouping by 'Region' and aggregation to calculate the mean of the 'Service' sector is correctly implemented using `.groupby()` and `.agg('mean')`. This achieves the desired statistical analysis. The main deductions are for not assigning the resulting Series to a variable and not printing the output. Adding `.sort_values(ascending=False)` would also improve readability, as shown in the golden answer, but this was not a major deduction point.

### Task 5
- **Score:** 0/20
- **Feedback:** This task has several critical issues:
1.  **Data Cleaning Omission:** The student's `cols_to_fix` list in the data setup did not include `'GDP ($ per capita)'`. This is crucial because `GDP` is used for color mapping (`c=df['GDP ($ per capita)']`) in the scatter plot. Without converting it to a numeric type, the `scatter` function will likely fail or produce an incorrect visualization.
2.  **Brittle Annotation:** Annotating China using a hardcoded index (`df['Area (sq. mi.)'][42]`) is extremely brittle and bad practice. If the data's order changes, this will point to the wrong country. The golden answer demonstrates a robust method by filtering for the country name.
3.  **Missing Plot Elements:** The plot is missing a descriptive `title` and a proper `colorbar` label (it just calls `plt.colorbar()` without linking to the `scatter` object). Crucially, `plt.show()` is missing, meaning the plot would not display in a non-interactive environment.
4.  **Incomplete Annotation Details:** The annotation lacks important parameters like `xytext`, `arrowprops`, and `fontweight` to make it clear and professional.

These issues significantly detract from the quality and functionality of the visualization, leading to a score of 0 for this task.

## Overall Feedback
Armen demonstrates a foundational understanding of NumPy, Pandas, and Matplotlib operations as requested in the quiz. The core logic for tasks 1, 2, 3, and 4 is mostly correct. However, a consistent and significant area for improvement across Tasks 1-4 is the lack of storing results in variables and displaying meaningful output (e.g., using `print()` or `.head()`). In a professional or educational setting, code should clearly communicate its results. For Task 5, the Matplotlib visualization, there are critical issues related to data preparation (not converting GDP to numeric), a brittle approach to data annotation (hardcoded index), and several missing essential plot elements (title, proper colorbar, `plt.show()`). Armen needs to pay closer attention to data cleaning prerequisites for visualizations and robust, dynamic ways to interact with data, rather than relying on fixed indices. Focusing on clear output and thoroughness in plotting will greatly enhance his Python and Data Science skills.
