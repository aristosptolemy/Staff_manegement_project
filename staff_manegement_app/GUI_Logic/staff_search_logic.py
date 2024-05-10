import json

class Search_Staff_List_INSERT(object):
    def __init__(self,data,widget):
        self.data = data
        self.widget = widget
        self.insert_data(self.data)
        self.widget.bind("<<TreeviewSelect>>",self.open_logic)
        
    
    def insert_data(self,data):
        
        count = 0
        for record in data:
            #print(record)
            shi_json = record['氏']  # '氏'に関するJSONデータが2番目に格納されていると仮定
            shi_data = json.loads(shi_json)
            mei_json = record['名']
            mei_data = json.loads(mei_json)
            in_data = [record['就業場所'],shi_data["氏"],mei_data["名"],record['雇用形態'],record['在籍状況'],record['id']]
            self.widget.insert(parent='', index='end', iid=count ,values=in_data)
            count += 1
            
            
    def open_logic(self,event=None):
        from staff_manegement_app.data.SQL_center import MySQL_Select_Details

        record_id = self.widget.focus()
        record_values = self.widget.item(record_id, 'values')
        
        
        
        MySQL_Select_Details(record_values,self.widget)
    
    def change_logic(self):
        
        print(self.widget.focus())
        