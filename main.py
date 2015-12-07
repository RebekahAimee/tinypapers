from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.listview import ListView
from kivy.factory import Factory
from kivy.properties import ListProperty, StringProperty, ObjectProperty
from kivy.uix.listview import ListItemButton

import json

#version 0.0.7

class TinypapersApp(App):
    pass
    
class TinypapersWindowManager(BoxLayout):

    def display_add_form(self):
        self.clear_widgets()
        self.add_widget(AddPage())
        
    def display_index_page(self):
        self.clear_widgets()
        self.add_widget(IndexPage())
            
    def display_main_page(self):
        self.clear_widgets()
        self.add_widget(MainPage())
        
    def display_confirmation_page(self):
        self.clear_widgets()
        self.add_widget(ConfirmationPage())

class MainPage(BoxLayout):
    pass
    
class IndexPage(BoxLayout):
    button_list_entries = []
        
class AddPage(BoxLayout):
    add_entry_text = ObjectProperty()

    def add_entry(self):
        IndexPage.button_list_entries.append(self.add_entry_text.text)
        #updates an iteration too late...

class ConfirmationPage(AnchorLayout):
    pass

if __name__ == '__main__':
    TinypapersApp().run()
