#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 20:56:58 2019

@author: mh70
"""

import random

def rnd_person_pair(pair=True, sex="M", guarantor=False):

    m_krestni_lst = ['Jakub', 'Jan', 'Adam', 'Tomáš', 'Matyáš', 'Filip', 'Matěj', 'Ondřej', 'David', 'Vojtěch', 'Lukáš', 'Daniel', 'Dominik', 'Martin', 'Petr', 'Šimon', 'Štěpán', 'Jiří', 'Marek', 'Michal', 'Kryštof', 'Václav', 'Antonín', 'Josef', 'Patrik', 'Samuel', 'Tobiáš', 'František', 'Tadeáš', 'Mikuláš', 'Pavel', 'Sebastian', 'Jonáš', 'Oliver', 'Vít', 'Michael', 'Jáchym', 'Jaroslav', 'Viktor', 'Miroslav', 'Karel', 'Alex', 'Matouš', 'Nikolas', 'Kristián', 'Jindřich', 'Denis', 'Eliáš', 'Tobias', 'Sebastián', 'Maxmilián', 'Milan', 'Vilém', 'Max', 'Teodor', 'Zdeněk', 'Eduard', 'Erik', 'Ladislav', 'Maxim', 'Vítek', 'Albert', 'Alexandr', 'Aleš', 'Damián', 'Nicolas', 'Vincent', 'Stanislav', 'Vladimír', 'Hynek', 'Adrian', 'Hugo', 'Oskar']
    z_krestni_lst = ['Eliška', 'Tereza', 'Anna', 'Adéla', 'Natálie', 'Ema', 'Sofie', 'Karolína', 'Viktorie', 'Nela', 'Kristýna', 'Veronika', 'Barbora', 'Lucie', 'Laura', 'Kateřina', 'Klára', 'Julie', 'Aneta', 'Marie', 'Amálie', 'Anežka', 'Nikola', 'Emma', 'Nikol', 'Sára', 'Michaela', 'Markéta', 'Ella', 'Magdaléna', 'Elena', 'Vanesa', 'Linda', 'Alžběta', 'Adriana', 'Jana', 'Hana', 'Elen', 'Štěpánka', 'Denisa', 'Nina', 'Eva', 'Valerie', 'Sabina', 'Liliana', 'Andrea', 'Monika', 'Dominika', 'Simona', 'Agáta', 'Stella', 'Beáta', 'Mia', 'Terezie', 'Ester', 'Johana', 'Klaudie', 'Nezjištěno', 'Magdalena', 'Daniela', 'Izabela', 'Stela', 'Leontýna', 'Lenka', 'Šárka', 'Vendula', 'Nella', 'Valentýna', 'Josefína', 'Alice', 'Petra', 'Justýna', 'Mariana', 'Antonie', 'Alena', 'Bára', 'Vanessa', 'Helena']
    mz_prijmeni_lst = [('Dobrovolný', 'Dobrovolná'), ('Černohorský', 'Černohorská'), ('Bělohlávek', 'Bělohlávková'), ('Přichystal', 'Přichystalová'), ('Laštovička', 'Laštovičková'), ('Martinovský', 'Martinovská'), ('Přecechtěl', 'Přecechtělová'), ('Červenokostelecký', 'Červenokostelecká'), ('Straširybka', 'Straširybková'), ('Skočdopole', 'Skočdopolová'), ('Kratochvíl', 'Kratochvílová'), ('Drahokoupil', 'Drahokoupilová'), ('Lev', 'Lvová'), ('Kůň', 'Koňová'), ('Dvůr', 'Dvorová'), ('Krtek', 'Krtková'), ('Šebek', 'Šebková'), ('Hrdobec', 'Hrdobcová'), ('Hrbec', 'Hrbcová'), ('Klek', 'Kleková'), ('Janů', 'Janů'), ('Chmel', 'Chmelová'), ('Zavřel', 'Zavřelová'), ('Havel', 'Havlová'), ('Ševec', 'Ševcová'), ('Švec', 'Švecová'), ('Nagy', 'Nagyová'), ('Nový', 'Nová'), ('Cajthaml', 'Cajthamlová'), ('Páleník', 'Páleníková'), ('Švanda', 'Švandová'), ('Spurný', 'Spurná'), ('Tancoš', 'Tancošová'), ('Koláček', 'Koláčková'), ('Schneider', 'Schneidrová'), ('Šefl', 'Šeflová'), ('Bříza', 'Břízová'), ('Půlpán', 'Půlpánová'), ('Štancl', 'Štanclová'), ('Borkovec', 'Borkovcová'), ('Matušek', 'Matušková'), ('Szotkowski', 'Szotkowská'), ('Dostálek', 'Dostálková'), ('Smolík', 'Smolíková'), ('Štrunc', 'Štruncová'), ('Brunclík', 'Brunclíková'), ('Lhotský', 'Lhotská'), ('Vyhlídal', 'Vyhlídalová'), ('Kamenský', 'Kamenská'), ('Onderka', 'Onderková'), ('Tauchman', 'Tauchmanová'), ('Michalčík', 'Michalčíková'), ('Tuček', 'Tučková'), ('Kavka', 'Kavková'), ('Kysilka', 'Kysilková'), ('Veselský', 'Veselská'), ('Alexa', 'Alexová'), ('Stoklásek', 'Stoklásková'), ('Vránek', 'Vránková'), ('Ficek', 'Ficková'), ('Pazourek', 'Pazourková'), ('Šembera', 'Šemberová'), ('Korecký', 'Korecká'), ('Ondráček', 'Ondráčková'), ('Szabo', 'Szabová'), ('Honzík', 'Honzíková'), ('Nedoma', 'Nedomová'), ('Vokáč', 'Vokáčová'), ('Holík', 'Holíková'), ('Makovec', 'Makovcová'), ('Zvoníček', 'Zvoníčková'), ('Kramerius', 'Krameriová')]
    
    m_gr_krestni_lst = ["Randall", "Rufus", "Romeo", 'Richard', 'Robin', 'Radek', 'Roman', 'Radim', 'Robert', 'Gabriel', 'Rostislav', 'Rudolf', 'Radovan', 'Rafael', 'René', "Gerhard"]
    z_gr_krestni_lst = ['Gertruda', 'Rozálie', 'Gabriela', 'Rozárie', 'Rebeka', 'Rozárka', 'Renata', 'Růžena', 'Romana', 'Gita', 'Rosalie', 'Ráchel', 'Radka', 'Gréta']
    mz_gr_prijmeni_lst = [('Růžička', 'Růžičková'), ('Richter', 'Richterová'), ('Gregor', 'Gregorová'), ('Ryšavý', 'Ryšavá'), ('Rozsypal', 'Rozsypalová'), ('Roubal', 'Roubalová'), ('Rambousek', 'Rambousková'), ('Gruber', 'Grubrová'), ('Richtr', 'Richtrová'), ('Gottwald', 'Gottwaldová'), ('Grundza', 'Grundzová'), ('Grygar', 'Grygarová'), ('Gajdošík', 'Gajdošíková'), ('Gebauer', 'Gebaurová'), ('Ryšánek', 'Ryšánková'), ('Grulich', 'Grulichová'), ('Rychlý', 'Rychlá'), ('Roubíček', 'Roubíčková'), ('Rousek', 'Rousková'), ('Rozehnal', 'Rozehnalová'), ('Rychlík', 'Rychlíková'), ('Rejman', 'Rejmanová'), ('Grossmann', 'Grossmannová'), ('Raszka', 'Raszková'), ('Reichl', 'Reichlová'), ('Gašpar', 'Gašparová'), ('Glaser', 'Glasrová'), ('Rotter', 'Rotterová'), ('Roučka', 'Roučková'), ('Rejzek', 'Rejzeková'), ('Roháček', 'Roháčková'), ('Rychtařík', 'Rychtaříková')]
    
    
    titles_before = [
            'Bc.',
            'BcA.',
            'Ing.',
            'Ing. arch.',
            'MUDr.',
            'MDDr.',
            'MVDr.',
            'MgA.',
            'Mgr.',
            'JUDr.',
            'RNDr.',
            'PharmDr.',
            'ThDr.',
            "",
                 ]
    titles_after = [
            "PhD",
            'PhDr.',
            "CSc",
            "DrSc",
            "MBA",
            "",            
            ]


    sex = sex.lower()
    if sex in ["m", "male"]:
        sex = "male"
    elif sex in ["f", "female", "z"]:
        sex = "female"
    
    if guarantor:
        m_krestni = random.choice(m_gr_krestni_lst)
        z_krestni = random.choice(z_gr_krestni_lst)
        m_prijmeni, z_prijmeni = random.choice(mz_gr_prijmeni_lst)
    else:
        m_krestni = random.choice(m_krestni_lst)
        z_krestni = random.choice(z_krestni_lst)
        m_prijmeni, z_prijmeni = random.choice(mz_prijmeni_lst)
    
    def norm(txt):
        # ToDo
        return(txt)
    
    def make_email(krestni, prijmeni):
        suffixes = ["seznam.cz", "google.com", "firma.provider.cz"]
        nk = norm(krestni)
        np = norm(prijmeni)
        suff = random.choice(suffixes)
        return f"{nk}.{np}@{suff}"
        
    
    #m_email = make_email(m_krestni, m_prijmeni)
    
    if pair:
        person_pair = {
                "male":{
                "TitleBefore": random.choice(titles_before),
                "Name": m_krestni,
                "Surname": m_prijmeni,
                "TitleAfter": random.choice(titles_after),
                "Email": make_email(m_krestni, m_prijmeni),
                },
                "female":{
                "TitleBefore": random.choice(titles_before),
                "Name": z_krestni,
                "Surname": z_prijmeni,
                "TitleAfter": random.choice(titles_after),
                "Email": make_email(z_krestni, z_prijmeni),
                        
                        }
                }
        return person_pair
    
    elif sex == "male":
        person = {
            "TitleBefore": random.choice(titles_before),
            "Name": m_krestni,
            "Surname": m_prijmeni,
            "TitleAfter": random.choice(titles_after),
            "Email": make_email(m_krestni, m_prijmeni),
            }
        
        return person
        
    elif sex ==  "female":
        person = {
        "TitleBefore": random.choice(titles_before),
        "Name": z_krestni,
        "Surname": z_prijmeni,
        "TitleAfter": random.choice(titles_after),
        "Email": make_email(z_krestni, z_prijmeni),
        }
        return person

#rnd_person_pair(pair=True, sex="M", guarantor="False")    