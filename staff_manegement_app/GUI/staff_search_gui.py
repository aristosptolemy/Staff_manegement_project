import tkinter as tk
from tkinter import ttk


def staff_search_tab(notebook):
    style = ttk.Style()
    style.configure("EntryStyle.TEntry", font=("Arial",18))
    
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text='スタッフ検索')