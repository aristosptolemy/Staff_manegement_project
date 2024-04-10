import json

from staff_manegement_app.data.SQL import MySQL_Select_Details




class Search_Staff_List_INSERT(object):
    def __init__(self,data,widget):
        self.data = data
        self.widget = widget
        self.insert_data(self.data)
        self.widget.bind("<<TreeviewSelect>>",self.open_logic)
    
    def insert_data(self,data):
        count = 0
        for record in data:
            shi_json = record[1]  # '氏'に関するJSONデータが2番目に格納されていると仮定
            shi_data = json.loads(shi_json)
            mei_json = record[2]
            mei_data = json.loads(mei_json)
            in_data = [record[14],shi_data["氏"],mei_data["名"],record[13],record[22],record[0]]
            self.widget.insert(parent='', index='end', iid=count ,values=in_data)
            count += 1
            
            
    def open_logic(self,event=None):
        record_id = self.widget.focus()
        record_values = self.widget.item(record_id, 'values')
        #MySQL_Select_Details(record_values)
        print(record_values)