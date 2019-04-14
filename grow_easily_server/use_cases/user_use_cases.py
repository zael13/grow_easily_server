from grow_easily_server.domain import user
from grow_easily_server.shared import use_case as uc
from grow_easily_server.shared import response_object as res


class UserListUseCase(uc.UseCase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        domain_item = self.repo.list(filters=request_object.filters)
        return res.ResponseSuccess(domain_item)


class UserAddUseCase(uc.UseCase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        domain_item = self.repo.list(filters={'email': request_object.filters['email']})
        if not domain_item:
            self.repo.insert(user.User.from_dict(request_object.filters))
            return res.ResponseSuccess(value="User has been successfully created")

        return res.ResponseFailure(type_=res.ResponseFailure.PARAMETERS_ERROR,
                                   message="Such user is already exist")
