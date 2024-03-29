import jaconv

import datetime
from datetime import date

import tkinter as tk
from tkinter import ttk



class FormatConvert(object):
    def __init__(self, widget):
        self.widget = widget
        date = self.widget.get()
        self.convert(date)
    
    def convert(self, date, event=None):
        # ウィジェットから値を取得し、全角を半角に変換
        #date_str = self.widget.get()
        format_date = jaconv.z2h(date, digit=True, ascii=True)
        
        try:
            # "･"または"/"で日付を分割し、整数のリストに変換
            date_parts = [int(part) for part in format_date.replace("･", "/").split("/")]
            if len(date_parts) == 3:
                # 日付オブジェクトを作成
                date_obj = datetime.date(date_parts[0], date_parts[1], date_parts[2])
                date_set = date_obj.strftime("%Y/%m/%d")
                self.widget.delete(0,tk.END)
                self.widget.insert(0,date_set)
            else:
                print("Invalid date format")
        except ValueError as e:
            print("Error converting date:", e)


class FormatConvert_tell(object):
    def __init__(self, widget,title,len_num,tell_num):
        self.widget = widget
        self.title = title
        self.tell_num = tell_num
        self.len_num = len_num

        self.convert()
        
    
    def convert(self,event=None):
        data = self.tell_num
        
        number_of_digits = len(data)
        if self.title == "携帯電話:":
            if number_of_digits == self.len_num:
                phone_number = f"{data[:3]}-{data[3:7]}-{data[7:]}"
                self.widget.delete(0,tk.END)
                self.widget.insert(tk.END,phone_number)
                return phone_number
            else:
                return
        else:
            if number_of_digits == self.len_num:
                phone_number = f"{data[:3]}-{data[3:6]}-{data[6:]}"
                self.widget.delete(0,tk.END)
                self.widget.insert(tk.END,phone_number)
                return phone_number
            else:
                return

class FormatConvert_Post(object):
    def __init__(self, widget,post_num,len_num):
        self.widget = widget
        self.post_num = post_num
        self.len_num = len_num
        self.convert()
        
    
    def convert(self,event=None):
        data = self.post_num

        number_of_digits = len(data)
        if number_of_digits == self.len_num:
            post_number = f"{data[:3]}-{data[3:]}"
            self.widget.delete(0,tk.END)
            self.widget.insert(tk.END,post_number)
            return post_number
        else:
            return
        