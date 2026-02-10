# Grading Report for Student Submission

## Question-by-Question Assessment

### Problem 1: The Secure Inventory Audit
**Score: 1/10**

**Feedback:**
You've made a good start on several aspects of this problem, demonstrating an understanding of file reading, basic parsing, and the concept of aggregation and error handling.

*   **Strengths:**
    *   You correctly opened `inventory.txt` for reading and iterated through its lines.
    *   You correctly split each line into parts.
    *   Your logic for using `.upper()` when adding/updating dictionary keys (`thisdict[parts[0].upper()]`) correctly handles the normalization requirement for the keys.
    *   The aggregation logic (`thisdict[parts[0].upper()] += parts[1]`) is correct for summing quantities.
    *   You implemented a `try-except` block to catch errors during integer conversion and attempted to log the problematic lines to `audit_errors.log`.
    *   You included a `try-except` for `FileNotFoundError` when opening the main inventory file.

*   **Areas for Improvement:**
    1.  **Critical Flaw: File Overwriting:** The most significant issue is that you open `inventory.txt` in write mode (`'w'`) *inside* your processing loop (`with open('/content/inventory.txt', 'w') as f:`). This action truncates (empties) the `inventory.txt` file in every iteration, destroying your input data and making the entire process incorrect. File writing should typically occur *after* all data has been processed, and usually to a *separate* output file, not the input file.
    2.  **Critical Flaw: Writing a Dictionary Directly:** You attempted to `f.write(thisdict)`. The `write()` method expects a string argument, not a dictionary. This line would cause a `TypeError` and crash your program. To write a dictionary, you would typically convert it to a string representation (e.g., using `str()`, `json.dumps()`, or iterating through its items).
    3.  **Ineffective Normalization Line:** The line `parts[0].upper()` by itself does not modify the `parts[0]` variable. `str.upper()` returns a *new* string. While you correctly use `parts[0].upper()` when interacting with `thisdict`, this specific line is redundant.
    4.  **Broad Exception Handling:** Using a bare `except:` (e.g., `except:`) is generally discouraged. It catches *all* exceptions, including unexpected ones, which can hide bugs. It's better to catch specific exceptions like `ValueError` for the `int()` conversion.

### Problem 2: The Login Security Monitor
**Score: 2/10**

**Feedback:**
You've correctly identified and implemented the core logic for filtering and deduplication, which is excellent.

*   **Strengths:**
    *   You correctly iterated through `all_logins`.
    *   You successfully filtered out blacklisted IPs using `if ip in blacklisted_ips: continue`.
    *   You correctly used a `set` (`new_set`) to efficiently deduplicate the safe IP addresses.
    *   Your logic for writing each IP to a new line (`fs.write(i); fs.write('\n')`) is correct.

*   **Areas for Improvement:**
    1.  **Critical Flaw: File Overwriting:** Similar to Problem 1, you opened `authorized_logins.txt` in write mode (`'w'`) *inside* your loop (`with open('authorized_logins.txt', 'w') as fs:`). This means the file is truncated and rewritten in every iteration. As a result, the file would only contain the IPs from the *last* iteration of the loop, not all the unique, safe IPs. The file should be opened *once* after `new_set` has been fully populated.
    2.  **Data Structure Requirement:** The problem explicitly asked to "Store: Save the safe, unique IPs into a Tuple." While using a `set` for deduplication is correct, you did not convert the final `new_set` into a `tuple` (e.g., `safe_ips_tuple = tuple(new_set)`) as required by the prompt.
    3.  **Efficiency:** Printing `new_set` and writing to the file in every loop iteration is inefficient and incorrect for the final output.

### Problem 3: The "Strict" Transaction Processor
**Score: 0/10**

**Feedback:**
No submission was provided for this problem.

### Problem 4: The Global Gradebook Merger
**Score: 0/10**

**Feedback:**
No submission was provided for this problem.

## Overall Feedback

Your submission shows a foundational understanding of Python syntax, list/set manipulation, and basic file I/O operations. You correctly grasped the concepts of filtering, deduplication, and aggregation for the problems you attempted. Your use of `set` for deduplication and `try-except` for error handling demonstrates good problem-solving instincts.

However, there are critical areas that need attention, particularly regarding file handling. The repeated error of opening files in write mode (`'w'`) inside a loop is a fundamental misunderstanding that leads to data loss and incorrect program behavior. Always ensure that files are opened for writing *after* all data processing is complete, and consider writing to a new output file rather than overwriting the input. Additionally, pay close attention to the specific data structure requirements (e.g., storing results in a tuple).

To improve, focus on:
1.  **File I/O Best Practices:** Understand when and how to open files for reading (`'r'`), writing (`'w'`), and appending (`'a'`). Crucially, avoid opening files in `'w'` mode within a processing loop unless that is the explicit, intended (and rare) behavior.
2.  **Specific Exception Handling:** Practice catching specific `Exception` types rather than using a broad `except:`.
3.  **Reading Instructions Carefully:** Ensure all requirements, such as the final data structure (e.g., tuple), are met.
4.  **Completing All Problems:** Attempting all problems, even if you're unsure, can help identify areas for learning.

Keep practicing! With a focus on these areas, you'll significantly improve your Python programming skills.

**FINAL SCORE: 8/100**