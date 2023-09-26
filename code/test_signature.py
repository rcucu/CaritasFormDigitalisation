from tkinter import Tk, Frame, Button, Label, Canvas, Entry, LabelFrame, ttk, Spinbox, PhotoImage
from PIL import Image, ImageDraw, ImageTk
from datetime import datetime
from pathlib import Path
import pandas as pd



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
          'transmis les informations sur les points (1) (2) de ce document.','Nom:', 'Prénom:' , 'Rue + nr:',
          'NPA + Ville:', 'n° Tél:', 'Email:', 'Situation familiale', 'Age', 'Marié(e)', 'Divorcé(e)',
          'Célibataire', 'Séparé(e)', ' Veuf(ve)', 'Prestations sociales', 'Oui', 'Non', 'CSR de:', 'Année d inscription', 'Assist. social:',
          'Avez-vous déjà suivi des prestations en informatique chez nous ou ailleurs (cours, ateliers, etc) ?', 'N° PC:', 'N° Ecran:',
          'Sauvegarder les données']
    eng = ['Personnal data', 'Done !', 'Clean']

    dict_lang = {'fr': fr, 'eng': eng}

    return dict_lang[lang]

#TODO: paragraphe parlant expliquant que par la signature, le bénéficiaire accepte
# que Caritas annonymise les données et les transmettent au canton


class Window(Frame):
    def __init__(self, w_number, *args, **kwargs):
        Frame.__init__(self, bg='', *args, **kwargs)
        self.number = w_number
        self.posx_1stcol = 400
        self.posx_1strow = 200

        #img1 = Image.open(r'C:\Users\rcucu\Documents\Bénévolat\Caritas\code\img_bkg.jpg').resize((w_screen, h_screen))
        #img2 = ImageTk.PhotoImage(img1)

        background_label = Label(self, image=img2)
        background_label['anchor'] = 'nw'
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.pack(side='top', fill='both', expand=True)

    def set_parent_current_page(self):
        Frame.current_page = self.number
        print(Frame.current_page)

    def save_data(self):
        Frame.save_data()

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
    def __init__(self, w_number=2, *args, **kwargs):
        self.number = w_number
        Window.__init__(self, self.number, *args, **kwargs)
        self.familial_label = Label(self, text=set_language(lang)[15])
        self.familial_label.place(x=self.posx_1stcol, y=self.posx_1strow)
        self.familial_box = ttk.Combobox(self, values=set_language(lang)[17:22])
        self.familial_box.place(x=self.posx_1stcol, y=self.posx_1strow+30)

        self.age_label = Label(self, text=set_language(lang)[16])
        self.age_label.place(x=self.posx_1stcol+300, y=self.posx_1strow)
        self.age_box = Spinbox(self, from_=18, to=110)
        self.age_box.place(x=self.posx_1stcol+300, y=self.posx_1strow+30)


class BenefitsWindow(Window):
    def __init__(self, w_number=3, *args, **kwargs):
        self.number = w_number
        Window.__init__(self, self.number, *args, **kwargs)
        self.social_benefits_label = Label(self, text=set_language(lang)[22])
        self.social_benefits_label.place(x=self.posx_1stcol, y=self.posx_1strow)
        self.social_benefits = ttk.Combobox(self, values=set_language(lang)[23:25])
        self.social_benefits.place(x=self.posx_1stcol, y=self.posx_1strow+30)

        self.CSR_lab = Label(self, text=set_language(lang)[25])
        self.CSR_lab.place(x=self.posx_1stcol+300, y=self.posx_1strow)
        self.CSR_box = ttk.Combobox(self, values=['Vaud', 'Yverdon', 'Neuchatel'])
        self.CSR_box.place(x=self.posx_1stcol+300, y=self.posx_1strow+30)

        self.subscrip_year_lab = Label(self, text=set_language(lang)[26])
        self.subscrip_year_lab.place(x=self.posx_1stcol, y=self.posx_1strow+60)
        self.subscrip_year = Spinbox(self, from_=1970, to=datetime.now().year)
        self.subscrip_year.place(x=self.posx_1stcol, y=self.posx_1strow+90)

        self.social_assist_label = Label(self, text=set_language(lang)[27])
        self.social_assist_label.place(x=self.posx_1stcol+300, y=self.posx_1strow+60)
        self.social_assist = Entry(self)
        self.social_assist.place(x=self.posx_1stcol+300, y=self.posx_1strow+90)

        self.it_benefits_label = Label(self, text=set_language(lang)[28])
        self.it_benefits_label.place(x=self.posx_1stcol, y=self.posx_1strow+120)
        self.it_benefits = ttk.Combobox(self, values=set_language(lang)[23:25])
        self.it_benefits.place(x=self.posx_1stcol,  y=self.posx_1strow+140)


