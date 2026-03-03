
import os
import glob
import google.generativeai as genai
from dotenv import load_dotenv
import json
import csv


# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("Warning: GEMINI_API_KEY not found in environment variables. Please set it in the .env file.")
    # We continue so the script can at least import packages and fail gracefully later if needed, 
    # but practically we should probably stop if we want to be strict. 
    # For now, let's let it crash at generation if key is missing to verify setup.

if API_KEY:
    genai.configure(api_key=API_KEY)

# Configuration
# User requested "gemini 3 flash". As of early 2025/2026, 1.5 Flash is standard. 
# If 2.0 or 3.0 is available, update this. 
# We'll use a placeholder that usually points to the latest efficient model or specifically 1.5 Flash.
MODEL_NAME = "gemini-2.5-flash" 

generation_config = {
  "temperature": 0.1, # Lower temperature for more consistent grading
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

def get_model():
    return genai.GenerativeModel(
      model_name=MODEL_NAME,
      generation_config=generation_config,
    )

def format_quiz_context(quiz_file_path="quiz.ipynb"):
    """Reads the quiz notebook and extracts markdown/code cells as context."""
    if not os.path.exists(quiz_file_path):
        return "Error: quiz.ipynb not found. Please ensure it is in the same directory."
    
    try:
        with open(quiz_file_path, "r", encoding="utf-8") as f:
            nb_data = json.load(f)
        
        context = "Here is the Quiz Content (consisting of multiple Problems wrapped in a Jupyter Notebook structure):\n\n"
        
        for index, cell in enumerate(nb_data.get("cells", [])):
            cell_type = cell.get("cell_type", "unknown")
            source_lines = cell.get("source", [])
            source_text = "".join(source_lines)
            
            context += f"--- Cell {index+1} ({cell_type}) ---\n"
            context += source_text + "\n\n"
            
        return context
    except Exception as e:
        return f"Error reading quiz notebook: {e}"

def grade_submission(student_content, quiz_context):
    model = get_model()
    prompt = f"""
    You are an expert automated teaching assistant. Your task is to grade a student's quiz submission against the provided answer key.
    
    CONTEXT:
    {quiz_context}
    
    STUDENT SUBMISSION:
    ---
    {student_content}
    ---
    
    INSTRUCTIONS:
    1.  **Analyze** each answer provided by the student.
    2.  **Compare** it strictly but fairly against the correct solution.
    3.  **Grade** each question on a scale of 0 to 10.
    4.  **Provide Feedback**: Explain why points were deducted or commend good answers.
    5.  **Calculate** the final total score out of 100 (assuming equal weight unless specified otherwise, or normalize the sum of question scores).
    6.  **Summary**: Write a encouraging but constructive summary of the student's performance.

    OUTPUT FORMAT:
    Please verify the output is valid Markdown.
    
    # Grading Report for Student Submission
    
    ## Question-by-Question Assessment
    
    ... [Details for each question] ...
    
    ## Overall Feedback
    [Your summary here]
    
    **FINAL SCORE: [Score]/100**
    """
    
    response = model.generate_content(prompt)
    return response.text

def main():
    if not API_KEY:
        print("Error: API Key is missing. Please check your .env file.")
        return

    submissions_dir = "student-submissions"
    # Look for common text-based source files
    submission_files = []
    for ext in ["*.ipynb", "*.py", "*.md"]:
        submission_files.extend(glob.glob(os.path.join(submissions_dir, ext)))
    
    if not submission_files:
        print(f"No submission files found in {submissions_dir}")
        return

    master_report = "MASTER_GRADE_REPORT.csv"
    
    # Initialize master report
    file_exists = os.path.isfile(master_report)
    with open(master_report, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Student File", "Score", "Summary Link"])

    print(f"Found {len(submission_files)} submissions.")

    quiz_ctx = format_quiz_context("quiz.ipynb")

    for sub_file in submission_files:
        print(f"Grading {sub_file}...")
        
        try:
            with open(sub_file, "r", encoding="utf-8") as f:
                student_content = f.read()
            
            feedback = grade_submission(student_content, quiz_ctx)
            
            # Save individual feedback
            base_name = os.path.basename(sub_file)
            feedback_filename = f"GRADING_{base_name}.md" 
            
            with open(feedback_filename, "w", encoding="utf-8") as f:
                f.write(feedback)
            
            # Extract score for master report
            score = "N/A"
            for line in feedback.splitlines():
                if "**FINAL SCORE:" in line or "FINAL SCORE:" in line:
                    # simplistic extraction, can be improved with regex
                    score = line.split(":")[-1].strip().replace("**", "").replace("/100", "")
            
            # Append to master report
            with open(master_report, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([base_name, score, feedback_filename])
                
        except Exception as e:
            print(f"Error grading {sub_file}: {e}")

    print(f"Grading complete! Check {master_report} and individual feedback files.")

if __name__ == "__main__":
    main()
