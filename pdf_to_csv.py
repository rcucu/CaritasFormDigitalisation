from pathlib import Path
import pdfplumber as ppb
import pandas as pd
import numpy as np
from re import findall

if __name__ == "__main__":

    form_directory = Path(r'C:\Users\rcucu\Documents\Bénévolat\Caritas\pdf_form_benef')
    form_en = form_directory / 'v_en.pdf'  # 136 champs
    form_tu = form_directory / 'v_turc.pdf'  # 138
    form_it = form_directory / 'v_it.pdf'  # 152
    form_fr = form_directory / 'v_fr.pdf'  # 135
    form_es = form_directory / 'v_es.pdf'  # 137
    form_uk = form_directory / 'v_uk.pdf'  # 150
    form_fa = form_directory / 'v_farsi.pdf'  # 131
    form_de = form_directory / 'v_de.pdf'  # 139

    all_forms = [(form_en, 'en'), (form_tu, 'Tü'), (form_it, 'it'), (form_fr, 'fr'),
                 (form_es, 'es'), (form_uk, 'Ук'), (form_fa, 'fa'), (form_de, 'de')]

    for form, name in all_forms:
        with ppb.open(form) as pdf:
            for page in pdf.pages:
                page.extract_text()
                # print(page.extract_text())

            content = pdf.pages[0]
            whole_str = content.extract_text()
            test = content.extract_words()
            table = whole_str.split('\r')
            tab_lines = []

            for line in table:
                # tab_lines += line.split('\n')
                # print(line.split('\n'))
                # new_tab = tab_lines[0].split(':')
                for field in line.split('\n'):
                    for i in field.split(':'):#TODO: chg for farsi
                        for j in i.split('. '):
                            if (' ……' not in j) and ('......' not in j) and ('……………………………………………………………' not in j) and ('………………TA…G' not in j): #for form_it: ' ........' not in
                                j = j.replace('\uf06f', ',')
                                for t in j.split(','):
                                    tab_lines.append(t.strip())

            print(len(tab_lines))

            tab_lines = np.array(tab_lines)
            names_col = [str(i) for i in range(0, len(tab_lines))]
            df = pd.DataFrame(tab_lines[:, None].T, columns=names_col)
            df = df.dropna(axis='columns')
            # print(df.to_string())
            output_csv = 'output_' + name + '.csv'
            df.to_csv(form_directory / output_csv, index=False)

            print(f'length: {df.size}')
            csv = pd.read_csv(form_directory / output_csv, na_values=" NaN")
            modif_csv = csv.dropna(axis='columns')
            names_col2 = [str(i) for i in range(0, modif_csv.size)]
            modif_csv.to_csv(form_directory / output_csv, index=False, header=names_col2)
            csv = pd.read_csv(form_directory / output_csv)
            print(csv.to_string())