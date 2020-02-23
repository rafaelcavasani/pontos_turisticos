from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from django.http import HttpResponse


class PontoTuristicoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao', 'enderecos__linha1')
    lookup_field = 'id'

    # SOBRESCREVE O METODO GET COM UM FILTRO
    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()
        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome=nome)
        if descricao:
            queryset = queryset.filter(descricao=descricao)
        return queryset

    # def list(self, request, *args, **kwargs): SOBRESCREVE O MÉTODO "GET": RETORNA 1 LISTA
    # def retrieve(self, request, *args, **kwargs): SOBRESCREVE O MÉTODO "GET": RETORNA 1 OBJETO
    # def create(self, request, *args, **kwargs): SOBRESCREVE O MÉTODO "POST"
    # def destroy(self, request, *args, **kwargs): SOBRESCREVE O MÉTODO "DELETE"
    # def update(self, request, *args, **kwargs): SOBRESCREVE O MÉTODO "PUT"
    # def partial_update(self, request, *args, **kwargs): SOBRESCREVE O MÉTODO "PATCH"

    @action(methods=['post'], detail=True)
    def denunciar(self, request, pk=None):
        ponto_turistico = PontoTuristico.objects.filter(pk=pk)
        return ponto_turistico

    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, id):
        atracoes = request.data['ids']
        
        ponto = PontoTuristico.objects.get(id=pk)
        ponto.atracoes.set(atracoes)
        ponto.save()
        return HttpReponse('ok')

