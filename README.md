# 520-Exercise Collection

This repository contains exercises and experiments for code generation, testing, and evaluation using various LLMs and benchmarks.

---

## **Exercise 1 (ex1/)**

### Project Structure

---

#### **Top-Level Overview**

##### 1. `AppsDataset/`  

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

##### 2. **`HumanEval/`**

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

##### 3. **`1/`**  

**Purpose:** Holds academic exercise PDFs.

- `Exercise1.pdf` — The PDF for the first exercise.

---

##### 4. **`Part 3/`**

**Purpose:** Advanced experimentation or supervised coding orchestration.

- `main.py` —  

  - A supervisor-coder (Gemini-Llama) chat-loop for automated code review.

  - Integrates Gemini (Google) and Llama (Groq) APIs for "junior vs senior" code review and multi-turn improvement of function implementations based on natural language prompts.

  - Useful for human-AI and AI-AI collaborative research.

---

#### **Purpose & Usage Examples**

##### - **Raw Problem Data and Metadata**

  - Use `AppsDataset/apps.json` for bulk problem ingestion.

  - Use `HumanEval/human-eval-v2-20210705.jsonl` for fine-tuned generative model evaluation.

##### - **Automated and Interactive Testing**

  - Use `test.py` in `AppsDataset/` to convert raw dataset I/O to easier-to-use test JSON.

##### - **Research Experiments**

  - Use `AppsDataset/problem1/` and `/problem2/` to compare Llama, Qwen, and other LLMs on the same tasks.

##### - **Development and AI Chat**

  - Use `Part 3/main.py` to experiment with multi-turn AI code review loops.

---

#### **Subfolder Relationships**

- **`AppsDataset/problem1/` and `/problem2/`** expand the main dataset with model-specific research outcomes or test sets.

- **`HumanEval/`** holds a standard benchmark as well as its problem breakdowns.

- **`Part 3/`** is a development/research "lab" for orchestrating AI-based code evaluation and supervision.

---

#### **Quick Reference Table**

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

#### **How to Add to the Collection**

- For a new competition or platform, add a JSON entry to `AppsDataset/apps.json`.

- To run a new experiment, add a new notebook under `AppsDataset/problemX/`.

- To test an evaluated problem, use or add scripts like `test.py` to process and validate results.

---

#### **For New Users**

- To get started, review `AppsDataset/apps.json` and `HumanEval/human-eval-v2-20210705.jsonl` to understand the structure of problems and test cases.

- Use `Part 3/main.py` to experiment with AI-augmented solving, fix your API keys, and run the supervisor loop.

---

_This project is highly modular, supporting new models, code review strategies, and test case expansions as required._

---

## **Exercise 2 (ex2/)**

### Project Structure

---

#### **Top-Level Overview**

Exercise 2 focuses on systematic testing, code coverage analysis, and evaluation of code generation solutions across different problem domains. It is organized into three main parts:

---

##### 1. **`Part1/`**

**Purpose:** Initial testing framework setup and baseline solution testing for both APPS and HumanEval benchmarks.

**Structure:**

- **`APPS/`**: Competitive programming problems from the APPS dataset
  - **`p1/`**: Sparrow problem
    - `solution.py`: Solution implementation
    - `test_solutions.py`: Pytest-based test suite
    - `test_cases.json`: Test cases loaded from JSON
  - **`p2/`**: Bracket problem
    - `solution.py`: Solution implementation
    - `test_solutions.py`: Pytest-based test suite
    - `test_cases.json`: Test cases loaded from JSON

- **`HumanEval/`**: OpenAI HumanEval benchmark problems
  - **`p1/`**: Intersperse problem (HumanEval/5)
    - `solution.py`: Solution implementation (`func1`)
    - `test_solutions.py`: Pytest test suite extracting test cases from JSON
    - `p5.json`: Problem definition and test cases
  - **`p2/`**: Parse nested parentheses problem (HumanEval/6)
    - `solution.py`: Solution implementation (`test1`)
    - `test_solutions.py`: Pytest test suite extracting test cases from JSON
    - `p6.json`: Problem definition and test cases

**Key Features:**
- Standardized test structure using `pytest`
- JSON-based test case loading with `load_test_cases()` helper function
- Iterative test execution pattern matching APPS testing methodology
- Support for pytest coverage tracking

---

##### 2. **`Part2/`**

**Purpose:** Expanded solution implementations with additional branches and edge case handling for improved code coverage.

**Structure:**

- **`p1/`**: Enhanced Sparrow problem solution
  - `solution.py`: Extended solution with type checking, value validation, and additional branches
  - `test_solutions.py`: Comprehensive test suite covering all branches
  - `test_cases.json`: Test cases for validation
  - `Ex2Part2APPSsparrow.ipynb`: Experimental notebook with analysis

- **`p2/`**: Enhanced Bracket problem solution
  - `solution.py`: Extended solution with additional validation
  - `test_solutions.py`: Comprehensive test suite
  - `test_cases.json`: Test cases for validation
  - `Ex2Part2APPSbracket.ipynb`: Experimental notebook with analysis

**Key Features:**
- Solutions include untested branches for coverage analysis:
  - Type checking (TypeError handling)
  - Value validation (ValueError handling)
  - Edge case handling
- Extended test suites with pytest.raises() for exception testing
- Coverage analysis to identify missed branches
- Jupyter notebooks for interactive experimentation

