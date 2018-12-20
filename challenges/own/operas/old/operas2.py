composers = {"beethoven":("Ludwig van Beethoven",
                          "17 December 1770", "26 March 1827"),
             "wagner":("Richard Wagner","22 May 1813","13 February 1883"),
             "verdi":("Giuseppe Verdi","9 October 1813","27 January 1901")
             }

wagner = [('The Fairies', '29 June 1888'),
 ('The Ban on Love', '29 March 1836'),
 ('Rienzi', '20 October 1842'),
 ('The Flying Dutchman', '2 January 1843'),
 ('Tannhäuser', '19 October 1845'),
 ('Lohengrin', '28 August 1850'),
 ('The Rhinegold', '22 September 1869'),
 ('The Valkyrie', '26 June 1870'),
 ('Siegfried', '16 August 1876'),
 ('Twilight of the Gods', '17 August 1876'),
 ('Tristan and Isolde', '10 June 1865'),
 ('The Master-Singers of Nuremberg', '21 June 1868'),
 ('Parsifal', '26 July 1882')]

beethoven = [("Fidelio", "20 November 1805")]

verdi = [('Oberto, conte di San Bonifacio', '17 November 1839'),
 ('Un giorno di regno, later Il finto Stanislao', '5 September 1840'),
 ('Nabucco', '9 March 1842'),
 ('I Lombardi alla prima crociata', '11 February 1843'),
 ('Ernani', '9 March 1844'),
 ('I due Foscari', '3 November 1844'),
 ("Giovanna d'Arco", '15 February 1845'),
 ('Alzira', '12 August 1845'),
 ('Attila', '17 March 1846'),
 ('Macbeth', '14 March 1847'),
 ('I masnadieri', '22 July 1847'),
 ('Jérusalem', '26 November 1847'),
 ('Il corsaro', '25 October 1848'),
 ('La battaglia di Legnano', '27 January 1849'),
 ('Luisa Miller', '8 December 1849'),
 ('Stiffelio', '16 November 1850'),
 ('Rigoletto', '11 March 1851'),
 ('Il trovatore', '19 January 1853'),
 ('La traviata', '6 March 1853'),
 ('Les vêpres siciliennes', '13 June 1855'),
 ('Giovanna de Guzman', '26 December 1855'),
 ('Le trouvère', '20 May 1856'),
 ('Simon Boccanegra', '12 March 1857'),
 ('Aroldo', '16 August 1857'),
 ('Un ballo in maschera', '17 February 1859'),
 ('La forza del destino', '10 November 1862'),
 ('Macbeth', '21 April 1865'),
 ('Don Carlos', '11 March 1867'),
 ('La forza del destino', '27 February 1869'),
 ('Aida', '24 December 1871'),
 ('Simon Boccanegra', '24 March 1881'),
 ('La force du destin', '14 March 1881'),
 ('Otello', '5 February 1887'),
 ('Falstaff', '9 February 1893')]

operas = []
operas.extend([("wagner", w[0], w[1]) for w in wagner])
operas.extend([("beethoven", w[0], w[1]) for w in beethoven])
operas.extend([("verdi", w[0], w[1]) for w in verdi])