from transformers import pipeline
import gradio as gr

model = pipeline("summerization")

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

with gr.Blocks() as demo:
    textbox = gr.Textbox(label="Input Text", lines=10, placeholder="Enter text to summarize...")
    gr.Interface(fn=predict, inputs=textbox, outputs="text").render()

demo.launch()


