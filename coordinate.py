#!/usr/bin/env python3
from pygeocoder import Geocoder
if __name__=='__main__':
    address = '10 Downing St, London SW1A 2AB, UK'
    print(Geocoder.geocode(address)[0].coordinates) 
