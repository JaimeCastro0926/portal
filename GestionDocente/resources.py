from import_export import resources
from .models import Historico

class bd_historico(resources.ModelResource):
    class Mesta:
        model = Historico