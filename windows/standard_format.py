import re
from datetime import datetime
from tkinter import Frame, Label, Entry, ttk, Spinbox, IntVar
import numpy as np
from data_io.errors import InvalidCharError, InvalidTelNumber, NoElementSelectedError, NoBoxTickedError, InvalidMail


# TODO: paragraphe parlant expliquant que par la signature, le bénéficiaire accepte
# que Caritas annonymise les données et les transmettent au canton


class Window(Frame):
    def __init__(self, parent, w_number):
        super().__init__(parent, bg='')
        self.parent = parent
        self.number = w_number
        self.posx_1stcol = 400
        self.posx_1strow = 200
        self.bgd_img_lab = Label(self, image=parent.img_bgd)
        self.bgd_img_lab['anchor'] = 'nw'
        self.bgd_img_lab.place(x=0, y=0, relwidth=1, relheight=1)
        self.bgd_img_lab.pack(side='top', fill='both', expand=True)
        self.width = parent.winfo_screenwidth()
        self.height = parent.winfo_screenheight()

    def set_parent_current_page(self):
        self.parent.current_page = self.number
        print(self.parent.current_page)

    def get_data(self):
        self.parent.save_data()

    def show(self):
        self.set_parent_current_page()
        self.lift()

    def erase(self):
        print('bonjour jefface tout')
        self.pack_forget()
        self.destroy()

    def check_entry(self):
        pass


class FamilialSituationAgeWindow(Window):
    def __init__(self, parent, w_number):
        super().__init__(parent, w_number)
        self.text_form = parent.form

        self.familial_label = Label(self, text=self.get_text_label('12'))
        self.familial_label.place(x=self.posx_1stcol, y=self.posx_1strow)
        self.familial_box = ttk.Combobox(self, values=[self.get_text_label(str(i)) for i in range(13, 18)])
        self.familial_box.place(x=self.posx_1stcol, y=self.posx_1strow + 30)

        self.age_label = Label(self, text='Age')  ##TODO: get it from an array in diff. translations or add a col in csv
        self.age_label.place(x=self.posx_1stcol + 300, y=self.posx_1strow)
        self.age_box = Spinbox(self, from_=18, to=90)
        self.age_box.place(x=self.posx_1stcol + 300, y=self.posx_1strow + 30)

    def get_all_entries(self):
        return np.array([self.familial_box.get(), self.age_box.get()])

    def get_text_label(self, number):
        return self.text_form.get_field_text(number)

    def check_entry(self):
        if len(self.familial_box.get()) == 0:
            raise NoElementSelectedError


class BenefitsWindow(Window):
    def __init__(self, parent, w_number):
        super().__init__(parent, w_number)
        self.text_form = parent.form

        self.social_benefits_label = Label(self, text=self.get_text_label('18'))
        self.social_benefits_label.place(x=self.posx_1stcol, y=self.posx_1strow)
        self.social_benefits = ttk.Combobox(self, values=[self.get_text_label(str(i)) for i in range(19, 21)])
        self.social_benefits.place(x=self.posx_1stcol, y=self.posx_1strow + 30)

        self.CSR_lab = Label(self, text=self.get_text_label('20')[-6:])
        self.CSR_lab.place(x=self.posx_1stcol + 300, y=self.posx_1strow)
        self.CSR_box = ttk.Combobox(self, values=['Vaud', 'Yverdon', 'Neuchatel'])
        self.CSR_box.place(x=self.posx_1stcol + 300, y=self.posx_1strow + 30)

        self.subscrip_year_lab = Label(self, text=self.get_text_label('21'))
        self.subscrip_year_lab.place(x=self.posx_1stcol, y=self.posx_1strow + 60)
        self.subscrip_year = Spinbox(self, from_=1970, to=datetime.now().year)
        self.subscrip_year.place(x=self.posx_1stcol, y=self.posx_1strow + 90)

        self.social_assist_label = Label(self,
                                         text='Nom Assitant(e)')  ##TODO: get it from an array in diff. translations or add a col in csv
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

    def get_text_label(self, number):
        return self.text_form.get_field_text(number)

    def check_entry(self):
        if any(len(v) == 0 for v in [self.social_benefits.get(), self.CSR_box.get(), self.it_benefits.get()]):
            raise NoElementSelectedError
        elif len(self.social_assist.get()) != 0 and \
                set('[~!@#$%^&*()_+{}":;\'0123456789]+$').intersection(self.social_assist.get()):
            raise InvalidCharError


