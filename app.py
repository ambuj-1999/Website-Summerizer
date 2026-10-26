import gradio as gr
from summerizer import summarize_website

gr.Interface(
    fn=summarize_website,
    inputs=gr.Textbox(label="Enter the website URL"),
    outputs=gr.Textbox(label="Summary"),
    title="🔍AI Website Summarizer",
).launch(share=True)