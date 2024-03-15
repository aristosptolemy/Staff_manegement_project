import jaconv

import datetime
from datetime import date


import tkinter as tk
from tkinter import ttk

class FormatConvert(object):
    def __init__(self, widget):
        self.widget = widget
        date = self.widget.get()
        #print(date)
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
                print("Formatted date:", date_obj)
                self.widget.delete( 0, tk.END )
                self.widget.insert(0,date_set)
            else:
                print("Invalid date format")
        except ValueError as e:
            print("Error converting date:", e)
        # ここで日付のフォーマット変換や検証を行う