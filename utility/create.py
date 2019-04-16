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
            'AttributeName': 'userId',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'name',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'userId',
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
            'AttributeName': 'deviceId',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'timestamp',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'deviceId',
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
            'AttributeName': 'userId',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'name',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'userId',
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
            'AttributeName': 'triggerId',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'hardwareId1',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'triggerId',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'hardwareId1',
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
            'AttributeName': 'moduleId',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'triggerId',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'moduleId',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'triggerId',
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
            'AttributeName': 'moduleId',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'hwType',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'moduleId',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'hwType',
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
