import countryinfo

def display_country_details(country_name):
    country = countryinfo.CountryInfo(country_name)
    info = country.info()

    print(f"\nCountry: {info.get('name', 'Unknown')}")
    print(f"Region: {info.get('region', 'Unknown')}")
    print(f"Subregion: {info.get('subregion', 'Unknown')}")
    print(f"Population: {info.get('population', 'Unknown')}")
    print(f"Area: {info.get('area', 'Unknown')} km²")
    print("Timezones: " +
          f"{', '.join(info.get('timezones', []))}")
    
    
def country_info_bot():
    print("\nWelcome! I'm CountryInfoBot.")
    print("Type the name of a country to get information about it.")
    print("Type 'exit' to end our chat.")

    while True:
        user_input = input("\nEnter a country name: ").strip()

        if user_input.lower() == "exit":
            print("CountryInfoBot: Goodbye! Explore the world, you must!")
            break

        display_country_details(user_input)

       