# Project Structure: `ex/` Directory

This directory is organized for advanced algorithmic, AI, and problem-solving experimentation, structured into thematic and utility subfolders. Below is an overview of the major components and their purposes:

---

## **Top-Level Overview**

### 1. `AppsDataset/`  
**Purpose:** Houses datasets, benchmarks, and experiment results for competitive programming ("apps") problems—useful for testing, evaluation, and tracking performance on various platforms like Codeforces.

Contains:
- **`apps.json`**:  
  A large consolidated dataset. Each entry typically has:
  - `id`: Numeric identifier.
  - `question`: Problem description (often from competitive programming).
  - `solutions`: Array of accepted solution strings in Python.
  - `input_output`: Example input/output pairs for testing.
  - `difficulty`, `url`, etc.

- **`problem1/` and `problem2/`**:  
  - Contain experiment notebooks (`.ipynb`), JSON datasets, and test cases for *specific* problems.
  - Example:  
    - `failedSet1Llama.ipynb`, `QwenPart2TestingP1.ipynb`: Results for Llama and Qwen models on Problem 1.
    - `p1.json`: Additional problem-specific metadata.
    - `test_cases.json`: Canonical test cases for automated evaluation.

- **`test.py`**:  
  - Script to extract, clean, and save test cases from the datasets to JSON, used for systematic testing.

---

### 2. **`HumanEval/`**
**Purpose:** Stores test, experimental, and official datasets for open-ended code generation and evaluation—modeled after OpenAI's "HumanEval" benchmarks.

Contains:
- Problem-specific subfolders:  
  - **`p1/`, `p2/`, ... `p8/`**:  
    Each holds a JSON file (e.g., `p1.json`) defining the problem and related artifacts (sometimes supporting files like notebooks for interactive solving or validation).
- **`human-eval-v2-20210705.jsonl`**:  
  A large JSONL-formatted set of human evaluation problems.
- **`fexEx.json`**:  
  Auxiliary data, possibly for problem variants or experiment configs.

---

### 3. **`1/`**  
**Purpose:** Holds academic exercise PDFs.
- `Exercise1.pdf` — The PDF for the first exercise.

---

### 4. **`Part 3/`**
**Purpose:** Advanced experimentation or supervised coding orchestration.
- `main.py` —  
  - A supervisor-coder (Gemini-Llama) chat-loop for automated code review.
  - Integrates Gemini (Google) and Llama (Groq) APIs for "junior vs senior" code review and multi-turn improvement of function implementations based on natural language prompts.
  - Useful for human-AI and AI-AI collaborative research.

---

## **Purpose & Usage Examples**

### - **Raw Problem Data and Metadata**
  - Use `AppsDataset/apps.json` for bulk problem ingestion.
  - Use `HumanEval/human-eval-v2-20210705.jsonl` for fine-tuned generative model evaluation.

### - **Automated and Interactive Testing**
  - Use `test.py` in `AppsDataset/` to convert raw dataset I/O to easier-to-use test JSON.

### - **Research Experiments**
  - Use `AppsDataset/problem1/` and `/problem2/` to compare Llama, Qwen, and other LLMs on the same tasks.

### - **Development and AI Chat**
  - Use `Part 3/main.py` to experiment with multi-turn AI code review loops.

---

## **Subfolder Relationships**
- **`AppsDataset/problem1/` and `/problem2/`** expand the main dataset with model-specific research outcomes or test sets.
- **`HumanEval/`** holds a standard benchmark as well as its problem breakdowns.
- **`Part 3/`** is a development/research "lab" for orchestrating AI-based code evaluation and supervision.

---

## **Quick Reference Table**

| Folder/File                       | Purpose/Contents                                                                                 |
|------------------------------------|-------------------------------------------------------------------------------------------------|
| `AppsDataset/apps.json`            | Main problem dataset with solutions and test inputs/outputs.                                     |
| `AppsDataset/problem1/`            | Notebooks/results for Problem 1 model experiments.                                              |
| `AppsDataset/problem2/`            | Notebooks/results for Problem 2 model experiments.                                              |
| `AppsDataset/test.py`              | Script to parse dataset entries and save canonical test cases as JSON.                          |
| `HumanEval/`                       | Benchmark problems and variants for human-level code evaluation.                                |
| `HumanEval/p1/`, ...`p8/`          | Each holds a specific HumanEval problem and its artifacts.                                      |
| `1/Exercise1.pdf`                  | Academic exercise or assignment description.                                                    |
| `Part 3/main.py`                   | Experimental supervised AI code chat/review system (Gemini+Llama, multi-turn).                  |

---

## **How to Add to the Collection**
- For a new competition or platform, add a JSON entry to `AppsDataset/apps.json`.
- To run a new experiment, add a new notebook under `AppsDataset/problemX/`.
- To test an evaluated problem, use or add scripts like `test.py` to process and validate results.

---

## **For New Users**
- To get started, review `AppsDataset/apps.json` and `HumanEval/human-eval-v2-20210705.jsonl` to understand the structure of problems and test cases.
- Use `Part 3/main.py` to experiment with AI-augmented solving, fix your API keys, and run the supervisor loop.

---

_This project is highly modular, supporting new models, code review strategies, and test case expansions as required._
