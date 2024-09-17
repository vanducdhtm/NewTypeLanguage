import os
import tkinter as tk
from ctypes import windll
from modules.parameters import PATH_FOLDER_DATA
from modules.window_notify import WindowDownloadData
from modules.window_manager import WindowManager


windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()
root.withdraw()

if not os.path.exists(PATH_FOLDER_DATA):
    WindowDownloadData(root)
if os.path.exists(PATH_FOLDER_DATA):
    WindowManager(root).switch_to_window_first()
    # WindowManager(root).switch_to_window_second("en", "vi")
    # WindowManager(root).switch_to_window_third("en", "vi")

root.mainloop()
