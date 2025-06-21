# src/serve.py

import gradio as gr
from generate import DevForgeGenerator

gen = DevForgeGenerator()

def handle_prompt(prompt):
    code = gen.generate_code(prompt)
    return code

ui = gr.Interface(
    fn=handle_prompt,
    inputs=[
        gr.Textbox(placeholder="Ask: Build a todo app in React", label="Prompt"),
        gr.Audio(source="microphone", type="filepath", label="Voice Input (Coming Soon)")
    ],
    outputs=gr.Code(language="python", label="Generated Code"),
    title="DevForge AI Assistant",
    description="Offline AI coding assistant for developers — supports prompts like: 'build a flask API'"
)

if __name__ == "__main__":
    ui.launch()
