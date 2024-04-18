import tkinter as tk
from tkinter import ttk



class Open_text_box(object):
    def __init__(self, widget):
        self.widget = widget
        self.text_box_window()
        
        
    def text_box_window(self):
        value = self.widget.get()
        self.top = tk.Toplevel()
        self.top.title("詳細")
        self.RE_text = tk.Text(self.top, wrap="word",height=10,width=30,font=("Arial",16))
        self.RE_text.insert('end', value)
        self.RE_text.pack(expand=True, fill='both')
        self.top.wm_overrideredirect(True)
        button = ttk.Button(self.top,text="入力",command=self.closed_window)
        button.pack()


        
    
    def closed_window(self):
        remarks_str = None
        remarks_str = self.RE_text.get("1.0", "end")
        self.widget.delete(0,tk.END)
        self.widget.insert(tk.END,remarks_str)
        self.top.destroy()
        



class Rank_open_text(object):
    def __init__(self,widget):
        self.widget = widget
        self.widget.bind("<Double-1>", self.open_text_editor)
        
    def open_text_editor(self,event=None):
        # 現在選択されているセルの行と列を取得
        col = self.widget.getSelectedColumn()
        row = self.widget.getSelectedRow()
        self.selected_rank_data = self.widget.model.df.iloc[row]
        self.selected_column_name = self.widget.model.df.columns[col]
        code = self.selected_rank_data["等級"]
        code2 = self.selected_rank_data["サブランク"]
        
        
        
        if col is not None and row is not None:
            value = self.widget.model.getValueAt(row, col)

            try:
                value = value.replace(',', '').strip()
                value = int(value) if value else 0
            except:
                pass

            # 新しいウィンドウを作成
            self.top = tk.Toplevel()
            self.top.title("詳細")
            self.rank_text = tk.Text(self.top, wrap="word")
            self.rank_text.insert('end', value)
            self.rank_text.pack(expand=True, fill='both')
            button = ttk.Button(self.top,text="更新",command=self.test)
            button.pack()
    def test(self):
        
        print("ボタンがクリックされました")