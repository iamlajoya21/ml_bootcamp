# Grading Feedback: Mels Tadevosyan

**Total Score: 0/100**

## Task Breakdown
### Task 1
- **Score:** 0/20
- **Feedback:** Your code for Task 1 is commented out, which means it cannot be executed or graded. Additionally, the data setup in your submission is missing a crucial data cleaning step (converting comma-decimals to float and stripping spaces) which would cause this numerical operation to fail if uncommented due to 'Infant mortality (per 1000 births)' likely being an object (string) type. Ensure all code is uncommented for submission and that data types are correct before performing numerical operations.

### Task 2
- **Score:** 0/20
- **Feedback:** Your code for Task 2 is commented out, preventing it from being graded. Similar to Task 1, without the proper data cleaning from the Golden Answers, the 'Birthrate' column would likely remain a string type, leading to an error when attempting the numerical comparison `df['Birthrate']>30` if the code were uncommented. Remember to ensure data is in the correct format (e.g., float) for numerical comparisons and computations.

### Task 3
- **Score:** 0/20
- **Feedback:** Your code for Task 3 is commented out, so it cannot be evaluated. If uncommented, this task would likely fail. First, the 'Region' column might contain leading/trailing whitespace (which the Golden Answer addresses with `.str.strip()`), preventing exact matches like `== 'SUB-SAHARAN AFRICA'`. Second, the 'Phones (per 1000)' column would likely be an object/string type without the necessary data cleaning, causing the numerical comparison `> 100` to fail.

### Task 4
- **Score:** 0/20
- **Feedback:** Your code for Task 4 is commented out, thus it cannot be graded. If uncommented, it would likely fail because the 'Service' column, without the data cleaning step, would be of string type due to comma-decimals. Attempting to calculate a `.mean()` on a string column will raise an error. The golden answer also included `.sort_values(ascending=False)` which was a minor omission, but the primary issue is the data type and the commented-out code.

### Task 5
- **Score:** 0/20
- **Feedback:** While your code for Task 5 is not commented out, it contains critical issues that prevent it from functioning correctly and fulfilling the requirements:
1.  **Data Type Error (Critical):** The most severe issue is the complete absence of data cleaning from the data setup. Columns like 'Area (sq. mi.)', 'Population', and 'GDP ($ per capita)' would still be string/object types due to comma-decimals. This means your `plt.scatter`, `plt.xscale('log')`, `plt.yscale('log')`, and `plt.colorbar` calls would all crash, as they expect numerical input.
2.  **Incorrect Annotation Logic (Severe):** You attempted to annotate 'China' by locating the *maximum* `Area` and `Population` in the entire dataset (`df['Area (sq. mi.)'].max()` and `df['Population'].max()`). This is incorrect; the requirement was to annotate the specific point corresponding to 'China' itself. This fundamentally misunderstands the annotation task.
3.  **Missing Features:** You omitted `plt.figure(figsize=(...))` for controlling plot size and `plt.grid(True)` for better readability, which were present in the Golden Answer. The `alpha` and `edgecolors` parameters for `plt.scatter` were also missing.

## Overall Feedback
Mels, your submission demonstrates a significant misunderstanding of the workflow required for data analysis tasks, particularly in the initial data preparation phase. The most critical issue across all tasks is the complete lack of data cleaning. Real-world datasets often have formatting inconsistencies (like comma-decimals) that must be addressed (e.g., replacing commas with periods and converting to numeric types) before any numerical operations (percentiles, comparisons, means, plotting) can be performed. Without this foundational step, almost all your subsequent code would fail.

Secondly, for Tasks 1-4, your code was entirely commented out. Code that is commented out cannot be executed or graded, resulting in zero points for those sections. For future submissions, please ensure your solutions are uncommented and fully functional.

Finally, even in Task 5, where the code was uncommented, it would crash due to the data cleaning issue, and the logic for annotating 'China' was incorrect, pointing to the maximum values in the dataset rather than China's specific coordinates.

To improve, please focus on:
1.  **Thorough Data Cleaning:** Understand that data often needs preparation before analysis. Always check data types (`df.info()`) and perform necessary conversions.
2.  **Uncommenting Code:** Ensure your solutions are executable.
3.  **Understanding Specific Requirements:** Pay close attention to the exact details of what needs to be calculated or visualized (e.g., annotating a specific country vs. the max point).
