from grow_easily_server.shared.domain_model import DomainModel


class Recipe(object):

    def __init__(self, code, size, price, latitude, longitude):
        self.code = code
        self.size = size
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

    @classmethod
    def from_dict(cls, adict):
        recipe = Recipe(
            code=adict['code'],
            size=adict['size'],
            price=adict['price'],
            latitude=adict['latitude'],
            longitude=adict['longitude'],
        )

        return recipe

    def to_dict(self):
        return {
            'code': self.code,
            'size': self.size,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()


DomainModel.register(Recipe)
