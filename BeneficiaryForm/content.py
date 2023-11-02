from os import makedirs, path
from pathlib import Path
from tkinter import Frame, Button, Label
from PIL import Image, ImageTk

import numpy as np
import pandas as pd

from windows.standard_format import set_language, WelcomeWindow, PersonalDataWindow, FamilialSituationAgeWindow, \
    BenefitsWindow
from signature.beneficiary import BeneficiarySignature
from signature.technician import TechnicianSignature


class MainView(Frame):
    def __init__(self, parent, language, img_bgd, *args, **kwargs):
        super().__init__(parent, padx=1, pady=1, *args, **kwargs)
        self.parent = parent
        self.language = language
        self.img_bgd = img_bgd
        self.current_page = 0
        self.output_path_dir = Path(r'C:\Users\rcucu\Documents\Bénévolat\Caritas\code\data')

        self.w_welcome = WelcomeWindow(self, w_number=0)
        self.w1 = PersonalDataWindow(self, w_number=1)
        self.w2 = FamilialSituationAgeWindow(self, w_number=2)
        self.w3 = BenefitsWindow(self,w_number=3)

        self.w22 = BeneficiarySignature(self,w_number=4)
        self.w23 = TechnicianSignature(self, w_number=5)
        self.list_windows = [self.w_welcome, self.w1, self.w2, self.w3, self.w22, self.w23]

        buttonframe = Frame(self, background='white')
        bottombuttonframe = Frame(self, background='')
        container = Frame(self, background='')
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side='top', fill="both", expand=True)
        bottombuttonframe.pack(side='bottom', fill="x", expand=False)

        self.w_welcome.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.w1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.w2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.w3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.w22.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.w23.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b00 = Button(buttonframe, text='Menu', command=self.w_welcome.show, bg='#99EDC3')
        b0 = Button(buttonframe, text='Données Personnelles', command=self.w1.show, bg='#99EDC3')
        b01 = Button(buttonframe, text='Situation Familiale', command=self.w2.show, bg='#99EDC3')
        b02 = Button(buttonframe, text=set_language(self.language)[22], command=self.w3.show, bg='#99EDC3')
        b1 = Button(buttonframe, text="Signature Bénéficiaire", command=self.w22.show, bg='#99EDC3')
        b2 = Button(buttonframe, text="Signature Technicien", command=self.w23.show, bg='#99EDC3')
        b3 = Button(bottombuttonframe, text="Suivant", bg='#3DED97', command=self.go_next_window)
        b4 = Button(bottombuttonframe, text="En arrière", bg='#3DED97', command=self.go_previous_window)

        b00.pack(side='left')
        b0.pack(side='left')
        b01.pack(side='left')
        b02.pack(side='left')
        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side='right')
        b4.pack(side='right')
        self.w_welcome.show()

    def set_page(self, w_number):
        self.current_page = w_number

    def go_previous_window(self):

        if self.current_page == 0:
            self.set_language(self.w_welcome.language_box.get())
            print(f'Language choosen: {self.language}')

        else:
            self.current_page = self.current_page - 1
            print(self.current_page)
            # name_window = "w" + str(self.current_page)
            current_window = [w for w in self.list_windows if w.number == self.current_page][0]
            print(current_window.number)
            current_window.show()

    def go_next_window(self):
        if self.current_page == 0:
            self.set_language(self.w_welcome.language_box.get())
            print(f'Language choosen: {self.language}')
            # TODO: top buttons should be inactive while being on w==0

        if self.current_page < len(self.list_windows) - 1:
            self.current_page = self.current_page + 1
            current_window = [w for w in self.list_windows if w.number == self.current_page][0]
            current_window.show()

    def save_signatures(self, output_folder):
        self.w22.save(output_folder / 'sig_beneficiary.jpg')
        self.w23.save(output_folder / 'sig_technician.jpg')

    def save_data(self):

        name_output_folder = self.output_path_dir / self.w23.nb_PC.get()

        if not path.exists(name_output_folder):
            makedirs(name_output_folder)

        self.save_signatures(name_output_folder)

        w0 = np.array([])
        for w in self.list_windows:
            w0 = np.concatenate((w0, w.get_all_entries()), axis=None)

        w0 = np.array(w0)
        data = pd.DataFrame(w0[:, None].T, columns=[str(i) for i in range(0, w0.size)])
        print(data.to_string())
        # TODO: ne pas laisser l'utilisateur sauvegarder s'il manque le n° de PC

        data.to_csv(name_output_folder / ('data_' + self.w23.nb_PC.get() + '.csv'), sep=',')

    def set_language(self, lang):
        self.language = lang
