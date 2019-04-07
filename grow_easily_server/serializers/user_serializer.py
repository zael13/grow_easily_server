import json
from grow_easily_server.domain.user import User


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
                    'reg_date': o.reg_date.timestamp(),
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






# table = dynamodb.create_table(
#     TableName='User',
#     KeySchema=[
#         {
#             'AttributeName': 'code',
#             'KeyType': 'HASH'  #Partition key
#         },
#         {
#             'AttributeName': 'email',
#             'KeyType': 'RANGE'  #Sort key
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'name',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'surname',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'password',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'age',
#             'AttributeType': 'N'
#         },
#         {
#             'AttributeName': 'gender',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'mobile',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'reg_date',
#             'AttributeType': 'N'
#         },
#         {
#             'AttributeName': 'rating',
#             'AttributeType': 'N'
#         }
#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 10,
#         'WriteCapacityUnits': 10
#     }
# )
