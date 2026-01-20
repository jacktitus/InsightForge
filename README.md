# InsightForge
InsightForge is an AI-ready Data Science Research Assistant that profiles datasets, detects data quality issues, applies rule-based data science reasoning, and generates expert-level analytical prompts and reports. It mimics how a senior data scientist thinks—bridging raw data to actionable ML strategy using modular Python architecture

# InsightForge – AI-Powered Data Science Research Assistant

InsightForge is a modular Python system that behaves like a junior-to-senior data scientist in code.

Given a dataset, it:
- Profiles the data (shape, types, missing values, target, imbalance)
- Applies rule-based data science reasoning
- Suggests preprocessing strategies and ML approaches
- Generates an expert-level analytical prompt/report
- Is fully AI-ready (LLM layer can be plugged in later)

This project demonstrates how real-world AI systems are engineered:
Data → Profiling → Reasoning → Prompt Engineering → Report Generation

It is designed for:
- Data analysts & ML learners
- Auto-ML style experimentation

## How to Run

1. Clone the repository:

git clone https://github.com/yourusername/InsightForge.git
cd InsightForge

2. Create and activate a virtual environment:

python -m venv venv

3. Install dependencies:

pip install -r requirements.txt
4.Place your dataset in the data/ folder
(or update the path in main.py).

5. Edit main.py and set your target column
6. Run the system:

data flow 

Dataset
↓
Data Profiler → Rule Engine → Prompt Builder → AI Layer
↓ ↓ ↓ ↓
Structure ML Reasoning Expert Prompt Final Report
