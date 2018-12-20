#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 18:11:19 2018

@author: mh70
"""

from operas import operas_both_at_premiere


def test_wagner_verdi():
    wagner_verdi = operas_both_at_premiere("wagner", "verdi")
    assert len(wagner_verdi) == 10
    assert "Otello" not in wagner_verdi


def test_verdi_wagner():
    verdi_wagner = operas_both_at_premiere("verdi", "wagner")
    assert len(verdi_wagner) == 11
    assert "The Fairies" not in verdi_wagner  # premiere after death


def test_beethoven_wagner():
    beethoven_wagner = operas_both_at_premiere("beethoven", "wagner")
    assert len(beethoven_wagner) == 0


def test_wagner_beethoven():
    wagner_beethoven = operas_both_at_premiere("wagner", "beethoven")
    assert len(wagner_beethoven) == 0

def test_beethoven_mozart():
    beethoven_mozart = operas_both_at_premiere("beethoven", "mozart")
    assert len(beethoven_mozart) == 5    
