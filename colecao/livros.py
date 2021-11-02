from urllib.request import urlopen


def consultar_livros(titulo_livro: str) -> str:
    dados = preparar_dados_para_requisicao(titulo_livro)
    url = obter_url("https://buscador", dados)
    result = executar_requisicao(url)
    return result

def preparar_dados_para_requisicao(titulo_livro: str) -> str:
    ...

def obter_url(url, dados):
    ...

def executar_requisicao(url) -> str:
    with urlopen(url, timeout=10) as resposta:
        resultado = resposta.read().decode("utf-8")

    return resultado
