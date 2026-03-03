# Grading Report for Student Submission

## Question-by-Question Assessment

### Problem 1: The Secure Inventory Audit
**Score: 0/10**

**Feedback:**
The student's code for Problem 1 only manages to open the `inventory.txt` file and iterate through its lines. However, it fails to implement any of the core requirements:
*   **Normalization:** `line.upper()` is called, but its return value is not assigned back to `line`, so the item names are not actually uppercased.
*   **Aggregation:** There is no logic to sum quantities for repeated items. The `dict` variable is initialized but never populated with inventory data.
*   **Error Handling:** There is no `try-except` block to catch `ValueError` if a quantity is not an integer, nor is there any logging to `audit_errors.log`.
*   **Output:** The expected dictionary output is not produced.

### Problem 2: The Login Security Monitor
**Score: 6/10**

**Feedback:**
The student correctly uses a `set` (`unique_ips`) to achieve both filtering of blacklisted IPs and deduplication of login attempts. The conversion to a `tuple` (`safe_ips`) is also correct.
*   **Filtering & Deduplication:** Achieved correctly by adding only non-blacklisted items to a set. (4 points)
*   **Storing in Tuple:** Correctly converted the set to a tuple. (2 points)
*   **File Writing:** This section has a critical flaw. The `with open('authorized_logins.txt','w')` statement is placed inside the loop that iterates over `safe_ips`. The `'w'` mode truncates (empties) the file every time it's opened. This means that for each IP, the file is overwritten, and only the *last* IP address from the `safe_ips` tuple will ultimately be present in `authorized_logins.txt`. To fix this, the file should be opened *once* before the loop, and then all IPs written within the loop. (Deducted 4 points)

### Problem 3: The "Strict" Transaction Processor
**Score: 3/10**

**Feedback:**
The student correctly implements the `while True` loop and the `exit` condition. However, there are several issues with the error handling and the `finally` block:
*   **"Invalid Data Type" Handling:** If the user enters non-numeric input (e.g., "abc"), the `int(amount)` conversion will raise a `ValueError`. This `ValueError` is caught by the *inner* `except ValueError` blocks, leading to the incorrect messages "High Value: Requires Approval" or "Invalid Amount" being printed, instead of "Invalid Data Type". The outer `try-except` is misplaced and does not correctly handle this specific error for each attempt. (Deducted 3 points)
*   **Manual Raise Messages:** The requirement was to `raise ValueError with the message "..."`. The student uses `raise ValueError()` which raises a generic `ValueError`. While the subsequent `except` block prints the correct message, the `ValueError` itself doesn't carry the specified message. (Deducted 1 point)
*   **`finally` Block Placement:** The `finally` block is associated with the *outer* `try` block. This means "System: Monitoring active." will only print *once* when the entire loop terminates (or an unhandled exception occurs), not "After every attempt (valid or invalid)" as required. The `finally` block should be inside the `while` loop to execute after each attempt. (Deducted 3 points)
*   **Redundant `int(amount)` calls:** The `int(amount)` conversion is attempted multiple times within the same loop iteration, which is inefficient and can lead to issues if the first conversion fails. (Deducted 1 point)

### Problem 4: The Global Gradebook Merger
**Score: 10/10**

**Feedback:**
Excellent solution! The student correctly iterates through `semester_1` to initialize the `all_grades` dictionary. Then, for `semester_2`, they correctly check if a student already exists. If the student is new, they are added. If the student already exists, `extend()` is used to append the new grades to the existing list, perfectly fulfilling the requirement to not overwrite data and include all grades. The output is exactly as expected.

## Overall Feedback
The student demonstrates a solid grasp of fundamental Python dictionary operations and iteration, as evidenced by the perfect score on Problem 4. This is a strong foundation.

However, there are significant areas for improvement, particularly in error handling, file I/O modes, and understanding the precise scope and behavior of `try-except-finally` blocks. In Problem 1, the solution was incomplete, missing key logic for normalization, aggregation, and error handling. Problem 2 showed a good approach to filtering and deduplication but contained a critical error in file writing that would lead to data loss. Problem 3 highlighted misunderstandings in catching specific `ValueError` types and the execution timing of `finally` blocks.

Focusing on these areas—especially practicing robust error handling with specific exception types and understanding file modes (`'w'` vs. `'a'`)—will greatly enhance your Python programming skills. Keep up the good work on the concepts you've mastered!

**FINAL SCORE: 48/100**