from modules.tklib import *
from modules.parameters import *


class WindowThird(WindowMain):
    def __init__(self, root, manager, language, native):
        super().__init__(root=root, title=TITLE_WINDOW_THIRD)
        self.manager = manager
        self.language = language
        self.native = native

        # add toolbar
        self.frame_1 = self.add_frame(pad=(10, 10, 10, 0))
        self.frame_1.columnconfigure(0, weight=1)
        self.add_button_sound()
        self.add_button_translate()
        self.add_button_definition()
        self.add_button_earphone()
        self.add_button_clock()
        self.add_button_writing()
        self.add_button_help()

        # add infomations
        self.add_frame(row=1, pad=(10, 10, 0, 0))
        self.add_button_phonetic()
        self.add_label_meaning()
        self.add_text_vocab()

        # add user bar
        self.add_frame_r2()
        self.add_entry_typing()
        self.add_label_countdown()
        self.add_button_refresh()

        # add result table
        self.add_frame_r3()
        self.add_label_col_0()

        # add navigation and instruction
        self.add_frame(row=4, row_weight=0, pad=(10, 10, 10, 0))
        self.add_button_previous()
        self.add_label_instruction()
        self.var_instruction.set("Đây là nội dung hướng dẫn")

    def add_button_sound(self):
        button_sound = ButtonTwo(col=1, image=self.manager.P.IMG_SOUND_ON)

    def add_button_translate(self):
        button_translate = ButtonTwo(
            col=2, image=self.manager.P.IMG_TRANSLATE_ON)

    def add_button_definition(self):
        button_definition = ButtonTwo(
            col=3, image=self.manager.P.IMG_DEFINITION_ON)

    def add_button_earphone(self):
        button_earphone = ButtonTwo(
            col=4, image=self.manager.P.IMG_EARPHONE_ON)

    def add_button_clock(self):
        button_clock = ButtonTwo(col=5, image=self.manager.P.IMG_MINUTE1)

    def add_button_writing(self):
        button_writing = ButtonTwo(col=6, image=self.manager.P.IMG_WRITING)

    def add_button_help(self):
        button_help = ButtonTwo(col=7, image=self.manager.P.IMG_HELP)

    def add_button_phonetic(self):
        button_phonetic = ButtonThree(
            text=" equipment /ɪˈkwɪp.mənt/",
            font=FONT_BUTTON_PHONETIC,
            image=self.manager.P.IMG_SOUND,
            compound="left")

    def add_label_meaning(self):
        label_meaning = LabelTwo(
            row=1,
            font=FONT_LABEL_MEANING,
            text="(n) trang thiết bị, sự trang bị")
        label_meaning.grid(pady=10)

    def add_text_vocab(self):
        self.text_vocab = Text(row=2)
        text = "against actually actual able afraid actually adventure bake acceptable adult bacteria admire accident account act accept additional action action adult accident adventure affair absolutely admit advantage absolute activity addition bag about background adapt affair achievement achievement affect account acquire account about bacteria add age advertising bad actor advanced afraid background advance baby again access acknowledge acquire accommodation accompany accompany admit accommodation advertise badly a actual bacteria absolute an afford advertise adventure admire badly adult about abroad according-to afraid backwards address ability afternoon actress above actual access activity backwards advantage accept affect achieve actress adapt a afterwards after advanced academic address bad abandon again above accurate accident according-to advance accurate adopt addition actor advise back advice advertising able add administration after academic afford back affect badly balance achieve absolutely addition able abandon absolute activity afford acceptable act bag against accompany an accuse acquire advantage accommodation bag adopt abroad balance back ability"
        self.text_vocab.insert('1.0', text)
        self.text_vocab.grid(pady=(10, 0))

    def add_entry_typing(self):
        entry_typing = Entry()

    def add_label_countdown(self):
        label_countdown = LabelOne(
            col=2,
            font=FONT_LABEL_COUNTDOWN,
            text="10:00",
            bg="gray",
            padx=10,
            pady=9)
        label_countdown.grid(padx=10)

    def add_button_refresh(self):
        button_refresh = ButtonOne(
            col=3,
            image=self.manager.P.IMG_REFRESH,
            bg='gray')

    def add_button_previous(self):
        button_previous = ButtonThree(
            image=self.manager.P.IMG_PREVIOUS,
            command=lambda: self.manager.switch_to_window_second(
                self.language,
                self.native))
        button_previous.grid(sticky="w")
    
    def __add_frame(self, row, height, bg=COLOR_BACKGROUND):
        Window.stack.append(self)
        FrameOne(row=row, height=height, bg=bg)
        self.text_vocab.update_idletasks()
        Window.stack[-1].config(width=self.text_vocab.winfo_width())
        Window.stack[-1].grid_propagate(False)
        
    def add_frame_r2(self):
        self.__add_frame(row=2, height=80, bg="light gray")
        Window.stack[-1].grid(pady=(10, 30))
        Window.stack[-1].columnconfigure(0, weight=1)
        Window.stack[-1].columnconfigure(4, weight=1)

    def add_frame_r3(self):
        self.__add_frame(row=3, height=150)
        self.rowconfigure(3, weight=1)
        Window.stack[-1].columnconfigure(1, weight=1)
        Window.stack[-1].columnconfigure(0, weight=5)
        Window.stack[-1].columnconfigure(2, weight=100)

    def add_label_col_0(self):
        LabelThree(text=TEXT_RESULT_TABLE_1)
        LabelThree(row=1, text=TEXT_RESULT_TABLE_2, bg='gray')
        LabelThree(row=2, text=TEXT_RESULT_TABLE_3)
        LabelThree(row=3, text=TEXT_RESULT_TABLE_4, bg='gray')
        LabelFour(text="0", fg='blue')
        LabelFour(row=1, text="0", bg='gray')
        LabelFour(row=2, text="0", fg='green')
        LabelFour(row=3, text="0", bg='gray', fg='red')
