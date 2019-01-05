import json


class RecipeEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            to_serialize = {
                'code': str(o.code),
                'duration': o.duration,
                'price': o.price,
                "rating": o.rating,
                "longitude": o.longitude,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
