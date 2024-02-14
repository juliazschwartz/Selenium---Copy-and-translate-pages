import googletrans
from googletrans import Translator

translator = Translator(service_urls=['translate.googleapis.com'])

print(translator.translate('Hoje esta tudo certo', dest="en"))