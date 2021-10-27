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
    return "3erg"
