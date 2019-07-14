"""
@author: mh70 , Created on Tue Jul  2 12:46:23 2019 
"""


#   VehicleStatus  [int]  0 Nové | 1 Ojeté  

#   SubjectType  1 SPO(FON) | 2 FOP | 3 PO
#   

#   Type of product  FO Operational leasing | FC Credit | FL Financial leasing
#   na SK zatim nebude OperL, nicmene pripravit vstup do budoucna

#   Foreigner - v CZK nesbirame pred vypoctem TMP2 / bude se na SK sbirat?

#    CalculationPrice aka VehiclePrice
#    Zdroj? jak s DPH? jak do budoucna s OperL?
Vehicle_Price_1 = 10000
Vehicle_Price_2 = 20000
Vehicle_Price_3 = 25000
Vehicle_Price_4 = 35000
Vehicle_Price_5 = 36000


#   AdvancedPaymentPercent
AdvPmtPct_1 = 25
AdvPmtPct_2 = 30
AdvPmtPct_3 = 35
AdvPmtPct_4 = 40
AdvPmtPct_5 = 50


subject_type = 1
vehicle_price = 23000
adv_pmt_pct = 26
vehicle_status = 0
varianta_tmp = "TMP2"


if subject_type == 1:       # SPO
    if vehicle_status == 0: #   nove vozidlo
        if ((adv_pmt_pct >= AdvPmtPct_1 and vehicle_price <= Vehicle_Price_2) or
            (adv_pmt_pct >= AdvPmtPct_4 and vehicle_price <= Vehicle_Price_5) or
            (adv_pmt_pct >= AdvPmtPct_5)):
            varianta_tmp = "TMP1"
            
    else:                   #   ojete
        if ((adv_pmt_pct >= AdvPmtPct_2 and vehicle_price <= Vehicle_Price_1) or
            (adv_pmt_pct >= AdvPmtPct_3 and vehicle_price <= Vehicle_Price_3) or
            (adv_pmt_pct >= AdvPmtPct_4)):
            varianta_tmp = "TMP1"

elif subject_type == 2:     # FOP
    if vehicle_status == 0: #   nove vozidlo
        if ((adv_pmt_pct >= AdvPmtPct_1 and vehicle_price <= Vehicle_Price_2) or
            (adv_pmt_pct >= AdvPmtPct_2 and vehicle_price <= Vehicle_Price_5) or
            (adv_pmt_pct >= AdvPmtPct_4)):
            varianta_tmp = "TMP1"           
    else:                   #   ojete
        if ((adv_pmt_pct >= AdvPmtPct_2 and vehicle_price <= Vehicle_Price_1) or
            (adv_pmt_pct >= AdvPmtPct_3 and vehicle_price <= Vehicle_Price_3) or
            (adv_pmt_pct >= AdvPmtPct_4)):
            varianta_tmp = "TMP1" 

else:                       # PO
    if vehicle_status == 0: #   nove vozidlo
        if ((adv_pmt_pct >= AdvPmtPct_1 and vehicle_price <= Vehicle_Price_2) or
            (adv_pmt_pct >= AdvPmtPct_2 and vehicle_price <= Vehicle_Price_5) or
            (adv_pmt_pct >= AdvPmtPct_4)):
            varianta_tmp = "TMP1"
    else:                   #   ojete
        if ((adv_pmt_pct >= AdvPmtPct_2 and vehicle_price <= Vehicle_Price_1) or
            (adv_pmt_pct >= AdvPmtPct_3 and vehicle_price <= Vehicle_Price_3) or
            (adv_pmt_pct >= AdvPmtPct_4)):
            varianta_tmp = "TMP1"

print(varianta_tmp)