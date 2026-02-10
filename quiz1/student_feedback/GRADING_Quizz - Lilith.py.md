# Grading Report for Student Submission

## Question-by-Question Assessment

### Problem 1: The Secure Inventory Audit
*   **Score: 0/10**
*   **Feedback:**
    *   **Positive:** You correctly opened both `inventory.txt` and `audit_errors.log` and used `strip()` and `upper()` for initial processing.
    *   **Areas for Improvement:**
        *   **Quantity Parsing:** The most significant issue is that you never parse the quantity as an integer. The `split_line` will contain `['ITEM_NAME', 'QUANTITY_STRING']`. You need to convert `QUANTITY_STRING` to an `int`.
        *   **Aggregation Logic:** Your loop `for item in split_line:` iterates over both the item name and the quantity string. The logic `res[item] = item` and `res[item] += 1` is incorrect. It attempts to store the item name as its own value and then increment a string, which would lead to a `TypeError`, not a `ValueError`. The goal was to sum quantities.
        *   **Error Handling:** The `try-except ValueError` block is syntactically incorrect (indentation) and would not catch the `TypeError` that your current aggregation logic would produce. Even if it were correct, the `ValueError` for non-integer quantities needs to be caught when attempting `int(quantity_string)`.
        *   **Expected Output:** Your current code would not produce the expected dictionary of item names and their total quantities.

### Problem 2: The Login Security Monitor
*   **Score: 7/10**
*   **Feedback:**
    *   **Positive:**
        *   You successfully filtered out blacklisted IPs from `all_logins`.
        *   You correctly used a `set` to deduplicate the IPs.
        *   You correctly converted the unique IPs into a `tuple`.
        *   Printing the `safe_uniqu` tuple to the console works as expected.
    *   **Areas for Improvement:**
        *   **File Writing Error:** Inside the `with open(...)` block, you used `file.write(ip + "\n")` instead of `err_file.write(ip + "\n")`. The variable name for the file object is `err_file`, not `file`. This would cause a `NameError` and prevent the program from writing to the file.
        *   **Filename Typo:** The problem asked to write to `authorized_logins.txt` (plural), but you used `authorized_login.txt` (singular). This is a minor detail but important for exact requirements.

### Problem 3: The "Strict" Transaction Processor
*   **Score: 2/10**
*   **Feedback:**
    *   **Positive:** You correctly implemented the `while True` loop and the `break` condition when the user types "exit".
    *   **Areas for Improvement:**
        *   **Input Type Conversion:** The `input()` function always returns a string. You attempted to compare this string directly with integers (`amount > 5000`, `amount <= 0`), which will raise a `TypeError` in Python 3, not a `ValueError`. You need to convert `amount` to an `int` or `float` *inside* the `try` block.
        *   **Specific Error Handling:**
            *   The `except:` block is a bare except, which catches all errors and is generally bad practice. It should specifically catch `ValueError` after attempting to convert the input to a number.
            *   Instead of printing an empty line (`print()`), you should print the specific error messages required by the problem (e.g., "Invalid Data Type", or the message from the raised `ValueError`).
        *   **`finally` Block:** The `finally` block should print "System: Monitoring active.", but you currently have `print()`, which prints an empty line.
        *   **Raised `ValueError` Messages:**
            *   Typo in "High Value Reuires approval" (should be "Requires").
            *   The message for `amount <= 0` is "Invalid", but the requirement was "Invalid Amount".
        *   **Minor Syntax:** Missing a closing quote in the `input()` prompt string.

### Problem 4: The Global Gradebook Merger
*   **Score: 0/10**
*   **Feedback:** No code was submitted for this problem.

## Overall Feedback

You've made a good start on understanding some core Python concepts, especially with basic file I/O, list manipulation, and the use of sets and tuples.

However, there are critical areas that need more attention:
1.  **Data Type Conversion:** This was a major stumbling block in Problems 1 and 3. Always remember that `input()` returns a string, and data read from files often needs explicit conversion (e.g., `int()`, `float()`) before numerical operations can be performed.
2.  **Precise Error Handling:** While you attempted `try-except` blocks, understanding *which* errors to catch and *where* they occur is crucial. Also, ensure your `except` and `finally` blocks perform the exact actions specified in the problem. Avoid bare `except` blocks.
3.  **Attention to Detail:** Small typos (like variable names in file writing, or specific error messages) can prevent code from running or meeting exact requirements.

I encourage you to review the concepts of data type conversion, `try-except-finally` blocks, and dictionary manipulation. Practice writing small, focused code snippets for each of these areas. Keep up the effort!

**FINAL SCORE: 23/100**