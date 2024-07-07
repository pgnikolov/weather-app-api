class FavouriteCities:

    @ staticmethod
    def add_city(city_name):
        with open('favourite_cities.txt', 'a') as f:
            f.write(city_name + "\n")

    @ staticmethod
    def get_cities():
        try:
            with open('favourite_cities.txt', 'r') as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            return []

    @ staticmethod
    def remove_city(city_index):
        cities = FavouriteCities.get_cities()
        if 0 <= city_index < len(cities):
            city = cities.pop(city_index)
            with open('favourite_cities.txt', 'w') as f:
                f.writelines(f"{city}\n" for city in cities)
            print(f"City '{city}' removed from favorites.")
        else:
            print("Invalid index.")
