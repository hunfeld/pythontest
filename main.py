from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="")
        self.button = Button(text="Klick mich")
        self.button.bind(on_press=self.button_clicked)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)
        return self.layout

    def button_clicked(self, instance):
        self.label.text = "Hallo Welt"

if __name__ == "__main__":
    MyApp().run()
