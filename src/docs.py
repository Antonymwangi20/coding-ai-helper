# src/docs.py

import os
import json

DOCS_PATH = "./docs"

def load_docs(language="python"):
    file_path = os.path.join(DOCS_PATH, f"{language}_docs.json")
    if not os.path.exists(file_path):
        return "📚 No offline documentation found for that language."
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return "❌ Failed to parse documentation JSON."

def search_docs(term, language="python"):
    docs = load_docs(language)
    if isinstance(docs, str):
        return docs
    matches = [doc for doc in docs if term.lower() in doc.get("title", "").lower()]
    if not matches:
        return "❌ No documentation entries matched your search."
    return matches[:5]

if __name__ == "__main__":
    print("📖 Search results for 'list':")
    results = search_docs("list", "python")
    if isinstance(results, list):
        for entry in results:
            print(f"🔹 {entry['title']}: {entry['content'][:100]}...")
    else:
        print(results)
