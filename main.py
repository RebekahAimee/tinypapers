from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListView
from kivy.factory import Factory
from kivy.properties import ListProperty, StringProperty, ObjectProperty
from kivy.uix.listview import ListItemButton

#version 0.0.6

class TinypapersApp(App):
    pass
    
class TinypapersWindowManager(BoxLayout):
    # render MainPage only once and store it?
    #main_page = ObjectProperty()

    def display_add_form(self):
        self.clear_widgets()
        self.add_widget(AddPage())
        
    def display_index_page(self):
        self.clear_widgets()
        self.add_widget(IndexPage())
            
    def display_main_page(self):
        self.clear_widgets()
        self.add_widget(MainPage())
        
        # figure out how to render MainPage only once and store it?
        #if self.main_page is None:
        #    self.main_page = self.add_widget(MainPage())
        #if self.main_page is not None:
        #    self.clear_widgets()
        #    self.add_widget(self.main_page)

class MainPage(BoxLayout):
    pass
    
class IndexPage(BoxLayout):
    button_list_entries = []
    #entry_list = ObjectProperty()
    
    #def __init__(self, **kwargs):
    #    self.update_entries()

    #def update_entries(self):
    #    self.entry_list.populate()
        
class AddPage(BoxLayout):
    add_entry_text = ObjectProperty()

    def add_entry(self):
        IndexPage.button_list_entries.append(self.add_entry_text.text)
        #updates an iteration too late...

if __name__ == '__main__':
    TinypapersApp().run()
