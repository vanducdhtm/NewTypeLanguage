from modules.tklib import *
from modules.parameters import *


class WindowSecond(WindowMain):
    def __init__(self, root, manager, language, native):
        super().__init__(root=root, title=TITLE_WINDOW_SECOND)
        self.manager = manager
        self.language = language
        self.native = native

        # add toolbar
        self.add_frame(pad=(10, 0, 10, 0))
        self.add_button_new()
        self.add_button_edit()
        self.add_button_copy()
        self.add_button_merge()
        self.add_button_delete()
        self.add_button_help()

        # add search bar
        self.add_frame(col=1, pad=(0, 10, 10, 0))
        self.add_entry_search()

        # add breadcrumb
        self.add_frame(row=1, pad=(10, 10, 0, 0), col_span=2)
        self.add_crumb_1()
        self.add_label_arrow(col=1)
        self.add_crumb_2()
        self.add_label_arrow(col=3)
        self.add_crumb_3()

        # add table
        self.add_frame(row=2, row_weight=20, pad=(10, 10, 0, 0), col_span=2)
        self.add_treeview()

        # add navigation and instruction
        self.add_frame(row=3, row_weight=0, pad=(10, 10, 10, 0), col_span=2)
        self.add_button_previous()
        self.add_button_next()
        self.add_label_instruction()
        self.var_instruction.set("Đây là nội dung hướng dẫn")

    def add_button_new(self):
        button_new = TButton(image=self.manager.P.IMG_NEW)

    def add_button_edit(self):
        button_edit = TButton(col=1, image=self.manager.P.IMG_EDIT)

    def add_button_copy(self):
        button_copy = TButton(col=2, image=self.manager.P.IMG_COPY)

    def add_button_merge(self):
        button_merge = TButton(col=3, image=self.manager.P.IMG_MERGE)

    def add_button_delete(self):
        button_delete = TButton(col=4, image=self.manager.P.IMG_DELETE)

    def add_button_help(self):
        button_help = TButton(col=5, image=self.manager.P.IMG_HELP)

    def add_entry_search(self):
        entry_search = TEntry()
        entry_search.insert(0, TEXT_ENTRY_SEARCH)
        entry_search.grid(pady=10, sticky="ne")

    def add_crumb_1(self):
        crumb_1 = TButton(text="Chủ đề")

    def add_crumb_2(self):
        crumb_2 = TButton(col=2, text="Đồ vật trong nhà")

    def add_crumb_3(self):
        crumb_3 = TButton(col=4, text="Máy gặt")

    def add_label_arrow(self, col):
        LabelOne(
            col=col,
            image=self.manager.P.IMG_NEXT2,
            bg=COLOR_BACKGROUND)

    def add_treeview(self):
        TTreeview()

    def add_button_previous(self):
        button_previous = ButtonThree(
            image=self.manager.P.IMG_PREVIOUS,
            command=self.manager.switch_to_window_first)
        button_previous.grid(sticky="w")

    def add_button_next(self):
        button_next = ButtonThree(
            col=1,
            image=self.manager.P.IMG_NEXT,
            command=lambda: self.manager.switch_to_window_third(
                self.language,
                self.native))
        button_next.grid(sticky="e")
