# src/explainer.py

import re

def explain_code(code: str) -> str:
    if not code.strip():
        return "⚠️ No code provided."

    explanation = []
    lines = code.splitlines()

    for i, line in enumerate(lines, start=1):
        stripped = line.strip()

        # Function
        if stripped.startswith("def "):
            fn_name = re.findall(r'def (\w+)', stripped)
            if fn_name:
                explanation.append(f"🔧 Line {i}: Defines a function named `{fn_name[0]}`.")
            else:
                explanation.append(f"🔧 Line {i}: Function definition detected.")

        # Class
        elif stripped.startswith("class "):
            cls_name = re.findall(r'class (\w+)', stripped)
            if cls_name:
                explanation.append(f"🏛️ Line {i}: Declares a class named `{cls_name[0]}`.")
            else:
                explanation.append(f"🏛️ Line {i}: Class declaration found.")

        # Imports
        elif stripped.startswith("import ") or "import " in stripped:
            modules = re.findall(r'import (\w+)', stripped)
            for mod in modules:
                explanation.append(f"📦 Line {i}: Imports module `{mod}`.")

        # Assignments
        elif "=" in stripped and not stripped.startswith(("if ", "for ", "while ")):
            explanation.append(f"📝 Line {i}: Assignment statement: `{stripped}`.")

        # Print
        elif "print" in stripped:
            explanation.append(f"🖨️ Line {i}: Prints to console with: `{stripped}`.")

        # Return
        elif stripped.startswith("return"):
            explanation.append(f"🔁 Line {i}: Returns value: `{stripped}`.")

        # Loops
        elif stripped.startswith("for ") or stripped.startswith("while "):
            explanation.append(f"🔂 Line {i}: Loop construct: `{stripped}`.")

        # Conditionals
        elif stripped.startswith("if "):
            explanation.append(f"🤔 Line {i}: Conditional check: `{stripped}`.")

        # Empty or other
        elif stripped:
            explanation.append(f"📄 Line {i}: Executes statement: `{stripped}`.")

    return "\n".join(explanation) if explanation else "ℹ️ No recognizable logic patterns found."
