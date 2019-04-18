import boto3


## For a Boto3 client ('client' is for low-level access to Dynamo service API)
dynamodb = boto3.client('dynamodb', endpoint_url='http://localhost:8000', region_name='us-west-2')
response = dynamodb.list_tables()
print(response)

table = dynamodb.create_table(
    TableName='User',
    KeySchema=[
        {
            'AttributeName': 'email',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'name',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'email',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

table = dynamodb.create_table(
    TableName='Device',
    KeySchema=[
        {
            'AttributeName': 'user_id',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'name',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'user_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

table = dynamodb.create_table(
    TableName='Measurement',
    KeySchema=[
        {
            'AttributeName': 'device_id',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'timestamp',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'device_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'timestamp',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)


table = dynamodb.create_table(
    TableName='Recipe',
    KeySchema=[
        {
            'AttributeName': 'recipe_id',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'name',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'recipe_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)


table = dynamodb.create_table(
    TableName='Module',
    KeySchema=[
        {
            'AttributeName': 'module_id',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'hardware_id1',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'module_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'hardware_id1',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)


table = dynamodb.create_table(
    TableName='Trigger',
    KeySchema=[
        {
            'AttributeName': 'module_id',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'trigger_id',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'module_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'trigger_id',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)



table = dynamodb.create_table(
    TableName='Hardware',
    KeySchema=[
        {
            'AttributeName': 'module_id',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'hw_type',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'module_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'hw_type',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)


response = dynamodb.list_tables()

print(response)
