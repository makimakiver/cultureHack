import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import pycountry_convert as pc

from typing import Tuple

from tqdm import tqdm
tqdm.pandas()

def get_continent_name(continent_code: str):
    continent_dict = {
        "NA": "North America",
        "SA": "South America",
        "AS": "Asia",
        "AF": "Africa",
        "OC": "Oceania",
        "EU": "Europe",
        "AQ" : "Antarctica"
    }
    return continent_dict[continent_code]


def get_details(lat:float,long:float):
    co_ord = [lat,long]
    locator = Nominatim(user_agent="<username@gmail.com>",timeout = 10)
    geocode = RateLimiter(locator.reverse, min_delay_seconds=1)
    location = locator.reverse(co_ord,language = 'en')

    if location is None:
        return "Antarctica","Antarctica","Antarctica"
    
    address = location.raw['address']   
    country_code = address['country_code'].upper()

    continent_code = pc.country_alpha2_to_continent_code(country_code)
    continent_name = get_continent_name(continent_code)

    return location.address,continent_name

if __name__ == "__main__":
    lat = float(input("Lat: "))
    long = float(input("Long: "))
    print(get_details(lat,long))

