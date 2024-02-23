import pandas as pd
from pathlib import Path
from data_io.errors import NoLanguageError


def get_shift_in_fields(lang):
    dict_lang = {'Fr': 0,
                 "En": 1,
                 "Es": 0,
                 "It": 1,
                 "De": 0,
                 "Ук": 1,
                 "Tü": 0}#"Fa": 2,#TODO: pb avec eng, de, tu, uk

    if dict_lang.get(lang) is None:
        raise NoLanguageError

    return dict_lang.get(lang)


class Form:
    def __init__(self, language):
        self.filename = 'output_' + language[0:2] + '.csv'
        self.shift = get_shift_in_fields(language[0:2])
        self.path = Path(r'C:\Users\rcucu\Documents\Bénévolat\Caritas\BeneficiaryForm\BeneficiaryForm-v2_languages'
                         r'\data_io') / self.filename

    def get_field_text(self, number):
        nb_field = str(int(number)+self.shift)
        df = pd.read_csv(self.path, usecols=[nb_field], sep=',', index_col=False)
        return df[nb_field].values[0]
        ##TODO gérer les erreurs autour de sp