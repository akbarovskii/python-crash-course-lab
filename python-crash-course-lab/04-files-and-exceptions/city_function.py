def city_country(city, country, population=''):
    if population:
        full = f"{city.title()}, {country.title()}, Population = {population}"
    else:
        full = f"{city.title()}, {country.title()}"
    return full