class PersonalDataWindow(Window):
    def __init__(self, parent, w_number):
        super().__init__(parent, w_number)
        self.text_form = parent.form

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

    def get_text_label(self, number):
        return self.text_form.get_field_text(number)

    def check_entry(self):
        if any(len(v) == 0 for v in [self.lastName.get(), self.firstName.get(), self.street.get(),
                                     self.town.get(), self.phone.get()]):
            raise NoElementSelectedError

        elif set('[~!@#$%^&*()_+{}":;\'0123456789]+$').intersection(self.lastName.get()) \
                or set('[~!@#$%^&*()_+{}":;\'0123456789]+$').intersection(self.firstName.get()):
            raise InvalidCharError

        #elif not re.match(r'[z0-9]+$', self.phone.get()):
            # TODO: be more precise/\(?([0-9]{6})\)?([ .-]?)([0-9]{3})\2([0-9]{4})/
            #raise InvalidTelNumber

        elif len(self.mail.get()) != 0 and not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
                                                        self.mail.get()):
            raise InvalidMail


class WelcomeWindow(Window):
    def __init__(self, parent, w_number):
        super().__init__(parent, w_number)
        self.welcome_label = Label(self, text='Bienvenue !', font=600)
        self.welcome_label.place(x=self.posx_1stcol, y=100)

        self.language_box = ttk.Combobox(self, values=['Francais', 'English', 'Espanol', 'Italiano',
                                                       'Deutsch', 'Українська', 'Türkçe'])  # 'Farsi'
        self.language_box.place(x=self.posx_1stcol, y=50)

    def get_all_entries(self):
        return np.array([self.language_box.get()])

    def get_language_settings(self):
        return self.language_box.get()

    def check_entry(self):
        pass


class UserWindow(Window):
    def __init__(self, parent, w_number):
        super().__init__(parent, w_number)
        self.text_form = parent.form
        self.user_label = Label(self, text=self.get_text_label('29'))
        self.user_label.place(x=self.posx_1stcol, y=self.posx_1strow)
        self.user_box = ttk.Combobox(self, values=[self.get_text_label(str(i)) for i in list([28, 30, 31])])
        self.user_box.place(x=self.posx_1stcol, y=self.posx_1strow + 30)

        self.level_it_label = Label(self, text=' '.join([self.get_text_label(str(i)) for i in list([32, 35])]))
        self.level_it_label.place(x=self.posx_1stcol + 300, y=self.posx_1strow)
        self.level_it_box = ttk.Combobox(self, values=[self.get_text_label(str(i)) for i in list([33, 34, 36, 37])])
        self.level_it_box.place(x=self.posx_1stcol + 300, y=self.posx_1strow + 30)

    def get_text_label(self, number):
        return self.text_form.get_field_text(str(number))

    def get_all_entries(self):
        return np.array([self.user_box.get(), self.level_it_box.get()])

    def check_entry(self):
        if any(len(v) == 0 for v in [self.user_box.get(), self.level_it_box.get()]):
            raise NoElementSelectedError


