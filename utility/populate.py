import boto3
import json
import uuid
from decimal import Decimal

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")


maxId = uuid.uuid4()
dianaId = uuid.uuid4()
antonId = uuid.uuid4()

def gen_id_list(n):
	return [str(uuid.uuid4()) for i in range(1, n+1)]

users = [maxId, dianaId, antonId]
devices = gen_id_list(9)
recipes = gen_id_list(9)
modules = gen_id_list(81)

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

for i in range(0, len(devices)):
	deviceTable.put_item(
		Item={
	       	'device_id': str(devices[i]),
			'user_id': str(users[int(i/3)]),
			'recipe_id': str(recipes[i]),
			'name': "dev"+str(i),
			'start_time': 1555331650+i,
		}
	)

recipeTable = dynamodb.Table('Recipe')

for i in range(0, len(recipes)):
	recipeTable.put_item(
		Item={
	        'recipe_id': str(recipes[i]),
			'device_id': str(devices[i]),
			'name': "recipe"+str(i),
			'rating': Decimal(int(i/10)),
			'culture': "tomatoes",
			'duration': Decimal(int(i)),
		}
	)

moduleTable = dynamodb.Table('Module')

for i in range(0, len(modules)):
	moduleTable.put_item(
		Item={
	        'module_id': str(modules[int(i/9)]),
	        'recipe_id': str(recipes[int(i/9)]),
	        'name': "Module"+str(i),
			'value': Decimal(int(i*2)),
	        'delta': Decimal(int(i/5)),
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

measurementTable = dynamodb.Table('Measurement')

measurementTable.put_item(
	Item={
        'measurement_id': '1',
        'device_id': str(device1),
        'timestamp': '1',
        'temperature': Decimal(20.0),
		'moisture': Decimal(60.0),
	}
)

measurementTable.put_item(
	Item={
        'measurement_id': '2',
        'device_id': str(device1),
        'timestamp': str(2),
        'temperature': Decimal(20.0),
		'moisture': Decimal(60.0),
		'light': Decimal(6.0),
	}
)

measurementTable.put_item(
	Item={
        'measurement_id': '3',
        'device_id': str(device1),
        'timestamp': str(4),
        'temperature': Decimal(22.0),
		'moisture': Decimal(60.0),
		'ph_level': Decimal(6.0),
	}
)

measurementTable.put_item(
	Item={
        'measurement_id': '4',
        'device_id': str(device1),
        'timestamp': str(4),
        'temperature': Decimal(20.0),
		'moisture': Decimal(50.0),
		'ph_level': Decimal(6.5),
	}
)

measurementTable.put_item(
	Item={
        'measurement_id': '5',
        'device_id': str(device1),
        'timestamp': str(5),
        'temperature': Decimal(21.0),
		'moisture': Decimal(50.0),
		'ph_level': Decimal(4.0),
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
