# Grading Report for Student Submission

## Question-by-Question Assessment

### Problem 1: The Secure Inventory Audit
*   **Score: 6/10**
*   **Feedback:**
    *   **Strengths:** You correctly implemented the file opening and closing using `with open()`. The logic for normalizing item names to uppercase (`parts[0].upper()`) and aggregating quantities into the dictionary (`d[name] += int(parts[1])`) is mostly correct for valid input.
    *   **Areas for Improvement:**
        *   **Error Handling Flaw:** The primary issue is with your error handling. The condition `if type(int(parts[1])) != int:` is logically flawed. If `int(parts[1])` successfully converts the string to an integer, its type will always be `int`. If it fails (e.g., `int("five")`), it will raise a `ValueError` *before* this `if` condition is even evaluated.
        *   **Incorrect Exception Type:** You are catching `TypeError`, but converting a non-integer string (like "five" or an empty string) to an `int` raises a `ValueError`, not a `TypeError`. This means your `except TypeError` block would not catch the intended errors, and your program would crash if it encountered corrupted quantity data.
        *   While you correctly log the line to `audit_errors.log`, this logging would not occur for the actual quantity conversion errors due to catching the wrong exception type.

### Problem 2: The Login Security Monitor
*   **Score: 4/10**
*   **Feedback:**
    *   **Strengths:** You correctly utilized a `set` (`s`) for deduplication and converted the final set to a `tuple` (`t`). You also correctly opened the output file (`authorized_logins.txt`) and wrote the IPs one per line.
    *   **Areas for Improvement:**
        *   **Flawed Filtering Logic:** The core filtering mechanism is incorrect.
            *   `all_logins.remove(i)` while iterating over `all_logins` is generally problematic and can lead to unexpected behavior (e.g., skipping elements).
            *   More critically, `s.add(i)` happens *unconditionally* for every IP `i` in `all_logins`, regardless of whether it's blacklisted. This means your `s` set (and consequently your `t` tuple) will contain *all* unique IPs from `all_logins`, including the blacklisted ones.
        *   To correctly filter, you should only add an IP to your `s` set if it is *not* present in `blacklisted_ips`.

### Problem 3: The "Strict" Transaction Processor
*   **Score: 7/10**
*   **Feedback:**
    *   **Strengths:** You successfully implemented the `while True` loop with the "exit" condition and correctly used a `finally` block to print "System: Monitoring active." You also correctly identified the conditions (`num > 5000` and `num <= 0`) for raising `ValueError`.
    *   **Areas for Improvement:**
        *   **Redundant Type Check:** Similar to Problem 1, the `if type(int(c)) != int:` check is redundant. If `c` cannot be converted to an integer, `int(c)` will raise a `ValueError` directly.
        *   **Error Message Handling:** The way error messages are handled needs refinement.
            *   When `int(c)` fails (e.g., input is "abc"), the `ValueError` is caught by your `except ValueError` block, which then prints a blank line (`print(" ")`). This means the specific "Invalid Data Type" message (which you attempted to print inside the `try` block) is not displayed as the final output for this error.
            *   For `num > 5000` and `num <= 0`, you print the specific message (e.g., "High Value: Requires Approval") *before* raising `ValueError`. Then, the `except ValueError` block catches it and prints a blank line, effectively losing the specific message that was just raised.
            *   A better approach would be to `raise ValueError("Your specific message")` and then catch it with `except ValueError as e: print(e)` to display the message carried by the exception.

### Problem 4: The Global Gradebook Merger
*   **Score: 0/10**
*   **Feedback:** No code was provided for this problem.

## Overall Feedback

You've made a good start on this quiz, demonstrating a foundational understanding of Python's core features like loops, conditionals, file I/O, and basic data structures (dictionaries, sets, tuples). Your attempts to use `try-except` blocks and manage data flow are commendable.

However, there are recurring themes in your solutions that need focused attention:

1.  **Error Handling Precision:** It's crucial to understand which specific exceptions (e.g., `ValueError`, `TypeError`) are raised by different operations. Your `try-except` blocks often caught the wrong exception type or handled the messages in a way that obscured the specific error, which can make debugging difficult.
2.  **Data Structure Manipulation Best Practices:** Be cautious when modifying a collection (like a list) while iterating over it, as this can lead to unexpected results. When filtering, it's often safer and clearer to build a new collection with the desired elements rather than trying to remove items from the original in-place.
3.  **Attention to Detail:** Carefully review problem requirements, especially regarding how error messages should be presented or how data should be filtered and stored.

Keep practicing these concepts, particularly error handling and list/set manipulation. With more practice, you'll develop a stronger intuition for robust and efficient Python programming. Don't be discouraged; these are common learning points, and your effort is clearly visible!

**FINAL SCORE: 43/100**