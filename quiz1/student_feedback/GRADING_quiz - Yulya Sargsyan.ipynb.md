# Grading Report for Student Submission

## Question-by-Question Assessment

### Problem 1: The Secure Inventory Audit
*   **Student Submission:** No code provided for Problem 1.
*   **Grade:** 0/10
*   **Feedback:** This problem was not attempted.

### Problem 2: The Login Security Monitor
*   **Student Submission:**
    ```python
    # problem 2
    all_logins = [
        "192.168.1.1", "10.0.0.5", "192.168.1.1", "172.16.0.1",
        "10.0.0.5", "192.168.1.10", "172.16.0.1", "8.8.8.8",
        "192.168.1.1", "10.0.0.9", "192.168.1.10", "10.0.0.5"
    ]
    blacklisted_ips = {"172.16.0.1", "8.8.8.8", "200.50.10.1"}
    unique_ips=set()
    for a in all_logins:
        if a in blacklisted_ips:
                del a # This line is ineffective
        else:
                unique_ips.add(a)
    print(unique_ips)
    with open("authorized_logins.txt","w") as file:
           file.write(unique_ips) # TypeError: write() argument must be str, not set
    ```
*   **Grade:** 5/10
*   **Feedback:**
    *   **Good:** You correctly identified the blacklisted IPs and used a `set` (`unique_ips`) to automatically handle deduplication, which is efficient. The final `unique_ips` set correctly contains only the safe, unique IPs.
    *   **Needs Improvement:**
        *   The line `del a` inside the `if` block is ineffective. It only deletes the local loop variable `a` and does not remove the element from the `all_logins` list or prevent it from being processed further. However, because you only add to `unique_ips` in the `else` block, the *result* of filtering is correct.
        *   The problem required storing the safe, unique IPs in a `Tuple`. Your code stores them in a `set` and prints the set, but does not convert it to a tuple.
        *   The file writing operation `file.write(unique_ips)` is incorrect. The `write()` method expects a string argument, but you are passing a `set`. To write the IPs to the file, you need to iterate through the `unique_ips` set and write each IP as a separate string, typically followed by a newline character (`\n`).

### Problem 3: The "Strict" Transaction Processor
*   **Student Submission:**
    ```python
    # problem 2 (Note: This is for Problem 3)
    try:
        number=int(input('')) # Input taken only once
        while True:
            if "exit": # This condition is always True
                break
            elif type(number)!=int: # Redundant and incorrect check here
                raise ValueError("anvavert tvyalneri tesal") # Armenian message
            elif number>=5000:
                raise ValueError("bardz arjeq") # Armenian message
            elif number<=0:
                raise ValueError("anvaver gumar") # Armenian message
    except ValueError:
        print(ValueError) # Prints the class, not the exception message
    finally:
        print("hamakargy aktiv e") # Armenian message, prints once
    ```
*   **Grade:** 1/10
*   **Feedback:**
    *   **Major Flaws:**
        *   **Input Loop:** The `input()` call is placed *before* the `while True` loop, meaning the program only asks for input once. The problem required asking for input repeatedly within the loop.
        *   **Loop Termination:** The condition `if "exit":` is always `True` because the string `"exit"` is a truthy value. This causes the `while True` loop to `break` immediately after the first (and only) iteration, preventing any of the validation logic from ever being executed.
        *   **Type Check:** The `elif type(number)!=int:` check is redundant and misplaced. If `int(input(''))` succeeded, `number` is already an integer. If it failed (e.g., user typed "abc"), a `ValueError` would be raised by `int()` itself, which would be caught by your `try-except` block *before* this `elif` is reached.
        *   **Exception Message Display:** `print(ValueError)` prints the `ValueError` class itself (e.g., `<class 'ValueError'>`), not the specific error message associated with the exception. To print the message, you should catch the exception as an object, e.g., `except ValueError as e: print(e)`.
        *   **`finally` Block:** The `finally` block executes only once, after the entire `try-except` block (and thus the loop) has finished. The requirement was to print "System: Monitoring active." *after every attempt* (i.e., within each iteration of the loop).
        *   **Language:** The error messages (`"anvavert tvyalneri tesal"`, `"bardz arjeq"`, `"anvaver gumar"`, `"hamakargy aktiv e"`) are in Armenian, but the problem specified English messages.
    *   **Recommendation:** Review fundamental concepts of `while` loops, `input()` within loops, and proper `try-except-finally` structure for handling user input and exceptions.

### Problem 4: The Global Gradebook Merger
*   **Student Submission:**
    ```python
    #  problem 4
    semester_1 = {
        "Alice": [85, 90], "Bob": [70, 65], "Charlie": [100],
        "David": [88], "Eve": [92, 91]
    }
    semester_2 = {
        "Alice": [95, 88], "Frank": [78, 80], "Bob": [72],
        "Grace": [99], "Charlie": [90, 85], "Heidi": [75]
    }
    dictionary={}
    for  name,score in semester_1.items():
        if name not in dictionary:
                dictionary[name]=score
    for name,score in semester_2.items():
        if name not in dictionary:
             dictionary[name]=score
        else:
             dictionary[name].extend(score)
    print(dictionary)
    ```
*   **Grade:** 10/10
*   **Feedback:**
    *   **Excellent:** This solution is perfectly correct and meets all requirements. You correctly initialized the merged dictionary with `semester_1` data and then iterated through `semester_2`, adding new students and correctly using `extend()` to append grades for existing students without overwriting previous data. Well done!

## Overall Feedback

You demonstrated a strong grasp of dictionary manipulation and merging in Problem 4, achieving a perfect score. This shows a good understanding of how to handle and combine data structures effectively.

However, there are significant areas for improvement in Problem 2 and especially Problem 3. In Problem 2, while your approach to filtering and deduplication using a set yielded the correct result, the implementation details for `del a` and the file writing were incorrect. For Problem 3, there were fundamental misunderstandings regarding loop control, taking input within a loop, and the proper use and display of exception handling messages. Problem 1 was not attempted.

To improve, I recommend focusing on:
1.  **Loop Control and Input:** Practice using `while` loops for continuous input and ensuring loop termination conditions are correctly implemented.
2.  **File I/O:** Understand the difference between writing strings and other data types to files, and how to format output (e.g., one item per line).
3.  **Exception Handling:** Review how to catch specific exceptions, access their messages, and ensure `try-except-finally` blocks execute as intended for the problem's requirements.

Keep practicing, and you'll master these concepts!

**FINAL SCORE: 40/100**