class PersonalDataWindow(Window):
    def __init__(self, w_number=1, *args, **kwargs):
        self.number = w_number
        Window.__init__(self, self.number, *args, **kwargs)

        self.lastName_lab = Label(self, text=set_language(lang)[9])
        self.lastName_lab.place(x=self.posx_1stcol, y=self.posx_1strow)
        self.firstName_lab = Label(self, text=set_language(lang)[10])
        self.firstName_lab.place(x=self.posx_1stcol+300, y=self.posx_1strow)
        self.street_lab = Label(self, text=set_language(lang)[11])
        self.street_lab.place(x=self.posx_1stcol, y=self.posx_1strow+60)
        self.town_lab = Label(self, text=set_language(lang)[12])
        self.town_lab.place(x=self.posx_1stcol+300, y=self.posx_1strow+60)
        self.phone_lab = Label(self, text=set_language(lang)[13])
        self.phone_lab.place(x=self.posx_1stcol, y=self.posx_1strow+120)
        self.mail_lab = Label(self, text=set_language(lang)[14])
        self.mail_lab.place(x=self.posx_1stcol+300, y=self.posx_1strow+120)

        self.lastName = Entry(self)
        self.lastName.place(x=self.posx_1stcol, y=self.posx_1strow+30)
        self.firstName = Entry(self)
        self.firstName.place(x=self.posx_1stcol+300, y=self.posx_1strow+30)
        self.street = Entry(self)
        self.street.place(x=self.posx_1stcol, y=self.posx_1strow+90)
        self.town = Entry(self)
        self.town.place(x=self.posx_1stcol+300, y=self.posx_1strow+90)
        self.phone = Entry(self)
        self.phone.place(x=self.posx_1stcol, y=self.posx_1strow+150)
        self.mail = Entry(self)
        self.mail.place(x=self.posx_1stcol+300, y=self.posx_1strow+150)


