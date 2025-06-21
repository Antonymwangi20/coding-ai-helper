# src/trainer.py

def train_locally(code_examples, labels):
    if len(code_examples) != len(labels):
        return "❌ Error: Number of examples and labels must match."

    print("🧠 Simulating local fine-tuning process...\n")
    for i, (code, label) in enumerate(zip(code_examples, labels)):
        print(f"[{i+1}] Prompt: {code[:40]}...\n     Label: {label[:40]}...\n")

    print("✅ Simulated training complete. (No real model changes in this stub)")
    return "🔄 DevForge model has been locally adjusted (simulated)."

if __name__ == "__main__":
    training_data = [
        "def add(a, b): return a + b",
        "console.log('Hello World');"
    ]
    labels = [
        "Function that adds two numbers in Python.",
        "Logs 'Hello World' in JavaScript."
    ]

    result = train_locally(training_data, labels)
    print(result)
