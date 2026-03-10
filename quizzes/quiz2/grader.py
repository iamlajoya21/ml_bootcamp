import os
import time
import json
import glob
from google import genai
from google.genai import types

# --- CONFIGURATION ---
QUIZ_DIR = "quizzes/quiz2"
SUBMISSIONS_DIR = os.path.join(QUIZ_DIR, "exam2_answers")
GOLDEN_ANSWERS_FILE = os.path.join(QUIZ_DIR, "golden_answers.py")
ENV_FILE = ".env"
GRADEBOOK_JSON = os.path.join(QUIZ_DIR, "gradebook.json")
GRADEBOOK_MD = os.path.join(QUIZ_DIR, "gradebook.md")

# --- LOAD API KEY ---
def load_api_key():
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, 'r') as f:
            for line in f:
                if line.startswith("GEMINI-API-KEY="):
                    return line.split("=")[1].strip()
    return os.getenv("GEMINI_API_KEY")

API_KEY = load_api_key()
if not API_KEY:
    raise ValueError("GEMINI-API-KEY not found in .env or environment variables.")

client = genai.Client(api_key=API_KEY)
MODEL_ID = "gemini-3.1-flash-lite-preview"

# --- HELPER FUNCTIONS ---
def read_file_content(filepath):
    """Reads content from .py, .ipynb, or .html files."""
    ext = os.path.splitext(filepath)[1].lower()
    try:
        if ext == '.ipynb':
            with open(filepath, 'r', encoding='utf-8') as f:
                nb = json.load(f)
                content = ""
                for cell in nb.get('cells', []):
                    if cell.get('cell_type') == 'code':
                        content += "".join(cell.get('source', [])) + "\n"
                    elif cell.get('cell_type') == 'markdown':
                        content += "".join(cell.get('source', [])) + "\n"
                return content
        else: # .py or .html (assuming html is a simple dump or text-like)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def get_student_name(filename):
    """Extracts student name from filename (e.g., 'quiz - Armen Gasparyan.py' -> 'Armen Gasparyan')"""
    name = os.path.splitext(filename)[0]
    if " - " in name:
        name = name.split(" - ")[1]
    return name.strip()

# --- GRADING LOGIC ---
def grade_submission(student_name, student_code, golden_code):
    prompt = f"""
    You are an expert Python and Data Science instructor. 
    Grade the following student's submission for 'Quiz 2' against the 'Golden Answers'.

    ### Golden Answers (Correct Implementation):
    ```python
    {golden_code}
    ```

    ### Student Submission ({student_name}):
    ```python
    {student_code}
    ```

    ### Instructions:
    1. Evaluate each of the 5 tasks:
       - Task 1: NumPy Percentiles
       - Task 2: NumPy Conditional Labeling
       - Task 3: Pandas Multi-Condition Filtering
       - Task 4: Pandas Grouped Aggregation
       - Task 5: Matplotlib Visualization & Annotation
    2. Provide a score (0-20) for each task.
    3. Calculate a total score (max 100).
    4. Provide detailed, constructive feedback for each task, especially where points were deducted.
    5. Be lenient with small typos but strict on logic and correct library usage (NumPy/Pandas/Matplotlib).

    ### Output Format (Strictly valid JSON):
    {{
      "student_name": "{student_name}",
      "tasks": [
        {{"task": 1, "score": 0, "feedback": ""}},
        {{"task": 2, "score": 0, "feedback": ""}},
        {{"task": 3, "score": 0, "feedback": ""}},
        {{"task": 4, "score": 0, "feedback": ""}},
        {{"task": 5, "score": 0, "feedback": ""}}
      ],
      "total_score": 0,
      "overall_feedback": ""
    }}
    """
    
    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json"
            )
        )
        return json.loads(response.text.strip())
    except Exception as e:
        print(f"Error grading {student_name}: {e}")
        return None

# --- MAIN EXECUTION ---
def main():
    golden_code = read_file_content(GOLDEN_ANSWERS_FILE)
    submissions = glob.glob(os.path.join(SUBMISSIONS_DIR, "*"))
    
    gradebook = []
    
    print(f"Found {len(submissions)} submissions. Starting grading with 60s delay...")
    
    for i, filepath in enumerate(submissions):
        filename = os.path.basename(filepath)
        student_name = get_student_name(filename)
        print(f"[{i+1}/{len(submissions)}] Grading {student_name} ({filename})...")
        
        student_code = read_file_content(filepath)
        result = grade_submission(student_name, student_code, golden_code)
        
        if result:
            gradebook.append(result)
            # Save individual Markdown feedback
            md_filename = f"GRADING_{filename}.md"
            md_path = os.path.join(QUIZ_DIR, md_filename)
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(f"# Grading Feedback: {student_name}\n\n")
                f.write(f"**Total Score: {result['total_score']}/100**\n\n")
                f.write("## Task Breakdown\n")
                for task in result['tasks']:
                    f.write(f"### Task {task['task']}\n")
                    f.write(f"- **Score:** {task['score']}/20\n")
                    f.write(f"- **Feedback:** {task['feedback']}\n\n")
                f.write(f"## Overall Feedback\n{result['overall_feedback']}\n")
            print(f"  - Saved feedback to {md_filename}")
        else:
            print(f"  - FAILED to grade {student_name}")
            
        # 1-minute delay to honor rate limits (except for the last one)
        if i < len(submissions) - 1:
            print("  - Waiting 60 seconds for next request...")
            time.sleep(60)

    # Save consolidated Gradebook
    with open(GRADEBOOK_JSON, 'w', encoding='utf-8') as f:
        json.dump(gradebook, f, indent=2)
        
    with open(GRADEBOOK_MD, 'w', encoding='utf-8') as f:
        f.write("# Quiz 2 Gradebook\n\n")
        f.write("| Student Name | Total Score |\n")
        f.write("| :--- | :--- |\n")
        for entry in sorted(gradebook, key=lambda x: x['student_name']):
            f.write(f"| {entry['student_name']} | {entry['total_score']} |\n")
    
    print(f"\nGrading complete! Gradebook saved to {GRADEBOOK_MD}")

if __name__ == "__main__":
    main()
