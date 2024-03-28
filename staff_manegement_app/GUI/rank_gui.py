import pandas as pd
from pandastable import Table, TableModel
import mysql.connector


import tkinter as tk
from tkinter import ttk

def rank_list_tab(notebook):
    rank_tab = ttk.Frame(notebook)
    notebook.add(rank_tab, text='等級一覧')
    #return

    def open_text_editor(event):
        # 現在選択されているセルの行と列を取得
        col = self.rank_pt.getSelectedColumn()
        row = self.rank_pt.getSelectedRow()
        self.selected_rank_data = self.rank_pt.model.df.iloc[row]
        self.selected_column_name = self.rank_pt.model.df.columns[col]
        if col is not None and row is not None:
            value = self.rank_pt.model.getValueAt(row, col)

            try:
                value = value.replace(',', '').strip()
                value = int(value) if value else 0
            except Exception as e:
                print(f"Error occurred: {e}")
            #print(value)

            
            # 新しいウィンドウを作成
            self.top = tk.Toplevel()
            self.top.title("詳細")
            self.rank_text = tk.Text(self.top, wrap="word")
            self.rank_text.insert('end', value)
            self.rank_text.pack(expand=True, fill='both')
            button = ttk.Button(self.top,text="更新",command=self.rank_list_update)
            button.pack()




    with sqlite3.connect('staff.db') as conn:
        c = conn.cursor()
        rank_list_df = pd.read_sql('SELECT * FROM rank_list', conn)


        int_df = rank_list_df[(rank_list_df['サブランク'] != '総務担当\n') & (rank_list_df['サブランク'] != 'As')]

        as_df = rank_list_df[rank_list_df['サブランク'] == 'As']



        office_work_df = rank_list_df[rank_list_df['サブランク'] == '総務担当\n']
        office_work_df = office_work_df.sort_values(by=['等級'],ascending=[False])


        int_df = int_df.sort_values(by=['等級', 'サブランク'],ascending=[False, True])

        #str_df = str_df.sort_values(by=['サブランク'],ascending=[False])

        
        result = pd.concat([int_df,as_df,office_work_df])

        #print(result)

        


        for col in new_format:
            result[col] = result[col].apply(self.format_with_commas)
        
        # PandasTableの作成と配置
        frame = tk.Frame(rank_tab)
        frame.pack(fill='both', expand=True)

        self.rank_pt = Table(frame, dataframe=result)

        self.rank_pt.show()
        self.rank_pt.bind("<Double-1>", open_text_editor)

        column_names = ['等級','サブランク','総支給額見込','基本給','役割実行手当','特別精勤手当','皆勤手当','支給額小計','時給','残業単価','残業時間','残業代見込']

        for colname in column_names:
            try:
                self.rank_pt.columnformats['alignment'][colname] = 'e'
            except KeyError:
                print(f'Column {colname} does not exist.')
