import jaconv
import pykakasi

import datetime
import tkinter as tk



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
    def __init__(self, widget, post_num, len_num, widget_2, widget_3):
        self.widget = widget
        self.address = widget_2
        self.kana = widget_3
        self.post_num = post_num
        self.len_num = len_num
        self.convert()
        self.post_request()
        
    def convert(self):
        data = self.post_num
        number_of_digits = len(data)
        if number_of_digits == self.len_num:
            post_number = f"{data[:3]}-{data[3:]}"
            self.widget.delete(0, tk.END)
            self.widget.insert(tk.END, post_number)
            return post_number

    def post_request(self):
        from jusho import Jusho, Address
        postman = Jusho()
        address_list = postman.by_zip_code(self.post_num)

        # APIからのレスポンスがリスト形式で返される場合、リストの最初の要素を使用する
        if address_list and isinstance(address_list, list):
            first_address = address_list[0]

            # Addressオブジェクトから情報を抽出
            if isinstance(first_address, Address):
                address_kanji = f'{first_address.city.kanji}{first_address.kanji}'
                address_kana = f'{first_address.city.kana}{first_address.kana}'
                self.address.insert(tk.END,address_kanji)
                self.kana.insert(tk.END,address_kana)
                return 
            
            elif isinstance(first_address, dict):
                # 辞書型の場合の処理
                address_kanji = f"{first_address['city']['kanji']}{first_address['kanji']}"
                self.address.insert(tk.END,address_kanji)
                #self.kana.insert(tk.END,address_kana)
                return 
                
            else:
                print("Error: Address format not recognized.")
        else:
            print("No address information found.")
        
        
        
    
        
class Kana_change(object):
    def __init__(self,widget1,widget2):
        self.widget1 = widget1#漢字
        self.widget2 = widget2#カタカナ
        self.kana_set()
    
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



