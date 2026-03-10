# Grading Feedback: Areg Ayvazyan

**Total Score: 93/100**

## Task Breakdown
### Task 1
- **Score:** 20/20
- **Feedback:** Correctly uses `np.nanpercentile` to calculate the 10th percentile for infant mortality, demonstrating proper NumPy function usage and handling of NaN values.

### Task 2
- **Score:** 20/20
- **Feedback:** Excellent application of `np.where` for conditional labeling. The logic for categorizing birth rates into 'High' or 'Normal' is accurate. Creating a copy of the DataFrame (`df.copy()`) is good practice for explicit data manipulation, even if not strictly necessary in this specific case for the original DataFrame.

### Task 3
- **Score:** 20/20
- **Feedback:** Flawless execution of multi-condition filtering using Pandas. The conditions for 'Region' and 'Phones (per 1000)' are combined correctly with the logical AND operator (`&`), effectively selecting the desired subset of data.

### Task 4
- **Score:** 18/20
- **Feedback:** The grouped aggregation is correctly performed using `groupby('Region').agg(economic_secrtor=('Service', 'mean'))`. This is a valid and often preferred way to name aggregated columns. However, the golden answer also included sorting the results by the mean service value in descending order, which was omitted in this submission. Adding `.sort_values(ascending=False)` would have made the output fully match the expected result.

### Task 5
- **Score:** 15/20
- **Feedback:** The core visualization and annotation are implemented correctly:
- The scatter plot shows Area vs. Population, colored by GDP ($ per capita).
- Log scales are correctly applied to both axes.
- Labels, title, and a colorbar are included.
- Annotation for 'China' is correctly positioned and pointed to.

Deductions are for:
- **Missing aesthetic enhancements (2 points):** The scatter plot lacks `cmap`, `alpha`, and `edgecolors`, which improve visual clarity. The colorbar linking (`plt.colorbar(scatter, ...)`) was also omitted, though `plt.colorbar()` works implicitly.
- **Missing annotation styling (2 points):** The annotation for 'China' misses specific styling for the arrow (`color`, `lw`) and text (`fontsize`, `fontweight`), making it less prominent than in the golden answer.
- **Suboptimal data cleaning practice (1 point):** While the annotation for 'China ' (with a trailing space) worked for the raw data, it's a best practice to strip whitespace from all string columns (e.g., `df['Country'].str.strip()`) during initial cleaning to ensure robust matching across varying data inputs. This was missed in the initial data setup.

## Overall Feedback
Areg demonstrated a very strong understanding of the core concepts in NumPy, Pandas, and Matplotlib. Tasks 1, 2, and 3 were perfectly executed, showcasing excellent command of fundamental data manipulation techniques. Task 4 was nearly perfect, only missing an additional sorting step. Task 5 achieved all fundamental visualization requirements, but could benefit from more attention to aesthetic details and robust data cleaning practices for text columns. Overall, this is an excellent submission, and with minor refinements, Areg's work would be production-ready.
