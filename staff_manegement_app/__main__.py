import tkinter as tk
from .GUI.gui_module import Apps

if __name__ == '__main__':
    root = tk.Tk()
    app = Apps(master=root)
    app.mainloop()