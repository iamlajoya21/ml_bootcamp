# Grading Feedback: Nona Zakoyan

**Total Score: 82/100**

## Task Breakdown
### Task 1
- **Score:** 20/20
- **Feedback:** Excellent work. Using `.dropna()` before `np.percentile` is a correct and effective way to handle missing values, achieving the same result as `np.nanpercentile`.

### Task 2
- **Score:** 20/20
- **Feedback:** Perfectly implemented! The use of `np.where` for conditional labeling is precise and efficient.

### Task 3
- **Score:** 18/20
- **Feedback:** Good job on filtering with multiple conditions. The logic `(df['Region'].str.strip() == "SUB-SAHARAN AFRICA") & (df['Phones (per 1000)'] > 100)` is correct. While `.str.strip()` on 'Region' was redundant due to prior cleaning, it ensures robustness. The golden answer printed the *count* of filtered items, but printing the DataFrame is also informative and the filtering logic itself is sound.

### Task 4
- **Score:** 19/20
- **Feedback:** The core aggregation is correct; you successfully grouped by 'Region' and calculated the mean 'Service'. To match the golden standard, you could have added `.sort_values(ascending=False)` to present the results in a sorted order, which is often helpful for analysis.

### Task 5
- **Score:** 5/20
- **Feedback:** This task has several areas for improvement. 
1.  **Critical Data Cleaning Miss:** The most significant issue is that the 'GDP ($ per capita)' column was not converted to a float type during the initial data cleaning, unlike the golden answer. While the plot might render if the column doesn't contain problematic characters, `c` in `plt.scatter` is intended for numerical values to map to a colormap. Failing to convert this data to a proper numerical type (float) means the visualization's coloring is not based on correctly processed numerical data. 
2.  **Missing Plot Elements:** You correctly used log scales and positioned the annotation for China. However, the plot lacks a title (`plt.title()`) and the colorbar is missing a descriptive label (`label='GDP ($ per capita)'`). 
3.  **Annotation Styling:** While 'China' is correctly annotated, the golden answer included more specific styling for the annotation (e.g., `xytext`, `textcoords`, `fontsize`, `fontweight`) to improve its readability and placement relative to the point. 
4.  **Missing Grid:** A minor point, but adding `plt.grid(True)` can enhance readability for plots with log scales. 
Focus on thorough data preparation and comprehensive plot labeling for future visualizations.

## Overall Feedback
Nona, you've demonstrated a strong understanding of NumPy and Pandas for data manipulation and aggregation, with excellent implementations for Tasks 1, 2, 3, and 4. Your logical approach to filtering and grouping is commendable.

The main area for improvement lies in data preparation for visualization and the completeness of plotting elements. For Task 5, remember that all data used in a visualization, especially for numerical mapping (like `c` for color), must be in the correct numerical data type. Additionally, ensure your plots include all necessary labels, titles, and potentially annotations with clear styling to make them fully informative and professional. Keep practicing your Matplotlib skills, particularly the details of data preparation and plot customization!
