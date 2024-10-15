"""https://www3.mte.gov.br/sistemas/mediador/consultarinstcoletivo"""
# Importações
import requests

class ExtratorMte:
    def __init__(self):
        self.url = "https://www3.mte.gov.br/sistemas/mediador/consultarinstcoletivo"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

    def enviar_requisicao(self, data):
        response = requests.post(self.url, headers=self.headers, data=data)
        return response

extrator = ExtratorMte()
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
response = extrator.enviar_requisicao(data)
print(response.status_code)
print(response.text)