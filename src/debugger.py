import ast

def debug_code(code: str):
    try:
        ast.parse(code)
        return "✅ No syntax errors detected."
    except SyntaxError as e:
        return f"❌ Syntax Error on line {e.lineno}: {e.msg}"
    except Exception as e:
        return f"❌ Unknown error: {str(e)}"

if __name__ == "__main__":
    broken_code = "def func()\n  print('oops')"
    print(debug_code(broken_code))
