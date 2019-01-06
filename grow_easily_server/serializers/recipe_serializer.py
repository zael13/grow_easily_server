import json


class RecipeEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            to_serialize = {
                'code': str(o.code),
                'duration': o.duration,
                'owner': o.owner,
                "rating": o.rating,
                "name": o.name,
                'items': ''.join(o.items)
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
