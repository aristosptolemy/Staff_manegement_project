import tkinter as tk
from GUI.gui_module import Apps
from data.update import UpdateVersion
#pyinstall __main__.spec



if __name__ == '__main__':
    updater = UpdateVersion()
    if not updater.check_for_updates():
        root = tk.Tk()
        app = Apps(master=root)
        app.mainloop()

