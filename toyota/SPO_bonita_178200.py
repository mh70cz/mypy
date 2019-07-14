"""
@author: mh70 , Created on Tue Jun 25 13:26:32 2019 

Životní a existenční minimum
https://www.mpsv.cz/cs/11852
Životní minimum je minimální společensky uznaná hranice peněžních příjmů k zajištění výživy a ostatních základních osobních potřeb.
Životní minimum ani existenční minimum nezahrnují nezbytné náklady na bydlení.
Výše částek normativních nákladů na bydlení
https://portal.mpsv.cz/soc/ssp/obcane/prisp_na_bydleni

"""
sam_dospela_osoba = 3410
prvni_dospela_osoba = 3140
dalsi_dospela_osoba = 2830
dite_do_6_let = 1740
dite_7az15_let = 2140
dite_16az26_let = 2450
koef_zm = 1.5 # koeficient zivotniho minima

naklady_bydleni = 15288 # 3 najem

pocet_osob_v_domacnosti = 3    # <HouseholdNumberPersons>3</HouseholdNumberPersons>
pocet_deti_do_6_let = 0        # <NumberDependentPersons>0</NumberDependentPersons>
pocet_deti_7az15_let = 1       # <NumberDependentPersons1>0</NumberDependentPersons1>
pocet_deti_16az26_let = 0      # <NumberDependentPersons2>0</NumberDependentPersons2>

pocet_dospelych_osob = (pocet_osob_v_domacnosti -  pocet_deti_do_6_let - 
                        pocet_deti_7az15_let  - pocet_deti_16az26_let)
pocet_dalsich_dospelych_osob = (
        pocet_dospelych_osob - 1 if pocet_dospelych_osob > 1 else 0)
if pocet_osob_v_domacnosti == 1:
    zivotni_minimum = sam_dospela_osoba * koef_zm
else:        
    zivotni_minimum = ( prvni_dospela_osoba + 
                        pocet_dalsich_dospelych_osob * dalsi_dospela_osoba +
                        pocet_deti_do_6_let * dite_do_6_let +
                        pocet_deti_7az15_let * dite_7az15_let +
                        pocet_deti_16az26_let * dite_16az26_let) * koef_zm

splatky = 5716           # <TotalInstalmentVAT>

splatky_stavajici_zadatel = 9500 # <Liabilities>9500</Liabilities>
splatky_stavajici_NRKI = 9561
splatky_stavajci = max(splatky_stavajici_zadatel, splatky_stavajici_NRKI)

cisty_mesicni_prijem = 26014     # Applicant <AverageMIAT>
cisty_mesicni_prijem_man = 15440 # coApplicant <AverageMIAT>

prijmy = cisty_mesicni_prijem + cisty_mesicni_prijem_man

naklady = zivotni_minimum + naklady_bydleni + splatky_stavajci
disponibilni_prijem = prijmy - naklady - splatky


print(f"Zivotni minimum:      {zivotni_minimum}")
print(f"Prijmy:               {prijmy}")
print(f"Naklady:              {naklady}")
print(f"Disponibilni prijem:  {disponibilni_prijem}")





