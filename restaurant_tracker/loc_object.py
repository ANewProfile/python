class Loc:
    def __init__(self, city, country, response) -> None:
        self.city = city
        self.country = country
        self.lalo = (response['latitude'], response['longitude'])

    def to_dictionary(self):
        return {'city': self.city,
                'country': self.country,
                'lat-long': list(self.lalo)}