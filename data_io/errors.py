from tkinter import messagebox


class UserInputError(Exception):
    """Base class for exceptions in this module."""
    def __init__(self, error_msg):
        messagebox.showinfo('UserError', error_msg)


class NoInputError(UserInputError):
    def __init__(self, str_input):
        super().__init__('Veuillez sélectionner ' + str_input)


class NoLanguageError(NoInputError):

    def __init__(self,):
        super().__init__('une langue !')


class NoBoxTickedError(NoInputError):
    def __init__(self):
        super().__init__('au moins un élèment qui vous concerne !')


class NoElementSelectedError(UserInputError):
    def __init__(self):
        super().__init__('Vous avez laissé un ou plusieurs champs vides !')


class InvalidCharError(UserInputError):
    def __init__(self):
        super().__init__('Attention, vous avez rentré des charactères spéciaux, veuillez changer')


class InvalidTelNumber(UserInputError):
    def __init__(self):
        super().__init__('Attention,le numéro de téléphone doit être composé de 13 chiffres, veuillez changer')

class InvalidMail(UserInputError):
    def __init__(self):
        super().__init__('Adresse mail invalide; veuillez vérifier une deuxième fois.')