class SignatureWindow(Window):

    def __init__(self, w_number, filename, *args, **kwargs):
        Window.__init__(self, w_number, *args, **kwargs)
        self.filename = filename
        self.posx, self.posy = 50, 300
        self.sizex, self.sizey = 600, 200
        self.xold, self.yold = None, None
        self.b1 = 'up'
        self.drawing_area = Canvas(self, width=self.sizex, height=self.sizey, bg='white', **kwargs)
        self.drawing_area.place(x=self.posx, y=self.posy)
        self.drawing_area.bind('<Motion>', self.motion)
        self.drawing_area.bind('<ButtonPress-1>', self.b1down)
        self.drawing_area.bind('<ButtonRelease-1>', self.b1up)
        self.butt_done = Button(self, text=set_language(lang)[6], width=10, command=self.save, bg='white')
        self.butt_done.place(x=(self.sizex / 6), y=2.5 * self.sizey + 20)
        self.butt_erase = Button(self, text=set_language(lang)[7], width=10, command=self.clear, bg='white')
        self.butt_erase.place(x=(self.sizex / 6) + 80, y=2.5 * self.sizey + 20)

        self.image = Image.new('RGB', (self.sizex, self.sizey), (255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)

    def b1down(self, event):
        self.b1 = 'down'

    def b1up(self, event):
        self.b1 = 'up'
        self.xold = None
        self.yold = None

    def save(self):
        print(self.b1)
        self.image.save(self.filename)

    def clear(self):
        print(f' clear: {self.b1}')
        self.drawing_area.delete('all')
        self.image = Image.new('RGB', (self.sizex, self.sizey), (255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)
        print('canvas erased')

    def motion(self, event):
        print(self.b1)
        # thickness = 4
        # x1, y1 = (event.x - thickness), (event.y - thickness)
        # x2, y2 = (event.x + thickness), (event.y + thickness)
        # event.widget.create_oval(x1, y1, x2, y2, fill='black')

        if self.b1 == 'down':
            if self.xold is not None and self.yold is not None:
                event.widget.create_line(self.xold, self.yold, event.x, event.y, smooth='true', width=3, fill='black')
                self.draw.line(((self.xold, self.yold), (event.x, event.y)), (0, 0, 0), width=3)

        self.xold = event.x
        self.yold = event.y

    def save_data(self):
        Window.save_data()


class BeneficiarySignature(SignatureWindow):
    def __init__(self, w_number=4, *args, **kwargs):
        self.number = w_number
        SignatureWindow.__init__(self, self.number, 'sig_bene.jpg', *args, **kwargs)
        self.label = Label(self, text=set_language(lang)[1], font=("bold", 15), bg='white')
        self.label.place(x=50, y=13)
        self.label2 = Label(self, text=set_language(lang)[2], font=("bold", 13), bg='white')
        self.label2.place(x=50, y=63)
        self.label3 = Label(self, text=set_language(lang)[3], font=("bold", 13), bg='white')
        self.label3.place(x=50, y=123)
        self.label4 = Label(self, text=set_language(lang)[4], font=("bold", 13), bg='white')
        self.label4.place(x=50, y=233) #TODO: ajouter une check boxe pour les conditions + msg d'erreur si pas fait
        self.label5 = Label(self, text=set_language(lang)[5], font=("bold", 13), bg='white')
        self.label5.place(x=50, y=263)
        self.pack(side="top", fill="both", expand=True)
        self.configure()


class TechnicianSignature(SignatureWindow):
    def __init__(self, w_number=5, *args, **kwargs):
        self.number = w_number
        SignatureWindow.__init__(self, self.number, 'sig_tech.jpg', *args, **kwargs)
        #TODO: rajouter box précisant si ordi fix ou portable

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

        button_save_data = Button(self, text=set_language(lang)[31], command=SignatureWindow.save_data, bg='#99EDC3')
        button_save_data.place(x=900, y=500)

        self.pack(side="top", fill="both", expand=True)
        self.configure()


class WelcomeWindow(Window):
    def __init__(self, w_number=0, *args, **kwargs):
        self.number = w_number

        Window.__init__(self, self.number, *args, **kwargs)
        self.welcome_label = Label(self, text='Welcome !', font=300)
        self.welcome_label.place(x=self.posx_1stcol, y=100)

        self.language_box = ttk.Combobox(self, values=['Francais', 'English', 'Espagnol', 'Italiano', 'Româna'])
        self.language_box.place(x=self.posx_1stcol, y=50)


class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, padx=1, pady=1, *args, **kwargs)
        self.current_page = 0
        self.language = 'Francais'

        self.w_welcome = WelcomeWindow(0)
        self.w1 = PersonalDataWindow(1)
        self.w2 = FamilialSituationAgeWindow(2)
        self.w3 = BenefitsWindow(3)

        self.w22 = BeneficiarySignature(4)
        self.w23 = TechnicianSignature(5)
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
        b02 = Button(buttonframe, text=set_language(lang)[22], command=self.w3.show, bg='#99EDC3')
        b1 = Button(buttonframe, text="Signature Bénéficiaire", command=self.w22.show, bg='#99EDC3')
        b2 = Button(buttonframe, text="Signature Technicien", command=self.w23.show, bg='#99EDC3')
        b3 = Button(bottombuttonframe, text="Suivant", bg='#3DED97', command=self.go_next_window)
        b4 = Button(bottombuttonframe, text="En arrière", bg='#3DED97', command=self.go_previous_window)

        background_label.pack(side='top', fill='both', expand=True)
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
            #name_window = "w" + str(self.current_page)
            current_window = [w for w in self.list_windows if w.number == self.current_page][0]
            print(current_window.number)
            current_window.show()

    def go_next_window(self):
        if self.current_page == 0:
            self.set_language(self.w_welcome.language_box.get())
            print(f'Language choosen: {self.language}')
            #TODO: top buttons should be inactive while being on w==0

        if self.current_page < len(self.list_windows)-1:
            self.current_page = self.current_page + 1
            current_window = [w for w in self.list_windows if w.number == self.current_page][0]
            current_window.show()


    def save_data(self):
        path_dir = Path(r'C:\Users\rcucu\Documents\Bénévolat\Caritas\code\data')
        data = pd.DataFrame(data=[self.w1.lastName.get(), self.w1.firstName.get(),
                                  self.w1.street.get(), self.w1.town.get(), self.w1.phone.get(), self.w1.mail.get()],
                            columns=list(range(0, 6)))
        print(data.to_string())

    def set_language(self, lang):
        self.language = lang


if __name__ == '__main__':

    path_dir = Path(r'C:\Users\rcucu\Documents\Bénévolat\Caritas\code')

    lang = 'fr'
    app = Tk()
    app.title('UserForm')
    app.wm_geometry('')
    #
    # app.attributes('-fullscreen', 1)  # make the root window fullscreen
    w_screen = app.winfo_screenwidth()
    h_screen = app.winfo_screenheight()

    img1 = Image.open(path_dir / 'img_bkg3.jpg').resize((w_screen, h_screen))
    img2 = ImageTk.PhotoImage(img1)

    background_label = Label(app, image=img2)
    background_label['anchor'] = 'nw'
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    main = MainView(background_label)

    main.pack(side="top", fill="both", expand=True)

    app.mainloop()

