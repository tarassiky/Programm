country_city_map = {
    "Canada": ['Toronto', 'Vancouver', 'Montreal'],
    "Japan": ['Tokyo', 'Osaka', 'Kyoto'],
    "Australia": ['Sydney', 'Melbourne', 'Brisbane'],
}

city_list = ['Toronto', 'Tokyo', 'Vancouver', 'Montreal']

class CityCountryIterator:

    def __init__(self, cities, country_map):
        self.cities = cities
        self.country_map = country_map
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.cities):
            current_city = self.cities[self.index]
            self.index += 1
            for country, cities in self.country_map.items():
                if current_city in cities:
                    return f"{current_city} is in {country}"
        else:
            raise StopIteration

city_iterator = CityCountryIterator(city_list, country_city_map)
for result in city_iterator:
    print(result)
