from grow_easily_server.shared import use_case as uc
from grow_easily_server.shared import response_object as res


class RecipeListUseCase(uc.UseCase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        domain_recipe = self.repo.list(filters=request_object.filters)
        return res.ResponseSuccess(domain_recipe)
