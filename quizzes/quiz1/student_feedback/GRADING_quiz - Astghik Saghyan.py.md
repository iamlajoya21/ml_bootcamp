# Grading Report for Student Submission

## Question-by-Question Assessment

### Problem 1: The Secure Inventory Audit
*   **Score**: 10/10
*   **Feedback**: Excellent solution! The student correctly implemented file I/O using `with` statements, handled different types of errors (malformed lines, non-integer quantities) by logging them to `audit_errors.log`, normalized item names to uppercase, and correctly aggregated quantities for repeated items. The use of `try-except-else` for quantity conversion and the `if len(data) != 2` check are robust.

### Problem 2: The Login Security Monitor
*   **Score**: 10/10
*   **Feedback**: Another strong answer. The student effectively used a `set` to filter out blacklisted IPs and automatically handle deduplication. Converting the final set to a `tuple` met the storage requirement, and writing each safe IP to `authorized_logins.txt` on a new line was correctly implemented. The solution is concise and efficient.

### Problem 3: The "Strict" Transaction Processor
*   **Score**: 4/10
*   **Feedback**: This problem had some good elements but also critical errors.
    *   **Positive**: The `while True` loop and `try-except` for `ValueError` on non-numeric input were correct. The `finally` block for "System: Monitoring active." was also correctly placed to execute after every attempt. Raising `ValueError("High Value: Requires Approval")` for numbers greater than 5000 was also correct.
    *   **Deductions**:
        *   The exit condition `if number == "Exit": break` is case-sensitive. The problem specified "exit" (lowercase), so typing "exit" would not terminate the loop. (-1 point)
        *   For numbers 0 or less, the requirement was to `raise a ValueError with the message "Invalid Amount"`. The student's code `raise ValueError("System: Monitoring active.")` uses the wrong error message and effectively misuses the `finally` block's intended output as an error message. This is a significant functional error as the program would crash with an incorrect error message. (-5 points)

### Problem 4: The Global Gradebook Merger
*   **Score**: 0/10
*   **Feedback**: No solution was provided for this problem.

## Overall Feedback
The student demonstrated a solid understanding of Python fundamentals, particularly in file I/O, data structures (sets, dictionaries), and basic error handling in Problems 1 and 2. These solutions were well-structured, efficient, and met all requirements.

However, there were notable gaps in Problem 3, specifically regarding precise error message handling and case sensitivity for input, and a complete omission of Problem 4. To improve, the student should pay closer attention to the exact specifications for error messages and input handling, and ensure all problems are attempted. Reviewing dictionary merging techniques, especially for appending to lists associated with existing keys, would be beneficial for future tasks.

**FINAL SCORE: 60/100**