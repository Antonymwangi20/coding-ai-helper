# src/generate.py

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

class DevForgeGenerator:
    def __init__(self, model_name="Salesforce/codet5-base"):
        print("🚀 Loading CodeT5 model... (may take a moment)")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def generate_code(self, prompt: str, max_length: int = 256) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True)
        output_ids = self.model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=max_length,
            num_beams=5,
            early_stopping=True
        )
        return self.tokenizer.decode(output_ids[0], skip_special_tokens=True)

if __name__ == "__main__":
    gen = DevForgeGenerator()
    prompt = "create a todo app using react"
    print(gen.generate_code(prompt))
