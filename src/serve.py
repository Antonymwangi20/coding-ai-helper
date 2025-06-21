import gradio as gr
from generate import DevForgeGenerator
from debugger import debug_code
from explainer import explain_code

generator = DevForgeGenerator()

def generate(prompt):
    return generator.generate_code(prompt)

def debug_and_explain(prompt):
    code = generator.generate_code(prompt)
    debug_result = debug_code(code)
    explanation = explain_code(code)
    return code, debug_result, explanation

ui = gr.Interface(
    fn=debug_and_explain,
    inputs=gr.Textbox(label="Prompt (e.g. 'Build a login page in Flask')"),
    outputs=[
        gr.Code(label="🧠 Generated Code"),
        gr.Textbox(label="🪲 Debug Result"),
        gr.Textbox(label="💬 Explanation"),
    ],
    title="DevForge AI Assistant",
    description="AI-Powered Offline Coding Helper — Generate • Debug • Understand Code"
)

if __name__ == "__main__":
    ui.launch()
