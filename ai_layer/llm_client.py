

def call_ai(prompt):
    
    """
    This function will later call a real AI API.
    For now, it just returns the prompt for testing.
    """
    return "\n--- AI WOULD pGENERATE REPORT FROM THIS PROMPT ---\n" + prompt

"" client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) def call_ai(prompt):    
    response = client.chat.completions.create(         
        model="gpt-4o-mini",         
        messages=[{"role": "user", "content": prompt}],         
        temperature=0.3     )     
    return response.choices[0].mess age.content ""
