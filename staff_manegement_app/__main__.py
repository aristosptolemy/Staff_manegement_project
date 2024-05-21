import tkinter as tk
from staff_manegement_app.GUI.gui_module import Apps




if __name__ == '__main__':
    root = tk.Tk()
    app = Apps(master=root)
    app.mainloop()
