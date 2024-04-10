

import tkinter as tk
from tkinter import ttk

def setup_gui():
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10, expand=True, fill='both')

    # ここでカラム名の設定を行う
    column_names = ['就業場所', '氏', '名', '雇用形態', '在籍状況']
    
    # スタイルの設定
    style = ttk.Style()
    style.configure("Treeview", font=('HGP教科書体', 16))
    style.configure("Treeview.Heading", font=('HGP教科書体', 16, 'bold'))

    # Treeviewの作成
    result_box = ttk.Treeview(frame, columns=column_names, show="headings", style="Treeview")
    result_box.column('就業場所', anchor='center', width=100)
    result_box.column('氏', anchor='center', width=100)
    result_box.column('名', anchor='center', width=100)
    result_box.column('雇用形態', anchor='center', width=100)
    result_box.column('在籍状況', anchor='center', width=100)

    result_box.heading('就業場所', text='就業場所', anchor='center')
    result_box.heading('氏', text='氏', anchor='center')
    result_box.heading('名', text='名', anchor='center')
    result_box.heading('雇用形態', text='雇用形態', anchor='center')
    result_box.heading('在籍状況', text='在籍状況', anchor='center')

    result_box.grid(row=0, column=0, sticky='nsew')

    root.mainloop()

setup_gui()