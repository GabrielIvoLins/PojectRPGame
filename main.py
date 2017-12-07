#!/usr/bin/env python
#coding: utf-8

from kivy.app import App
from kivy.app import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.label import Label
from kivy.uix.image import Image

class PaginaInicial(Screen):#tela
    pass

class LabelConfig(Screen):
    pass

class Creditos(Screen):
    pass

class Objetivo(Screen):
    pass

class TextoA0(Screen):
    pass

class TextoA1(Screen):
    pass

class TextoA1A(Screen):
    pass

class TextoA1B(Screen):
    pass

class TextoA1C(Screen):
    pass

class TextoA1BD(Screen):
    pass

class TextoB0(Screen):
    pass

class TextoB1(Screen):
    pass

class TextoB1A(Screen):
    pass

class TextoB1B(Screen):
    pass

class TextoB1C(Screen):
    pass

class TextoB1AA(Screen):
    pass

class TextoB1AB(Screen):
    pass

class TextoB1BB(Screen):
    pass

class TextoB1CA(Screen):
    pass

class ContinuaC1(Screen):
    pass

class ContinuaC2(Screen):
    pass

class ContinuaC3(Screen):
    pass

class LojaArmas(Screen):
    pass

#Gerencia as trocas de jalena
class ScreenManagement(ScreenManager):
    def switch_to_labelConfig(self):
        self.current = 'labelConfig'

    def switch_to_paginaInicial(self):
        self.current = 'paginaInicial'

    def switch_to_creditos(self):
        self.current = 'creditos'

    def switch_to_objetivo(self):
        self.current = 'objetivo'

    def switch_to_textoA0(self):
        self.current = 'textoA0'

    def switch_to_textoA1(self):
        self.current = 'textoA1'

    def switch_to_textoA1A(self):
        self.current = 'textoA1A'

    def switch_to_textoA1B(self):
        self.current = 'textoA1B'

    def switch_to_textoA1C(self):
        self.current = 'textoA1C'
        
    def switch_to_textoA1BD(self):
        self.current = 'textoA1BD'

    def switch_to_textoB0(self):
        self.current = 'textoB0'

    def switch_to_textoB1(self):
        self.current = 'textoB1'

    def switch_to_textoB1A(self):
        self.current = 'textoB1A'

    def switch_to_textoB1B(self):
        self.current = 'textoB1B'

    def switch_to_textoB1C(self):
        self.current = 'textoB1C'

    def switch_to_textoB1AA(self):
        self.current = 'textoB1AA'

    def switch_to_textoB1AB(self):
        self.current = 'textoB1AB'

    def switch_to_textoB1BB(self):
        self.current = 'textoB1BB'

    def switch_to_textoB1CA(self):
        self.current = 'textoB1CA'

    def switch_to_continuaC1(self):
        self.current = 'continuaC1'

    def switch_to_continuaC2(self):
        self.current = 'continuaC2'

    def switch_to_continuaC3(self):
        self.current = 'continuaC3'

    def switch_to_lojaArmas(self):
        self.current = 'lojaArmas'

from kivy.config import Config
Config.set('graphics', 'resizable', False)

from kivy.core.window import Window
Window.size = 960,681

#Window.fullscreen = 'auto'
#Window.fullscreen = True

class kivyWizardApp(App):
    def build(self):
        self.root = ScreenManagement()
        self.title = 'RPGame'
        self.icon = "favicon.ico"
        return self.root

if __name__ == '__main__':
    kivyWizardApp().run()