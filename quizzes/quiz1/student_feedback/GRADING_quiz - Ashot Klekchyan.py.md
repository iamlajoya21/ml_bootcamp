# Grading Report for Student Submission

## Question-by-Question Assessment

### Problem 1: The Secure Inventory Audit
*   **Score:** 0/10
*   **Feedback:** No solution was provided for this problem. To earn points, you would need to implement the file reading, error handling for non-integer quantities (logging them to `audit_errors.log`), normalizing item names to uppercase, and aggregating quantities for repeated items into a dictionary.

### Problem 2: The Login Security Monitor
*   **Score:** 9/10
*   **Feedback:** Your solution is very good! You correctly filtered out blacklisted IPs, used a set for efficient deduplication, converted the result to a tuple, and wrote the safe IPs to `authorized_logins.txt`. The verification step at the end is also a nice touch.
    The only minor point deduction is for printing `Safe and unique IPs: {safe_ips_set}` inside the loop. This causes the set to be printed multiple times as it's being built. It's generally better to print the final result once after all processing is complete.

### Problem 3: The "Strict" Transaction Processor
*   **Score:** 0/10
*   **Feedback:** No solution was provided for this problem. This problem required implementing a `while True` loop for user input, handling `ValueError` for non-numeric input, and manually raising `ValueError` for amounts greater than 5000 or less than or equal to 0. A `finally` block to print "System: Monitoring active." after each attempt was also a key requirement.

### Problem 4: The Global Gradebook Merger
*   **Score:** 10/10
*   **Feedback:** Excellent solution! Your code correctly merges the two semester gradebooks. You accurately handle students present in both semesters by extending their grade list, and correctly add new students from `semester_2`. The use of `list(grades)` when assigning to `merged_grades` is also good practice to ensure you're working with copies and not modifying the original dictionary's lists.

## Overall Feedback
You demonstrated strong understanding and implementation skills for the problems you attempted (Problem 2 and Problem 4). Your solutions for these problems were clear, correct, and followed the requirements well.

However, a significant portion of the quiz (Problem 1 and Problem 3) was left unanswered. To improve your overall score, it's crucial to attempt all problems, even if you're not entirely confident. Partial solutions or attempts to address specific requirements can still earn points. Focus on time management during quizzes to ensure you allocate time to each problem.

Keep up the great work on the problems you did solve, and remember to tackle all parts of future assignments!

**FINAL SCORE: 48/100**