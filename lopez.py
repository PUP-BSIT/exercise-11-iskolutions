import pycountry

def search_country(query):
    try:
        countries = list(pycountry.countries.search_fuzzy(query))
        if countries:
            return countries[0]
    except LookupError:
        pass
    
    return None
