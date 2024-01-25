from tkinter import Label
from signature.standard import SignatureWindow


class BeneficiarySignature(SignatureWindow):
    def __init__(self, parent, w_number):
        super().__init__(parent, w_number)
        # TODO: rajouter box précisant si ordi fix ou portable

        self.label = Label(self, text=self.get_text_label('95'), font=("bold", 15), bg='white')
        self.label.place(x=50, y=13)
        self.label2 = Label(self, text=self.get_text_label('74'), font=("bold", 13), bg='white')
        self.label2.place(x=50, y=63)
        self.label3 = Label(self, text=' '.join([self.get_text_label(str(s)) for s in list(range(75, 94, 2))]), font=("bold", 13), bg='white')
        self.label3.place(x=50, y=123)
        #self.label4 = Label(self, text=self.get_text_label('75'), font=("bold", 13), bg='white')
        #self.label4.place(x=50, y=233)  # TODO: ajouter une check boxe pour les conditions + msg d'erreur si pas fait
        self.label5 = Label(self, text=' '.join([self.get_text_label(str(s)) for s in list(range(98, 103, 2))]),
                                                font=("bold", 13), bg='white')
        self.label5.place(x=50, y=263)
        self.pack(side="top", fill="both", expand=True)
        self.configure()

    def save(self, filename='sig_beneficiary.jpg'):
        self.image.save(filename)

    def get_all_entries(self):
        pass
