from kivy.metrics import dp

from Model.TableClass import Table
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

import os
import math

from controller.controller import Controller

Window.size = (800, 600)
Window.title = "Tables"
# Window.clearcolor = (40/255, 40/255, 40/255, 1)

table_title_helper="""
TextInput:
    hint_text: "Enter table name"
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_y: 1    
"""

table_add_title_product_name_helper="""
TextInput:
    hint_text: "Enter product name"   
"""
table_add_title_manufacture_name_helper="""
TextInput:
    hint_text: "Enter manufacture name"  
"""
table_add_title_manufacture_UNP_helper="""
TextInput:
    hint_text: "Enter manifacture UNP"  
"""
table_add_title_quantility_in_stock_helper="""
TextInput:
    hint_text: "Enter quantility in stock"   
"""
table_add_title_address_helper="""
TextInput:
    hint_text: "Enter address"  
"""

table_remove_title_helper="""
TextInput:
    hint_text: "Enter column title"   
"""
table_remove_product_name_helper="""
TextInput:
    hint_text: "Enter product name"   
"""

table_search_title_helper="""
TextInput:
    hint_text: "Enter column title"   
"""
table_search_product_name_helper="""
TextInput:
    hint_text: "Enter product name"   
"""


class Interface(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.table = Table()
        self.controller = Controller()
        self.screen = Screen()
        self.main_layout = BoxLayout()
        self.menu_choose_table()

        self.current_pages_popup_search = 1
        self.current_page = 1
        self.records_on_page = 5

    def menu_choose_table(self, obj=None):
        self.controller.clear_table()
        self.screen.clear_widgets()
        buttons_create_and_list_tabels=GridLayout(cols=2,size_hint=(1,.6), pos_hint={'center_x':.5,'center_y':.5})
        label_menu=Label(text="Manufactures", font_size='40sp', pos_hint={'center_x': .5, 'center_y': .95})
        self.screen.add_widget(label_menu)

        button_new_table = Button(text="Create new table", font_size='20sp')
        button_list_tabel = Button(text="List of tables", font_size='20sp')
        buttons_create_and_list_tabels.add_widget(button_new_table)
        buttons_create_and_list_tabels.add_widget(button_list_tabel)
        button_new_table.bind(on_release=self.create_new_table_popup)
        button_list_tabel.bind(on_release=self.check_list_tabel)
        self.screen.add_widget(buttons_create_and_list_tabels) 
    #////////////////////////COMPLIT////////////////////////#        
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
        button_back_to_main_menu=Button(text="Back", 
                                        font_size='15sp',
                                        size_hint=(.14,.07),
                                        pos_hint={'center_x':.08,'center_y':.05})
        button_back_to_main_menu.bind(on_release=self.menu_choose_table)
        self.screen.add_widget(button_back_to_main_menu)
        

        
    def create_new_table_popup(self,instance):
        screen_popup=Screen()
        table_box=BoxLayout(size_hint=(1,.8), pos_hint={'center_x':.5, 'center_y':.6})
        button_create_close=GridLayout(cols=2,size_hint=(1,.2))
        closeButton = Button(text="Close the pop-up")
        createButton = Button(text="Create table")
        #creating background text
        self.table_title = Builder.load_string(table_title_helper)
        
        table_box.add_widget(self.table_title)
        screen_popup.add_widget(table_box)
        button_create_close.add_widget(closeButton)
        button_create_close.add_widget(createButton)
        screen_popup.add_widget(button_create_close)
        popup = Popup(title='Create new table',
                      content=screen_popup,
                      size_hint=(.5, .5))
        popup.open()
        closeButton.bind(on_press=popup.dismiss)
        createButton.bind(on_release=self.create_new_table, on_press=popup.dismiss)
        
    def create_new_table(self, obj=None):
        title = self.table_title.text
        # replace(old, new) : old -> new
        title = title.replace(' ', '')
        self.controller.create_xml_file(title)
        self.screen.clear_widgets()
        self.table_ui()
    
        
    def open_table(self, button):
        self.screen.clear_widgets()
        self.current_page = 1
        self.controller.load_from_xml(str(button.text + ".xml"))
        self.table_ui() 


    # ##########################################################################
    # ### ------------------------- table/tools ui ------------------------- ###
    # ##########################################################################

    # create empty table
    def table_ui(self, obj=None):
        self.screen.clear_widgets()
        self.generate_table_widget()
        
        self.screen.add_widget(self.generate_table_tools_widget())
        self.screen.add_widget(self.generate_table_widget())

    # #######################
    # ### ---- table ---- ###
    # #######################
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

        # buttons of pagination
        pages_buttons = BoxLayout(size_hint_y=0.1)
        button_page_first = Button(text="<<")
        button_page_previous = Button(text="<")
        button_page_next = Button(text=">")
        button_page_last = Button(text=">>")
        button_back_to_main_menu=Button(text="Back")

        button_page_first.bind(on_release=self.table_page_first)
        button_page_previous.bind(on_release=self.table_page_previous)
        button_page_next.bind(on_release=self.table_page_next)
        button_page_last.bind(on_release=self.table_page_last)
        button_back_to_main_menu.bind(on_release=self.menu_choose_table)

        pages_buttons.add_widget(button_back_to_main_menu)
        pages_buttons.add_widget(button_page_first)
        pages_buttons.add_widget(button_page_previous)
        pages_buttons.add_widget(button_page_next)
        pages_buttons.add_widget(button_page_last)

        # container
        container_table_and_pages.add_widget(table_widget)
        container_table_and_pages.add_widget(pages_buttons)

        return container_table_and_pages

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

    # #######################
    # ### ---- tools ---- ###
    # #######################
    def generate_table_tools_widget(self):
        
        tools_widget = BoxLayout(orientation='vertical',
                                 size_hint=(1,.1),
                                 pos_hint={'center_x':.5,'center_y':.95})
        tools_label_widget=GridLayout(cols=3)
        tools_label_widget.add_widget(Label(text="Tools",
                                            font_size='15sp',
                                            size_hint=(.8,.05)),)
        tools_label_widget.add_widget(Label(text="Lines on page",
                                            font_size='15sp',
                                            size_hint=(.1,.05)))
        tools_label_widget.add_widget(Label(text="Pages",
                                            font_size='15sp',
                                            size_hint=(.1,.05)))
        tools_button_widget=GridLayout(cols=8)
        button_delite=Button(text="Delite",
                            font_size='15sp',
                            size_hint=(.2,.05))
        button_add=Button(text="Add",
                          font_size='15sp',
                          size_hint=(.2,.05))
        button_search=Button(text="Search",
                            font_size='15sp',
                            size_hint=(.2,.05))
        button_save_to_file=Button(text="Save",
                            font_size='15sp',
                            size_hint=(.2,.05))
        self.spinner_object=Spinner(text="{}".format(self.records_on_page),
                                               values=('1','2','3','4','5','6','7','8','9','10'),
                                               font_size='15sp')
        self.spinner_object.size_hint=(.1,.05)
        self.spinner_object.sync_height=True
        button_delite.bind(on_release=self.generate_remove_record_widget)
        button_add.bind(on_release=self.generate_add_record_widget)
        button_search.bind(on_release=self.generate_search_record_widget)
        button_save_to_file.bind(on_release=self.generate_save_widget)
        self.spinner_object.bind(text=self.on_spinner_select)
        tools_button_widget.add_widget(button_delite)
        tools_button_widget.add_widget(button_add)
        tools_button_widget.add_widget(button_search)
        tools_button_widget.add_widget(button_save_to_file)
        tools_button_widget.add_widget(self.spinner_object)
        tools_button_widget.add_widget(Label(text="{}/{}".format(self.current_page, self.count_of_all_pages()),
                                              font_size='15sp',
                                              size_hint=(.1,.05)))
        
        tools_widget.add_widget(tools_label_widget)
        tools_widget.add_widget(tools_button_widget)
        return tools_widget

    def on_spinner_select(self,spinner,text):
        self.records_on_page=int(self.spinner_object.text)
        self.table_ui()
    
    def count_of_all_pages(self):
        if (self.controller.get_len_rec()%self.records_on_page) > 0:           
            return int(self.controller.get_len_rec()//self.records_on_page)+1
        else:
            if int(self.controller.get_len_rec()/self.records_on_page) == 0:
                return 1
            else:
                return int(self.controller.get_len_rec()/self.records_on_page)
        
    def count_of_all_pages_for_search(self):
        if (len(self.found_records)%self.records_on_page) > 0:           
            return (int(len(self.found_records)//self.records_on_page))+1
        else:
            if int(len(self.found_records)/self.records_on_page) == 0:
                return 1
            else:
                return int(len(self.found_records)/self.records_on_page)

    # #################################
    # ###  implementation of tools  ###
    # #################################

    def generate_search_record_widget(self, obj=None):
        self.screen_popup_search=Screen()
        table_box=BoxLayout(size_hint=(1,.8), pos_hint={'center_x':.5, 'center_y':.7})
        closeButton = Button(text="Close the pop-up")
        search_button=Button(text="Search")
        button_close_search=GridLayout(cols=2,size_hint=(1,.3))
        
        button_close_search.add_widget(closeButton)
        button_close_search.add_widget(search_button)
        
        table_search=GridLayout(cols=1,size_hint=(1,.8))
        self.table_search_select_title=Spinner(text="Select title",
                                               values=('Product','Manufacture','UMN','Quantity','Address'),
                                               font_size='15sp')
        self.table_search_select_title.size_hint=(.1,.45)
        self.table_search_select_title.sync_height=True
        self.table_search_enter_product_name=Builder.load_string(table_search_product_name_helper)
        table_search.add_widget(self.table_search_select_title)
        table_search.add_widget(self.table_search_enter_product_name)
        
        table_box.add_widget(table_search)
        self.screen_popup_search.add_widget(button_close_search)
        self.screen_popup_search.add_widget(table_box)
        self.popup_search = Popup(title='Search product',
                      content=self.screen_popup_search,
                      size_hint=(.6, .3))
        self.popup_search.open()
        closeButton.bind(on_press=self.popup_search.dismiss)
        search_button.bind(on_release=self.table_tool_search_record)
    
    def table_search_ui(self, obj=None):
        self.screen_popup_search.clear_widgets()
        self.popup_search.size_hint=(1,.8)
        self.screen_popup_search.add_widget(self.generate_table_search_widget())

    def table_tool_search_record(self, obj=None):#          
        conditions = dict()
        column_title = self.table_search_select_title.text
        element = self.table_search_enter_product_name.text
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
                    
        pages_buttons = BoxLayout(size_hint_y=0.1)
        button_page_first = Button(text="<<")
        button_page_previous = Button(text="<")
        button_page_next = Button(text=">")
        button_page_last = Button(text=">>")
        button_close_popup=Button(text="Close")

        button_page_first.bind(on_release=self.table_popup_search_page_first)
        button_page_previous.bind(on_release=self.table_popup_search_page_previous)
        button_page_next.bind(on_release=self.table_popup_search_page_next)
        button_page_last.bind(on_release=self.table_popup_search_page_last)
        button_close_popup.bind(on_release=self.change_current_popup_search_page, on_press=self.popup_search.dismiss)

        pages_buttons.add_widget(button_close_popup)
        pages_buttons.add_widget(button_page_first)
        pages_buttons.add_widget(button_page_previous)
        #add pages
        pages_buttons.add_widget(Label(text="{}/{}".format(self.current_pages_popup_search, self.count_of_all_pages_for_search())))
        pages_buttons.add_widget(button_page_next)
        pages_buttons.add_widget(button_page_last)

        # container
        container_table_and_pages.add_widget(table_widget)
        container_table_and_pages.add_widget(pages_buttons)

        return container_table_and_pages
    
    def change_current_popup_search_page(self, obj=None):
        self.current_pages_popup_search=1

    def table_popup_search_page_first(self,obj=None):
        self.current_pages_popup_search = 1
        self.table_search_ui()
    
    def table_popup_search_page_previous(self,obj=None):
        if self.current_pages_popup_search > 1:
            self.current_pages_popup_search -= 1
            self.table_search_ui()

    def table_popup_search_page_next(self,obj=None):
        if self.current_pages_popup_search < math.ceil(len(self.found_records)/self.records_on_page):
            self.current_pages_popup_search += 1
            self.table_search_ui()
    
    def table_popup_search_page_last(self,obj=None):
        self.current_pages_popup_search = math.ceil(len(self.found_records)/self.records_on_page)
        self.table_search_ui()
    
    def generate_add_record_widget(self, obj=None):
        screen_popup=Screen()
        table_box=BoxLayout(size_hint=(1,.8), pos_hint={'center_x':.5, 'center_y':.7})
        table_adding=GridLayout(cols=5,size_hint=(1,.8))
        
        button_add_close=GridLayout(cols=2,size_hint=(1,.2))
        closeButton = Button(text="Close the pop-up")
        add_Button = Button(text="Add product")
        
        #creating background text
        self.table_add_enter_product_name=Builder.load_string(table_add_title_product_name_helper)
        self.table_add_enter_manufacture_name=Builder.load_string(table_add_title_manufacture_name_helper)
        self.table_add_enter_manufacture_UNP=Builder.load_string(table_add_title_manufacture_UNP_helper)
        self.table_add_enter_quantility_in_stock=Builder.load_string(table_add_title_quantility_in_stock_helper)
        self.table_add_enter_address=Builder.load_string(table_add_title_address_helper)       
        
        table_adding.add_widget(self.table_add_enter_product_name)
        table_adding.add_widget(self.table_add_enter_manufacture_name)
        table_adding.add_widget(self.table_add_enter_manufacture_UNP)
        table_adding.add_widget(self.table_add_enter_quantility_in_stock)
        table_adding.add_widget(self.table_add_enter_address)
        
        table_box.add_widget(table_adding)
        screen_popup.add_widget(table_box)
        button_add_close.add_widget(closeButton)
        button_add_close.add_widget(add_Button)
        screen_popup.add_widget(button_add_close)
        popup = Popup(title='Add product',
                      content=screen_popup,
                      size_hint=(.8, .4))
        popup.open()
        closeButton.bind(on_press=popup.dismiss)
        add_Button.bind(on_release=self.table_tool_add_record, on_press=popup.dismiss)

    def table_tool_add_record(self, obj=None):
        screen_popup=Screen()
        
        closeButton = Button(text="Close the pop-up", size_hint=(1,.5))
        popup = Popup(title='Adding window',
                      content=screen_popup,
                      size_hint=(.3, .2))
        popup.open()
        closeButton.bind(on_press=popup.dismiss)
        screen_popup.add_widget(Label(text="added successfully", font_size='15sp', pos_hint={'center_x':.5,'center_y':.75}))
        screen_popup.add_widget(closeButton)
        
        elements = list()        
        elements.append(self.table_add_enter_product_name.text)
        elements.append(self.table_add_enter_manufacture_name.text)
        elements.append(self.table_add_enter_manufacture_UNP.text)
        elements.append(self.table_add_enter_quantility_in_stock.text)
        elements.append(self.table_add_enter_address.text)

        self.controller.table_add_rec(elements)
        self.table_ui()

    def generate_save_widget(self, obj=None):
        screen_popup=Screen()
        
        closeButton = Button(text="Close the pop-up", size_hint=(1,.5))
        popup = Popup(title='Save window',
                      content=screen_popup,
                      size_hint=(.3, .2))
        popup.open()
        closeButton.bind(on_press=popup.dismiss)
        screen_popup.add_widget(Label(text="saved successfully", font_size='15sp', pos_hint={'center_x':.5,'center_y':.75}))
        screen_popup.add_widget(closeButton)
        
        self.table_tool_save()

    def table_tool_save(self, obj=None):
        self.controller.save_to_xml()

    def generate_remove_record_widget(self, obj=None):
       
        screen_popup=Screen()
        table_box=BoxLayout(size_hint=(1,.8), pos_hint={'center_x':.5, 'center_y':.7})
        closeButton = Button(text="Close the pop-up")
        remove_button=Button(text="Remove")
        button_close_remove=GridLayout(cols=2,size_hint=(1,.3))
        
        button_close_remove.add_widget(closeButton)
        button_close_remove.add_widget(remove_button)
        
        table_remove=GridLayout(cols=1,size_hint=(1,.8))
        self.table_remove_select_title=Spinner(text="Select title",
                                               values=('Product','Manufacture','UMN','Quantity','Address'),
                                               font_size='15sp')
        self.table_remove_select_title.size_hint=(.1,.45)
        self.table_remove_select_title.sync_height=True
        self.table_remove_enter_product_name=Builder.load_string(table_remove_product_name_helper)
        table_remove.add_widget(self.table_remove_select_title)
        table_remove.add_widget(self.table_remove_enter_product_name)
        
        table_box.add_widget(table_remove)
        screen_popup.add_widget(button_close_remove)
        screen_popup.add_widget(table_box)
        popup = Popup(title='Delite product',
                      content=screen_popup,
                      size_hint=(.6, .3))
        popup.open()
        closeButton.bind(on_press=popup.dismiss)
        remove_button.bind(on_release=self.table_tool_remove_record, on_press=popup.dismiss) 
    
    def table_tool_remove_record(self, obj=None):
        conditions = dict()
        column_title = self.table_remove_select_title.text
        element = self.remove_choose.text
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
        self.generate_remove_record_widget()

        info_text = "There are no records with the specified conditions"
        if quantity_of_records_were_deleted != 0:
            info_text = f"{quantity_of_records_were_deleted} records where deleted"
        self.open_popup(info_text)

    def generate_change_record_widget(self, obj=None):
        self.table_ui()

        change_record_widget = BoxLayout(size_hint_y=0.2)

        # several conditions
        conditions = BoxLayout(orientation='vertical', size_hint_x=1.5)

        # first condition
        condition = BoxLayout()
        condition.add_widget(TextInput(multiline=False, size_hint_x=1, text="column title"))
        condition.add_widget(TextInput(multiline=False, size_hint_x=1, text="element"))

        conditions.add_widget(condition)

        # buttons
        button_add_condition = Button(text="add\ncondition", size_hint_x=0.5)
        button_add_condition.bind(on_release=self.table_tool_change_record_add_condition)

        # field change record to condition
        replacement_info = BoxLayout(orientation='vertical')
        replacement_info.add_widget(TextInput(multiline=False, size_hint_x=1, text="column title to change"))
        replacement_info.add_widget(TextInput(multiline=False, size_hint_x=1, text="element to change"))

        button_remove = Button(text="change", size_hint_x=0.5)
        button_remove.bind(on_release=self.table_tool_change_record)

        change_record_widget.add_widget(conditions)
        change_record_widget.add_widget(button_add_condition)
        change_record_widget.add_widget(replacement_info)
        change_record_widget.add_widget(button_remove)

        self.main_layout.children[0].add_widget(change_record_widget)

    def table_tool_change_record_add_condition(self, obj=None):
        condition = BoxLayout()
        condition.add_widget(TextInput(multiline=False, size_hint_x=1, text="column title"))
        condition.add_widget(TextInput(multiline=False, size_hint_x=1, text="element"))
        self.main_layout.children[0].children[0].children[3].add_widget(condition)

    def table_tool_change_record(self, obj=None):

        conditions = dict()
        for condition_box in self.main_layout.children[0].children[0].children[3].children:
            column_title = condition_box.children[1].text
            element = condition_box.children[0].text
            conditions[str(column_title)] = element

        element_to_change = self.main_layout.children[0].children[0].children[1].children[0].text
        column_title_to_change = self.main_layout.children[0].children[0].children[1].children[1].text

        records_to_change = list()
        first_condition = True

        for condition in conditions:

            #   condition    | conditions.get(condition)
            #  column_title  |         element

            suitable_records = self.controller.get_rec_find(condition, conditions.get(condition))
            if first_condition:
                records_to_change = suitable_records
                first_condition = False
            else:
                records_to_change = list(set(records_to_change) & set(suitable_records))

        quantity_of_records_were_changed = len(records_to_change)
        for record in records_to_change:
            # print(record)
            self.controller.table_rec_change(record, column_title_to_change, element_to_change)

        self.table_ui()
        self.generate_change_record_widget()

        info_text = f"{quantity_of_records_were_changed} records where changed"
        self.open_popup(info_text)
        
    # OTHER TOOLS
    def open_popup(self, text):
        popup_layout = BoxLayout(orientation="vertical")
        button = Button(text='Close')
        label = Label(text=text)
        popup_layout.add_widget(label)
        popup_layout.add_widget(button)

        popup = Popup(title='Table ifo', content=popup_layout, size_hint=(0.5, 0.3))
        button.bind(on_release=popup.dismiss)
        popup.open()

    def build(self):
        return self.screen