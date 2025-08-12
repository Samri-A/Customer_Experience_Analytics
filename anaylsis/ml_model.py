from transformers import pipeline

print("Loading BART zero-shot classifier...")
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
print("Model loaded.")
