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