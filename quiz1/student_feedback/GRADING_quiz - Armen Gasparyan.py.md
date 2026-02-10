# Grading Report for Student Submission

## Question-by-Question Assessment

### Problem 1: The Secure Inventory Audit
*   **Score**: 0/25
*   **Feedback**: No submission provided for this problem.

### Problem 2: The Login Security Monitor
*   **Score**: 0/25
*   **Feedback**: No submission provided for this problem.

### Problem 3: The "Strict" Transaction Processor
*   **Score**: 16/25
*   **Feedback**:
    *   **Positive Aspects**:
        *   The use of `while True` for the continuous loop and `if str(x) == 'exit': break` for exiting the loop is correctly implemented.
        *   The `finally` block is correctly used to print "System: Monitoring active." after every attempt.
        *   The code correctly catches a `ValueError` if the input cannot be converted to an integer (e.g., "abc") and prints "Invalid Data Type".
        *   The conditions for raising "High Value: Requires Approval" (`int(x) > 5000`) and "Invalid Amount" (`int(x) < 0`) are identified, and the `ValueError` is raised with the specified messages.
    *   **Areas for Improvement**:
        *   **Error Handling Logic (Major Issue)**: The primary flaw is that the single `except ValueError` block catches *all* `ValueError`s. This means that when you manually `raise ValueError("High Value: Requires Approval")` or `raise ValueError("Invalid Amount")`, these specific errors are immediately caught by the generic `except ValueError` block, and the user *always* sees "Invalid Data Type" instead of the intended specific error messages. To fix this, you should separate the `try-except` blocks, or handle the specific `ValueError` types differently. For example, convert to `int` in one `try` block, then apply business logic in another.
        *   **Condition for "Invalid Amount"**: The problem states "If the number is 0 or less". Your condition `if int(x) < 0:` correctly handles negative numbers but misses the case where the amount is exactly `0`. It should be `if int(x) <= 0:`.

### Problem 4: The Global Gradebook Merger
*   **Score**: 0/25
*   **Feedback**: No submission provided for this problem.

## Overall Feedback
Your submission for Problem 3 demonstrates a good understanding of basic loop structures, `try-except-finally` blocks, and how to manually raise exceptions. You've correctly identified several key requirements of the problem.

However, there's a critical logical error in your error handling for Problem 3. By using a single `except ValueError` block, you're inadvertently catching your custom `ValueError`s and masking their specific messages with the generic "Invalid Data Type" message. This is a common pitfall when first learning about exception handling. Focus on refining your `try-except` structure to differentiate between different types of errors or to allow specific error messages to propagate when intended. Additionally, pay close attention to edge cases in conditions, such as including `0` in "0 or less".

For future quizzes, please ensure you attempt all problems. Even partial solutions can earn points and demonstrate your thought process. Keep practicing, and you'll master these concepts!

**FINAL SCORE: 16/100**