"""translator file"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey=os.environ['apikey']
url=os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(e_text):
    "english to french translation"
    if e_text=="":
        return None
    f_text = language_translator.translate(
    text=e_text,
    model_id='en-fr').get_result()
    return f_text['translations'][0]['translation']

def french_to_english(f_text):
    "french to english translation"
    if f_text=="":
        return None
    e_text=language_translator.translate(
    text=f_text,
    model_id='fr-en').get_result()
    return e_text['translations'][0]['translation']
print(english_to_french('Hello'))
