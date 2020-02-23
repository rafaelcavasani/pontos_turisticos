from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from core.models import PontoTuristico, DocIdentificacao
from atracoes.models import Atracao
from enderecos.models import Endereco
from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from enderecos.api.serializers import EnderecoSerializer


class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    # comentarios = ComentarioSerializer(many=True)
    # avaliacoes = AvaliacaoSerializer(many=True)
    enderecos = EnderecoSerializer()
    descricao_completa = SerializerMethodField()
    doc_identificacao = DocIdentificacaoSerializer()

    class Meta():
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao', 'atracoes', 'comentarios', 'avaliacoes',
            'enderecos', 'descricao_completa', 'doc_identificacao'
        )
        read_only_fields = ('comentarios', 'avaliacoes')
    
    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']
        
        endereco = validated_data['enderecos']
        del validated_data['enderecos']

        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        
        doc_identificacao = DocIdentificacao.objects.create(**doc)
        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)
        end = Endereco.objects.create(**endereco)
        ponto.enderecos = end
        ponto.doc_identificacao = doc_identificacao
        ponto.save()

        return ponto

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)