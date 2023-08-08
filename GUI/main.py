from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import OptionProperty, NumericProperty, ListProperty, \
        BooleanProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivy.core.window import Window
from kivy.config import Config

class MainWidget(FloatLayout):
    name_input = ObjectProperty()

class MainApp(App):
    def build(self):
        return MainWidget()
    
if __name__ == '__main__':
    # Window.fullscreen = True
    # Window.size = (1080, 1920)
    # Config.set('graphics', 'width', '1920')
    # Config.set('graphics', 'height', '1080')
    
    app = MainApp()
    app.run()
    # Config.write()