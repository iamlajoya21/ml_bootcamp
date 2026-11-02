# ML Engineer Certification Exam Bank — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate two bilingual Jupyter notebooks: a 30-question sample exam and a 4-version, 100-question-per-version certification bank.

**Architecture:** A temporary Python build package defines 100 parameterized item templates across 10 topics, renders four parallel variants per template, and emits nbformat notebooks with student sections, coding cells, instructor keys, hidden tests, and rubrics.

**Tech Stack:** Python 3.13, nbformat, numpy, pandas, scikit-learn, torch, FastAPI/httpx.

## Global Constraints

- Bilingual English + Armenian for all student-facing content.
- Each version: 50 MCQ, 20 quick checks, 15 code-reading, 8 debug, 7 coding = 100 items.
- 90 minutes per version; 70% pass mark.
- Offline only: no dataset downloads during the exam.
- Do not commit changes unless explicitly requested.

---

### Task 1: Build package and rendering schema

**Files:**
- Create: `/var/folders/yj/59_sfbzx45154p29ff4rlyg80000gn/T/opencode/exam_build/common.py`
- Create: `/var/folders/yj/59_sfbzx45154p29ff4rlyg80000gn/T/opencode/exam_build/__init__.py`

- [ ] Define `Item` with id, topic, type, difficulty, bilingual stems/options, answer, explanation, variants, coding fields.
- [ ] Implement `render_item(item, variant_index)` using `string.Template.safe_substitute`.
- [ ] Implement option rotation and answer-index remapping.
- [ ] Implement markdown renderers for student questions, answer keys, coding tasks, and rubrics.
- [ ] Smoke-test rendering with one MCQ and one coding item.

### Task 2: Author Python, NumPy, and Pandas items

**Files:**
- Create: `/var/folders/.../exam_build/items_core.py`

- [ ] Author 8 Python/OOP templates (4 MCQ, 2 quick, 1 code-reading, 1 debug).
- [ ] Author 6 NumPy templates (3 MCQ, 1 quick, 1 code-reading, 1 coding).
- [ ] Author 11 Pandas/EDA templates (5 MCQ, 2 quick, 2 code-reading, 1 debug, 1 coding).
- [ ] Provide four variants per template with different data/options.
- [ ] Verify every rendered MCQ answer matches its options.

### Task 3: Author scikit-learn and ensembles items

**Files:**
- Create: `/var/folders/.../exam_build/items_ml.py`

- [ ] Author 16 scikit-learn/classical-ML templates (8 MCQ, 3 quick, 2 code-reading, 2 debug, 1 coding).
- [ ] Author 8 ensembles/unsupervised templates (4 MCQ, 2 quick, 1 code-reading, 1 debug).
- [ ] Cover leakage, metrics, pipelines, regularization, imbalance, CV, PCA, clustering.
- [ ] Verify four variants each and answer-key correctness.

### Task 4: Author NLP/LLM and deep-learning items

**Files:**
- Create: `/var/folders/.../exam_build/items_ai.py`

- [ ] Author 11 NLP/transformers/LLM/RAG templates (6 MCQ, 2 quick, 2 code-reading, 1 debug).
- [ ] Author 12 deep-learning templates (6 MCQ, 2 quick, 2 code-reading, 1 debug, 1 coding).
- [ ] Cover TF-IDF, attention, BERT, RAG, embeddings, CNNs, RNN/LSTM, PyTorch shapes and training.
- [ ] Verify four variants each and answer-key correctness.

### Task 5: Author time-series, recommender, and deployment items

**Files:**
- Create: `/var/folders/.../exam_build/items_ops.py`

- [ ] Author 8 time-series templates (4 MCQ, 2 quick, 1 code-reading, 1 coding).
- [ ] Author 8 recommender templates (4 MCQ, 2 quick, 1 code-reading, 1 coding).
- [ ] Author 12 deployment/API/MLOps templates (6 MCQ, 2 quick, 2 code-reading, 1 debug, 1 coding).
- [ ] Cover stationarity, ARIMA/Prophet, lag leakage, collaborative/content-based filtering, cold start, FastAPI, Docker, secrets, drift, monitoring.
- [ ] Verify four variants each and answer-key correctness.

### Task 6: Generate the question-bank notebook

**Files:**
- Create: `/var/folders/.../exam_build/build.py`
- Create: `exams/certification_question_bank.ipynb`

- [ ] Assemble Versions A–D from all 100 templates.
- [ ] Render cover page, rules, blueprint, timing guide, and sections.
- [ ] Add coding starter cells and visible example tests.
- [ ] Add instructor appendix per version: answer matrix, explanations, hidden tests, solutions, rubrics.
- [ ] Add coverage audit and scoring sheet.
- [ ] Write the notebook with nbformat.

### Task 7: Generate the sample notebook

**Files:**
- Create: `/var/folders/.../exam_build/sample.py`
- Create: `exams/certification_sample_exam.ipynb`

- [ ] Author 30 separate sample items mirroring the blueprint: 15 MCQ, 6 quick, 5 code-reading, 2 debug, 2 coding.
- [ ] Add 30-minute instructions, answer key, explanations, coding solutions, and rubric.
- [ ] Ensure sample items do not duplicate live-bank variants.

### Task 8: Validate and QA

- [ ] Run `python -m exam_build.validate` to check per-version counts and blueprint totals.
- [ ] Execute all coding reference solutions and hidden tests with `pytest`/asserts.
- [ ] Validate both notebooks open with `nbformat.read(..., as_version=4)`.
- [ ] Confirm every question has English and Armenian text.
- [ ] Confirm no missing answer-key entries.
- [ ] Report file paths, item counts, and validation results.
