# Grading Report for Student Submission

## Question-by-Question Assessment

### Problem 1: The Secure Inventory Audit
**Score: 9/10**

**Feedback:**
The student's code for Problem 1 is very well-structured and robust.
*   **File I/O:** Correctly uses `with open(...)` for both input and error log files.
*   **Normalization:** Successfully converts item names to uppercase (`item.upper()`).
*   **Aggregation:** Correctly sums quantities for repeated items (`inventory[item] += qty`).
*   **Error Handling:** The `try-except (ValueError, IndexError)` block is comprehensive. It correctly catches `ValueError` for non-integer quantities (from `int(qty)`) and for the manually raised "Invalid format" error. It also correctly catches `IndexError` which could occur if `split` doesn't produce enough parts (e.g., a line like "apple,").
*   **Logging Errors:** Corrupted lines are correctly written to `audit_errors.log`.
*   **Delimiter Handling:** The code correctly handles both comma and colon delimiters.

The only minor deduction is for the final output dictionary not matching the *specific* "Expected Result" provided in the problem description (`{'APPLE': 30, 'CHERRY': 7, 'BANANA': 12}`). While your code logic is sound and would produce the correct output for a given `inventory.txt`, the problem implicitly defined the `inventory.txt` content by providing that specific expected result. It's likely you used a slightly different `inventory.txt` for testing.

### Problem 2: The Login Security Monitor
**Score: 10/10**

**Feedback:**
Excellent solution for Problem 2!
*   **Filtering:** You correctly filter out blacklisted IPs. The use of `all_logins[:]` to iterate over a copy while modifying the original list is a good practice to avoid runtime errors.
*   **Deduplication:** Using `set(all_logins)` effectively deduplicates the IPs.
*   **Storing:** The `tuple(...)` conversion correctly stores the unique, safe IPs in a tuple.
*   **Writing to File:** The `authorized_logins.txt` file is correctly opened and each IP is written on a new line.
*   The final printed tuple matches the expected elements (order may vary due to set conversion, which is acceptable).

All requirements were met perfectly.

### Problem 3: The "Strict" Transaction Processor
**Score: 10/10**

**Feedback:**
Another excellent solution!
*   **Loop and Exit:** The `while True` loop with the 'exit' condition is implemented correctly.
*   **Validation:**
    *   Non-numeric input is correctly caught by `int(user_input)` raising a `ValueError`, and your `except` block correctly prints "Invalid Data Type".
    *   Amounts greater than 5000 correctly raise a `ValueError` with the specified message.
    *   Amounts 0 or less correctly raise a `ValueError` with the specified message.
*   **Error Message Handling:** Your `except ValueError as e:` block intelligently checks the error message to differentiate between the custom-raised errors and the generic `int()` conversion error, printing the appropriate message.
*   **Finally Block:** The `finally` block correctly ensures "System: Monitoring active." is printed after every attempt, regardless of success or failure.

This solution demonstrates a strong understanding of error handling and control flow.

### Problem 4: The Global Gradebook Merger
**Score: 4/10**

**Feedback:**
The approach taken for Problem 4 has a significant flaw in its iteration strategy.
*   **Correct Logic for Overlapping Students:** For students present in *both* `semester_1` and `semester_2` (e.g., Alice, Bob, Charlie), your code correctly merges their grades using `+` to concatenate the lists.
*   **Correct Logic for Students Only in Semester 1:** For students only in `semester_1` (e.g., David, Eve), your code correctly adds them to the `students` dictionary.

*   **Major Flaw: Iteration Strategy:** The use of `for child, grades in zip(semester_1, semester_2):` is incorrect for merging dictionaries in this manner. `zip` pairs keys from the two dictionaries based on their iteration order, and it stops as soon as the shorter dictionary's keys are exhausted. This means that any students present *only* in `semester_2` but not in `semester_1` (e.g., Frank, Grace, Heidi) are completely missed by your loop and are not included in the final `students` dictionary. The `grades` variable in your loop also incorrectly receives the *key* from `semester_2` rather than a list of grades, though this doesn't cause a direct error in your `if/elif` logic because you're using `child` to access the dictionaries.

To correctly merge, you need to iterate over all unique student names from *both* semesters. A common approach is to iterate through one dictionary, adding or extending grades, and then iterate through the second dictionary, doing the same.

## Overall Feedback

You've demonstrated a strong grasp of Python fundamentals, especially in file I/O, error handling, and list/set manipulations. Problems 2 and 3 were solved perfectly, showcasing excellent understanding of the requirements and best practices. Your solution for Problem 1 was also very good, with robust error handling, even if the final output didn't match the specific example due to what appears to be an input file discrepancy.

The main area for improvement is in Problem 4, where the dictionary merging logic using `zip` was not suitable for the task of combining all unique keys from two dictionaries. This is a common pitfall when working with dictionary iteration. Focus on ensuring your iteration strategy covers all necessary data points when merging collections.

Keep up the great work! Your code is generally clean, readable, and effective.

**FINAL SCORE: 83/100**