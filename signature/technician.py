from tkinter import Button, Label, Entry
from tkinter.ttk import Combobox
import numpy as np
import re
from signature.standard import SignatureWindow

from data_io.errors import NoElementSelectedError, InvalidCharError


class TechnicianSignature(SignatureWindow):
    def __init__(self, parent, w_number):
        super().__init__(parent, w_number)

        self.nb_PC_label = Label(self, text='N° PC:')
        self.nb_PC_label.place(x=50, y=13)
        self.nb_PC = Entry(self)
        self.nb_PC.place(x=50, y=63)

        self.nb_screen_label = Label(self, text='N° Ecran:')
        self.nb_screen_label.place(x=250, y=13)
        self.nb_screen = Entry(self)
        self.nb_screen.place(x=250, y=63)

        self.PC_type_lab = Label(self, text='Type ordinateur')
        self.PC_type_lab.place(x=450, y=13)
        self.PC_type = Combobox(self, values=['Fixe', 'Portable'])
        self.PC_type.place(x=450, y=63)

        self.label_bs = Label(self, text=' '.join([self.get_text_label(str(s)) for s in list(range(99, 106, 2))]),
                              font=("bold", 13), background='white', wraplength=self.width * 3 / 4)
        self.label_bs.place(x=50, y=263)

        self.button_save_data = Button(self, text='Sauvegarder données', command=self.get_data, bg='#f08080')
        self.button_save_data.place(x=900, y=500)

        self.pack(side="top", fill="both", expand=True)
        self.configure()

    def save(self, filename='sig_technician.jpg'):
        self.image.save(filename)

    def get_all_entries(self):
        return np.array([self.nb_PC.get(), self.nb_screen.get(), self.PC_type.get()])

    def check_entry(self):
        if any(len(v) == 0 for v in [self.nb_PC.get(), self.PC_type.get()]):
            raise NoElementSelectedError

        #elif not re.match(r'[z0-9]+$', self.nb_PC.get()):
        #TODO: be more precise/\(?([0-9]{6})\)?([ .-]?)([0-9]{3})\2([0-9]{4})/
            #raise InvalidCharError

        #elif len(self.nb_screen.get()) != 0 and not re.match(r'[z0-9]+$', self.nb_screen.get()):
            #raise InvalidCharError