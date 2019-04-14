import json
from grow_easily_server.domain.user import User
import decimal


class UserEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            if isinstance(o, User):
                to_serialize = {
                    'code': str(o.code),
                    'name': o.name,
                    'surname': o.surname,
                    'email': o.email,
                    'password': o.password,
                    'reg_date': o.reg_date,
                    'mobile': o.mobile,
                    'age': o.age,
                    'gender': o.gender,
                    'rating': str(o.rating)
                }
                print(to_serialize)
            elif isinstance(o, decimal.Decimal):
                if abs(o) % 1 > 0:
                    return float(o)
                else:
                    return int(o)
            else:
                to_serialize = super().default(o)
            return to_serialize
        except AttributeError:
            return super().default(o)
