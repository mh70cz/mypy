#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 06:25:48 2019

@author: mh70
"""
import datetime

za60 = (datetime.datetime.now() + datetime.timedelta(days=60)).strftime("%d.%m.%Y")


def spo_m():
    app_values = {
        "TitleBefore": "ing.",
        "Name": "Andrej",
        "Surname": "Bureš",
        "TitleAfter": "MBA",
        "MaritalStatus": "1",
        "Foreigner": "0",
        "DateOfBirth": "19.1.1968",
        "PIN": "6811248851",
        "Gender": "M",
        "Citizenship": "CZ",
        "BankAccountNumber1": "31",
        "BankAccountNumber": "314159",
        "BankCode": "0100",
        "DocumentType": "0",
        "DocumentNumber": "OP913746",
        "DocumentValidTo": "19.12.2068",
        "SecondDocumentType": "6",
        "SecondDocumentNumber": "RP853257",
        "SecondDocumentValidTo": "14.12.2027",
        "PhoneNumber": "+420398827620",
        "Email": "andrej.bures@elposta.cz",
        "NRKISign": "1",
    }

    app_address_values = {
        "HomeAddressStreet": "Koněvova 242",
        "HomeAddressCity": "Praha 3",
        "HomeAddressZip": "13000",
        "HomeAddressState": "CZ",
        "AddressSame": "0",
        "AddressServicesStreet": "Park Str. 37",
        "AddressServicesCity": "Köln Chorweiler",
        "AddressServicesZip": "50765",
        "AddressServicesState": "DE",
    }

    coapp_values = {
        "TitleBefore": "JUDr",
        "Name": "Marika",
        "Surname": "Burešová",
        "TitleAfter": "PhD",
        "Foreigner": "0",
        "DateOfBirth": "1.1.1970",
        "AverageMIAT": "22656",
        "AddressServicesStreet": "Augsburger Strasse 44",
        "AddressServicesCity": "Wershofen",
        "AddressServicesZip": "53520",
        "AddressServicesState": "DE",
    }
    guar_values = {
        "TitleBefore": "RNDr",
        "Name": "Radka",
        "Surname": "Rychlá",
        "TitleAfter": "PhD",
        "Foreigner": "0",
        "DateOfBirth": "26.1.1979",
        "PIN": "7951266884",
        "AverageMIAT": "22656",
        "AddressServicesStreet": "Via Appia Nuova 823/4",
        "AddressServicesCity": "Roma",
        "AddressServicesZip": "00184",
        "AddressServicesState": "DE",
    }
    emp_values = {
        "RegistrationNumber": "04134940",
        "ProbationPeriod": "0",
        "EmploymentIndefinitePeriod": "0",
        "NoticePeriod": "0",
        "WorkPhoneNumber": "+420731555999",
        "Foreigner": "0",
        "EmploymentIndefinitePeriodUntil": "21.11.2020",
    }
    vehicle_values = {"ExpectedDeliveryDate": za60}
    contract_values = {"RequestSign": "1"}

    return (
        app_values,
        app_address_values,
        coapp_values,
        guar_values,
        emp_values,
        vehicle_values,
        contract_values,
    )


def spo_z():
    app_values = {
        "TitleBefore": "ing.",
        "Name": "Monika",
        "Surname": "Burešová",
        "TitleAfter": "MBA",
        "MaritalStatus": "1",
        "Foreigner": "0",
        "DateOfBirth": "22.11.1966",
        "PIN": "6661228013",
        "Gender": "M",
        "Citizenship": "CZ",
        "BankAccountNumber1": "31",
        "BankAccountNumber": "314159",
        "BankCode": "0100",
        "DocumentType": "0",
        "DocumentNumber": "OP913746",
        "DocumentValidTo": "24.11.2022",
        "SecondDocumentType": "6",
        "SecondDocumentNumber": "RP853257",
        "SecondDocumentValidTo": "14.12.2027",
        "PhoneNumber": "+420398827620",
        "Email": "andrej.bures@elposta.cz",
        "NRKISign": "1",
    }

    app_address_values = {
        "HomeAddressStreet": "Koněvova 242",
        "HomeAddressCity": "Praha 3",
        "HomeAddressZip": "13000",
        "HomeAddressState": "CZ",
        "AddressSame": "0",
        "AddressServicesStreet": "Park Str. 37",
        "AddressServicesCity": "Köln Chorweiler",
        "AddressServicesZip": "50765",
        "AddressServicesState": "DE",
    }

    coapp_values = {
        "TitleBefore": "JUDr",
        "Name": "Marika",
        "Surname": "Burešová",
        "TitleAfter": "PhD",
        "Foreigner": "0",
        "DateOfBirth": "1.1.1970",
        "AverageMIAT": "22656",
        "AddressServicesStreet": "Augsburger Strasse 44",
        "AddressServicesCity": "Wershofen",
        "AddressServicesZip": "53520",
        "AddressServicesState": "DE",
    }
    guar_values = {
        "TitleBefore": "RNDr",
        "Name": "Radka",
        "Surname": "Rychlá",
        "TitleAfter": "PhD",
        "Foreigner": "0",
        "DateOfBirth": "26.1.1979",
        "PIN": "7951266884",
        "AverageMIAT": "22656",
        "AddressServicesStreet": "Via Apipa Nuova 823/4",
        "AddressServicesCity": "Roma",
        "AddressServicesZip": "00184",
        "AddressServicesState": "DE",
    }
    emp_values = {
        "RegistrationNumber": "04134940",
        "ProbationPeriod": "0",
        "EmploymentIndefinitePeriod": "0",
        "NoticePeriod": "0",
        "WorkPhoneNumber": "+420731555999",
        "Foreigner": "0",
        "EmploymentIndefinitePeriodUntil": "21.11.2020",
    }
    vehicle_values = {"ExpectedDeliveryDate": za60}
    contract_values = {"RequestSign": "1"}

    return (
        app_values,
        app_address_values,
        coapp_values,
        guar_values,
        emp_values,
        vehicle_values,
        contract_values,
    )

