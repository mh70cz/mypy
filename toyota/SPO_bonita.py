"""
@author: mh70 , Created on Tue Jun 25 13:26:32 2019 
"""
prvni_dospela_osoba = 3410
dalsi_dospela_osoba = 2830
dite_do_6_let = 1740
dite_7az15_let = 2140
dite_16az26_let = 2450
koef_zm = 1.5 # koeficient zivotniho minima

naklady_bydleni = 4670 # 1 osoby vlastni 

pocet_osob_v_domacnosti = 1    # <HouseholdNumberPersons>3</HouseholdNumberPersons>
pocet_deti_do_6_let = 0        # <NumberDependentPersons>0</NumberDependentPersons>
pocet_deti_7az15_let = 0       # <NumberDependentPersons1>0</NumberDependentPersons1>
pocet_deti_16az26_let = 0      # <NumberDependentPersons2>0</NumberDependentPersons2>

pocet_dospelych_osob = (pocet_osob_v_domacnosti -  pocet_deti_do_6_let - 
                        pocet_deti_7az15_let  - pocet_deti_16az26_let)
pocet_dalsich_dospelych_osob = (
        pocet_dospelych_osob - 1 if pocet_dospelych_osob > 1 else 0)

mesicni_splatky = 9691           #<TotalInstalmentVAT>9691</TotalInstalmentVAT>
cisty_mesicni_prijem = 25500     #<AverageMIAT>25500</AverageMIAT>

zivotni_minimum = ( prvni_dospela_osoba + 
                    pocet_dalsich_dospelych_osob * dalsi_dospela_osoba +
                    pocet_deti_do_6_let * dite_do_6_let +
                    pocet_deti_7az15_let * dite_7az15_let +
                    pocet_deti_16az26_let * dite_16az26_let) * koef_zm

naklady = zivotni_minimum + naklady_bydleni
disponibilni_prijem = cisty_mesicni_prijem - naklady - mesicni_splatky








