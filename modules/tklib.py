import tkinter as tk
from tkinter import ttk
from modules.parameters import *


class Window(tk.Toplevel):
    stack = [None]  # store toplevel and frames

    def __init__(self, root, title, geometry):
        super().__init__(root)
        self.root = root
        self.title(title)
        self.geometry(geometry)
        self.configure(bg=COLOR_BACKGROUND)
        self.iconbitmap(PATH_ICON_TYPING)
        Window.stack.append(self)

    def add_label_instruction(self, row=1, padx=0, pady=0):
        self.var_instruction = tk.StringVar()

        self.label_instruction = LabelTwo(
            row=row,
            textvariable=self.var_instruction,
            font=FONT_LABEL_INSTRUCTION,
            anchor="se")
        self.label_instruction.grid(columnspan=2, padx=padx, pady=pady)

    def close(self):
        self.protocol(
            'WM_DELETE_WINDOW',
            func=lambda: (self.destroy(), self.root.destroy()))


class WindowNotify(Window):
    def __init__(self, root, title):
        super().__init__(
            root=root,
            title=title,
            geometry=GEOMETRY_WINDOW_NOTIFY)

    def add_label(self, row, text: str):
        LabelTwo(
            row=row,
            text=text,
            font=FONT_LABEL_NOTIFY,
            wraplength=300,
            anchor="center")
        self.update()


class WindowMain(Window):
    def __init__(self, root, title):
        super().__init__(
            root=root,
            title=title,
            geometry=GEOMETRY_WINDOW_MAIN)
        self.close()

    def add_frame(self, row=0, col=0, row_weight=1,
                  col_weight=1, pad=(0, 0, 0, 0), col_span=1, **kw):
        Window.stack.append(self)

        frame = FrameTwo(row=row, col=col, pad=pad)
        frame.grid(columnspan=col_span)

        self.rowconfigure(row, weight=row_weight)
        self.columnconfigure(col, weight=col_weight)
        return frame


class FrameOne(tk.Frame):
    def __init__(self, row=0, col=0, **kw):
        super().__init__(Window.stack[-1], **kw)
        self.grid(row=row, column=col)
        Window.stack.append(self)


class FrameTwo(FrameOne):
    # pad = (left, right, top, bottom)
    def __init__(self, row=0, col=0, pad=(0, 0, 0, 0), **kw):
        super().__init__(row=row, col=col, bg=COLOR_BACKGROUND, **kw)
        self.grid(sticky="nesw", padx=(pad[0], pad[1]), pady=(pad[2], pad[3]))


class LabelOne(tk.Label):
    def __init__(self, row=0, col=0, **kw):
        super().__init__(Window.stack[-1], **kw)
        self.grid(row=row, column=col)


class LabelTwo(LabelOne):
    def __init__(self, row=0, col=0, **kw):
        super().__init__(row=row, col=col, bg=COLOR_BACKGROUND, **kw)
        self.grid(sticky="nesw")
        Window.stack[-1].rowconfigure(row, weight=1)
        Window.stack[-1].columnconfigure(col, weight=1)


class LabelThree(LabelOne):
    def __init__(self, row=0, bg='light gray', **kw):
        super().__init__(row=row, col=0, bg=bg, font=FONT_LABEL_RESULT,
                         anchor='w', padx=10, pady=5, **kw)
        self.grid(sticky="nesw")


class LabelFour(LabelOne):
    def __init__(self, row=0, bg='light gray', fg='black', **kw):
        super().__init__(row=row, col=1, bg=bg, fg=fg,
                         font=FONT_LABEL_RESULT, anchor='center', padx=5, **kw)
        self.grid(sticky="nesw")


class ButtonOne(tk.Button):
    def __init__(self, row=0, col=0, **kw):
        super().__init__(Window.stack[-1],
                         relief=tk.FLAT, cursor="heart", **kw)
        self.grid(row=row, column=col)


class ButtonTwo(ButtonOne):
    def __init__(self, row=0, col=0, **kw):
        super().__init__(row=row, col=col, bg=COLOR_BACKGROUND, **kw)


class ButtonThree(ButtonTwo):
    def __init__(self, row=0, col=0, **kw):
        super().__init__(row=row, col=col, **kw)
        Window.stack[-1].rowconfigure(row, weight=1)
        Window.stack[-1].columnconfigure(col, weight=1)


class Text(tk.Text):
    def __init__(self, row=0, col=0, **kw):
        super().__init__(
            Window.stack[-1],
            width=60,
            height=2,
            font=FONT_TEXT_VOCABULARY,
            wrap="word",
            padx=20,
            pady=20,
            **kw)
        self.grid(row=row, column=col)
        Window.stack[-1].rowconfigure(row, weight=1)
        Window.stack[-1].columnconfigure(col, weight=1)


class Entry(tk.Entry):
    def __init__(self, row=0, col=1, **kw):
        super().__init__(
            Window.stack[-1],
            width=35,
            font=FONT_ENTRY_TYPING,
            borderwidth=10,
            relief=tk.FLAT,
            **kw)
        self.grid(row=row, column=col)
        Window.stack[-1].rowconfigure(row, weight=1)
        Window.stack[-1].columnconfigure(col, weight=0)


class TButton(ttk.Button):
    def __init__(self, row=0, col=0, **kw):
        super().__init__(Window.stack[-1], style="TButton", width=0, **kw)
        self.grid(row=row, column=col)


class TCombobox(ttk.Combobox):
    def __init__(self, variable, options: dict, row=0, col=0):
        values = list(options.keys())
        default = values[0]
        variable.set(default)
        longest_option = max(values, key=len)
        combobox_width = len(longest_option)
        super().__init__(
            Window.stack[-1],
            values=values,
            textvariable=variable,
            state="readonly",
            font=FONT_TCOMBOBOX,
            width=combobox_width,
            justify="center")
        self.grid(row=row, column=col, ipady=2)
        Window.stack[-1].option_add('*TCombobox*Listbox*Font', FONT_TCOMBOBOX)
        Window.stack[-1].rowconfigure(row, weight=1)
        Window.stack[-1].columnconfigure(col, weight=1)


class TEntry(ttk.Entry):
    def __init__(self, row=0, col=0, **kw):
        super().__init__(
            Window.stack[-1],
            style="TEntry",
            font=FONT_TENTRY_SEARCH,
            foreground='gray',
            **kw)
        self.grid(row=row, column=col)
        Window.stack[-1].rowconfigure(row, weight=1)
        Window.stack[-1].columnconfigure(col, weight=1)


class TTreeview(ttk.Treeview):
    def __init__(self, row=0, col=0, **kw):
        super().__init__(
            Window.stack[-1],
            columns=("No.", "Topic", "Size"),
            show="headings",
            **kw)
        self.grid(row=row, column=col, sticky="nesw")
        Window.stack[-1].rowconfigure(row, weight=1)
        Window.stack[-1].columnconfigure(col, weight=1)
