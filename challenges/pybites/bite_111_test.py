#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 14:35:47 2018

@author: mh70
"""

from unittest.mock import patch, Mock
import pytest
import sys

import requests

from bite_111 import get_ip_country



@patch.object(requests, 'get')
def test_ipinfo_mexican_ip(mockget):
    # hardcoding a requests response
    content = (b'{\n  "ip": "187.190.38.36",\n  "hostname": "domain.net",\n'
               b'  "city": "Mexico City",\n  "region": "Mexico City",\n  '
               b'"country": "MX",\n ' b'"loc": "11.0000,-00.1111",\n  '
               b'"postal": "12345",\n  "org": "some org"\n}')
    mockget.return_value = Mock(content=content)
    assert get_ip_country('187.190.38.36') == 'MX'


@patch.object(requests, 'get')
def test_ipinfo_japan_ip(mockget):
    # and another IP in Japan
    content = (b'{\n  "ip": "185.161.200.10",\n  "city": "Tokyo",\n  '
               b'"region": "Tokyo",\n ' b'"country": "JP",\n  "loc": '
               b'"00.1111,11.0000",\n  "postal": "123-4567",\n  '
               b'"org": "some other org"\n}')
    mockget.return_value = Mock(content=content)
    assert get_ip_country('185.161.200.10') == 'JP'
    
if __name__ == '__main__':
    pytest.main(sys.argv)      