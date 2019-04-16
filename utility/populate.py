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
		'user_id': str(maxId),
		'name': "Tomato",
		'rank': Decimal(5.0),
		'culture': "tomatoes",
		'length': 2,
		'modules': [str(module1), str(module2)],
	}
)

recipeTable.put_item(
	Item={
        'recipe_id': str(uuid.uuid4()),
		'user_id': str(maxId),
		'name': "Potaito",
		'rank': Decimal(5.0),
		'culture': "potaito",
		'length': 0,
		'modules': None,
	}
)

recipeTable.put_item(
	Item={
        'recipe_id': str(recipe1),
		'user_id': str(dianaId),
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
        'module_id': str(module1),
        'name': "Temperature",
		'trigger_id': str(trigger1),
		'name': "Tomato",
		'hardwareId1': str(hardware1),
		'value': Decimal(20.0),
        'delta': Decimal(2.0),
	}
)

moduleTable.put_item(
	Item={
        'module_id': str(module2),
        'name': "Moisure",
		'trigger_id': str(trigger2),
		'hardwareId1': str(hardware1),
		'hardwareId2': str(hardware2),
        'value': Decimal(60.0),
        'delta': Decimal(5.0),
		'user_id': str(maxId),
	}
)

hardwareTable = dynamodb.Table('Hardware')

hardwareTable.put_item(
	Item={
        'hardware_id': str(hardware1),
        'module_id': str(module1),
        'hw_type': "DHT_TEMPERATURE",
        'name': "DHT",
        'pins': [1,2],
		'value': Decimal(20.0),
        'delta': Decimal(2.0),
        'user_id': str(maxId),
    }
)

hardwareTable.put_item(
	Item={
        'hardware_id': str(hardware2),
        'module_id': str(module1),
        'hw_type': "DIGITAL_WRITER",
        'name': "Pin",
        'pins': [3],
		'value': Decimal(60.0),
        'delta': Decimal(2.0),
        'user_id': str(maxId),
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
