import pandas as pd

if __name__ == '__main__':
    # csv_languages
    ##nb de champs à remplir pr chg langues : 59

    fr = ['Nom',
          'Prénom', 'Rue + nr', 'Tél', 'NPA + Ville', 'Email', 'Situation familiale', 'Marié(e)', 'Divorcé(e)',
          'Célibataire', 'Séparé(e)', ' Veuf(ve)',
          'Prestations sociales', 'Oui', 'Non', 'CSR de',
          'Année d’inscription', 'Assistant(e) social(e)',
          'Prestations en informatique (cours, ateliers, etc.)', 'Oui'  'Non',
          'N°de PC', 'TAG', 'N°d’écran', 'S/N écran',
          'UTILISATEURS PRINCIPAUX',
          'Adulte',
          'Enfants',
          'Famille',
          'NIVEAU INFORMATIQUE DES UTILISATEURS (1 seul choix)',
          'Aucune connaissance',
          'Débutant',
          'Autonome',
          'Avancé', 
          'USAGE DE L’ORDINATEUR',
          'Professionnel / Recherche d’emploi',
          'Formation / Scolarité',
          'Loisirs / Jeux',
          'Multimédia (photos, vidéos)',
          'Personnel',
          'Familiale',
          'Communication (MSN, Skype, etc.)',
          'Réseaux sociaux',
          'Administratif (courriers, compta, etc.)',
          'Recherche logement',
          'CONNEXION INTERNET', 'Non',
          'Oui – Fournisseur',
          'SOUHAITS / BESOINS EN PRESTATIONS INFORMATIQUES',
          'PC d’occasion de 2ème main',
          'Installation à domicile'
          'Ordinateur portable',
          'Assistance utilisateur',
          'Assistance technique',
          'Conseils',
          'Atelier d’introduction à l’informatique',
          'Autres',
          'GESTION DES PROBLEMES INFORMATIQUES (1 seul choix)',
          'Seul',
          'Avec un ami / connaissance',
          'Caritas Informatique',
          'DATE']

    en = ['Last Name', 'First Name', 'Street + Num', 'Tel',
          'Postal + City', 'Email',
          'Family Situation:',
          'Married', 'Divorced', 'Single', 'Separate', 'Widow',
          'Social Security Benefits (Caritas culture care, course etc.)',
          'Yes', 'No',
          'CSR of',
          'Year of Registration',
          'Social Assistance',
          'IT services(courses, workshops, etc):',
          'Yes', 'No',
          'PC Num', 'TAG', 'Screen Num', 'Screen S / N:',
          'MAIN USERS OF THE PC',
          'Adult',
          'Kids',
          'Family',
          'COMPUTER USER LEVEL (Choose only 1)',
          'No Knowledge',
          'Beginner', 'Autonomous',
          'Advanced',
          'COMPUTER USE',
          'Professional / Job Search',
          'Training / Education',
          'Hobbies / Games',
          'Multimedia(photos, videos)',
          'Personal', 'Family',
          'Communication(MSN, Skype, etc.)',
          'Social Networks',
          'Administrative(Mail, Accounting, etc,)',
          'Accommodation Search',
          'INTERNET CONNECTION',
          'No',
          'Yes – Vendor:',
          'WISHES / NEEDS IN BENEFITS IT',
          '2nd Hand Used PC',
          'Home Installation',
          'Laptop',
          'User Support',
          'Technical Assistance',
          'Tips',
          'Introductory Computer Workshop',
          'Other', 'PROBLEM MANAGEMENT IT (Choose only 1)',
          'Alone',
          'With a friend / Acquaintance',
          'Caritas IT',
          'Private Breakdown Service',
          'DATE'
          ]

    summary = pd.DataFrame(columns=[str(n) for n in list(range(0, 59, 1))], index=['fr', 'en'])
    summary['fr'] = fr
    summary['en'] = en

    summary.to_csv('csv_langues.csv')