---

##### 3. **`Part3/`**

**Purpose:** Testing and evaluation of buggy/incorrect solution implementations to understand failure modes and improve test quality.

**Structure:**

- **`p1/`**: Buggy Sparrow problem solution
  - `buggy_solutions.py`: Incorrect implementation with logical errors
  - `test_solutions.py`: Test suite that identifies bugs and tests edge cases
  - `test_cases.json`: Test cases that expose bugs

- **`p2/`**: Buggy Bracket problem solution
  - `buggy_solutions.py`: Incorrect implementation with logical errors
  - `test_solutions.py`: Test suite that identifies bugs and tests edge cases
  - `test_cases.json`: Test cases that expose bugs

**Key Features:**
- Intentional buggy implementations for testing purposes
- Comprehensive test suites that catch logical errors
- Edge case testing (invalid inputs, boundary conditions)
- Exception testing for error handling
- Analysis of failure modes and test coverage gaps

---

#### **Testing Framework**

All parts use a consistent testing framework:

**Common Pattern:**
```python
from solution import func1
import pytest
import json

def load_test_cases(filename):
    """A helper function to load test cases from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)

def test_problem():
    test_cases = load_test_cases('./test_cases.json')
    for case in test_cases:
        input_str = case['input']
        expected_output = str(case['output'])
        # Parse inputs, run function, assert results
        assert actual_output == expected_output
```

**Running Tests:**
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=solution test_solutions.py

# Run specific test file
pytest Part1/APPS/p1/test_solutions.py
```

---

#### **Purpose & Usage Examples**

##### - **Part 1: Baseline Testing**
  - Establish testing framework and patterns
  - Create baseline test suites for APPS and HumanEval problems
  - Verify basic functionality and correctness

##### - **Part 2: Coverage Analysis**
  - Identify untested code branches
  - Add comprehensive test cases for edge cases
  - Improve code coverage metrics
  - Analyze test quality and completeness

##### - **Part 3: Bug Detection**
  - Test buggy implementations to understand failure modes
  - Develop robust test suites that catch logical errors
  - Improve test quality through negative testing
  - Analyze coverage gaps in buggy code

---

#### **Quick Reference Table**

| Folder/File                           | Purpose/Contents                                                                                 |
|---------------------------------------|-------------------------------------------------------------------------------------------------|
| `Part1/APPS/p1/`                      | Baseline Sparrow problem with solution and tests                                                 |
| `Part1/APPS/p2/`                      | Baseline Bracket problem with solution and tests                                                 |
| `Part1/HumanEval/p1/`                 | HumanEval/5 (Intersperse) with solution and tests                                                |
| `Part1/HumanEval/p2/`                 | HumanEval/6 (Parse nested parens) with solution and tests                                        |
| `Part2/p1/`                           | Enhanced Sparrow solution with extended coverage and notebooks                                   |
| `Part2/p2/`                           | Enhanced Bracket solution with extended coverage and notebooks                                   |
| `Part3/p1/`                           | Buggy Sparrow solution for failure mode analysis                                                 |
| `Part3/p2/`                           | Buggy Bracket solution for failure mode analysis                                                 |

---

#### **Key Differences: Part 1 vs Part 2 vs Part 3**

| Aspect               | Part 1                          | Part 2                          | Part 3                          |
|----------------------|---------------------------------|---------------------------------|---------------------------------|
| **Purpose**          | Baseline testing                | Coverage analysis               | Bug detection                   |
| **Solutions**        | Basic implementations           | Extended with validation        | Intentional bugs                |
| **Test Focus**       | Functional correctness          | Branch coverage                 | Failure modes                   |
| **Test Types**       | Basic assertions                | Exception testing + assertions  | Negative testing + edge cases   |
| **Notebooks**        | None                            | Analysis notebooks              | None                            |

---

#### **How to Use**

##### **Running Tests:**
```bash
# From ex2/ directory
cd Part1/APPS/p1
pytest test_solutions.py

# With coverage
pytest --cov=solution --cov-report=html test_solutions.py
```

##### **Adding New Problems:**
1. Create a new problem folder (e.g., `p3/`)
2. Add `solution.py` with your implementation
3. Create `test_solutions.py` following the standard pattern
4. Add `test_cases.json` or problem JSON file
5. Run tests to verify correctness

##### **Coverage Analysis:**
1. Run tests with coverage: `pytest --cov=solution test_solutions.py`
2. Identify untested branches in `solution.py`
3. Add test cases for missing coverage
4. Re-run coverage to verify improvement

---

#### **For New Users**

1. **Start with Part 1**: Understand the basic testing framework and patterns
2. **Explore Part 2**: See how extended solutions and comprehensive tests improve coverage
3. **Study Part 3**: Learn how to identify and test for bugs and edge cases
4. **Run Examples**: Execute test suites to see the testing framework in action
5. **Experiment**: Modify solutions and tests to understand the testing process

---

#### **Dependencies**

- `pytest`: Testing framework
- `pytest-cov`: Coverage plugin (optional)
- `json`: For loading test cases
- Standard library: `typing`, `re`, `ast` (as needed)

---

_Exercise 2 provides a comprehensive framework for testing code generation solutions, analyzing coverage, and understanding failure modes through systematic testing methodologies._
