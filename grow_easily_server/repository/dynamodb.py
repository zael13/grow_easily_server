# from grow_easily_server.domain import recipe as sr
import boto3
from boto3.dynamodb.conditions import Key


class Dynamodb:
    def __init__(self, db_objects_type):
        self.db_objects_type = db_objects_type
        self.dynamodb = boto3.resource('dynamodb',
                                       endpoint_url='http://localhost:8000',
                                       region_name='us-west-2')
        self.table = self.dynamodb.Table(db_objects_type.__name__)

    def list(self, filters=None):
        if not filters:
            response = self.table.scan()
        else:
            for key, value in filters.items():
                response = self.table.query(KeyConditionExpression=Key(key).eq(value))
        # result = [e for e in result if self._check(e, key, value)]

        result = []
        for i in response['Items']:
            result.append(i)
        return [self.db_objects_type.from_dict(r) for r in result]

    def insert(self, item):
        if not isinstance(item, self.db_objects_type):
            raise TypeError('item is not of type %s' % self.db_objects_type)
        self.table.put_item(Item=self.db_objects_type.to_dict(item))
