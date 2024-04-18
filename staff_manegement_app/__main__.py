import tkinter as tk
from .GUI.gui_module import Apps
import cProfile
import pstats

if __name__ == '__main__':
    with cProfile.Profile() as pr:
        root = tk.Tk()
        app = Apps(master=root)
        app.mainloop()
        

    """
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    
    with open('status.txt', 'w') as file:
        stats.stream = file
        stats.print_stats()
        
    """