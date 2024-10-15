from ParsingStrategy import BeautifulSoupStrategy
from RequestFactory import RequestFactory


class ExtratorMte:
    def __init__(self, request_factory, parsing_strategy):
        self.request_factory = request_factory
        self.parsing_strategy = parsing_strategy

    def enviar_requisicao(self, data):
        response = self.request_factory.create_post_request(data)
        return self.parsing_strategy.parse(response.content)

# Configurações
url = "https://www3.mte.gov.br/sistemas/mediador/ConsultarInstColetivo/getConsultaAvancada"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
data = {
    "nrCnpj": "",
    "nrCei": "",
    "noRazaoSocial": "",
    "dsCategoria": "",
    "tpRequerimento": [
        "acordo",
        "acordoColetivoEspecificoPPE",
        "acordoColetivoEspecificoDomingosFeriados",
        "convencao",
        "termoAditivoAcordo",
        "termoAditivoConvecao",
        "termoAditivoAcordoEspecificoPPE",
        "termoAditivoAcordoEspecificoDomingoFeriado"
    ],
    "tpVigencia": "2",
    "sgUfDeRegistro": "AC",
    "dtInicioRegistro": "",
    "dtFimRegistro": "",
    "dtInicioVigenciaInstrumentoColetivo": "",
    "dtFimVigenciaInstrumentoColetivo": "",
    "tpAbrangencia": "Todos+os+tipos",
    "ufsAbrangidasTotalmente": "AC",
    "cdMunicipiosAbrangidos": "",
    "cdGrupo": "",
    "cdSubGrupo": "",
    "noTituloClausula": "",
    "utilizarSiracc": "",
    "pagina": "1",
    "qtdTotalRegistro": "665"
}

# Instanciação
request_factory = RequestFactory(url, headers)
parsing_strategy = BeautifulSoupStrategy()
extrator = ExtratorMte(request_factory, parsing_strategy)

# Envio da requisição e parsing da resposta
parsed_response = extrator.enviar_requisicao(data)
print(parsed_response)