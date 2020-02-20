from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao', 'enderecos__linha1')
    lookup_field = 'nome'

    # SOBRESCREVE O METODO GET COM UM FILTRO
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    # def list(self, request, *args, **kwargs): SOBRESCREVE O MÉTODO "GET": RETORNA 1 LISTA
    # def retrieve(self, request, *args, **kwargs): SOBRESCREVE O MÉTODO "GET": RETORNA 1 OBJETO
    # def create(self, request, *args, **kwargs): SOBRESCREVE O MÉTODO "POST"
    # def destroy(self, request, *args, **kwargs): SOBRESCREVE O MÉTODO "DELETE"
    # def update(self, request, *args, **kwargs): SOBRESCREVE O MÉTODO "PUT"
    # def partial_update(self, request, *args, **kwargs): SOBRESCREVE O MÉTODO "PATCH"