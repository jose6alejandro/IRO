from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Container(BoxLayout):
    None

class MainApp(App):
    title = 'Hello world'
    
    def build(self):
        return Container()

if __name__ == "__main__":
    MainApp().run()
