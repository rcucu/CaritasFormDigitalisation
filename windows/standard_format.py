from datetime import datetime
from tkinter import Frame, Label, Entry, ttk, Spinbox
import numpy as np

# TODO: paragraphe parlant expliquant que par la signature, le bénéficiaire accepte
# que Caritas annonymise les données et les transmettent au canton


class Window(Frame):
    def __init__(self, parent, w_number):
        super().__init__(parent, bg='')
        self.parent = parent
        self.number = w_number
        self.posx_1stcol = 400
        self.posx_1strow = 200
        self.text_form = parent.form
        self.bgd_img_lab = Label(self, image=parent.img_bgd)
        self.bgd_img_lab['anchor'] = 'nw'
        self.bgd_img_lab.place(x=0, y=0, relwidth=1, relheight=1)
        self.bgd_img_lab.pack(side='top', fill='both', expand=True)

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

    def erase(self):
        print('bonjour jefface tout')
        self.pack_forget()
        self.destroy()

    def get_text_label(self, number):
        return self.text_form.get_field_text(number)


class FamilialSituationAgeWindow(Window):
    def __init__(self, parent, w_number):
        super().__init__(parent, w_number)
        self.familial_label = Label(self, text=self.get_text_label('12'))
        self.familial_label.place(x=self.posx_1stcol, y=self.posx_1strow)
        self.familial_box = ttk.Combobox(self, values=[self.get_text_label(str(i)) for i in range(13, 18)])
        self.familial_box.place(x=self.posx_1stcol, y=self.posx_1strow + 30)

        self.age_label = Label(self, text='Age')##TODO: get it from an array in diff. translations or add a col in csv
        self.age_label.place(x=self.posx_1stcol + 300, y=self.posx_1strow)
        self.age_box = Spinbox(self, from_=18, to=110)
        self.age_box.place(x=self.posx_1stcol + 300, y=self.posx_1strow + 30)

    def get_all_entries(self):
        return np.array([self.familial_box.get(), self.age_box.get()])


class BenefitsWindow(Window):
    def __init__(self, parent,  w_number):
        super().__init__(parent, w_number)
        self.social_benefits_label = Label(self, text=self.get_text_label('20'))
        self.social_benefits_label.place(x=self.posx_1stcol, y=self.posx_1strow)
        self.social_benefits = ttk.Combobox(self, values=[self.get_text_label(str(i)) for i in range(18, 20)])
        self.social_benefits.place(x=self.posx_1stcol, y=self.posx_1strow + 30)

        self.CSR_lab = Label(self, text=self.get_text_label('19')[-6:])
        self.CSR_lab.place(x=self.posx_1stcol + 300, y=self.posx_1strow)
        self.CSR_box = ttk.Combobox(self, values=['Vaud', 'Yverdon', 'Neuchatel'])
        self.CSR_box.place(x=self.posx_1stcol + 300, y=self.posx_1strow + 30)

        self.subscrip_year_lab = Label(self, text=self.get_text_label('21'))
        self.subscrip_year_lab.place(x=self.posx_1stcol, y=self.posx_1strow + 60)
        self.subscrip_year = Spinbox(self, from_=1970, to=datetime.now().year)
        self.subscrip_year.place(x=self.posx_1stcol, y=self.posx_1strow + 90)

        self.social_assist_label = Label(self, text='Nom Assitant(e)')##TODO: get it from an array in diff. translations or add a col in csv
        self.social_assist_label.place(x=self.posx_1stcol + 300, y=self.posx_1strow + 60)
        self.social_assist = Entry(self)
        self.social_assist.place(x=self.posx_1stcol + 300, y=self.posx_1strow + 90)

        self.it_benefits_label = Label(self, text=' '.join([self.get_text_label(str(i)) for i in range(22, 25, 1)]))
        self.it_benefits_label.place(x=self.posx_1stcol, y=self.posx_1strow + 120)
        self.it_benefits = ttk.Combobox(self, values=[self.get_text_label(str(i)) for i in range(25, 27)])
        self.it_benefits.place(x=self.posx_1stcol, y=self.posx_1strow + 140)

    def get_all_entries(self):
        return np.array([self.social_benefits.get(), self.CSR_box.get(), self.subscrip_year.get(),
                         self.social_assist.get(), self.it_benefits.get()])


class PersonalDataWindow(Window):
    def __init__(self, parent, w_number):
        super().__init__(parent,  w_number)

        self.lastName_lab = Label(self, text=self.get_text_label('6'))
        self.lastName_lab.place(x=self.posx_1stcol, y=self.posx_1strow)
        self.firstName_lab = Label(self, text=self.get_text_label('7'))
        self.firstName_lab.place(x=self.posx_1stcol + 300, y=self.posx_1strow)
        self.street_lab = Label(self, text=self.get_text_label('8'))
        self.street_lab.place(x=self.posx_1stcol, y=self.posx_1strow + 60)
        self.town_lab = Label(self, text=self.get_text_label('9'))
        self.town_lab.place(x=self.posx_1stcol + 300, y=self.posx_1strow + 60)
        self.phone_lab = Label(self, text=self.get_text_label('10'))
        self.phone_lab.place(x=self.posx_1stcol, y=self.posx_1strow + 120)
        self.mail_lab = Label(self, text=self.get_text_label('11'))
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
    def __init__(self, parent,  w_number):
        super().__init__(parent,   w_number)
        self.welcome_label = Label(self, text='Welcome !', font=300)
        self.welcome_label.place(x=self.posx_1stcol, y=100)

        self.language_box = ttk.Combobox(self, values=['Francais', 'English', 'Espanol', 'Italiano',
                                                       'Deutsch', 'Farsi', 'Українська', 'Türkçe'])
        self.language_box.place(x=self.posx_1stcol, y=50)

    def get_all_entries(self):
        return np.array([self.language_box.get()])

    def get_language_settings(self):
        return self.language_box.get()

