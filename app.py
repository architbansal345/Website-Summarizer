import gradio as gr
from summarizer import summarize_text

gr.Interface(
    fn=summarize_text, 
    inputs=gr.Textbox(label="Enter the URL of the website to summarize"),
    outputs=gr.Textbox(label="Summary"),
    title="Website Summarizer",
    description="Enter the URL of the website to summarize",
    # theme="compact"
).launch(share=True)