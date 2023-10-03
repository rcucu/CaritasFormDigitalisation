from datetime import datetime
from tkinter import Frame, Label, Entry, ttk, Spinbox

import numpy as np


def set_language(lang):
    fr = ['Données Personnelles',
          'Conditions générales faisant office de garantie et de l acception du matériel par le bénéficiaire',
          '(1) Etat du matériel:  Le matériel distribué est de seconde main, avec 4 ans d’âge minimum. Son état de fonctionnement est celui observé lors de la distribution.\r'
          'Les disfonctionnements créés par le bénéficiaire en modifiant la configuration logicielle ou matérielle relèvent de sa responsabilité et non celle de l’atelier informatique Caritas Vaud.\r',
          '(2) La garantie: Le matériel distribué est garanti sur une période de 6 mois main, à compter du jour de sa distribution au bénéficiaire.\r'
          'Cette garantie ne prend pas en compte \r le système d’exploitation, ni les logiciels installés lors de la distribution; moins encore ceux ajoutés ou réinstallés par le bénéficiaire lui-même. \r'
          'Seul le matériel est pris en charge pour une réparation ou à défaut un remplacement du composant/équipement défectueux. \r'
          'La garantie n’est valable que si le bénéficiaire n’a aucune responsabilité avérée dans le disfonctionnement constaté.\r',
          'Bénéficiaire: par sa signature, le bénéficiaire certifie avoir lu et remplis le sondage au mieux de ses possibilités.\r '
          'et reçu les explications et les informations sur les points (1) (2) de ce document.',
          'Lausanne, le ____________',
          'Fini !', 'Effacer',
          'Technicien: par sa signature, le technicien certifie avoir aidé le bénéficiaire à remplir correctement le questionnaire du sondage, '
          'transmis les informations sur les points (1) (2) de ce document.', 'Nom:', 'Prénom:', 'Rue + nr:',
          'NPA + Ville:', 'n° Tél:', 'Email:', 'Situation familiale', 'Age', 'Marié(e)', 'Divorcé(e)',
          'Célibataire', 'Séparé(e)', ' Veuf(ve)', 'Prestations sociales', 'Oui', 'Non', 'CSR de:',
          'Année d inscription', 'Assist. social:',
          'Avez-vous déjà suivi des prestations en informatique chez nous ou ailleurs (cours, ateliers, etc) ?',
          'N° PC:', 'N° Ecran:',
          'Sauvegarder les données']
    eng = ['Personnal data', 'Done !', 'Clean']

    dict_lang = {'fr': fr, 'eng': eng}

    return dict_lang[lang]


# TODO: paragraphe parlant expliquant que par la signature, le bénéficiaire accepte
# que Caritas annonymise les données et les transmettent au canton


class Window(Frame):
    def __init__(self, parent, w_number):
        super().__init__(parent, bg='')
        self.parent = parent
        self.number = w_number
        self.posx_1stcol = 400
        self.posx_1strow = 200

        bgd_label = Label(self, image=img_bgd)
        bgd_label['anchor'] = 'nw'
        bgd_label.place(x=0, y=0, relwidth=1, relheight=1)
        bgd_label.pack(side='top', fill='both', expand=True)

    def set_parent_current_page(self):
        self.parent.current_page = self.number
        print(self.parent.current_page)

    def get_data(self):
        self.parent.save_data()

    def show(self):
        self.set_parent_current_page()
        self.lift()

        '''
            try:
                if self.number == window_number:
                    self.lift()

            except ValueError:
                print('This window does not exist')

        '''


class FamilialSituationAgeWindow(Window):
    def __init__(self, parent, w_number):
        super().__init__(parent, w_number)
        self.familial_label = Label(self, text=set_language(lang)[15])
        self.familial_label.place(x=self.posx_1stcol, y=self.posx_1strow)
        self.familial_box = ttk.Combobox(self, values=set_language(lang)[17:22])
        self.familial_box.place(x=self.posx_1stcol, y=self.posx_1strow + 30)

        self.age_label = Label(self, text=set_language(lang)[16])
        self.age_label.place(x=self.posx_1stcol + 300, y=self.posx_1strow)
        self.age_box = Spinbox(self, from_=18, to=110)
        self.age_box.place(x=self.posx_1stcol + 300, y=self.posx_1strow + 30)

    def get_all_entries(self):
        return np.array([self.familial_box.get(), self.age_box.get()])


