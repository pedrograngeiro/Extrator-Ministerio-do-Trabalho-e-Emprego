import json
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
with open('data.json', 'r') as file:
    data = json.load(file)

total_registros = int(data['qtdTotalRegistro'])
total_paginas = total_registros // 10 + 1
estado = 'MG'
# Loop para percorrer todas as páginas
for i in range(1, total_paginas + 1):
    # Alterar o valor do atributo "pagina"
    data['sgUfDeRegistro'] = estado
    data['ufsAbrangidasTotalmente'] = estado
    data['pagina'] = f"{i}"
    print(f"Extraindo dados da página {i} de {total_paginas}...")


    # Instanciação
    request_factory = RequestFactory(url, headers)
    parsing_strategy = BeautifulSoupStrategy()
    extrator = ExtratorMte(request_factory, parsing_strategy)

    # Envio da requisição e parsing da resposta
    try:
        parsed_response = extrator.enviar_requisicao(data)
        rows_with_indice = parsed_response.find_all('tr', {'indice': True})
    except Exception as e:
        print(f"Erro ao extrair dados da página {i}: {e}")
        continue

    # Salvar os índices em um arquivo
    nomeArquivo = ("indices{}.txt").format(estado)
    with open(nomeArquivo, 'a') as file:
        for row in rows_with_indice:
            indice_value = row['indice']
            file.write(indice_value + '\n')

