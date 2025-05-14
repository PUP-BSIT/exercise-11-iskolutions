import pycountry

def search_country(query):
    try:
        countries = list(pycountry.countries.search_fuzzy(query))
        if countries:
            return countries[0]
    except LookupError:
        pass
    
    return None

def display_country_info(country):
    print("\n--- Country Information ---")
    print(f"Name: {country.name}")
    print(f"Alpha-2 code: {country.alpha_2}")
    print(f"Alpha-3 code: {country.alpha_3}")
    print(f"Numeric code: {country.numeric}")
