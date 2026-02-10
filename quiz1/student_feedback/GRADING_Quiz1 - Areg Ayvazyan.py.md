# Grading Report for Student Submission

## Question-by-Question Assessment

### Problem 1: The Secure Inventory Audit
*   **Score: 7/10**
*   **Feedback:**
    *   **Strengths:** The student correctly implemented file reading, normalization (uppercasing item names), and aggregation of quantities. The `ValueError` for non-integer quantities was correctly caught, and the full line was logged to `audit_errors.log`, which is excellent. The `FileNotFoundError` handling is also good.
    *   **Areas for Improvement:**
        1.  **Incomplete Error Logging:** The problem stated, "If the quantity is not an integer (e.g., 'ten' or missing), catch the error and log the full line to audit_errors.log." While `ValueError` (for "ten") was logged, the `IndexError` (for "missing" quantity, e.g., "grape:") was caught but only printed to the console, not logged to `audit_errors.log`. This misses a part of the error handling requirement.
        2.  **Variable Naming:** The variable `item_price` was used to store the quantity. While functionally correct, `item_quantity` would have been more semantically accurate and clearer.

### Problem 2: The Login Security Monitor
*   **Score: 10/10**
*   **Feedback:**
    *   **Strengths:** This solution is excellent. The student correctly used a `set` to efficiently filter out blacklisted IPs and automatically handle deduplication. Converting the `set` to a `tuple` for storage and then writing each safe IP to `authorized_logins.txt` on a new line demonstrates a clear understanding of the requirements and appropriate data structures. The code is clean, efficient, and perfectly meets all criteria.

### Problem 3: The "Strict" Transaction Processor
*   **Score: 6/10**
*   **Feedback:**
    *   **Strengths:** The student correctly implemented the `while True` loop with an 'exit' condition and the `finally` block to print "System: Monitoring active." The outer `try-except ValueError` correctly catches non-numeric input and prints "Invalid Data Type."
    *   **Areas for Improvement:**
        1.  **Incorrect Exception Raising:** The problem explicitly asked to "raise a ValueError *with the message*" (e.g., `raise ValueError("High Value: Requires Approval")`). The student raised a generic `ValueError` (`raise ValueError`) and then immediately caught it in a nested `try-except` block to print the required message. This approach bypasses the intended mechanism of associating the message directly with the exception object.
        2.  **Suboptimal `try-except` Structure:** The use of nested `try-except` blocks for each custom validation (high value, invalid amount) makes the code less clear and less robust than it could be. A more idiomatic approach would be to raise `ValueError` with the specific message, and then have a single `except ValueError as e:` block that inspects `str(e)` to determine which message to print, or to handle different custom exception types. While the current code produces the correct output messages, the underlying exception handling mechanism is not fully aligned with the prompt's intent for raising exceptions *with* messages.

### Problem 4: The Global Gradebook Merger
*   **Score: 10/10**
*   **Feedback:**
    *   **Strengths:** This solution is perfect. The `merger` function correctly iterates through the semester data. It accurately checks if a student already exists in `final_grades` and uses `extend()` to add new grades to the existing list, ensuring no data is overwritten and all grades are collected. For new students, it correctly assigns their grades. This demonstrates a strong grasp of dictionary manipulation and list methods.

## Overall Feedback

The student demonstrates a solid foundation in Python programming, particularly in handling data structures like lists, sets, tuples, and dictionaries, as well as file I/O operations. Problems 2 and 4 were solved flawlessly, showcasing excellent problem-solving skills and an understanding of efficient data manipulation.

Problem 1 was very close to perfect, with a minor oversight in ensuring all types of quantity-related errors were logged to the specified file. This highlights the importance of thoroughly reviewing all conditions in error handling requirements.

Problem 3, while producing the correct output, revealed an opportunity to deepen the understanding of Python's exception handling mechanisms, specifically how to `raise` exceptions with custom messages and how to structure `try-except` blocks for clarity and robustness. Focusing on raising specific `ValueError` messages and allowing them to propagate to a single, more comprehensive `except` block would be a valuable learning exercise.

Keep up the great work! Your ability to tackle complex tasks and your strong grasp of fundamental concepts are commendable. With a bit more focus on the nuances of exception handling, your solutions will become even more robust and Pythonic.

**FINAL SCORE: 83/100**