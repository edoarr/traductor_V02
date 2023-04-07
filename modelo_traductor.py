#from transformers import MarianTokenizer, TFMarianMTModel
#from typing import List
from transformers import pipeline


class ModelTraductor:

  def __init__(self):
     self.switch_lang = False
    
  def switch_language(self):
     self.switch_lang = not(self.switch_lang) 


  def traducir(self, src_text):
      if self.switch_lang:
         src_lang, trg_lang = "en","es"
      else:
         src_lang, trg_lang = "es", "en"
           
         
      model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{trg_lang}"
      pipe = pipeline("translation", model=model_name)
      return pipe(src_text)[0]["translation_text"]










"""Ambos métodos se usaron para construir def traducir()
#Metodo Prueba01
def predict(text):
  return pipe(text)[0]["translation_text"]



#Metodo Prueba02
def traducir_02(src_text, src, trg):
    src = "fr"  # source language
    trg = "en"  # target language

    sample_text = "où est l'arrêt de bus ?"

    #model_name = f"Helsinki-NLP/opus-mt-{src}-{trg}"
    model_name = "Helsinki-NLP/opus-mt-en-ROMANCE"

    model = TFMarianMTModel.from_pretrained(model_name, from_pt=True)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    batch = tokenizer([sample_text], return_tensors="tf")
    gen = model.generate(**batch)
    tokenizer.batch_decode(gen, skip_special_tokens=True)
"""