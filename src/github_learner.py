# src/github_learner.py

import requests

def fetch_github_snippets(query, language="python", max_results=3):
    url = f"https://api.github.com/search/code?q={query}+language:{language}"
    headers = {"Accept": "application/vnd.github.v3+json"}
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        items = r.json().get("items", [])[:max_results]
        return [item.get("html_url", "N/A") for item in items]
    except Exception as e:
        return [f"Error: {e}"]

if __name__ == "__main__":
    results = fetch_github_snippets("flask rest api", "python")
    print("Top GitHub results:")
    for url in results:
        print("→", url)
