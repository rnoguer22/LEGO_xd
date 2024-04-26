import gradio as gr

def color_reco(image):
    return 'Imagen subida'

gr.Interface(fn=color_reco, inputs=gr.Image(), outputs="text").launch()
