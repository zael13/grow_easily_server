class User:
    def __init__(self, code, name, surname, email, password, reg_date, mobile=None, age=None, gender=None, rating=None):
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
        user = User(code=adict['code'], name=adict['name'], surname=adict['surname'], email=adict['email'],
                    password=adict['password'], reg_date=adict['reg_date'], mobile=adict['mobile'],
                    age=adict['age'], gender=adict['gender'], rating=adict['rating'])
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

