from tkinter import Button, Label, Entry

import numpy as np

from signature.standard import SignatureWindow
from windows.standard_format import set_language


class TechnicianSignature(SignatureWindow):
    def __init__(self, parent, w_number):
        super().__init__(parent, w_number)

        self.nb_PC_label = Label(self, text=set_language(lang)[29])
        self.nb_PC_label.place(x=50, y=13)
        self.nb_PC = Entry(self)
        self.nb_PC.place(x=50, y=63)

        self.nb_screen_label = Label(self, text=set_language(lang)[30])
        self.nb_screen_label.place(x=250, y=13)
        self.nb_screen = Entry(self)
        self.nb_screen.place(x=250, y=63)

        label_bs = Label(self, text=set_language(lang)[8], font=("bold", 13), background='white')
        label_bs.place(x=50, y=263)

        button_save_data = Button(self, text=set_language(lang)[31], command=self.get_data, bg='#99EDC3')
        button_save_data.place(x=900, y=500)

        self.pack(side="top", fill="both", expand=True)
        self.configure()

    def save(self, filename='sig_technician.jpg'):
        self.image.save(filename)

    def get_all_entries(self):
        return np.array([self.nb_PC.get(), self.nb_screen.get()])