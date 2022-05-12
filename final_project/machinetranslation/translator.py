import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

VERSION_LT='2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=VERSION_LT,
authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(english_text='Hello'):
    """
    Function converts english text to french
    Args:
       englishText - The english text to be converted
    Return:
       returns converted french text
    """
    french_translation = language_translator.translate(
        text=english_text, model_id='en-fr').get_result()

    french_text = french_translation['translations'][0]['translation']

    return french_text

def french_to_english(french_text='Bonjour'):
    """
    Function converts french text to english
    Args:
       frenchText - The french text to be converted
    Return:
       returns converted english text
    """
    english_translation = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()

    english_text = english_translation['translations'][0]['translation']

    return english_text