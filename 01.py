import kivy

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.app import App

import math, random

class GL(GridLayout):
    def __init__(self):
        super().__init__()

        self.cols = 3

class MyApp(App):
    def build(self):
        return GL()
    
MyApp().run()