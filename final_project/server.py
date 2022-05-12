from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    french_translation = language_translator.translate(
        text=textToTranslate, model_id='en-fr').get_result()

    french_text = french_translation['translations'][0]['translation']

    return french_text

@app.route("/frenchToEnglish")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    english_translation = language_translator.translate(
        text=english_to_french(), model_id='fr-en').get_result()

    english_text = english_translation['translations'][0]['translation']

    return english_text

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return templates('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
