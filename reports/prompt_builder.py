def build_prompt(profile,suggestions):
    prompt = f"""
    You are a senior data scientist acting as an AI Research Assistant.
    
    Dataset Overview:
    - Rows: {profile.get('rows')}
    - Columns: {profile.get('columns')}
    - Numerical Features: {profile.get('numerical_columns', [])}
    - Categorical Features: {profile.get('categorical_columns', [])}
    - Target Column: {profile.get('target')}

   Data Quality:
    - Missing Values (% per column): {profile.get('missing', {})}
    - Class Imbalance Ratio: {profile.get('imbalance_ratio')}
    
System Observations & Recommendations:

"""
    for s in suggestions:
        prompt += f"- {s}\n"
    prompt +="""
Your Task:
1. Identify the key data quality issues.
2. Explain why each preprocessing step is necessary.
3. Recommend suitable machine learning models and justify them.
4. Highlight risks and pitfalls.
5. Propose a clean end-to-end ML pipeline.

Write in a professional tone, as if advising a real analytics team.
"""

    return prompt