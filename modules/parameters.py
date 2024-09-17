import os
import datetime
import sys
import tkinter as tk
from tkinter import ttk


# link
URL_DRIVE_DATA = r"https://drive.google.com/file/d/1Eh6yjHuu-MEwQ3vY6mlqHDzsF6GoJxmQ/view?usp=drive_link"
FILE_ID = URL_DRIVE_DATA.split("/")[5]
URL_GDOWN = f"https://drive.google.com/uc?id={FILE_ID}"

# path
PATH_FOLDER_PROJET = os.path.abspath(".")
PATH_FOLDER_DATA = PATH_FOLDER_PROJET + "\\TypeLanguageData"
PATH_FILE_TAR = PATH_FOLDER_PROJET + "\\TypeLanguageData.tar"

try:
    PATH_FOLDER_IMG = sys._MEIPASS + "\\imgs"
except Exception:
    PATH_FOLDER_IMG = PATH_FOLDER_PROJET + "\\imgs"

PATH_IMG_AFTERNOON = PATH_FOLDER_IMG + "\\afternoon.png"
PATH_IMG_COPY = PATH_FOLDER_IMG + "\\copy.png"
PATH_IMG_DEFINITION_OFF = PATH_FOLDER_IMG + "\\definition_off.png"
PATH_IMG_DEFINITION_ON = PATH_FOLDER_IMG + "\\definition_on.png"
PATH_IMG_DELETE = PATH_FOLDER_IMG + "\\delete.png"
PATH_IMG_EARPHONE_ON = PATH_FOLDER_IMG + "\\earphone_on.png"
PATH_IMG_EARPHONE_OFF = PATH_FOLDER_IMG + "\\earphone_off.png"
PATH_IMG_EDIT = PATH_FOLDER_IMG + "\\edit.png"
PATH_IMG_EVENING = PATH_FOLDER_IMG + "\\evening.png"
PATH_IMG_HELP = PATH_FOLDER_IMG + "\\help.png"
PATH_IMG_MAP_ENGLAND = PATH_FOLDER_IMG + "\\map_england.png"
PATH_IMG_MAP_FRANCE = PATH_FOLDER_IMG + "\\map_france.png"
PATH_IMG_MERGE = PATH_FOLDER_IMG + "\\merge.png"
PATH_IMG_MINUTE1 = PATH_FOLDER_IMG + "\\minute1.png"
PATH_IMG_MINUTE2 = PATH_FOLDER_IMG + "\\minute2.png"
PATH_IMG_MINUTE5 = PATH_FOLDER_IMG + "\\minute5.png"
PATH_IMG_MINUTE10 = PATH_FOLDER_IMG + "\\minute10.png"
PATH_IMG_MORNING = PATH_FOLDER_IMG + "\\morning.png"
PATH_IMG_NEW = PATH_FOLDER_IMG + "\\new.png"
PATH_IMG_NEXT = PATH_FOLDER_IMG + "\\next.png"
PATH_IMG_NEXT2 = PATH_FOLDER_IMG + "\\next2.png"
PATH_IMG_PREVIOUS = PATH_FOLDER_IMG + "\\previous.png"
PATH_IMG_REFRESH = PATH_FOLDER_IMG + "\\refresh.png"
PATH_IMG_SOUND_OFF = PATH_FOLDER_IMG + "\\sound_off.png"
PATH_IMG_SOUND_ON = PATH_FOLDER_IMG + "\\sound_on.png"
PATH_IMG_SOUND = PATH_FOLDER_IMG + "\\sound.png"
PATH_IMG_TRANSLATE_OFF = PATH_FOLDER_IMG + "\\translate_off.png"
PATH_IMG_TRANSLATE_ON = PATH_FOLDER_IMG + "\\translate_on.png"
PATH_IMG_WRITING = PATH_FOLDER_IMG + "\\writing.png"
PATH_ICON_TYPING = PATH_FOLDER_IMG + "\\typing.ico"

# title
TITLE_WINDOW_DOWNLOAD_DATA = "Tải dữ liệu"
TITLE_WINDOW_FIRST = "Xin chào"
TITLE_WINDOW_SECOND = "Chủ đề"
TITLE_WINDOW_THIRD = "Luyện tập"

