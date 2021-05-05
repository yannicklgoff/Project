from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
import requests
import json
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.textinput import TextInput
from kivy.uix.switch import Switch



# eerst alle classes om te switchen van schrerm
class HomeScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class DerdePartij(Screen):
    pass

class ProfileScreen(Screen):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

class AnswerInput(BoxLayout):
    pass

GUI = Builder.load_file("main.kv")

class MainApp(App):
    user_id = 1
    def build(self):
        return GUI

    def on_start(self):
        # get database data
        result = requests.get("https://chainapp-1e9a9-default-rtdb.europe-west1.firebasedatabase.app/{}.json".format(str(self.user_id)))
        print("ok?", result)
        data = json.loads(result.content.decode())
        print(data)


    # Root is the main widget in layout, = gridlayout
    def change_screen(self, screen_name):
        print(self.root.ids)
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name

    def callback(instance, value):
        print('the switch', instance, 'is', value)

    switch = Switch()
    switch.bind(active=callback)

MainApp().run()