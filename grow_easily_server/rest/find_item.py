import json
import sys
from flask import Blueprint, request, Response

from grow_easily_server.use_cases import request_objects as req
from grow_easily_server.shared import response_object as res
from grow_easily_server.repository import dynamodb as dbr
from grow_easily_server.use_cases import user_use_cases as uc
from grow_easily_server.serializers import item_serializer as ser

from grow_easily_server.domain.user import User
from grow_easily_server.domain.device import Device
from grow_easily_server.domain.recipe import Recipe
from grow_easily_server.domain.module import Module
from grow_easily_server.domain.hardware import Hardware
from grow_easily_server.domain.trigger import Trigger
from grow_easily_server.domain.measurement import Measurement


blueprint = Blueprint('find_<item>', __name__)

STATUS_CODES = {
    res.ResponseSuccess.SUCCESS: 200,
    res.ResponseFailure.RESOURCE_ERROR: 404,
    res.ResponseFailure.PARAMETERS_ERROR: 400,
    res.ResponseFailure.SYSTEM_ERROR: 500
}


def parse_request_object():
    qrystr_params = {
        'filters': {},
    }

    for arg, values in request.args.items():
        if arg.startswith('filter_'):
            qrystr_params['filters'][arg.replace('filter_', '')] = values

    return req.RecipeListRequestObject.from_dict(qrystr_params)


def str_to_class(str):
    return getattr(sys.modules[__name__], str)


@blueprint.route('/find_<item>', methods=['GET'])
def find_item(item):
    request_object = parse_request_object()
    repo = dbr.Dynamodb(str_to_class(item.capitalize()))
    use_case = uc.UserListUseCase(repo)
    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser.ItemEncoder),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])


@blueprint.route('/add_<item>', methods=['GET'])
def add_user(item):
    request_object = parse_request_object()
    repo = dbr.Dynamodb(str_to_class(item.capitalize()))
    use_case = uc.UserAddUseCase(repo)
    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser.ItemEncoder),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])
