# Grading Feedback: Lilith

**Total Score: 71/100**

## Task Breakdown
### Task 1
- **Score:** 18/20
- **Feedback:** Correct logic for calculating the percentile. You used dropna and np.percentile, which is valid, though np.nanpercentile is more direct and avoids creating an extra dataframe.

### Task 2
- **Score:** 15/20
- **Feedback:** The logic is correct, but the task asked for the results to be assigned back to the dataframe as a new column and to display specific columns, whereas you just printed the numpy array.

### Task 3
- **Score:** 18/20
- **Feedback:** Correct logic. While your implementation is slightly more verbose than necessary, the filtering is accurate.

### Task 4
- **Score:** 15/20
- **Feedback:** The calculation is correct, but you missed the requirement to sort the values in descending order as requested in the instructions.

### Task 5
- **Score:** 5/20
- **Feedback:** Significant errors: You did not clean the 'GDP ($ per capita)' column before plotting (it contains commas as strings), causing the plot to fail or produce errors. The annotation for 'China' uses incorrect hardcoded coordinates (1, 1) instead of fetching China's actual location data.

## Overall Feedback
Overall, you have a solid grasp of basic Pandas and NumPy operations. You lost points primarily in Task 5 due to data cleaning issues and incorrect annotation logic. Remember to ensure all columns used in visualization are correctly converted to numeric types and to use the dataframe to dynamically locate points for annotations.