# screen
root = tk.Tk()
root.withdraw()
root.update_idletasks()
SCREEN_DPI = root.winfo_fpixels("1i")
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()
root.destroy()

# geometry
def center_window(width, height):
    x = (SCREEN_WIDTH - width) // 2
    y = (SCREEN_HEIGHT - height) // 2
    return f"{width}x{height}+{x}+{y}"

WIDTH_WINDOW_NOTIFY = 320
WIDTH_WINDOW_FIRST = 960
WIDTH_WINDOW_MAIN = 1280

HEIGHT_WINDOW_NOTIFY = 180
HEIGHT_WINDOW_FIRST = 540
HEIGHT_WINDOW_MAIN = 720

GEOMETRY_WINDOW_NOTIFY = center_window(
    WIDTH_WINDOW_NOTIFY, HEIGHT_WINDOW_NOTIFY)
GEOMETRY_WINDOW_FIRST = center_window(
    WIDTH_WINDOW_FIRST, HEIGHT_WINDOW_FIRST)
GEOMETRY_WINDOW_MAIN = center_window(
    WIDTH_WINDOW_MAIN, HEIGHT_WINDOW_MAIN)

# font
def size(size: int):
    new_size = round((size * 96) / SCREEN_DPI)
    return new_size

FONT_LABEL_NOTIFY = ("Arial", size(16))
FONT_LABEL_GREETING = ("Arial", size(16), "italic")
FONT_LABEL_NAME = ("Times New Roman", size(36), "italic")
FONT_LABEL_INSTRUCTION = ("Arial", size(16), "italic")
FONT_LABEL_MEANING = ("Helvetica", size(28), "italic")
FONT_LABEL_COUNTDOWN = ("Times New Roman", size(24))
FONT_LABEL_RESULT = ("Helvetica", size(15))

FONT_BUTTON_PHONETIC = ("Helvetica", size(19), "bold")
FONT_TEXT_VOCABULARY = ("Times New Roman", size(24))
FONT_ENTRY_TYPING = ("Times New Roman", size(24))
FONT_TCOMBOBOX = ("Arial", size(16))
FONT_TENTRY_SEARCH = ("Arial", size(16), "italic")
FONT_TBUTTON = ("Arial", size(16), "italic")

# color
COLOR_BACKGROUND = "light blue"

# time
TIME_CURRENT = datetime.datetime.now().time()
TIME_MORNING_START = datetime.time(5, 0)
TIME_MORNING_END = datetime.time(12, 0)
TIME_AFTERNOON_START = TIME_MORNING_END
TIME_AFTERNOON_END = datetime.time(18, 0)

# text
TEXT_MORNING = "Chào buổi sáng!"
TEXT_AFTERNOON = "Chào buổi chiều!"
TEXT_EVENING = "Buổi tối vui vẻ!"

TEXT_NAME_SOFTWARE = "Học ngoại ngữ bằng gõ 10 ngón"

TEXT_INSTRUCTION_1 = "Lựa chọn ngôn ngữ phiên dịch"
TEXT_INSTRUCTION_2 = "Lựa chọn ngoại ngữ bạn muốn học"

TEXT_DOWNLOAD_DATA_1 = "Đang tải dữ liệu..."
TEXT_DOWNLOAD_DATA_2 = "Đang giải nén dữ liệu..."
TEXT_DOWNLOAD_DATA_3 = "Hoàn tất."
TEXT_DOWNLOAD_DATA_4 = "Vui lòng kết nối mạng để tải dữ liệu.\n\nCảm ơn!"

TEXT_ENTRY_SEARCH = "Tìm kiếm"

TEXT_RESULT_TABLE_1 = "Số từ trên phút"
TEXT_RESULT_TABLE_2 = "Số phím đã gõ"
TEXT_RESULT_TABLE_3 = "Số từ đúng"
TEXT_RESULT_TABLE_4 = "Số từ đúng"

# combobox
COMBOBOX_NATIVE = {
    "Tiếng Việt": "vi",
    "Tiếng Anh": "en",
    "Tiếng Pháp": "fr"
}


