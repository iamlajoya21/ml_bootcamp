# Grading Report for Student Submission

## Question-by-Question Assessment

### Problem 1: The Secure Inventory Audit
*   **Score: 3/10**
*   **Feedback:**
    *   **Positive:** You correctly opened both files and handled `FileNotFoundError` (though the message was for `raw_data.txt` instead of `inventory.txt`). You also correctly caught `ValueError` when converting quantity to an integer and wrote the problematic line to `audit_errors.log`.
    *   **Areas for Improvement:**
        *   **Normalization:** The method `uppercase()` is incorrect; it should be `upper()`. This would cause a `AttributeError`.
        *   **Aggregation:** Your code `final_result[item]=num` *overwrites* the quantity for an item if it appears multiple times. The requirement was to *sum* the quantities for repeated items. You need to check if the item already exists in `final_result` and add to its current value.
        *   **Error Message:** `print(f"the errors {audit}")` prints the file object itself, not the content or a useful error message.
        *   **FileNotFoundError Message:** The error message `Could not find raw_data.txt` should refer to `inventory.txt`.
        *   **Unused Variables:** `repeat` and `qunatity` (typo for quantity) were declared but not used.

### Problem 2: The Login Security Monitor
*   **Score: 8/10**
*   **Feedback:**
    *   **Positive:** You successfully filtered out blacklisted IPs and used a `set` to deduplicate the logins, which is an excellent approach. You also correctly wrote the unique, safe IPs to `authorized_logins.txt`, one per line.
    *   **Areas for Improvement:**
        *   **Data Structure:** The problem explicitly asked to "Store: Save the safe, unique IPs into a Tuple." Your final `final` variable is a `set`. To meet the requirement, you would need to convert the set to a tuple (e.g., `safe_ips_tuple = tuple(final)`).

### Problem 3: The "Strict" Transaction Processor
*   **Score: 4/10**
*   **Feedback:**
    *   **Positive:** You correctly implemented the `while True` loop and the "exit" condition. The `finally` block also correctly prints "System: Monitoring active." after every attempt.
    *   **Areas for Improvement:**
        *   **Type Mismatch in Comparisons:** Inside the `try` block, after converting `n` to `amount = int(n)`, you then use `if n > 5000:` and `if n <= 0:`. Here, `n` is still a string. You should be comparing the integer `amount` (e.g., `if amount > 5000:`). This would either lead to a `TypeError` or incorrect logical evaluation.
        *   **Generic Error Handling:** Your `except ValueError:` block catches *all* `ValueError`s, including the specific ones you manually `raise` (e.g., "High Value: Requires Approval", "Invalid Amount"). This means the user will always see "invalid data type" instead of the specific, descriptive error messages you intended to raise. To fix this, you could catch the specific `ValueError`s by their messages or structure your `try-except` blocks differently to print the raised exception's message.

### Problem 4: The Global Gradebook Merger
*   **Score: 10/10**
*   **Feedback:**
    *   **Positive:** This solution is excellent! You correctly identified all unique student names and then iterated through them, using `extend()` to combine all grades from both semesters into a single list for each student. This perfectly meets the requirement of not overwriting data and aggregating all grades. The logic is clear and effective.

## Overall Feedback
You've demonstrated a solid foundational understanding of Python, especially with data structures like dictionaries, lists, and sets, as evidenced by your strong performance in Problem 4 and Problem 2. Your ability to handle file I/O and basic error catching is also present.

To further improve, pay close attention to:
1.  **Method Names and Syntax:** Double-check method names (e.g., `upper()` vs. `uppercase()`).
2.  **Variable Types:** Be mindful of variable types, especially after type conversions (e.g., using `amount` (int) for comparisons after converting from `n` (str)).
3.  **Specific Requirements:** Ensure all parts of the prompt are met, including specific data types for output (e.g., a tuple instead of a set).
4.  **Error Handling Flow:** Understand how `try-except` blocks interact with `raise` statements to ensure the intended error messages are displayed to the user.

Keep practicing these concepts, and you'll continue to grow your programming skills!

**FINAL SCORE: 63/100**