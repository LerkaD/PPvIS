from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.factory import Factory
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from controller.controller import Controller
import math 
import os

class MainWindow(Screen):
    pass
class ToolseWidget(Screen):
    pass
class Window(Screen):
    pass
Builder.load_file('view\InterfaceClass.kv')

class Interface1(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = Controller()
        self.screen = MainWindow()
        self.tools_widget = ToolseWidget()
        self.current_pages_popup_search = 1
        self.current_page = 1
        self.records_on_page = 5
        
    def create_new_table(self, text):
        title = text
        title = title.replace(' ', '')
        self.controller.create_xml_file(title)
        self.screen.clear_widgets()
        self.table_ui()
    
    def table_ui(self, obj=None):
        self.screen.clear_widgets()
        self.generate_table_tools_widget()
        
        self.screen.add_widget(self.generate_table_tools_widget())
        self.screen.add_widget(self.generate_table_widget())
        
    def generate_table_widget(self):
        container_table_and_pages = BoxLayout(orientation='vertical', size_hint=(1,.88), pos_hint={'center_x':.5,'center_y':.45})

        table_widget = GridLayout()
        table_widget.cols = self.controller.get_len_col()

        for i in range(self.controller.get_len_col()):
            column_title = Label(text=self.controller.get_title_column(i), size_hint=(.2,.05))
            column_title.color = (160/255, 160/255, 160/255, 1)
            table_widget.add_widget(column_title)

        for index in range((self.current_page - 1) * self.records_on_page, self.current_page * self.records_on_page):
            if index < self.controller.get_len_rec() != 0:
                for i in range(self.controller.get_len_rec_el(index)):
                    element_widget = Label(text=str(self.controller.get_el_rec(index,i)), size_hint_x=1)
                    table_widget.add_widget(element_widget)
                    
        container_table_and_pages.add_widget(table_widget)
        container_table_and_pages.add_widget(Factory.PagesButtons())
        return container_table_and_pages    
    
    def check_list_tabel(self, obj=None):
        self.screen.clear_widgets()
        label_menu=Label(text="List of tables", font_size='40sp', pos_hint={'center_x': .5, 'center_y': .95})
        self.screen.add_widget(label_menu)
        
        table_buttons_widget = BoxLayout(orientation='vertical',size_hint=(1,.8),pos_hint={'center_x': .5, 'center_y': .5})
        count_of_file_xml = 0
        # find other table in directory
        for file in os.listdir():
            file_name = file.split(".")[0]
            file_expansion = file.split(".")[-1]
            if file_expansion == "xml":
                count_of_file_xml+=1
                button_table_box = BoxLayout()  # padding=10)
                button_table = Button(text=file_name)
                button_table.bind(on_release=self.open_table)
                button_table_box.add_widget(button_table)
                table_buttons_widget.add_widget(button_table_box)
        self.screen.add_widget(table_buttons_widget)
        self.screen.add_widget(Label(text="C. of the 'xml' files: {}".format(count_of_file_xml),
                                     font_size='15sp',
                                     pos_hint={'center_x':.9,'center_y':.05}))
        
        
    def open_table(self, button):
        self.screen.clear_widgets()
        self.current_page = 1
        self.controller.load_from_xml(str(button.text + ".xml"))
        self.table_ui()
        
    def table_page_next(self, obj=None):
        if self.current_page < math.ceil(self.controller.get_len_rec()/self.records_on_page):
            self.current_page += 1
            self.table_ui()

    def table_page_previous(self, obj=None):
        if self.current_page > 1:
            self.current_page -= 1
            self.table_ui()

    def table_page_first(self, obj=None):
        self.current_page = 1
        self.table_ui()

    def table_page_last(self, obj=None):
        self.current_page = math.ceil(self.controller.get_len_rec()/self.records_on_page)
        self.table_ui()
    
    def build(self):
        return self.screen
    
    def generate_table_tools_widget(self):
        print(self.tools_widget.ids.notes_on_page.text)
        self.tools_widget.ids.notes_on_page.text = "{}".format(self.records_on_page)
        print(self.tools_widget.ids.notes_on_page.text)
        self.tools_widget.ids.count_pages.text = "{}/{}".format(self.current_page, self.count_of_all_pages())
        print(self.tools_widget.ids.count_pages.text)
        return Factory.ToolseWidget()
    
    def count_of_all_pages(self):
        if (self.controller.get_len_rec()%self.records_on_page) > 0:           
            return int(self.controller.get_len_rec()//self.records_on_page)+1
        else:
            if int(self.controller.get_len_rec()/self.records_on_page) == 0:
                return 1
            else:
                return int(self.controller.get_len_rec()/self.records_on_page)    
    
    def on_spinner_select(self,spinner,text):
        self.records_on_page=int(self.spinner_object.text)
        self.table_ui()
    
    def table_tool_save(self, obj=None):
        self.controller.save_to_xml()
    
    def table_tool_remove_record(self, column, el, obj=None):
        print(column)
        print(el)
        conditions = dict()
        column_title = column
        element = el
        conditions[str(column_title)] = element

        records_to_remove = list()
        first_condition = True

        for condition in conditions:
    
            suitable_records = self.controller.get_rec_find(condition, conditions.get(condition))
            if first_condition:
                records_to_remove = suitable_records
                first_condition = False
            else:
                records_to_remove = list(set(records_to_remove) & set(suitable_records))

        quantity_of_records_were_deleted = len(records_to_remove)
        for record in records_to_remove:
            self.controller.table_rec_remove(record)
        self.table_ui()
        Factory.RemoveRecordWidget().open()

        info_text = "There are no records with the specified conditions"
        if quantity_of_records_were_deleted != 0:
            info_text = f"{quantity_of_records_were_deleted} records where deleted"
        #self.open_popup(info_text)
        Factory.Openpopup().open()
    
    def adding_in_table(self,table_add_enter_product_name,table_add_enter_manufacture_name,table_add_enter_manufacture_UNP,table_add_enter_quantility_in_stock,table_add_enter_address):
        elements = list()        
        elements.append(table_add_enter_product_name)
        elements.append(table_add_enter_manufacture_name)
        elements.append(table_add_enter_manufacture_UNP)
        elements.append(table_add_enter_quantility_in_stock)
        elements.append(table_add_enter_address)

        self.controller.table_add_rec(elements)
        
    def table_tool_search_record(self,column, el, obj=None):#    
        conditions = dict()
        column_title = column
        element = el
        conditions[str(column_title)] = element

        self.found_records = list()
        first_condition = True

        for condition in conditions:
            suitable_records = self.controller.get_rec_find(condition, conditions.get(condition))
            if first_condition:
                self.found_records = suitable_records
                first_condition = False
            else:
                self.found_records = list(set(self.found_records) & set(suitable_records))
        all_records = self.controller.get_records()
        self.controller.change_records(self.found_records)
        self.table_search_ui()
        self.controller.change_records(all_records)
   
    def table_search_ui(self, obj=None):
        self.screen.clear_widgets()
        self.screen.add_widget(self.generate_table_search_widget())
        
        
    def generate_table_search_widget(self):
        container_table_and_pages = BoxLayout(orientation='vertical', size_hint=(1,.88), pos_hint={'center_x':.5,'center_y':.45})

        table_widget = GridLayout()
        table_widget.cols = self.controller.get_len_col()

        for i in range(self.controller.get_len_col()):
            column_title = Label(text=self.controller.get_title_column(i), size_hint=(.2,.05))
            column_title.color = (160/255, 160/255, 160/255, 1)
            table_widget.add_widget(column_title)

        for index in range((self.current_pages_popup_search - 1) * self.records_on_page, self.current_pages_popup_search * self.records_on_page):
            if index < len(self.found_records) != 0:
                for element in self.found_records[index].elements:
                    element_widget = Label(text=str(element), size_hint_x=1)
                    # element_widget = Button(text=str(element), background_color=(80/255,80/255,80/255,1))
                    table_widget.add_widget(element_widget)

        container_table_and_pages.add_widget(table_widget)
        
        container_table_and_pages.add_widget(Factory.PagesButtons())
        return container_table_and_pages 
   