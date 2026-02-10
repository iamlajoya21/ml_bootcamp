# Grading Report for Student Submission

## Question-by-Question Assessment

### Problem 1: The Secure Inventory Audit
**Score: 5/10**

**Feedback:**
The student demonstrated a good understanding of file I/O, error handling, and the concept of normalization (uppercasing item names). The `try-except` block correctly catches `ValueError` when `int()` conversion fails and logs the full line to `audit_error.log` in append mode, which is excellent.

However, there's a critical logical flaw in the aggregation step. The code only adds quantities for items *already present* in the `inventory` dictionary (`if item.upper() in inventory.keys():`). If an item is encountered for the first time, it is completely skipped and not added to the `inventory` dictionary. This means the final `inventory` will be incomplete.

**Example of missing logic:**
```python
# ... inside the loop ...
if item.upper() in inventory.keys():
    inventory[item.upper()] += quantity
else: # This 'else' block is missing in the student's code
    inventory[item.upper()] = quantity # This line is crucial for new items
```

### Problem 2: The Login Security Monitor
**Score: 9/10**

**Feedback:**
This solution is very well-executed.
*   **Deduplication:** Converting `all_logins` to a `set` (`Secure_IPs`) is an efficient and correct way to deduplicate the IP addresses.
*   **Filtering:** Iterating through `blacklisted_ips` and removing them from `Secure_IPs` is a clear and effective filtering mechanism.
*   **Storing:** Converting the final set to a `tuple` (`safe_ips`) correctly meets the storage requirement.
*   **Writing:** The IPs are correctly written to `authorized_logins.txt`, one per line.

The only minor point is that the file is opened in append mode (`'a'`). While not explicitly stated to overwrite, for a "log" of authorized logins, typically a fresh file is created each time (`'w'`) to reflect the current state. Using `'a'` would append to previous runs, which might not be the intended behavior. This is a minor detail and doesn't detract significantly from the core logic.

### Problem 3: The "Strict" Transaction Processor
**Score: 6/10**

**Feedback:**
The student correctly implemented the `while True` loop and the `break` condition for "exit". The use of `try-except-finally` is also structurally correct.
*   **Manual Raises:** The `ValueError`s for amounts `> 5000` and `<= 0` are correctly raised with the specified messages.
*   **Finally Block:** The `finally` block correctly prints "System: Monitoring active." after every attempt.

However, there are a few issues:
1.  **Stray Code:** There's a stray `5` on a line by itself after the `if transaction_amount == 'exit': break` statement. This would cause a syntax error.
2.  **Error Handling for Invalid Data Type:** The `except ValueError` block's conditional logic (`if 'High values...' in e.args or 'Invalid amount' in e.args:`) is overly complex and brittle.
    *   If the `int(transaction_amount)` conversion fails (e.g., user types "hello"), the `else` branch is taken, printing `'Invalid Input Type10'`. The problem asked for "Invalid Data Type", and the "10" is a typo.
    *   A more robust approach for handling the `int()` conversion error would be to simply print "Invalid Data Type" in the `else` block, without trying to parse the error message arguments.

### Problem 4: The Global Gradebook Merger
**Score: 10/10**

**Feedback:**
This solution is excellent and perfectly meets all requirements.
*   **Identifying all students:** The use of `set.union()` to get all unique student names from both semesters is a very clean and efficient approach.
*   **Merging Logic:** The conditional checks (`if name in semester_1 and name in semester_2`, `elif name in semester_1`, `else`) correctly handle all scenarios.
*   **Concatenation:** For students present in both semesters, `semester_1[name] + semester_2[name]` correctly concatenates their grade lists, ensuring no data is overwritten and all grades are included.

This is a robust and well-thought-out solution.

## Overall Feedback
The student demonstrates a solid foundational understanding of Python programming concepts, including file I/O, error handling, data structures (sets, tuples, dictionaries), and control flow.

**Strengths:**
*   Excellent use of sets for deduplication and union operations (Problems 2 and 4).
*   Strong grasp of `try-except-finally` blocks for error handling (Problems 1 and 3).
*   Effective dictionary manipulation for merging and aggregation (Problems 1 and 4).
*   Clear and readable code structure.

**Areas for Improvement:**
*   **Attention to Detail:** Minor issues like the missing logic for new items in Problem 1, the file write mode in Problem 2, and the stray `5` and typo in Problem 3 suggest a need for more thorough testing and review of the code.
*   **Robust Error Handling:** While the student uses `try-except`, the specific implementation in Problem 3 for distinguishing `ValueError` types could be simplified and made more robust to avoid relying on specific error message strings. A more general `except ValueError` for `int()` conversion and then specific `if` conditions *before* the `int()` conversion or simpler `except` blocks would be beneficial.

Keep up the great work! Focusing on these details will elevate your code quality and robustness significantly.

**FINAL SCORE: 75/100**