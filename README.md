# 🚀 PyForge - Python Project Reverse Engineer & Static Code Analyzer

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-Report-red?style=for-the-badge)
![NetworkX](https://img.shields.io/badge/NetworkX-Graphs-green?style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

</p>

---

## 📌 Overview

**PyForge** is a Python Static Code Analysis and Project Reverse Engineering tool that helps developers understand any Python codebase quickly.

Instead of manually exploring hundreds of files, PyForge automatically scans an entire project, extracts useful software metrics, detects code smells, measures code quality, visualizes dependencies, and generates an interactive dashboard along with a professional HTML report.

The project was built as a lightweight developer productivity tool inspired by modern static analysis platforms such as SonarQube, Radon, and Pylint.

---

## ✨ Key Features

### 📂 Project Analysis

- Recursive project scanning
- Automatic Python file discovery
- Project summary generation
- File-level statistics

---

### 📊 Code Metrics

PyForge extracts useful metrics including:

- Lines of Code (LOC)
- Number of Classes
- Number of Functions
- Number of Imports
- Comment Count
- Blank Lines
- Average Function Length

---

### 📈 Code Quality Analysis

PyForge evaluates software quality using:

- Cyclomatic Complexity
- Maintainability Index
- Health Score
- Project Health Status

---

### 🔍 Code Smell Detection

Automatically detects common issues including:

- Long Functions
- Large Classes
- Deep Nesting
- Excessive Parameters
- Long Files

---

### 🕸 Dependency Graph

Generates a visual dependency graph showing module relationships inside the project using NetworkX and Matplotlib.

---

### 📄 HTML Report Generation

Creates a professional HTML report containing:

- Project Summary
- Metrics
- Charts
- Health Score
- Complexity Analysis
- Code Smells
- Dependency Graph

---

### 📊 Interactive Dashboard

Built using **Streamlit**, the dashboard provides:

- KPI Cards
- Interactive Charts
- File Statistics
- Complexity Rankings
- Maintainability Analysis
- Project Health Visualization

---

## 🖥 Dashboard Preview

### Dashboard

![Dashboard](screenshots/dashboard.png)

---

### Analytics

![Charts](screenshots/charts.png)

---

### Code Smells

![Code Smells](screenshots/smells.png)

---

### HTML Report

![HTML Report](screenshots/report.png)

---

# 🏗 System Architecture

```text
                 +------------------------+
                 |     Python Project     |
                 +-----------+------------+
                             |
                             ▼
                  Project Scanner
                             |
         +-------------------+-------------------+
         |                   |                   |
         ▼                   ▼                   ▼
    AST Parser         Metrics Engine     Dependency Analyzer
         |                   |                   |
         +-------------------+-------------------+
                             |
                             ▼
                    Project Analyzer
                             |
        +--------------------+--------------------+
        |                                         |
        ▼                                         ▼
 Streamlit Dashboard                     HTML Report Generator
```

---

# 📂 Project Structure

```text
PyForge/
│
├── assets/
│   └── templates/
│       └── report_template.html
│
├── pyforge/
│   ├── scanner.py
│   ├── parser.py
│   ├── metrics.py
│   ├── complexity.py
│   ├── maintainability.py
│   ├── dependency.py
│   ├── code_smells.py
│   ├── project_analyzer.py
│   └── report_generator.py
│
├── reports/
│
├── screenshots/
│
├── streamlit_app.py
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| AST | Source Code Parsing |
| Streamlit | Interactive Dashboard |
| Plotly | Interactive Charts |
| NetworkX | Dependency Graph |
| Matplotlib | Graph Visualization |
| Jinja2 | HTML Report Generation |
| Pandas | Data Processing |
| HTML/CSS | Report Styling |

---

# ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/Yashvardhan0901/PyForge.git
```

Move into the project directory:

```bash
cd PyForge
```

Create a virtual environment (recommended):

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

# 🚀 Running PyForge

Launch the Streamlit dashboard:

```bash
streamlit run streamlit_app.py
```

The application will open in your default web browser.

Select a Python project folder and start the analysis.

---

# 📄 Generated Outputs

PyForge automatically generates:

- Interactive Streamlit Dashboard
- Dependency Graph
- HTML Analysis Report
- Project Metrics Summary
- Code Smell Analysis
- Complexity Rankings
- Maintainability Report

Generated reports are saved in:

```text
reports/
```

---

# 🔍 Example Analysis Workflow

1. Select a Python project.
2. Scan all Python files.
3. Parse source code using Python AST.
4. Extract project metrics.
5. Calculate Cyclomatic Complexity.
6. Compute Maintainability Index.
7. Detect Code Smells.
8. Build Dependency Graph.
9. Display results in Streamlit.
10. Generate a professional HTML report.