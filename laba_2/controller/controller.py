from Model.TableClass import Table

class Controller:
    def __init__(self):
        self.model = Table()
    
    def clear_table(self):
        self.model.clear()
        
    def create_xml_file(self, title: str):
        self.model = Table(title)
        self.model.create_xml_file()
        
    def load_from_xml(self, text):
        self.model.load_from_xml(text)
         
    def get_len_col(self):
        return len(self.model.columns)
    
    def get_title_column(self, i):
        return self.model.columns[i].title
        
    def get_len_rec(self):
        return len(self.model.records)
    
    def get_len_rec_el(self, index):
        return len(self.model.records[index].elements)
    
    def get_el_rec(self, index, i):
        return self.model.records[index].elements[i]
    
    def get_rec_find(self, condition, con):
        return self.model.record_find(condition, con)
        
    def get_records(self):
        return self.model.records
    
    def change_records(self, found_records):
        self.model.records = found_records
    
    def table_add_rec(self, elements):
        self.model.record_add(elements)
    
    def table_rec_remove(self, record):
        self.model.record_remove(record)
    
    def table_rec_change(self, record, column_title_to_change, element_to_change):
        self.model.record_change(record, column_title_to_change, element_to_change)
            
    def save_to_xml(self):
        self.model.save_to_xml()