import pandas as pd
from pathlib import Path


def get_shift_in_fields(lang):
    dict_lang = {'fr': 0,
                 "en": 1,
                 "es": 0,
                 "it": 1,
                 "de": 0,
                 "fa": 2,
                 "Ук": 1,
                 "Tü": 0,
                 '': 0}
    return dict_lang[lang]


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