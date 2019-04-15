import pytest

from grow_easily_server.shared.domain_model import DomainModel
from grow_easily_server.repository import memrepo


@pytest.fixture
def recipe_dicts():
    return [
        {
            'code': 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
            'duration': 215,
            'owner': 39,
            'name': -0.09998975,
            'rating': 51.75436293,
            'items': '',
        },
        {
            'code': 'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
            'duration': 405,
            'owner': 66,
            'name': 0.18228006,
            'rating': 51.74640997,
            'items': '',
        },
        {
            'code': '913694c6-435a-4366-ba0d-da5334a611b2',
            'duration': 56,
            'owner': 60,
            'name': 0.27891577,
            'rating': 51.45994069,
            'items': '',
        },
        {
            'code': 'eed76e77-55c1-41ce-985d-ca49bf6c0585',
            'duration': 93,
            'owner': 48,
            'name': 0.33894476,
            'rating': 51.39916678,
            'items': '',
        }
    ]


def _check_results(domain_models_list, data_list):
    assert len(domain_models_list) == len(data_list)
    assert all([isinstance(dm, DomainModel) for dm in domain_models_list])
    assert set([dm.code for dm in domain_models_list]
               ) == set([d['code'] for d in data_list])


def test_repository_list_without_parameters(recipe_dicts):
    repo = memrepo.MemRepo(recipe_dicts)

    _check_results(
        repo.list(),
        recipe_dicts
    )


def test_repository_list_with_filters_unknown_key(recipe_dicts):
    repo = memrepo.MemRepo(recipe_dicts)

    with pytest.raises(KeyError):
        repo.list(filters={'unknown_key': 'an_unknown_key'})


def test_repository_list_with_filters_unknown_operator(recipe_dicts):
    repo = memrepo.MemRepo(recipe_dicts)

    with pytest.raises(ValueError):
        repo.list(filters={'owner__in': [20, 30]})


def test_repository_list_with_filters_owner(recipe_dicts):
    repo = memrepo.MemRepo(recipe_dicts)

    _check_results(
        repo.list(filters={'owner': 60}),
        [recipe_dicts[2]]
    )


def test_repository_list_with_filters_owner_eq(recipe_dicts):
    repo = memrepo.MemRepo(recipe_dicts)

    _check_results(
        repo.list(filters={'owner__eq': 60}),
        [recipe_dicts[2]]
    )


def test_repository_list_with_filters_owner_lt(recipe_dicts):
    repo = memrepo.MemRepo(recipe_dicts)

    _check_results(
        repo.list(filters={'owner__lt': 60}),
        [recipe_dicts[0], recipe_dicts[3]])


def test_repository_list_with_filters_owner_gt(recipe_dicts):
    repo = memrepo.MemRepo(recipe_dicts)
    _check_results(
        repo.list(filters={'owner__gt': 60}),
        [recipe_dicts[1]]
    )


def test_repository_list_with_filters_duration(recipe_dicts):
    repo = memrepo.MemRepo(recipe_dicts)

    _check_results(
        repo.list(filters={'duration': 93}),
        [recipe_dicts[3]]
    )


def test_repository_list_with_filters_duration_eq(recipe_dicts):
    repo = memrepo.MemRepo(recipe_dicts)
    _check_results(
        repo.list(filters={'duration__eq': 93}),
        [recipe_dicts[3]]
    )


def test_repository_list_with_filters_duration_lt(recipe_dicts):
    repo = memrepo.MemRepo(recipe_dicts)
    _check_results(
        repo.list(filters={'duration__lt': 60}),
        [recipe_dicts[2]]
    )


def test_repository_list_with_filters_duration_gt(recipe_dicts):
    repo = memrepo.MemRepo(recipe_dicts)
    _check_results(
        repo.list(filters={'duration__gt': 400}),
        [recipe_dicts[1]]
    )


def test_repository_list_with_filters_rating(recipe_dicts):
    repo = memrepo.MemRepo(recipe_dicts)

    _check_results(
        repo.list(filters={'rating': 51.39916678}),
        [recipe_dicts[3]]
    )


def test_repository_list_with_filters_code(recipe_dicts):
    repo = memrepo.MemRepo(recipe_dicts)

    _check_results(
        repo.list(filters={'code': '913694c6-435a-4366-ba0d-da5334a611b2'}),
        [recipe_dicts[2]]
    )
