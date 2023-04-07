from kivy.app import App
#from esping import traducir_deprecated
from modelo_traductor import ModelTraductor

class TraducerApp(App):

    #def __init__(self):
    #   self.src_lang = "es"
    #   self.trg_lang = "en"


    def button1_press(self):
        """Traduce"""
        #src_lang = "es"
        #trg_lang = "en"

        text_output = mt.traducir(self.root.ids['text_input'].text)
        #ORIGINALself.root.ids['text_rst'].text = list.pop()
        #COPIA:
        self.root.ids['text_rst'].text = text_output

    def button2_press(self):
        """Limpia los cuadros de texto"""
        self.root.ids['text_rst'].text = self.root.ids['text_input'].text = " "

    def button3_press(self):
        """Invierte la traducción"""
        print('Cambio de idioma')
        #mt = ModelTraductor()
        mt.switch_language()
        
        


if __name__ == '__main__':
    #Ejemplo1: MyApp().run()
    #CodigoAnterior
    #app = TraducerApp()
    #app.run()
    mt = ModelTraductor()

    #Uniendo ambos ejemplos
    TraducerApp().run()
