import tkinter as tk
from tkinter import ttk






class Staff_Details_Display(object):
    def __init__(self,data):
        self.data = data
        
        self.setup_tab()

    def setup_tab(self):
        

        # スタイル設定
        style = ttk.Style()
        style.configure("EntryStyle.TEntry", font=("Arial", 18))

        # スクロール機能を持つフレームの設定
        self.staff_details_frame = self.setup_scrollable_frame()
        
        self.details_display(self.staff_details_frame)

        # スタッフ詳細入力ウィジェットの設定
        #self.setup_staff_detail_widgets(self.staff_input_frame)
        
    def setup_scrollable_frame(self):
        # スクロールバーの設定
        tab1_scrollbar = ttk.Scrollbar(orient='vertical')
        tab1_scrollbar.pack(side='right', fill='y')

        # スクロール可能なキャンバスの作成
        canvas = tk.Canvas(yscrollcommand=tab1_scrollbar.set)
        canvas.pack(side='top', fill='both', expand=True)

        # スクロールバーとキャンバスの連動設定
        tab1_scrollbar.configure(command=canvas.yview)

        # マウスホイールでスクロール
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        # タッチパッドやトラックパッドによる横スクロールのサポートが必要な場合（例: 横長のコンテンツ）
        def on_shift_mousewheel(event):
            canvas.xview_scroll(int(-1*(event.delta/120)), "units")  # 横スクロール用

        canvas.bind("<MouseWheel>", on_mousewheel)
        canvas.bind("<Shift-MouseWheel>", on_shift_mousewheel)  # 横スクロールのためにShiftキーを使用


        # キャンバス上に配置するウィジェット用のフレーム
        staff_details_frame = ttk.Frame(canvas)
        staff_details_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=staff_details_frame, anchor='nw')
        return staff_details_frame
    
    def details_display(self):
        test = 0