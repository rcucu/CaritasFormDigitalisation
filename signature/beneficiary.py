from tkinter import Label
from signature.standard import SignatureWindow


class BeneficiarySignature(SignatureWindow):
    def __init__(self, parent, w_number):
        super().__init__(parent, w_number)

        self.label = Label(self, text=self.get_text_label('76'), font=("bold", 15), bg='white')
        self.label.place(x=50, y=13)
        self.label3 = Label(self, text=' '.join([self.get_text_label(str(s)) for s in list(range(77, 95, 1))]),
                            font=("bold", 13), bg='white', wraplength=self.width*3/4)
        self.label3.place(x=50, y=123)
        self.label5 = Label(self, text=' '.join([self.get_text_label(str(s)) for s in list(range(98, 106, 2))]),
                                                font=("bold", 13), bg='white', wraplength=self.width*3/4)
        self.label5.place(x=50, y=263)
        self.pack(side="top", fill="both", expand=True)
        self.configure()

    def save(self, filename='sig_beneficiary.jpg'):
        self.image.save(filename)

    def get_all_entries(self):
        pass

    def check_entry(self):
        pass
