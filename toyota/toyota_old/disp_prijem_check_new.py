# -*- coding: utf-8 -*-
"""
po úpravě dle typu bydlení
v případě že applicant (neaplikuje se na coApplicant) je v pronájmu,
se odečítá 
mesačné výdavky na domácnosť (náklady na bývanie, energia, strava, ...) v €   
->  Applicant: SpendingPerHousehold


"""

ApplicantNRKIMonthlyInstallment =417
CoApplicantNRKIMonthlyInstallment = 484


AppAverMIAT = 560
OtherIncomeAmount = 0
AverAgrGrossWage = 0


CoAppAverMIAT = 1250
CoAppOtherIncomeAmount = 0
CoAppAverAgrGrossWage = 0

#MesacneVydajeDomacnosti 
AppMonthlyHouseholdExpenditures = 537   #applicant.MonthlyHouseholdExpenditures
CoAppMonthlyHouseholdExpenditures = 484 #coapplicant.MonthlyHouseholdExpenditures


#typ bydlení 3 - pronájem
AppHomeAddressFormOfHousing = 3
CoAppHomeAddressFormOfHousing = 3

#mesačné výdavky na domácnosť (náklady na bývanie, energia, strava, ...)
AppSpendingPerHousehold = 0   #Applicant: SpendingPerHousehold
CoAppSpendingPerHousehold = 0 


MonthlyLivingCosts = 348.13 + 2 * 93.61 #ZivotneMinimum

FinStandCoeff = 0.8

CreditAmountVAT = 7553
NoOfInstalments = 48

#FON 

#pokud v pronájmu odečti mesačné výdavky na domácnosť (náklady na bývanie, energia, strava, ...)
if AppHomeAddressFormOfHousing == 3:
    AppMonthlyHouseholdExpenditures = AppMonthlyHouseholdExpenditures - AppSpendingPerHousehold 
    

DipInc = (AppAverMIAT + OtherIncomeAmount + AverAgrGrossWage + CoAppAverMIAT  + CoAppOtherIncomeAmount+CoAppAverAgrGrossWage-MonthlyLivingCosts)*FinStandCoeff-MonHouseExp-CoAppMonthlyHouseholdExpenditures-(CreditAmountVAT/NoOfInstalments)





MesacnePrijmyZadatela = AppAverMIAT + OtherIncomeAmount + AverAgrGrossWage
MesacnePrijmyDomacnosti = MesacnePrijmyZadatela
MesacnePrijmySpoluzadatela = CoAppAverMIAT + CoAppOtherIncomeAmount + CoAppAverAgrGrossWage


MesacneVydajeDomacnosti = AppMonthlyHouseholdExpenditures
MesacneVydajeSpoluziadatela = CoAppMonthlyHouseholdExpenditures
ZivotneMinimum = MonthlyLivingCosts
SplatkaUveru = CreditAmountVAT/NoOfInstalments


DipInc2 = (MesacnePrijmyDomacnosti + MesacnePrijmySpoluzadatela - ZivotneMinimum  ) * FinStandCoeff - MesacneVydajeDomacnosti - MesacneVydajeSpoluziadatela - SplatkaUveru


ApplicantAverageMIAT = AppAverMIAT
ApplicantOtherIncomeAmount = OtherIncomeAmount
CoApplicantAverageMIAT = CoAppAverMIAT
CoApplicantOtherIncomeAmount = CoAppOtherIncomeAmount
AnnualIncome = (ApplicantAverageMIAT + ApplicantOtherIncomeAmount) * 12 + (CoApplicantAverageMIAT + CoApplicantOtherIncomeAmount)*12
ApplicantResidualValue = 0
CoApplicantResidualValue = 0
ApplicantNRKIResidualValue =  26432
CoApplicantNRKIResidualValue = 27410


ApplicantResidualValue =  ApplicantResidualValue if ApplicantResidualValue >= ApplicantNRKIResidualValue else ApplicantNRKIResidualValue
CoApplicantResidualValue = CoApplicantResidualValue if CoApplicantResidualValue >= CoApplicantNRKIResidualValue else CoApplicantNRKIResidualValue

CreditCeilingFO = (AnnualIncome * 8) - ApplicantResidualValue - CoApplicantResidualValue - CreditAmountVAT


"""

 <expr  name  ="  FinancialStanding  "  type  ="  expr  "  direction  ="  Output  "  defaultValue  ="  0  "  expression  ="  
 IF(applicant.FOPDataCheckbox=1,
 ((applicant.TaxBase-applicant.TaxTotal)/12+CoAppAverMIAT-MonthlyLivingCosts)*FinStandCoeff-InstalmentAVGWithVAT-MonHouseExp-CoAppMonthlyHouseholdExpenditures,
 (AppAverMIAT+OtherIncomeAmount+AverAgrGrossWage+CoAppAverMIAT+CoAppOtherIncomeAmount+CoAppAverAgrGrossWage-MonthlyLivingCosts)*FinStandCoeff-MonHouseExp-CoAppMonthlyHouseholdExpenditures-(CreditAmountVAT/NoOfInstalments))  "  value  ="  1463.096  " />
 


<expr  name  ="  CreditCeilingFO  "  type  ="  expr  "  direction  ="  Output  "  defaultValue  ="  0  "  expression  ="  (AnnualIncome * 8) - IF(ApplicantResidualValue >= ApplicantNRKIResidualValue, ApplicantResidualValue , ApplicantNRKIResidualValue) - IF(CoApplicantResidualValue >= CoApplicantNRKIResidualValue, CoApplicantResidualValue , CoApplicantNRKIResidualValue) - CreditAmountVAT  "  value  ="  257931  " />

""" 

