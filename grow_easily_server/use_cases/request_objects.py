import collections

from grow_easily_server.shared import request_object as req


class RecipeListRequestObject(req.ValidRequestObject):

    def __init__(self, filters=None):
        self.filters = filters

    @classmethod
    def from_dict(cls, adict):
        invalid_req = req.InvalidRequestObject()

        if 'filters' in adict and not isinstance(adict['filters'], collections.Mapping):
            invalid_req.add_error('filters', 'Is not iterable')

        if invalid_req.has_errors():
            return invalid_req

        return RecipeListRequestObject(filters=adict.get('filters', None))
