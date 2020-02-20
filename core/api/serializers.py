from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from enderecos.api.serializers import EnderecoSerializer

class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    enderecos = EnderecoSerializer()
    descricao_completa = SerializerMethodField()

    class Meta():
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'atracoes', 'comentarios', 'avaliacoes', 'enderecos', 'descricao_completa')

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)