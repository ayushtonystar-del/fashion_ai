import gradio as gr
import requests

def generate(query):

    response = requests.get(
        "http://127.0.0.1:8000/generate-fashion",
        params={"query": query}
    )

    data = response.json()

    return (
        data["prompt"],
        data["image_path"]
    )

demo = gr.Interface(
    fn=generate,

    inputs=gr.Textbox(
        label="Fashion Query"
    ),

    outputs=[
        gr.Textbox(
            label="Generated Prompt"
        ),
        gr.Image(
            label="Fashion Design"
        )
    ],

    title="AI Fashion Assistant"
)

demo.launch()