import tkinter as tk
import time

class App:
    def __init__(self, master):
        self.master = master
        self.label = tk.Label(master, text="Initializing...")
        self.label.pack()
        self.initialize()

    def initialize(self):
        time.sleep(5)  # 長時間の初期化処理をシミュレート
        self.label.config(text="Initialization Complete")

root = tk.Tk()
app = App(root)
root.mainloop()
