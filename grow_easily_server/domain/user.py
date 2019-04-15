from grow_easily_server.shared.domain_model import DomainModel


class User:
    def __init__(self, code, name, surname, email, password, reg_date,
                 mobile=None, age=None, gender=None, rating=None):
        self.code = code
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.reg_date = reg_date
        self.mobile = mobile
        self.age = age
        self.gender = gender
        self.rating = rating

    @classmethod
    def from_dict(cls, adict):
        user = User(code=adict['code'], name=adict['name'],
                    surname=adict['surname'], email=adict['email'],
                    password=adict['password'], reg_date=adict['reg_date'],
                    mobile=adict['mobile'] if ('mobile' in adict) else None,
                    age=adict['age'] if ('age' in adict) else None,
                    gender=adict['gender'] if ('gender' in adict) else None,
                    rating=adict['rating'] if ('rating' in adict) else None)
        return user

    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'password': self.password,
            'reg_date': self.reg_date,
            'mobile': self.mobile,
            'age': self.age,
            'gender': self.gender,
            'rating': self.rating
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()


DomainModel.register(User)
