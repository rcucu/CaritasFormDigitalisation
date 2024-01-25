from pathlib import Path
from os import listdir, walk, path
import pandas as pd
from matplotlib import pyplot as plt

if __name__ == '__main__':

    data_dir = Path(r'C:\Users\rcucu\Documents\Bénévolat\Caritas\benef_data')
    csv_all_beneficiaries = pd.DataFrame(columns=[str(i) for i in range(0, 56)])

    for root, dirs, files in walk(data_dir):
        for file in files:
            if file.endswith('.csv'):
                print(file)
                path_file = path.join(root, file)
                benef_csv = pd.read_csv(path_file, index_col=0)
                #print(benef_csv.to_string())
                csv_all_beneficiaries = pd.concat([csv_all_beneficiaries, benef_csv], axis=0, ignore_index=True)

    print(csv_all_beneficiaries.to_string())

    plt.figure()
    csv_all_beneficiaries['8'].plot.pie(figsize=(6, 6))
    plt.show()


