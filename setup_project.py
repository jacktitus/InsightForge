import os

Folders = [
    "data",
    "profiler",
    "engine",
    "ai_layer",
    "reports",
]

Files = {
    "main.py":" ",
    "requirements.txt":" ", 
    "data/sample_data.csv":" ",
    "profiler/__init__.py":" ",
    "profiler/data_profiler.py":" ",
    "engine/__init__.py":" ",
    "engine/data_engine.py":" ",
    "ai_layer/__init__.py":" ",
    "ai_layer/llm_client.py":" ",
    "reports/__init__.py":" ",
    "reports/prompt_builder.py":" ",
}

for folder in Folders:
    os.makedirs(folder, exist_ok=True)

for file_path, content in Files.items():
    with open(file_path,'w') as f:
        f.write(content)