# Grading Report for Student Submission

## Question-by-Question Assessment

### Problem 1: The Secure Inventory Audit
*   **Score**: 10/10
*   **Feedback**: Excellent work on Problem 1!
    *   You correctly implemented file I/O using `with` statements for both `inventory.txt` and `audit_errors.log`.
    *   Normalization to uppercase (`item.upper()`) was applied correctly.
    *   Aggregation of quantities for repeated items (`items[item] += price`) was handled perfectly.
    *   Error handling for malformed lines (`len(data) != 2`) and non-integer quantities (`try-except ValueError` for `int(price)`) was robust and correctly logged the full problematic lines.
    *   This solution fully meets all requirements.

### Problem 2: The Login Security Monitor
*   **Score**: 10/10
*   **Feedback**: Another strong solution!
    *   You effectively used a `set` (`safe_ips = set()`) to both filter out blacklisted IPs (`if ip not in blacklisted_ips:`) and automatically deduplicate the safe IPs.
    *   Converting the set to a tuple (`safe_ips = tuple(safe_ips)`) was done correctly as required.
    *   Writing the safe IPs to `authorized_logins.txt`, one per line, was also implemented perfectly.
    *   The solution is concise, efficient, and correct.

### Problem 3: The "Strict" Transaction Processor
*   **Score**: 0/10
*   **Feedback**: While you attempted to use `try-except` and `raise ValueError`, there are several critical issues that prevent this solution from functioning as intended:
    1.  **Case-Sensitive Exit**: The exit condition `if number == "Exit":` is case-sensitive. The problem stated "if the user types 'exit'", implying a case-insensitive check (e.g., `number.lower() == "exit"`). (Minor deduction, but contributes to overall functionality).
    2.  **Incorrect Error Message**: For amounts 0 or less, you raised `ValueError("System: Monitoring active.")`. The requirement was to raise `ValueError` with the message "Invalid Amount".
    3.  **Unhandled Raised Errors**: The `ValueError`s you manually raised (for amounts > 5000 and <= 0) are not caught within the loop. This means that whenever these conditions are met, the program will crash instead of continuing to prompt for input, which is essential for a "terminal-based transaction logger". The `finally` block executes just before the crash, but the program does not recover.
    4.  **Incorrect `finally` Placement**: The `finally` block is nested inside the `else` clause of the initial `try-except` for `int(number)`. This means "System: Monitoring active." is *only* printed if the input was successfully converted to an integer. The requirement was "After every attempt (valid or invalid)", meaning it should print even if the input was non-numeric (e.g., "abc").
    5.  **Missing Action for Valid Transactions**: For valid transactions (e.g., input "100"), your code simply prints "System: Monitoring active." but doesn't perform any "logging" or acknowledgement of the valid transaction itself. While not explicitly asked to store, a "logger" typically does something with valid data.

    To fix this, you would need a single `try-except` block that wraps the entire processing logic for an input, catching both the `int()` conversion errors and your manually raised `ValueError`s, and then placing the `finally` block at the end of the `while` loop's iteration to ensure it always executes.

### Problem 4: The Global Gradebook Merger
*   **Score**: 0/10
*   **Feedback**: No solution was provided for this problem.

## Overall Feedback
You demonstrated a strong understanding of Python fundamentals, particularly in file I/O, data structures (dictionaries, sets, tuples), and basic error handling with `try-except` for `ValueError` in Problems 1 and 2. Your solutions for these problems were efficient, accurate, and followed all instructions perfectly.

However, Problem 3 highlighted areas where your understanding of advanced error handling, specifically raising and catching custom `ValueError`s within a continuous loop, and the precise behavior of `finally` blocks, needs improvement. The unhandled exceptions and incorrect `finally` placement led to a solution that would not function as a robust, continuous logger. Additionally, Problem 4 was not attempted.

Focus on practicing more complex error handling scenarios, especially how to structure `try-except-finally` blocks to ensure program continuity and proper execution flow, even when exceptions are raised. Reviewing loop control and exception propagation will be beneficial. Keep up the good work on your strengths!

**FINAL SCORE: 50/100**