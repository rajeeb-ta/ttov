# %cd /content/ttovai
import subprocess
import gradio as gr
import time

# Start ComfyUI in background
process = subprocess.Popen(
    [
        "python",
        "../main.py",
        "--listen",
        "0.0.0.0",
        "--port",
        "8188"
    ]
)

time.sleep(10)

def status():
    return "ComfyUI is running on port 8188"

app = gr.Interface(
    fn=status,
    inputs=[],
    outputs="text",
    title="ComfyUI Launcher"
)

app.launch(share=True)