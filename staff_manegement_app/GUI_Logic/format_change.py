import jaconv
import pykakasi

import datetime
from datetime import date

import tkinter as tk
from tkinter import ttk

from pprint import pprint
import requests


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
    def __init__(self, widget,post_num,len_num,widget_2,widget_3):
        self.widget = widget
        self.address = widget_2
        self.kana = widget_3
        self.post_num = post_num
        self.len_num = len_num
        self.convert()
        self.post_request()
        
    
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

    def post_request(self):
        
        post_code = self.post_num
        URL = 'https://zipcloud.ibsnet.co.jp/api/search'
        res = requests.get(URL, params={'zipcode': post_code})
        pprint(res.json())
        data = res.json()
        
        insert_post = f"{data["results"][0]["address1"]}{data["results"][0]["address2"]}{data["results"][0]["address3"]}"
        kana_data = f"{data["results"][0]["kana1"]}{data["results"][0]["kana2"]}{data["results"][0]["kana3"]}"
        print(insert_post)
        if self.address.get() == "":
            self.address.insert(tk.END,insert_post)
            ad_kana = jaconv.h2z(kana_data)
            self.kana.insert(tk.END,ad_kana)
        
        
    
        
class Kana_change(object):
    def __init__(self,widget1,widget2):
        self.widget1 = widget1#漢字
        self.widget2 = widget2#カタカナ
        self.widget1.bind('<FocusOut>',self.kana_set)
    
    def kana_set(self,event=None):
        kks = pykakasi.kakasi()
        kanji = self.widget1.get()
        result = kks.convert(kanji)
        #kana = result[0]['kana']
        kana_result = []
        for i in result:
            k = i['kana']
            kana_result.append(k)
            
        ins_kana = "".join(kana_result)
        #print(ins_kana)
        
            
        if self.widget2.get() == "":
            self.widget2.insert(tk.END,ins_kana)

        