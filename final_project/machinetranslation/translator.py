"""using ibm watson translation service"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

# translate text input from english to french
def english_to_french(english_text):
    """using ibm watson language translator to translate from english to french"""
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()

    return translation['translations'][0]['translation']

# translate text input from french to english
def french_to_english(french_text):
    """using ibm watson language translator to translate from french to english"""
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return translation['translations'][0]['translation']
