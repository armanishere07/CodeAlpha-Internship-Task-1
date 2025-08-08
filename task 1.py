# %pip install googletrans==4.0.0rc1 gradio

from googletrans import Translator, LANGUAGES
import gradio as gr

translator = Translator()
langs = list(LANGUAGES.values())
lang_map = {v: k for k, v in LANGUAGES.items()}

def translate_text(text, src_lang, tgt_lang):
    src = lang_map[src_lang]
    tgt = lang_map[tgt_lang]
    result = translator.translate(text, src=src, dest=tgt)
    return result.text

gr.Interface(
    fn=translate_text,
    inputs=[
        gr.Textbox(label="Enter text"),
        gr.Dropdown(langs, label="From", value="english"),
        gr.Dropdown(langs, label="To", value="hindi")
    ],
    outputs="text",
    title="Language Translator"
).launch()
