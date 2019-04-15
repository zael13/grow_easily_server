import boto3


## For a Boto3 client ('client' is for low-level access to Dynamo service API)
dynamodb = boto3.client('dynamodb', endpoint_url='http://localhost:8000', region_name='us-west-2')
response = dynamodb.list_tables()
print(response)

params = {
    'TableName': 'Hardware'
}
dynamodb.delete_table(**params)

params = {
    'TableName': 'Trigger'
}
dynamodb.delete_table(**params)

params = {
    'TableName': 'Module'
}
dynamodb.delete_table(**params)

params = {
    'TableName': 'Device'
}
dynamodb.delete_table(**params)

params = {
    'TableName': 'Measurement'
}
dynamodb.delete_table(**params)

params = {
    'TableName': 'Recipe'
}
dynamodb.delete_table(**params)

params = {
    'TableName' : 'User'
}
dynamodb.delete_table(**params)

response = dynamodb.list_tables()

print(response)
