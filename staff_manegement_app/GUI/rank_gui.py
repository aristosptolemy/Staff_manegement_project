
from tkinter import ttk

class rank_list_map():
    def __init__(self, notebook):
        self.notebook = notebook
        
        self.setup_tab()

    def setup_tab(self):
        
        # スタイル設定
        style = ttk.Style()
        style.configure("EntryStyle.TEntry", font=("Arial", 18))

        # タブの作成
        tab3 = ttk.Frame(self.notebook)
        self.notebook.add(tab3, text='等級一覧表')
        
        self.rank_list_detail(tab3)
        

    
    
        
    def rank_list_detail(self, rank_list_frame):
        from ..GUI_Logic.Logic_etc import Toggle_Button_rank
        from ..GUI_Logic.text_box_RE import Rank_open_text
        from pandastable import Table
        from staff_manegement_app.data.SQL_center import Rank_list_all
        
        button_frame = ttk.Frame(rank_list_frame)
        button_frame.pack()
        table_frame = ttk.Frame(rank_list_frame)
        table_frame.pack(fill='both', expand=True)
        
        self.rank_data = Rank_list_all()
        rank_data = self.rank_data.get_data()
        column_names = self.rank_data.column_get()
        
        def format_with_commas(x):
            if x in exclusion:
                pass
            else:
                if isinstance(x, (int, float)):
                    return ' ' + '{:,}'.format(x)
                return x
        rank_data = rank_data.sort_values('総支給額見込', ascending=False)
        exclusion = ["等級","サブランク","能力"]
        for col in column_names:
            rank_data[col] = rank_data[col].apply(format_with_commas)
        
        rank_data.fillna(0).infer_objects()
            
        rank_table = Table(table_frame,dataframe=rank_data)
        
        Toggle_Button_rank(button_frame,rank_table)
        
        rank_table.show()
        
        
        Rank_open_text(rank_table)
        
        for colname in column_names:
            try:
                if colname in exclusion:
                    pass
                else:
                    rank_table.columnformats['alignment'][colname] = 'e'
            except KeyError:
                print(f'Column {colname} does not exist.')
        
        rank_table.columnwidths["等級"] = 50

   

        