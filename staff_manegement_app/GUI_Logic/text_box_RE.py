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
        
        if col is not None and row is not None:
            self.value = self.widget.model.getValueAt(row, col)

            try:
                self.value = self.value.replace(',', '').strip()
                self.value = int(self.value) if self.value else 0
            except:
                pass

            # 新しいウィンドウを作成
            self.top = tk.Toplevel()
            self.top.title("詳細")
            self.rank_text = tk.Text(self.top, wrap="word",font=("Arial",16))
            self.rank_text.insert('end', self.value)
            self.rank_text.pack(expand=True, fill='both')
            button = ttk.Button(self.top,text="更新",command=self.update)
            button.pack()
            
            
    def update(self):
        from staff_manegement_app.data.SQL_center import Rank_Detail_update
        Rank_Detail_update(self.selected_rank_data["等級"],self.selected_rank_data["サブランク"],
                           self.selected_column_name,self.rank_text.get('1.0', 'end'),self.widget)

        self.top.destroy()
        