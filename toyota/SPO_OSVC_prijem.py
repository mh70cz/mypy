# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Sat Jul 13 19:41:33 2019 
"""


# vypocet v BEE:
# pokud In.Applicant.EmployerType = 5  (Zdroj příjmů OSVC)

# (In.Applicant.TrReceivedFromAllEmployers + In.Applicant.TrTaxBaseLineTotals 
#  - In.Applicant.TrTaxAfterApplyingDiscount)/12 + $SpouseIncome

TrReceivedFromAllEmployers = 0 # ze STEP nic neprislo
TrTaxBaseLineTotals = 330857 # zaslano ze STEP
TrTaxAfterApplyingDiscount = 0 # ze STEP nic neprislo

# BEE $SpouseIncome
CoApplicant_AverageMIAT = 18329  # zaslano ze STEP puvodni hodnota prepsana  

TotalIncome = (TrReceivedFromAllEmployers + TrTaxBaseLineTotals 
               - TrTaxAfterApplyingDiscount) /12 + CoApplicant_AverageMIAT 

45900.41666666667

print(TotalIncome)