class BenefitsWindow(Window):
    def __init__(self, parent, w_number):
        super().__init__(parent, w_number)
        self.social_benefits_label = Label(self, text=set_language(lang)[22])
        self.social_benefits_label.place(x=self.posx_1stcol, y=self.posx_1strow)
        self.social_benefits = ttk.Combobox(self, values=set_language(lang)[23:25])
        self.social_benefits.place(x=self.posx_1stcol, y=self.posx_1strow + 30)

        self.CSR_lab = Label(self, text=set_language(lang)[25])
        self.CSR_lab.place(x=self.posx_1stcol + 300, y=self.posx_1strow)
        self.CSR_box = ttk.Combobox(self, values=['Vaud', 'Yverdon', 'Neuchatel'])
        self.CSR_box.place(x=self.posx_1stcol + 300, y=self.posx_1strow + 30)

        self.subscrip_year_lab = Label(self, text=set_language(lang)[26])
        self.subscrip_year_lab.place(x=self.posx_1stcol, y=self.posx_1strow + 60)
        self.subscrip_year = Spinbox(self, from_=1970, to=datetime.now().year)
        self.subscrip_year.place(x=self.posx_1stcol, y=self.posx_1strow + 90)

        self.social_assist_label = Label(self, text=set_language(lang)[27])
        self.social_assist_label.place(x=self.posx_1stcol + 300, y=self.posx_1strow + 60)
        self.social_assist = Entry(self)
        self.social_assist.place(x=self.posx_1stcol + 300, y=self.posx_1strow + 90)

        self.it_benefits_label = Label(self, text=set_language(lang)[28])
        self.it_benefits_label.place(x=self.posx_1stcol, y=self.posx_1strow + 120)
        self.it_benefits = ttk.Combobox(self, values=set_language(lang)[23:25])
        self.it_benefits.place(x=self.posx_1stcol, y=self.posx_1strow + 140)

    def get_all_entries(self):
        return np.array([self.social_benefits.get(), self.CSR_box.get(), self.subscrip_year.get(),
                         self.social_assist.get(), self.it_benefits.get()])


class PersonalDataWindow(Window):
    def __init__(self, parent, w_number):
        super().__init__(parent, w_number)

        self.lastName_lab = Label(self, text=set_language(lang)[9])
        self.lastName_lab.place(x=self.posx_1stcol, y=self.posx_1strow)
        self.firstName_lab = Label(self, text=set_language(lang)[10])
        self.firstName_lab.place(x=self.posx_1stcol + 300, y=self.posx_1strow)
        self.street_lab = Label(self, text=set_language(lang)[11])
        self.street_lab.place(x=self.posx_1stcol, y=self.posx_1strow + 60)
        self.town_lab = Label(self, text=set_language(lang)[12])
        self.town_lab.place(x=self.posx_1stcol + 300, y=self.posx_1strow + 60)
        self.phone_lab = Label(self, text=set_language(lang)[13])
        self.phone_lab.place(x=self.posx_1stcol, y=self.posx_1strow + 120)
        self.mail_lab = Label(self, text=set_language(lang)[14])
        self.mail_lab.place(x=self.posx_1stcol + 300, y=self.posx_1strow + 120)

        self.lastName = Entry(self)
        self.lastName.place(x=self.posx_1stcol, y=self.posx_1strow + 30)
        self.firstName = Entry(self)
        self.firstName.place(x=self.posx_1stcol + 300, y=self.posx_1strow + 30)
        self.street = Entry(self)
        self.street.place(x=self.posx_1stcol, y=self.posx_1strow + 90)
        self.town = Entry(self)
        self.town.place(x=self.posx_1stcol + 300, y=self.posx_1strow + 90)
        self.phone = Entry(self)
        self.phone.place(x=self.posx_1stcol, y=self.posx_1strow + 150)
        self.mail = Entry(self)
        self.mail.place(x=self.posx_1stcol + 300, y=self.posx_1strow + 150)

    def get_all_entries(self):
        return np.array([self.lastName.get(), self.firstName.get(), self.street.get(),
                         self.town.get(), self.phone.get(), self.mail.get()])


class WelcomeWindow(Window):
    def __init__(self, parent, w_number):
        super().__init__(parent, w_number)
        self.welcome_label = Label(self, text='Welcome !', font=300)
        self.welcome_label.place(x=self.posx_1stcol, y=100)

        self.language_box = ttk.Combobox(self, values=['Francais', 'English', 'Espagnol', 'Italiano', 'Româna'])
        self.language_box.place(x=self.posx_1stcol, y=50)

    def get_all_entries(self):
        return np.array([self.language_box.get()])

