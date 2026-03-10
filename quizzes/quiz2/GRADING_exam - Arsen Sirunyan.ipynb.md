# Grading Feedback: Arsen Sirunyan

**Total Score: 52/100**

## Task Breakdown
### Task 1
- **Score:** 0/20
- **Feedback:** The task required calculating the 10th percentile of 'Infant mortality'. Your code `new_df["Infant mortality (per 1000 births)"].iloc[10]` attempts to access the element at index 10, which is a single value, not a percentile calculation. You should use `np.nanpercentile()` to correctly calculate percentiles, especially when dealing with potential missing values (NaNs).

### Task 2
- **Score:** 20/20
- **Feedback:** You correctly implemented the conditional labeling using `np.where()` to create the 'Birth_Category' column based on the 'Birthrate'. This is an excellent use of NumPy for vectorized operations.

### Task 3
- **Score:** 20/20
- **Feedback:** You successfully filtered the DataFrame using multiple conditions for 'Region' and 'Phones (per 1000)'. Your use of `loc` and the `&` operator for combining conditions is correct and efficient.

### Task 4
- **Score:** 12/20
- **Feedback:** You correctly performed the `groupby` operation on 'Region' and calculated the `mean()` of the 'Service' column. However, you missed two parts of the golden answer:
1.  **Sorting:** The result was expected to be sorted by the mean service sector in descending order (`.sort_values(ascending=False)`).
2.  **Display/Assignment:** While the mean is calculated, the result is not assigned to a variable or explicitly printed, so it would not be displayed in a script environment. Remember to assign the result or `print()` it if you want to see the output.

### Task 5
- **Score:** 0/20
- **Feedback:** This task had several critical issues that prevented it from fully working as intended:
1.  **Data Cleaning (`GDP ($ per capita)`):** You did not include 'GDP ($ per capita)' in your initial `cols_to_fix` list. This means the GDP column likely remained as strings with commas (e.g., '1,200'), which can cause `plt.scatter` to either fail or silently coerce values, leading to unexpected behavior.
2.  **Data Cleaning (`Country` Column):** You did not strip leading/trailing spaces from the 'Country' column. As a result, when trying to find 'China' with `df[df["Country"] == "China "]`, the trailing space in your query meant no match was found. This caused your `china` DataFrame to be empty, leading to an `IndexError` when trying to access `china_x` and `china_y`. The annotation feature failed completely because of this fundamental data preparation oversight, causing the script to crash.
3.  **Visualization Details:** You missed several details from the golden answer's scatter plot and overall visualization, including `cmap='viridis'`, `alpha`, `edgecolors='white'` for the scatter plot, a descriptive `plt.title()`, and `plt.grid()`.
4.  **Annotation Details:** While you attempted to annotate 'China', in addition to the crash caused by the empty `china` DataFrame, you also missed `xytext`, `textcoords`, `fontsize`, and `fontweight` parameters for better placement and styling of the annotation text and arrow.

To improve, focus on robust data cleaning at the beginning, as it directly impacts later analysis and visualization steps. Ensure all relevant columns are in the correct data types and formats, and pay attention to specific details in plotting requirements.

## Overall Feedback
Arsen, your submission demonstrates a solid understanding of fundamental Pandas operations for multi-condition filtering and basic NumPy for conditional labeling. These tasks were implemented correctly and efficiently.

However, there are significant areas for improvement, particularly in data preparation and attention to detail for more complex tasks like NumPy percentiles and Matplotlib visualizations. The complete failure to calculate percentiles in Task 1 and the critical errors in data cleaning (missing GDP conversion, unstripped 'Country' column) that led to an `IndexError` and prevented Task 5's annotation from running are major deductions. Additionally, consistently ensure that the final results of calculations are either assigned to variables or explicitly printed to be visible in a script's output.

Moving forward, focus on:
1.  **Understanding the Core Task:** For Task 1, ensure you understand the difference between accessing an element by index and calculating a statistical measure like a percentile.
2.  **Thorough Data Cleaning:** Before performing analysis or visualization, meticulously check all relevant columns for data types and format issues (like leading/trailing spaces, commas in numbers). This is a foundational step that impacts everything downstream.
3.  **Attention to Detail:** Pay close attention to all specified requirements in a task, from sorting aggregated results to specific plot customization parameters (cmap, alpha, titles, grids, detailed annotations).

Keep practicing these concepts, and you will see significant improvement in your data science skills!
