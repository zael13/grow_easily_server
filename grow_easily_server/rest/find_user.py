import json
from flask import Blueprint, request, Response

from grow_easily_server.use_cases import request_objects as req
from grow_easily_server.shared import response_object as res
from grow_easily_server.repository import dynamodb as dbr
from grow_easily_server.use_cases import user_use_cases as uc
from grow_easily_server.serializers import user_serializer as ser
from grow_easily_server.domain import user


blueprint = Blueprint('find_user', __name__)

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


@blueprint.route('/find_user', methods=['GET'])
def find_user():
    request_object = parse_request_object()

    repo = dbr.Dynamodb(user.User)
    use_case = uc.UserListUseCase(repo)

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser.UserEncoder),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])


@blueprint.route('/add_user', methods=['GET'])
def add_user():
    request_object = parse_request_object()
    repo = dbr.Dynamodb(user.User)
    use_case = uc.UserAddUseCase(repo)
    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser.UserEncoder),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])


from grow_easily_server.serializers import device_serializer as ser2
from grow_easily_server.domain import device


@blueprint.route('/find_device', methods=['GET'])
def find_device():
    request_object = parse_request_object()

    repo = dbr.Dynamodb(device.Device)
    use_case = uc.UserListUseCase(repo)

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser2.DeviceEncoder),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])


@blueprint.route('/add_device', methods=['GET'])
def add_device():
    request_object = parse_request_object()
    repo = dbr.Dynamodb(device.Device)
    use_case = uc.UserAddUseCase(repo)
    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser2.DeviceEncoder),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])


from grow_easily_server.serializers import trigger_serializer as ser3
from grow_easily_server.domain import trigger


@blueprint.route('/find_trigger', methods=['GET'])
def find_trigger():
    request_object = parse_request_object()

    repo = dbr.Dynamodb(trigger.Trigger)
    use_case = uc.UserListUseCase(repo)

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser3.TriggerEncoder),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])


from grow_easily_server.serializers import recipe_serializer as ser4
from grow_easily_server.domain import recipe


@blueprint.route('/find_recipe', methods=['GET'])
def find_recipe():
    request_object = parse_request_object()

    repo = dbr.Dynamodb(recipe.Recipe)
    use_case = uc.UserListUseCase(repo)

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser4.RecipeEncoder),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])


from grow_easily_server.domain import module


@blueprint.route('/find_module', methods=['GET'])
def find_module():
    request_object = parse_request_object()

    repo = dbr.Dynamodb(module.Module)
    use_case = uc.UserListUseCase(repo)

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser4.RecipeEncoder),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])


from grow_easily_server.serializers import hardware_serializer as ser5
from grow_easily_server.domain import hardware


@blueprint.route('/find_hardware', methods=['GET'])
def find_hardware():
    request_object = parse_request_object()

    repo = dbr.Dynamodb(hardware.Hardware)
    use_case = uc.UserListUseCase(repo)

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser5.HardwareEncoder),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])


from grow_easily_server.serializers import measurement_serializer as ser6
from grow_easily_server.domain import measurement


@blueprint.route('/find_measurement', methods=['GET'])
def find_measurement():
    request_object = parse_request_object()

    repo = dbr.Dynamodb(measurement.Measurement)
    use_case = uc.UserListUseCase(repo)

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser6.MeasurementEncoder),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])
