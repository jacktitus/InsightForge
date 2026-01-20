import pandas as pd
from profiler.data_profiler import profile_dataset
from engine.data_engine import suggest_strategy
from reports.prompt_builder import build_prompt
from ai_layer.llm_client import call_ai

df = pd.read_csv('data/sample_data.csv')

targetcol = 'churn'  # specify your target column here

#run profiling
profile = profile_dataset(df,targetcol)

suggestions = suggest_strategy(profile)

prompt = build_prompt(profile,suggestions)

report = call_ai(prompt)

for key, value in profile.items():
    print(f"{key}: {value}")

print("\n===== SYSTEM SUGGESTIONS =====\n")
for s in suggestions:
    print('-',s)
print("\n===== PROMPT SENT TO AI =====\n")
print(prompt)
print("\n===== AI REPORT =====\n")
print(report)