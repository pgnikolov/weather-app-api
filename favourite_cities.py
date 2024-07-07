class FavouriteCities:
    """
    A class to manage favourite cities stored in a text file.
    """

    @ staticmethod
    def add_city(city_name):
        """
            Adds a new city to the list of favourite cities.
        Args:
            city_name (str): The name of the city to add.
        """
        with open('favourite_cities.txt', 'a') as f:
            f.write(city_name + "\n")

    @ staticmethod
    def get_cities():
        """
            Retrieves the list of favourite cities from the text file.
        Returns:
            list: A list of favourite cities.
        """
        try:
            with open('favourite_cities.txt', 'r') as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            return []

    @ staticmethod
    def remove_city(city_index):
        """
            Removes a city from the list of favourite cities based on its index.
        Args:
            city_index (int): The index of the city to remove.
        Raises:
            IndexError: If the city index is out of range.
        """
        cities = FavouriteCities.get_cities()
        if 0 <= city_index < len(cities):
            city = cities.pop(city_index)
            with open('favourite_cities.txt', 'w') as f:
                f.writelines(f"{city}\n" for city in cities)
            print(f"City '{city}' removed from favorites.")
        else:
            print("Invalid index.")
