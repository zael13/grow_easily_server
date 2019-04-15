import pytest

from grow_easily_server.domain.user import User
from grow_easily_server.shared.domain_model import DomainModel

from grow_easily_server.repository import dynamodb
from botocore.exceptions import ClientError


@pytest.fixture
def recipe_dicts():
    return [
        {
            'code': "qqqqqqq",
            'name': "Ivan",
            'surname': "ivan@gmail.com",
            'email': "ivan@gmail.com",
            'password': "ivan@gmail.com",
            'reg_date': 10,
            'mobile': "ivan@gmail.com",
            'age': 20,
            'gender': "ivan@gmail.com",
            'rating': 1,
        },
        {
            'code': "qqqqqqq",
            'name': "Vova",
            'surname': "ivan@gmail.com",
            'email': "ivan@gmail.com",
            'password': "ivan@gmail.com",
            'reg_date': 10,
            'mobile': "ivan@gmail.com",
            'age': 20,
            'gender': "ivan@gmail.com",
            'rating': 1,
        },
        {
            'code': "qqqqqqq",
            'name': "Ivan",
            'surname': "ivan@gmail.com",
            'email': "ivan2@gmail.com",
            'password': "ivan@gmail.com",
            'reg_date': 10,
            'mobile': "ivan@gmail.com",
            'age': 20,
            'gender': "ivan@gmail.com",
            'rating': 1,
        },
        {
            'code': "qqqqqqq",
            'name': "Ivan",
            'surname': "ivan@gmail.com",
            'email': "ivan3@gmail.com",
            'password': "ivan@gmail.com",
            'reg_date': 10,
            'mobile': "ivan@gmail.com",
            'age': 20,
            'gender': "ivan@gmail.com",
            'rating': 1,
        }
    ]


def _check_results(domain_models_list, data_list):
    assert len(domain_models_list) == len(data_list)
    assert all([isinstance(dm, DomainModel) for dm in domain_models_list])
    assert set([dm.code for dm in domain_models_list]
               ) == set([d['code'] for d in data_list])


def test_repository_list_without_parameters(recipe_dicts):
    repo = dynamodb.Dynamodb(User)
    for i in recipe_dicts:
        repo.insert(User.from_dict(i))

    _check_results(
        repo.list(),
        recipe_dicts
    )


def test_repository_list_with_filters_unknown_key():
    repo = dynamodb.Dynamodb(User)

    with pytest.raises(ClientError):
        repo.list(filters={'unknown_key': 'an_unknown_key'})


def test_repository_list_with_filters_email(recipe_dicts):
    repo = dynamodb.Dynamodb(User)

    _check_results(
        repo.list(filters={'email': 'ivan2@gmail.com'}),
        [recipe_dicts[2]]
    )


def test_repository_list_with_wrong_item_type(recipe_dicts):
    repo = dynamodb.Dynamodb(User)
    for i in recipe_dicts:
        repo.insert(User.from_dict(i))

    with pytest.raises(TypeError):
        repo.insert("error")


# def test_repository_list_with_filters_unknown_operator(recipe_dicts):
#     repo = dynamodb.Dynamodb(User)
#
#     with pytest.raises(ValueError):
#         repo.list(filters={'user__in': [20, 30]})


# def test_repository_list_with_filters_owner(recipe_dicts):
#     repo = dynamodb.Dynamodb(User)
#
#     _check_results(
#         repo.list(filters={'owner': 60}),
#         [recipe_dicts[2]]
#     )
#
#
# def test_repository_list_with_filters_owner_eq(recipe_dicts):
#     repo = dynamodb.Dynamodb(User)
#
#     _check_results(
#         repo.list(filters={'owner__eq': 60}),
#         [recipe_dicts[2]]
#     )
#
#
# def test_repository_list_with_filters_owner_lt(recipe_dicts):
#     repo = dynamodb.Dynamodb(User)
#
#     _check_results(
#         repo.list(filters={'owner__lt': 60}),
#         [recipe_dicts[0], recipe_dicts[3]])
#
#
# def test_repository_list_with_filters_owner_gt(recipe_dicts):
#     repo = dynamodb.Dynamodb(User)
#     _check_results(
#         repo.list(filters={'owner__gt': 60}),
#         [recipe_dicts[1]]
#     )
#
#
# def test_repository_list_with_filters_duration(recipe_dicts):
#     repo = dynamodb.Dynamodb(User)
#
#     _check_results(
#         repo.list(filters={'duration': 93}),
#         [recipe_dicts[3]]
#     )
#
#
# def test_repository_list_with_filters_duration_eq(recipe_dicts):
#     repo = dynamodb.Dynamodb(User)
#     _check_results(
#         repo.list(filters={'duration__eq': 93}),
#         [recipe_dicts[3]]
#     )
#
#
# def test_repository_list_with_filters_duration_lt(recipe_dicts):
#     repo = dynamodb.Dynamodb(User)
#     _check_results(
#         repo.list(filters={'duration__lt': 60}),
#         [recipe_dicts[2]]
#     )
#
#
# def test_repository_list_with_filters_duration_gt(recipe_dicts):
#     repo = dynamodb.Dynamodb(User)
#     _check_results(
#         repo.list(filters={'duration__gt': 400}),
#         [recipe_dicts[1]]
#     )
#
#
# def test_repository_list_with_filters_rating(recipe_dicts):
#     repo = dynamodb.Dynamodb(User)
#
#     _check_results(
#         repo.list(filters={'rating': 51.39916678}),
#         [recipe_dicts[3]]
#     )