class UsageWindow(Window):
    def __init__(self, parent, w_number):
        super().__init__(parent, w_number)
        self.text_form = parent.form

        self.pc_usage_lab = Label(self, text=self.get_text_label('45'))
        self.pc_usage_lab.place(x=self.posx_1stcol, y=self.posx_1strow)

        self.var_checkbox, self.list_checkboxes = [], []
        j = 0
        for text in [self.get_text_label(str(i)) for i in list([39, 40, 41, 46, 47, 53, 54])]:
            self.var_checkbox.append(IntVar())
            self.list_checkboxes.append(ttk.Checkbutton(self, text=text, variable=self.var_checkbox[j]))
            self.list_checkboxes[j].place(x=self.posx_1stcol + 300, y=self.posx_1strow + j * 30)
            j += 1

        self.var_checkbox.append(IntVar())
        self.com_checkbox = ttk.Checkbutton(self, text=', '.join([self.get_text_label(str(i)) for i in range(42, 45)]),
                                            variable=self.var_checkbox[-1])
        self.list_checkboxes.append(self.com_checkbox)
        self.list_checkboxes[-1].place(x=self.posx_1stcol + 300,
                                       y=self.posx_1strow + (len(self.list_checkboxes) - 1) * 30)

        self.var_checkbox.append(IntVar())
        self.multimedia_checkbox = ttk.Checkbutton(self,
                                                   text=', '.join([self.get_text_label(str(i)) for i in range(48, 50)]),
                                                   variable=self.var_checkbox[-1])
        self.list_checkboxes.append(self.multimedia_checkbox)
        self.list_checkboxes[-1].place(x=self.posx_1stcol + 300,
                                       y=self.posx_1strow + (len(self.list_checkboxes) - 1) * 30)

        self.var_checkbox.append(IntVar())
        self.admin_checkbox = ttk.Checkbutton(self,
                                              text=', '.join([self.get_text_label(str(i)) for i in range(50, 53)]),
                                              variable=self.var_checkbox[-1])
        self.list_checkboxes.append(self.admin_checkbox)
        self.list_checkboxes[-1].place(x=self.posx_1stcol + 300,
                                       y=self.posx_1strow + (len(self.list_checkboxes) - 1) * 30)

        self.connexion_lab = Label(self, text=self.get_text_label('56'))
        self.connexion_lab.place(x=self.posx_1stcol + 300, y=self.posx_1strow + (len(self.list_checkboxes) * 1.5) * 30)
        self.connexion_box = ttk.Combobox(self, values=[self.get_text_label(str(i)) for i in list([55, 57])])
        self.connexion_box.place(x=self.posx_1stcol + 300, y=self.posx_1strow + (len(self.list_checkboxes) * 1.5) * 33)

    def get_text_label(self, number):
        return self.text_form.get_field_text(str(number))

    def get_all_entries(self):
        return np.append([[var.get() for var in self.var_checkbox]], [self.connexion_box.get()])

    def check_entry(self):
        if all(var.get() == 0 for var in self.var_checkbox):
            raise NoBoxTickedError
        elif len(self.connexion_box.get()) == 0:
            raise NoElementSelectedError


class NeedsWindow(Window):
    def __init__(self, parent, w_number):
        super().__init__(parent, w_number)
        self.text_form = parent.form

        self.it_needs_lab = Label(self, text=' '.join([self.get_text_label(str(i)) for i in list([60, 61, 64])]))
        self.it_needs_lab.place(x=self.posx_1stcol, y=self.posx_1strow)

        self.var_checkbox, self.list_checkboxes = [], []
        j = 0
        for text in [self.get_text_label(str(i)) for i in list([58, 59, 62, 63, 65, 67, 68])]:
            self.var_checkbox.append(IntVar())
            self.list_checkboxes.append(ttk.Checkbutton(self, text=text, variable=self.var_checkbox[j]))
            self.list_checkboxes[j].place(x=self.posx_1stcol + 300, y=self.posx_1strow + j * 30)
            j += 1

        self.var_checkbox.append(IntVar())
        self.com_checkbox = ttk.Checkbutton(self, text=', '.join([self.get_text_label(str(i)) for i in list([66])]),
                                            variable=self.var_checkbox[-1])
        self.list_checkboxes.append(self.com_checkbox)
        self.list_checkboxes[-1].place(x=self.posx_1stcol + 300,
                                       y=self.posx_1strow + (len(self.list_checkboxes) - 1) * 30)

        self.pb_IT_lab = Label(self, text=' '.join([self.get_text_label(str(i)) for i in list([71, 72])]))
        self.pb_IT_lab.place(x=self.posx_1stcol + 300, y=self.posx_1strow + (len(self.list_checkboxes) * 1.5) * 30)
        self.pb_IT_box = ttk.Combobox(self, values=[self.get_text_label(str(i)) for i in list([69, 70, 73, 75])])
        self.pb_IT_box.place(x=self.posx_1stcol + 300, y=self.posx_1strow + (len(self.list_checkboxes) * 1.5) * 33)

    def get_text_label(self, number):
        return self.text_form.get_field_text(str(number))

    def get_all_entries(self):
        return np.append([[var.get() for var in self.var_checkbox]], [self.pb_IT_box.get()])

    def check_entry(self):
        if all(var.get() == 0 for var in self.var_checkbox):
            raise NoBoxTickedError
        elif len(self.pb_IT_box.get()) == 0:
            raise NoElementSelectedError
