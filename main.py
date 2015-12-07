from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.listview import ListView
from kivy.factory import Factory
from kivy.uix.listview import ListItemButton

#version 0.0.3

class TinypapersApp(App):
    pass
    
class TinypapersWindowManager(BoxLayout):
    pass
    
class BasicListPage(BoxLayout):
    pass
    
class ItemButton(ListItemButton):
    pass
    
class MainPage(BasicListPage):
    pass
    
class ButtonList(ScrollView):
    # needs an args_converter
    
    data = ["this", "is", "sample", "data"]
    
    def args_converter(self, index, data_item):
        return {'xyzzy': data_item}
    

if __name__ == '__main__':
    TinypapersApp().run()
    
    
    
    
