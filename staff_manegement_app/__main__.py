import tkinter as tk
from GUI.gui_module import Apps
from data.update import Update_Version
#起動　python 



if __name__ == '__main__':
    updater = Update_Version()
    if not updater.check_for_updates():
        root = tk.Tk()
        app = Apps(master=root)
        app.mainloop()

