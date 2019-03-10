#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rnd_person_pair returns 
pseudo-random male-femail pair of the following:
name, surname, titles, email

rnd_person
pseudo-random male or female: 
name, surname, titles, email

if guarantor == True 
name and surname start with G  

if representive == True 
name and surname start with R  

if guarantor == True and representive == True
name starts with G and surname with R

"""

import random
import unicodedata


def rnd_person_pair(guarantor=False, representative=False):

    m_krestni, m_prijmeni, z_krestni, z_prijmeni = _rnd_names(guarantor, representative)

    person_pair = {
        "male": {
            "TitleBefore": _rnd_titles()[0],
            "Name": m_krestni,
            "Surname": m_prijmeni,
            "TitleAfter": _rnd_titles()[1],
            "Email": make_email(m_krestni, m_prijmeni),
        },
        "female": {
            "TitleBefore": _rnd_titles()[0],
            "Name": z_krestni,
            "Surname": z_prijmeni,
            "TitleAfter": _rnd_titles()[1],
            "Email": make_email(z_krestni, z_prijmeni),
        },
    }
    return person_pair


def rnd_person(gender="M", guarantor=False, representative=False):

    gender = gender.lower()
    if gender in ["m", "male"]:
        krestni, prijmeni, _, _ = _rnd_names(guarantor, representative)
    elif gender in ["f", "female", "z"]:
        _, _, krestni, prijmeni = _rnd_names(guarantor, representative)

    person = {
        "TitleBefore": _rnd_titles()[0],
        "Name": krestni,
        "Surname": prijmeni,
        "TitleAfter": _rnd_titles()[1],
        "Email": make_email(krestni, prijmeni),
    }

    return person


def make_email(krestni, prijmeni):
    suffixes = [
        "outlook.com",
        "posta.cz",
        "zoho.com",
        "protonmail.com",
        "yahoo.com",
        "firma.provider.cz",
    ]
    nk = _norm(krestni)
    np = _norm(prijmeni)
    suff = random.choice(suffixes)
    return f"{nk}.{np}@{suff}"


def _norm(txt):
    # ToDo
    txt = txt.lower().strip()
    txt = txt.replace("ß", "ss").replace("ł", "l")
    txt_norm = unicodedata.normalize("NFD", txt).encode("ascii", "ignore")
    txt_norm = txt_norm.decode("ascii")
    return txt_norm


def _rnd_names(guarantor, representative):
    m_krestni_lst = [
        "Jakub",
        "Jan",
        "Adam",
        "Tomáš",
        "Matyáš",
        "Filip",
        "Matěj",
        "Ondřej",
        "David",
        "Vojtěch",
        "Lukáš",
        "Daniel",
        "Dominik",
        "Martin",
        "Petr",
        "Šimon",
        "Štěpán",
        "Jiří",
        "Marek",
        "Michal",
        "Kryštof",
        "Václav",
        "Antonín",
        "Josef",
        "Patrik",
        "Samuel",
        "Tobiáš",
        "František",
        "Tadeáš",
        "Mikuláš",
        "Pavel",
        "Sebastian",
        "Jonáš",
        "Oliver",
        "Vít",
        "Michael",
        "Jáchym",
        "Jaroslav",
        "Viktor",
        "Miroslav",
        "Karel",
        "Alex",
        "Matouš",
        "Nikolas",
        "Kristián",
        "Jindřich",
        "Denis",
        "Eliáš",
        "Tobias",
        "Sebastián",
        "Maxmilián",
        "Milan",
        "Vilém",
        "Max",
        "Teodor",
        "Zdeněk",
        "Eduard",
        "Erik",
        "Ladislav",
        "Maxim",
        "Vítek",
        "Albert",
        "Alexandr",
        "Aleš",
        "Damián",
        "Nicolas",
        "Vincent",
        "Stanislav",
        "Vladimír",
        "Hynek",
        "Adrian",
        "Hugo",
        "Oskar",
    ]
    z_krestni_lst = [
        "Eliška",
        "Tereza",
        "Anna",
        "Adéla",
        "Natálie",
        "Ema",
        "Sofie",
        "Karolína",
        "Viktorie",
        "Nela",
        "Kristýna",
        "Veronika",
        "Barbora",
        "Lucie",
        "Laura",
        "Kateřina",
        "Klára",
        "Julie",
        "Aneta",
        "Marie",
        "Amálie",
        "Anežka",
        "Nikola",
        "Emma",
        "Nikol",
        "Sára",
        "Michaela",
        "Markéta",
        "Ella",
        "Magdaléna",
        "Elena",
        "Vanesa",
        "Linda",
        "Alžběta",
        "Adriana",
        "Jana",
        "Hana",
        "Elen",
        "Štěpánka",
        "Denisa",
        "Nina",
        "Eva",
        "Valerie",
        "Sabina",
        "Liliana",
        "Andrea",
        "Monika",
        "Dominika",
        "Simona",
        "Agáta",
        "Stella",
        "Beáta",
        "Mia",
        "Terezie",
        "Ester",
        "Johana",
        "Klaudie",
        "Magdalena",
        "Daniela",
        "Izabela",
        "Stela",
        "Leontýna",
        "Lenka",
        "Šárka",
        "Vendula",
        "Nella",
        "Valentýna",
        "Josefína",
        "Alice",
        "Petra",
        "Justýna",
        "Mariana",
        "Antonie",
        "Alena",
        "Bára",
        "Vanessa",
        "Helena",
    ]
    mz_prijmeni_lst = [
        ("Dobrovolný", "Dobrovolná"),
        ("Černohorský", "Černohorská"),
        ("Bělohlávek", "Bělohlávková"),
        ("Přichystal", "Přichystalová"),
        ("Laštovička", "Laštovičková"),
        ("Martinovský", "Martinovská"),
        ("Přecechtěl", "Přecechtělová"),
        ("Červenokostelecký", "Červenokostelecká"),
        ("Straširybka", "Straširybková"),
        ("Skočdopole", "Skočdopolová"),
        ("Kratochvíl", "Kratochvílová"),
        ("Drahokoupil", "Drahokoupilová"),
        ("Lev", "Lvová"),
        ("Kůň", "Koňová"),
        ("Dvůr", "Dvorová"),
        ("Krtek", "Krtková"),
        ("Šebek", "Šebková"),
        ("Hrdobec", "Hrdobcová"),
        ("Hrbec", "Hrbcová"),
        ("Klek", "Kleková"),
        ("Janů", "Janů"),
        ("Chmel", "Chmelová"),
        ("Zavřel", "Zavřelová"),
        ("Havel", "Havlová"),
        ("Ševec", "Ševcová"),
        ("Švec", "Švecová"),
        ("Nagy", "Nagyová"),
        ("Nový", "Nová"),
        ("Cajthaml", "Cajthamlová"),
        ("Páleník", "Páleníková"),
        ("Švanda", "Švandová"),
        ("Spurný", "Spurná"),
        ("Tancoš", "Tancošová"),
        ("Koláček", "Koláčková"),
        ("Schneider", "Schneidrová"),
        ("Šefl", "Šeflová"),
        ("Bříza", "Břízová"),
        ("Půlpán", "Půlpánová"),
        ("Štancl", "Štanclová"),
        ("Borkovec", "Borkovcová"),
        ("Matušek", "Matušková"),
        ("Szotkowski", "Szotkowská"),
        ("Dostálek", "Dostálková"),
        ("Smolík", "Smolíková"),
        ("Štrunc", "Štruncová"),
        ("Brunclík", "Brunclíková"),
        ("Lhotský", "Lhotská"),
        ("Vyhlídal", "Vyhlídalová"),
        ("Kamenský", "Kamenská"),
        ("Onderka", "Onderková"),
        ("Tauchman", "Tauchmanová"),
        ("Michalčík", "Michalčíková"),
        ("Tuček", "Tučková"),
        ("Kavka", "Kavková"),
        ("Kysilka", "Kysilková"),
        ("Veselský", "Veselská"),
        ("Alexa", "Alexová"),
        ("Stoklásek", "Stoklásková"),
        ("Vránek", "Vránková"),
        ("Ficek", "Ficková"),
        ("Pazourek", "Pazourková"),
        ("Šembera", "Šemberová"),
        ("Korecký", "Korecká"),
        ("Ondráček", "Ondráčková"),
        ("Szabo", "Szabová"),
        ("Honzík", "Honzíková"),
        ("Nedoma", "Nedomová"),
        ("Vokáč", "Vokáčová"),
        ("Holík", "Holíková"),
        ("Makovec", "Makovcová"),
        ("Zvoníček", "Zvoníčková"),
        ("Kramerius", "Krameriová"),
    ]

    m_g_krestni_lst = [
        "Gabriel",
        "Garcia",
        "Giacomo",
        "Giulio",
        "Gaspar",
        "Gerhard",
        "Gustav",
        "Gregor",
        "Gerald",
        "Geoffrey",
        "Günter",
        "Guido",
        "Gottlieb",
        "Gilbert",
        "Georg",
        "Gebbert",
        "Gilroy",
        "Gobán",
        "Gofraidh",
        "Gallagher",
    ]
    m_r_krestni_lst = [
        "Randall",
        "Rufus",
        "Romeo",
        "Richard",
        "Robin",
        "Radek",
        "Roman",
        "Radim",
        "Robert",
        "Rostislav",
        "Rudolf",
        "Radovan",
        "Rafael",
        "René",
        "Remigio",
        "Rochus",
        "Roger",
        "Roland",
        "Rolf",
        "Rüdiger",
        "Rupert",
        "Reinhold",
    ]

    z_g_krestni_lst = [
        "Gertruda",
        "Gaia",
        "Giulita",
        "Gustava",
        "Gilberta",
        "Graciana",
        "Galena",
        "Gabriela",
        "Gita",
        "Gréta",
        "Gretel",
        "Gretchen",
        "Gloria",
        "Gisela",
        "Gerlinde",
        "Georgina",
        "Gratia",
        "Guenievere",
        "Grania",
    ]
    z_r_krestni_lst = [
        "Rebeka",
        "Rozárka",
        "Renata",
        "Růžena",
        "Romana",
        "Rosalie",
        "Ráchel",
        "Radka",
        "Rihana",
        "Ruth",
        "Ruby",
        "Rufina",
        "Regina",
        "Rolanda",
        "Roxana",
        "Raisa",
        "Rosa",
        "Rita",
        "Roslyn",
        "Rapunzel",
        "Rosemary",
        "Rosemonde",
        "Rusalka",
        "Radana",
    ]

    mz_g_prijmeni_lst = [
        ("Gregor", "Gregorová"),
        ("Gruber", "Grubrová"),
        ("Gottwald", "Gottwaldová"),
        ("Grundza", "Grundzová"),
        ("Grygar", "Grygarová"),
        ("Gajdošík", "Gajdošíková"),
        ("Gebauer", "Gebaurová"),
        ("Grulich", "Grulichová"),
        ("Grossmann", "Grossmannová"),
        ("Gašpar", "Gašparová"),
        ("Glaser", "Glasrová"),
        ("Glisník", "Glisníková"),
    ]

    mz_r_prijmeni_lst = [
        ("Růžička", "Růžičková"),
        ("Richter", "Richterová"),
        ("Ryšavý", "Ryšavá"),
        ("Rozsypal", "Rozsypalová"),
        ("Roubal", "Roubalová"),
        ("Rambousek", "Rambousková"),
        ("Richtr", "Richtrová"),
        ("Ryšánek", "Ryšánková"),
        ("Rychlý", "Rychlá"),
        ("Roubíček", "Roubíčková"),
        ("Rousek", "Rousková"),
        ("Rozehnal", "Rozehnalová"),
        ("Rychlík", "Rychlíková"),
        ("Rejman", "Rejmanová"),
        ("Raszka", "Raszková"),
        ("Reichl", "Reichlová"),
        ("Rotter", "Rotterová"),
        ("Roučka", "Roučková"),
        ("Rejzek", "Rejzková"),
        ("Roháček", "Roháčková"),
        ("Rychtařík", "Rychtaříková"),
        ("Rubáš", "Rubášová"),
        ("Rumcajz", "Rumcajzová"),
        ("Robátko", "Robátková"),
        ("Rákosník", "Rákosníková"),
        ("Rádl", "Rádlová"),
        ("Ruml", "Rumlová"),
    ]

    if guarantor:
        m_krestni = random.choice(m_g_krestni_lst)
        z_krestni = random.choice(z_g_krestni_lst)
        if representative:
            m_prijmeni, z_prijmeni = random.choice(mz_r_prijmeni_lst)
        else:
            m_prijmeni, z_prijmeni = random.choice(mz_g_prijmeni_lst)
    elif representative:
        m_krestni = random.choice(m_r_krestni_lst)
        z_krestni = random.choice(z_r_krestni_lst)
        m_prijmeni, z_prijmeni = random.choice(mz_r_prijmeni_lst)
    else:
        m_krestni = random.choice(m_krestni_lst)
        z_krestni = random.choice(z_krestni_lst)
        m_prijmeni, z_prijmeni = random.choice(mz_prijmeni_lst)

    return (m_krestni, m_prijmeni, z_krestni, z_prijmeni)


def _rnd_titles():
    titles_before = [
        "Bc.",
        "BcA.",
        "Ing.",
        "Ing. arch.",
        "MUDr.",
        "MDDr.",
        "MVDr.",
        "MgA.",
        "Mgr.",
        "JUDr.",
        "RNDr.",
        "PharmDr.",
        "ThDr.",
        "",
    ]
    titles_after = ["PhD", "PhDr.", "CSc", "DrSc", "MBA", ""]
    return (random.choice(titles_before), random.choice(titles_after))


# rnd_person_pair( guarantor=False)
# rnd_person(gender="M", guarantor=False)

