from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.listview import ListView
from kivy.factory import Factory
from kivy.properties import ListProperty, StringProperty, ObjectProperty
from kivy.uix.listview import ListItemButton

#version 0.0.5

class TinypapersApp(App):
    pass
    
class TinypapersWindowManager(BoxLayout):

    def display_add_form(self):
        self.clear_widgets()
        self.add_widget(AddPage())
        
    def display_main_page(self):
        self.clear_widgets()
        self.add_widget(MainPage())
    
class BasicListPage(BoxLayout):
    button_list_entries = []
    
class MainPage(BasicListPage):
    pass

class AddPage(BoxLayout):
    add_entry_text = ObjectProperty()

    def add_entry(self):
        BasicListPage.button_list_entries.append(self.add_entry_text.text)
    
class ButtonList(ListView):
    pass

class TinypapersHeader(BoxLayout):
    pass

class ItemButton(ListItemButton):
    pass

if __name__ == '__main__':
    TinypapersApp().run()