class Parameters():
    def __init__(self):
        self.style()
        self.image()

    @staticmethod
    def style():
        style = ttk.Style()
        style.configure(
            'TButton',
            padding=(5, 5, 5, 5),
            background=COLOR_BACKGROUND,
            font=FONT_TBUTTON)
        style.configure(
            'TEntry',
            padding=(10, 5, 10, 5),
            background=COLOR_BACKGROUND)

    def image(self):
        self.IMG_MORNING = tk.PhotoImage(
            file=PATH_IMG_MORNING).subsample(10, 10)
        self.IMG_AFTERNOON = tk.PhotoImage(
            file=PATH_IMG_AFTERNOON).subsample(10, 10)
        self.IMG_EVENING = tk.PhotoImage(
            file=PATH_IMG_EVENING).subsample(10, 10)
        self.IMG_MAP_ENGLAND = tk.PhotoImage(
            file=PATH_IMG_MAP_ENGLAND).subsample(2, 2)
        self.IMG_MAP_FRANCE = tk.PhotoImage(
            file=PATH_IMG_MAP_FRANCE).subsample(2, 2)
        self.IMG_NEW = tk.PhotoImage(
            file=PATH_IMG_NEW).subsample(10, 10)
        self.IMG_EDIT = tk.PhotoImage(
            file=PATH_IMG_EDIT).subsample(10, 10)
        self.IMG_COPY = tk.PhotoImage(
            file=PATH_IMG_COPY).subsample(10, 10)
        self.IMG_MERGE = tk.PhotoImage(
            file=PATH_IMG_MERGE).subsample(10, 10)
        self.IMG_DELETE = tk.PhotoImage(
            file=PATH_IMG_DELETE).subsample(10, 10)
        self.IMG_HELP = tk.PhotoImage(
            file=PATH_IMG_HELP).subsample(10, 10)
        self.IMG_NEXT2 = tk.PhotoImage(
            file=PATH_IMG_NEXT2).subsample(25, 25)
        self.IMG_PREVIOUS = tk.PhotoImage(
            file=PATH_IMG_PREVIOUS).subsample(10, 10)
        self.IMG_NEXT = tk.PhotoImage(
            file=PATH_IMG_NEXT).subsample(10, 10)
        self.IMG_SOUND_ON = tk.PhotoImage(
            file=PATH_IMG_SOUND_ON).subsample(10, 10)
        self.IMG_SOUND_OFF = tk.PhotoImage(
            file=PATH_IMG_SOUND_OFF).subsample(10, 10)
        self.IMG_TRANSLATE_ON = tk.PhotoImage(
            file=PATH_IMG_TRANSLATE_ON).subsample(10, 10)
        self.IMG_TRANSLATE_OFF = tk.PhotoImage(
            file=PATH_IMG_TRANSLATE_OFF).subsample(10, 10)
        self.IMG_DEFINITION_ON = tk.PhotoImage(
            file=PATH_IMG_DEFINITION_ON).subsample(10, 10)
        self.IMG_DEFINITION_OFF = tk.PhotoImage(
            file=PATH_IMG_DEFINITION_OFF).subsample(10, 10)
        self.IMG_EARPHONE_ON = tk.PhotoImage(
            file=PATH_IMG_EARPHONE_ON).subsample(10, 10)
        self.IMG_EARPHONE_OFF = tk.PhotoImage(
            file=PATH_IMG_EARPHONE_OFF).subsample(10, 10)
        self.IMG_MINUTE1 = tk.PhotoImage(
            file=PATH_IMG_MINUTE1).subsample(10, 10)
        self.IMG_MINUTE2 = tk.PhotoImage(
            file=PATH_IMG_MINUTE2).subsample(10, 10)
        self.IMG_MINUTE5 = tk.PhotoImage(
            file=PATH_IMG_MINUTE5).subsample(10, 10)
        self.IMG_MINUTE10 = tk.PhotoImage(
            file=PATH_IMG_MINUTE10).subsample(10, 10)
        self.IMG_WRITING = tk.PhotoImage(
            file=PATH_IMG_WRITING).subsample(10, 10)
        self.IMG_SOUND = tk.PhotoImage(
            file=PATH_IMG_SOUND).subsample(20, 20)
        self.IMG_REFRESH = tk.PhotoImage(
            file=PATH_IMG_REFRESH).subsample(10, 10)
