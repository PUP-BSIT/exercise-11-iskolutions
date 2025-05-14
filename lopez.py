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

def country_explorer():
    print("\nWelcome to the Country Explorer!")
    print("Reference: https://www.iban.com/country-codes")

    while True:
        print("\nType 'exit' to quit.")
        user_input = input("\nEnter country name or code: ").strip()
        
        if user_input.lower() == 'exit':
            break

        country = search_country(user_input)
        
        if country:
            display_country_info(country)
        else:
            print("Country not found. Please try again.")
