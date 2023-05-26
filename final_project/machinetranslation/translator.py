# '''py
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('gsifIW4kI8Kls25lSA9-6ayzk_e1oNtYS2D9nPDY2ua7')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com/instances/0de0b726-704a-4956-a1f4-459f6435db71')

def englishToFrench(englishText):
    frenchText = language_translator.translate(text=englishText, model_id='en-fr').get_result()
    frenchText = frenchText['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    englishText = language_translator.translate(text=frenchText, model_id='fr-en').get_result()
    englishText = englishText['translations'][0]['translation']
    return englishText

"""
    text_fr = language_translator.translate(text='Hello, how are you today?', model_id='en-fr').get_result()
    print(text_fr)
    print(json.dumps(text_fr, indent=2, ensure_ascii=False))
""" 