from grow_easily_server.domain.user import User
from grow_easily_server.serializers.decimal_serializer import DecimalEncoder


class UserEncoder(DecimalEncoder):
    def default(self, o):
        try:
            if isinstance(o, User):
                to_serialize = {
                    'user_id': str(o.user_id),
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
            else:
                to_serialize = super().default(o)
            return to_serialize
        except AttributeError:
            return super().default(o)
