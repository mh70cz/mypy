"""
Bite 111. Use the ipinfo API to lookup IP country 

https://codechalleng.es/bites/111
"""
import json

import requests


IPINFO_URL = 'http://ipinfo.io/{ip}/json'


def get_ip_country_(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    r = requests.get(IPINFO_URL.format(ip=ip_address))
    return json.loads(r.text)["country"]
        
    
def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    r = requests.get(IPINFO_URL.format(ip=ip_address))
    
    return json.loads(r.content)["country"]