from modules.tklib import *
from modules.parameters import *


class WindowFirst(Window):
    def __init__(self, root, manager):
        super().__init__(
            root=root,
            title=TITLE_WINDOW_FIRST,
            geometry=GEOMETRY_WINDOW_FIRST
        )
        self.manager = manager
        self.add_label_greeting()
        self.add_combobox()
        self.add_label_name()
        self.add_button_england()
        self.add_button_france()
        self.add_label_instruction(row=3, padx=10, pady=10)
        self.close()

    def add_label_greeting(self):
        label_greeting = LabelTwo(
            font=FONT_LABEL_GREETING,
            compound='left',
            anchor="nw")
        label_greeting.grid(padx=10, pady=10)

        if TIME_MORNING_START <= TIME_CURRENT < TIME_MORNING_END:
            label_greeting.config(
                image=self.manager.P.IMG_MORNING,
                text=" " + TEXT_MORNING
            )
        elif TIME_AFTERNOON_START <= TIME_CURRENT < TIME_AFTERNOON_END:
            label_greeting.config(
                image=self.manager.P.IMG_AFTERNOON,
                text=" " + TEXT_AFTERNOON
            )
        else:
            label_greeting.config(
                image=self.manager.P.IMG_EVENING,
                text=" " + TEXT_EVENING
            )

    def add_combobox(self):
        self.var_option = tk.StringVar()

        option_menu = TCombobox(
            col=1,
            variable=self.var_option,
            options=COMBOBOX_NATIVE)
        option_menu.grid(sticky="ne", padx=20, pady=20)

        option_menu.bind(
            "<Enter>",
            lambda e: self.var_instruction.set(TEXT_INSTRUCTION_1))
        option_menu.bind("<Leave>", lambda e: self.var_instruction.set(""))

    def add_label_name(self):
        label_name = LabelTwo(
            row=1,
            text=TEXT_NAME_SOFTWARE,
            font=FONT_LABEL_NAME,
            anchor="center")
        label_name.grid(columnspan=2, pady=15)

    def add_button_england(self):
        button_england = ButtonThree(
            row=2,
            image=self.manager.P.IMG_MAP_ENGLAND,
            command=self.click_button_england
        )
        button_england.grid(sticky="e", padx=15)
        button_england.bind(
            "<Enter>",
            lambda e: self.var_instruction.set(TEXT_INSTRUCTION_2))
        button_england.bind("<Leave>", lambda e: self.var_instruction.set(""))

    def add_button_france(self):
        button_france = ButtonThree(
            row=2,
            col=1,
            image=self.manager.P.IMG_MAP_FRANCE,
            command=self.click_button_france
        )
        button_france.grid(sticky="w", padx=15)
        button_france.bind(
            "<Enter>",
            lambda e: self.var_instruction.set(TEXT_INSTRUCTION_2))
        button_france.bind("<Leave>", lambda e: self.var_instruction.set(""))

    def click_button_england(self):
        native = COMBOBOX_NATIVE[self.var_option.get()]
        self.manager.switch_to_window_second(language="en", native=native)

    def click_button_france(self):
        native = COMBOBOX_NATIVE[self.var_option.get()]
        self.manager.switch_to_window_second(language="fr", native=native)
