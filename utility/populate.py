import boto3
import json
import uuid
from decimal import Decimal

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")


maxId = uuid.uuid4()
dianaId = uuid.uuid4()
antonId = uuid.uuid4()

device1 = uuid.uuid4()
device2 = uuid.uuid4()
device3 = uuid.uuid4()
device4 = uuid.uuid4()

recipe1 = uuid.uuid4()
recipe2 = uuid.uuid4()

module1 = uuid.uuid4()
module2 = uuid.uuid4()

trigger1 = uuid.uuid4()
trigger2 = uuid.uuid4()

hardware1 = uuid.uuid4()
hardware2 = uuid.uuid4()

userTable = dynamodb.Table('User')

userTable.put_item(
	Item={
        'userId': str(maxId),
		'name': "Max",
		'surname': "Some surname",
		'email': "diana.sukhinina1@gmail.com",
		'password': "123456",
		'reg_date': 1555331630,
		'mobile': None,
		'age': 30,
		'gender': "male",
		'rating': Decimal(3.0),
	}
)

userTable.put_item(
	Item={
		'userId': str(dianaId),
		'name': "Diana",
		'surname': "Some surname",
		'email': "diana.sukhinina1@gmail.com",
		'password': "123456",
		'reg_date': 1555331650,
		'mobile': "12345678",
		'gender': "female",
		'rating': Decimal(4.0),
	}
)

userTable.put_item(
	Item={
		'userId': str(antonId),
		'name': "Anton",
		'surname': "Some surname",
		'email': "antonioua1340@gmail.com",
		'password': "123456",
		'reg_date': 1555331680,
		'mobile': "12345678",
		'gender': "male",
		'rating': Decimal(5.0),
	}
)

userTable.put_item(
	Item={
		'userId': str(uuid.uuid4()),
		'name': "Ivan",
		'surname': "Ivanov",
		'email': "ivan@gmail.com",
		'password': "123456",
		'reg_date': 1555331680,
		'mobile': "12345678",
		'age': 20,
		'gender': "male",
		'rating': 1,
	}
)

deviceTable = dynamodb.Table('Device')

deviceTable.put_item(
	Item={
        'deviceId': str(device1),
		'userId': str(maxId),
		'recipeId': str(recipe1),
		'name': "dev1",
		'startTime': 1555331650,
	}
)

deviceTable.put_item(
	Item={
        'deviceId': str(device2),
		'userId': str(maxId),
		'recipeId': str(recipe1),
		'name': "dev2",
		'startTime': 1555331650,
	}
)

deviceTable.put_item(
	Item={
        'deviceId': str(device3),
		'userId': str(dianaId),
		'recipeId': str(recipe2),
		'name': "dev3",
		'startTime': 1555331650,
	}
)

deviceTable.put_item(
	Item={
        'deviceId': str(device4),
		'userId': str(antonId),
		'recipeId': str(recipe2),
		'name': "dev4",
		'startTime': 1555331650,
	}
)


recipeTable = dynamodb.Table('Recipe')

recipeTable.put_item(
	Item={
        'recipeId': str(recipe1),
		'userId': str(maxId),
		'name': "Tomato",
		'rank': Decimal(5.0),
		'culture': "tomatoes",
		'length': 2,
		'modules': [str(module1), str(module2)],
	}
)

recipeTable.put_item(
	Item={
        'recipeId': str(uuid.uuid4()),
		'userId': str(maxId),
		'name': "Potaito",
		'rank': Decimal(5.0),
		'culture': "potaito",
		'length': 0,
		'modules': None,
	}
)

recipeTable.put_item(
	Item={
        'recipeId': str(recipe1),
		'userId': str(dianaId),
		'name': "Salad",
		'rank': Decimal(5.0),
		'culture': "salad",
		'length': 1,
		'modules': str(module1),
	}
)

moduleTable = dynamodb.Table('Module')

moduleTable.put_item(
	Item={
        'moduleId': str(module1),
        'name': "Temperature",
		'triggerId': str(trigger1),
		'name': "Tomato",
		'hardwareId1': str(hardware1),
		'value': Decimal(20.0),
        'delta': Decimal(2.0),
	}
)

moduleTable.put_item(
	Item={
        'moduleId': str(module2),
        'name': "Moisure",
		'triggerId': str(trigger2),
		'hardwareId1': str(hardware1),
		'hardwareId2': str(hardware2),
        'value': Decimal(60.0),
        'delta': Decimal(5.0),
		'userId': str(maxId),
	}
)

hardwareTable = dynamodb.Table('Hardware')

hardwareTable.put_item(
	Item={
        'hardwareId': str(hardware1),
        'type': "DHT_TEMPERATURE",
        'name': "DHT",
        'pins': [1,2],
		'value': Decimal(20.0),
        'delta': Decimal(2.0),
        'userId': str(maxId),
    }
)

hardwareTable.put_item(
	Item={
        'hardwareId': str(hardware2),
        'type': "DIGITAL_WRITER",
        'name': "Pin",
        'pins': [3],
		'value': Decimal(60.0),
        'delta': Decimal(2.0),
        'userId': str(maxId),
	}
)

triggerTable = dynamodb.Table('Trigger')

triggerTable.put_item(
	Item={
        'triggerId': str(trigger1),
        'type': "PeriodicEvent",
		'startTime': 1555331650,
		'endTime': 1555331650,
        'delta': Decimal(2.0),
	}
)

triggerTable.put_item(
	Item={
        'triggerId': str(trigger2),
        'type': "DailyEvent",
		'startTime': 1555331650,
		'endTime': 1555331650,
        'delta': Decimal(2.0),
	}
)



print(userTable.scan())
print("----------------------")
print(deviceTable.scan())
print("----------------------")
print(moduleTable.scan())
print("----------------------")
print(recipeTable.scan())
print("----------------------")
print(triggerTable.scan())
