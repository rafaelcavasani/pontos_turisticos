from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    # SOBRESCREVE O METODO GET COM UM FILTRO
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    # def list(self, request, *args, **kwargs): SOBRESCREVE O MÉTODO "GET": RETORNA 1 LISTA
    # def retrieve(self, request, *args, **kwargs): SOBRESCREVE O MÉTODO "GET": RETORNA 1 OBJETO
    # def create(self, request, *args, **kwargs): SOBRESCREVE O MÉTODO "POST"
    # def destroy(self, request, *args, **kwargs): SOBRESCREVE O MÉTODO "DELETE"
    # def update(self, request, *args, **kwargs): SOBRESCREVE O MÉTODO "PUT"
    # def partial_update(self, request, *args, **kwargs): SOBRESCREVE O MÉTODO "PATCH"