# -*- coding: utf-8 -*-
"""
VariantaTMP
"""

VariantaTMP = 1

AdvPmtPct_1 = 20
AdvPmtPct_2 = 25
AdvPmtPct_3 = 35

VehiclePrice_1 = 300000.0
VehiclePrice_2 = 600000.0
VehiclePrice_3 = 900000.0
VehiclePrice_4 = 1000000.0

SubjType = 2
VehiclePrice = 942000
AdvPmtPct = 34.9
VehicleStatus = 1 # 0 - nove , 1 - ojete

if SubjType == 1:
    VariantaTMP = 2
elif VehicleStatus == 0:
    if (
        ((VehiclePrice <= VehiclePrice_2) and (AdvPmtPct < AdvPmtPct_1))
        or (
            (VehiclePrice <= VehiclePrice_4)
            and (VehiclePrice > VehiclePrice_2)
            and (AdvPmtPct < AdvPmtPct_2)
        )
        or ((VehiclePrice > VehiclePrice_4) and (AdvPmtPct < AdvPmtPct_3))
    ):

        VariantaTMP = 2

else:
    if (
        ((VehiclePrice <= VehiclePrice_1) and (AdvPmtPct < AdvPmtPct_1))
        or (
            (VehiclePrice > VehiclePrice_1)
            and (VehiclePrice <= VehiclePrice_3)
            and (AdvPmtPct < AdvPmtPct_2)
        )
        or ((VehiclePrice > VehiclePrice_3) and (AdvPmtPct < AdvPmtPct_3))
    ):
        VariantaTMP = 2

print (f"VariantaTMP: TMP{VariantaTMP}")

"""
($VehiclePrice <= $VehiclePrice_2 & In.Contract.AdvancePaymentPercent < $AdvPmtPct_1) |
($VehiclePrice <= $VehiclePrice_4 & $VehiclePrice > $VehiclePrice_2 & In.Contract.AdvancePaymentPercent < $AdvPmtPct_2) |
($VehiclePrice > $VehiclePrice_4 & In.Contract.AdvancePaymentPercent < $AdvPmtPct_3)


($VehiclePrice <= $VehiclePrice_1 & In.Contract.AdvancePaymentPercent <$AdvPmtPct_1) |
($VehiclePrice > $VehiclePrice_1 & $VehiclePrice <= $VehiclePrice_3 & In.Contract.AdvancePaymentPercent <$AdvPmtPct_2) |
($VehiclePrice > $VehiclePrice_3 & In.Contract.AdvancePaymentPercent <$AdvPmtPct_3)


    if  ((VehiclePrice <= VehiclePrice_2) and (AdvancePaymentPercent < AdvPmtPct_1)) or
        ((VehiclePrice <= VehiclePrice_4) and (VehiclePrice > VehiclePrice_2) and( AdvPmtPct < AdvPmtPct_2)) or
        ((VehiclePrice > VehiclePrice_4) and (AdvPmtPct < AdvPmtPct_3):

"""
