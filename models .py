
from transformers import pipeline

fashion_nlp = pipeline("text-generation", model="gpt2")

def generate_advice(preferences: str):
    result = fashion_nlp(f"Give fashion advice for {preferences}", max_length=50)
    return result[0]['generated_text']
    