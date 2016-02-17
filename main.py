#The MIT License (MIT)
#Copyright (c) 2016, Rebekah Yoder

#Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
#and associated documentation files (the "Software"), to deal in the Software without restriction, 
#including without limitation the rights to use, copy, modify, merge, publish, distribute, 
#sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is 
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or 
#substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
#NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES 
#OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
#CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.listview import ListView, ListItemButton
from kivy.factory import Factory
from kivy.properties import ListProperty, StringProperty, ObjectProperty
from kivy.storage.jsonstore import JsonStore

import json

#version 0.0.8

class TinypapersApp(App):
    pass
    
class TinypapersWindowManager(BoxLayout):
    add_entry_text = ObjectProperty()
    # This is also declared under the Add page. Sort out the program's 
    # structure before you program JSON in formally.
    def __init__(self, **kwargs):
        super(TinypapersWindowManager, self).__init__(**kwargs)
        #self.store = JsonStore("window_mgr_store.json")
        #if self.store.exists('entries'):
        #    print "Store found!"
            
    def save_entry(self):
        #working on this code
        # Needs to access the add_entry_text through an ObjectProperty.
        pass
            
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

    def add_entry(self): #also pass other entry fields: eg content, phone #
        #maybe *args should handle parsing the arrays later on
        #that would allow code reuse because you could also pass a type var
        #and add a switch statement to unpack depending on what type
        IndexPage.button_list_entries.append(self.add_entry_text.text)

class ConfirmationPage(AnchorLayout):
    pass

if __name__ == '__main__':
    TinypapersApp().run()
