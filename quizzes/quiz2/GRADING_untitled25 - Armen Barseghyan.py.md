# Grading Feedback: Armen Barseghyan

**Total Score: 58/100**

## Task Breakdown
### Task 1
- **Score:** 19/20
- **Feedback:** Your implementation correctly calculates the 10th percentile for infant mortality. You correctly handled the comma-to-dot conversion and used `.dropna()` to manage missing values, which is an effective alternative to `np.nanpercentile`. A minor point: the golden answer included a more descriptive print statement with formatting. Excellent work overall for this task.

### Task 2
- **Score:** 19/20
- **Feedback:** You successfully applied `np.where` to create the 'Birth_Category' column based on the birthrate condition. The cleaning of the 'Birthrate' column was also correctly performed. Similar to Task 1, the golden answer included an explicit print of sample rows with a descriptive message, whereas your submission just shows `df`. For future quizzes, ensure output clarity as requested.

### Task 3
- **Score:** 10/20
- **Feedback:** You correctly applied the multi-condition filtering syntax using boolean indexing and the `&` operator, and you properly cleaned the 'Phones (per 1000)' column. However, a crucial data cleaning step was missed: stripping whitespace from the 'Region' column (`df['Region'].str.strip()`). Without this, regions with leading or trailing spaces (e.g., ' SUB-SAHARAN AFRICA') will not be correctly matched, leading to an incomplete or incorrect filtered dataset. This omission significantly impacts the accuracy of the result.

### Task 4
- **Score:** 10/20
- **Feedback:** You correctly performed the `groupby()` operation to calculate the mean 'Service' for each 'Region', and the 'Service' column was properly cleaned. However, there are two deductions: 
1. Similar to Task 3, you missed stripping whitespace from the 'Region' column. This will cause regions with differing whitespace to be treated as separate groups, leading to incorrect aggregation results.
2. You did not sort the results as shown in the golden answer, which typically improves readability and insights from aggregated data. The omission of the `strip()` method for 'Region' is the more significant issue here, impacting data integrity.

### Task 5
- **Score:** 0/20
- **Feedback:** This task was not attempted. No code related to Matplotlib visualization or annotation was found in your submission.

## Overall Feedback
Armen, your submission demonstrates a solid understanding of basic NumPy and Pandas operations for Tasks 1 and 2, including correct data type conversion and handling of missing values. Your syntax for filtering and grouping (Tasks 3 and 4) is also correct. 

However, a recurring and critical issue in your submission is the lack of comprehensive data cleaning, particularly for string columns like 'Region'. The golden answers included a centralized cleaning step to strip whitespace from 'Region' and 'Country' and convert relevant columns to numeric types *once* at the beginning. Your approach of cleaning columns just before their specific task is less efficient and led to the omission of the essential `str.strip()` for 'Region' in Tasks 3 and 4. This omission means your filtered and grouped results for those tasks would likely be incorrect due to unmatched or incorrectly grouped categories. Always remember that thoroughly cleaning your data, especially for categorical and numerical columns, is paramount for accurate analysis.

Finally, Task 5 was completely omitted. For future quizzes, please ensure all tasks are attempted. Focus on reinforcing your data cleaning practices, especially whitespace management in string columns, and aim for a more centralized cleaning approach.
