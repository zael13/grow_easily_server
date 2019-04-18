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
        'user_id': str(maxId),
		'name': "Max",
		'surname': "Some surname",
		'email': "max.zastavny@gmail.com",
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
		'user_id': str(dianaId),
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
		'user_id': str(antonId),
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
		'user_id': str(uuid.uuid4()),
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
        'device_id': str(device1),
		'user_id': str(maxId),
		'recipe_id': str(recipe1),
		'name': "dev1",
		'start_time': 1555331650,
	}
)

deviceTable.put_item(
	Item={
        'device_id': str(device2),
		'user_id': str(maxId),
		'recipe_id': str(recipe1),
		'name': "dev2",
		'start_time': 1555331650,
	}
)

deviceTable.put_item(
	Item={
        'device_id': str(device3),
		'user_id': str(dianaId),
		'recipe_id': str(recipe2),
		'name': "dev3",
		'start_time': 1555331650,
	}
)

deviceTable.put_item(
	Item={
        'device_id': str(device4),
		'user_id': str(antonId),
		'recipe_id': str(recipe2),
		'name': "dev4",
		'start_time': 1555331650,
	}
)


recipeTable = dynamodb.Table('Recipe')

recipeTable.put_item(
	Item={
        'recipe_id': str(recipe1),
		'device_id': str(maxId),
		'name': "Tomato",
		'rating': Decimal(5.0),
		'culture': "tomatoes",
		'duration': 2,
	}
)

recipeTable.put_item(
	Item={
        'recipe_id': str(uuid.uuid4()),
		'device_id': str(device2),
		'name': "Potaito",
		'rating': Decimal(5.0),
		'culture': "potaito",
		'duration': 0,
	}
)

recipeTable.put_item(
	Item={
        'recipe_id': str(recipe2),
		'device_id': str(device3),
		'name': "Potaito",
		'rating': Decimal(4.5),
		'culture': "salad",
		'duration': 3,
	}
)

moduleTable = dynamodb.Table('Module')

moduleTable.put_item(
	Item={
        'module_id': str(module1),
        'recipe_id': str(recipe1),
        'name': "Temperature",
		'value': Decimal(20.0),
        'delta': Decimal(2.0),
	}
)

moduleTable.put_item(
	Item={
        'module_id': str(module2),
        'recipe_id': str(recipe2),
        'name': "Moisure",
        'value': Decimal(60.0),
        'delta': Decimal(5.0),
	}
)

hardwareTable = dynamodb.Table('Hardware')

hardwareTable.put_item(
	Item={
        'hardware_id': str(hardware1),
        'module_id': str(module1),
        'name': "DHT",
        'hw_type': "DHT_TEMPERATURE",
		'value': Decimal(20.0),
        'delta': Decimal(2.0),
        'pins': [1,2],
    }
)

hardwareTable.put_item(
	Item={
        'hardware_id': str(hardware2),
        'module_id': str(module1),
        'name': "Pin",
        'hw_type': "DIGITAL_WRITER",
        'value': Decimal(60.0),
        'delta': Decimal(2.0),
        'pins': [3],
	}
)

triggerTable = dynamodb.Table('Trigger')

triggerTable.put_item(
	Item={
        'trigger_id': str(trigger1),
        'module_id': str(module1),
        'name': "PeriodicEvent",
		'start_time': 1555331650,
		'end_time': 1555331650,
        'delta': Decimal(2.0),
	}
)

triggerTable.put_item(
	Item={
        'trigger_id': str(trigger2),
        'module_id': str(module1),
        'name': "DailyEvent",
		'start_time': 1555331650,
		'end_time': 1555331650,
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
