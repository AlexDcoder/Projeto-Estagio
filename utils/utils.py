import pandas as pd
import random
from datetime import datetime, timedelta


def gerar_notas_fiscais_ficticias(numero_registros, produtos, emitentes, destinatarios, data_inicial="2023-01-01"):
    """
    Gera uma tabela fictícia de notas fiscais com dados aleatórios.

    Parâmetros:
    - numero_registros: Número de registros na tabela.
    - produtos: Lista de dicionários com produtos (chaves: 'Codigo', 'Descricao', 'ValorUnitario').
    - emitentes: Lista de dicionários com emitentes (chaves: 'CNPJ', 'RazaoSocial').
    - destinatarios: Lista de dicionários com destinatários (chaves: 'CNPJ', 'RazaoSocial').
    - data_inicial: Data inicial para emissão das notas (formato YYYY-MM-DD).

    Retorna:
    - Um DataFrame pandas com os dados gerados.
    """
    data_inicial = datetime.strptime(data_inicial, "%Y-%m-%d")
    dados_notas = []

    for i in range(numero_registros):
        emitente = random.choice(emitentes)
        destinatario = random.choice(destinatarios)
        produto = random.choice(produtos)
        quantidade = random.randint(1, 50)
        valor_total = quantidade * produto["ValorUnitario"]
        aliquota_icms = 18.0  # Em percentual
        valor_icms = valor_total * (aliquota_icms / 100)
        aliquota_ipi = 10.0  # Em percentual
        valor_ipi = valor_total * (aliquota_ipi / 100)

        nota = {
            "NumeroNF": f"NF-{i+1:06d}",
            "DataEmissao": (data_inicial + timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d"),
            "CNPJEmitente": emitente["CNPJ"],
            "RazaoSocialEmitente": emitente["RazaoSocial"],
            "CNPJDestinatario": destinatario["CNPJ"],
            "RazaoSocialDestinatario": destinatario["RazaoSocial"],
            "CodigoProduto": produto["Codigo"],
            "DescricaoProduto": produto["Descricao"],
            "Quantidade": quantidade,
            "UnidadeMedida": "UN",
            "ValorUnitario": produto["ValorUnitario"],
            "ValorTotal": valor_total,
            "CFOP": "5405",
            "AliquotaICMS": aliquota_icms,
            "ValorICMS": valor_icms,
            "AliquotaIPI": aliquota_ipi,
            "ValorIPI": valor_ipi,
        }
        dados_notas.append(nota)

    return pd.DataFrame(dados_notas)


def gerar_produtos_aleatorios(qtd=10):
    """
    Gera uma lista de produtos aleatórios.

    Parâmetros:
    - qtd: Número de produtos a serem gerados.

    Retorna:
    - Lista de dicionários com os produtos.
    """
    nomes_bebidas = [
        "Whiskey Jack Daniels", "Vodka Absolut", "Gin Tanqueray",
        "Rum Bacardi", "Tequila Jose Cuervo", "Cerveja Heineken",
        "Espumante Chandon", "Whiskey Jameson", "Whiskey Chivas Regal",
        "Cachaça 51", "Licores Amarula", "Whiskey Ballantine's"
    ]
    produtos = []
    for i in range(qtd):
        nome = random.choice(nomes_bebidas)
        valor_unitario = round(random.uniform(5.0, 300.0), 2)
        produto = {
            "Codigo": f"{1000 + i}",
            "Descricao": nome,
            "ValorUnitario": valor_unitario
        }
        produtos.append(produto)
    return produtos


def gerar_emitentes_aleatorios(qtd=5):
    """
    Gera uma lista de emitentes aleatórios.

    Parâmetros:
    - qtd: Número de emitentes a serem gerados.

    Retorna:
    - Lista de dicionários com os emitentes.
    """
    nomes_empresas = [
        "Distribuidora Nacional LTDA", "Whiskey Premium Brasil SA",
        "Bebidas do Sul LTDA", "Exportadora de Destilados SA",
        "Comercial de Bebidas Norte LTDA"
    ]
    emitentes = []
    for i in range(qtd):
        nome = random.choice(nomes_empresas)
        cnpj = f"{random.randint(
            10_000_000, 99_999_999):08d}/{random.randint(1, 999):04d}-{random.randint(1, 99):02d}"
        emitente = {"CNPJ": cnpj, "RazaoSocial": nome}
        emitentes.append(emitente)
    return emitentes


def gerar_destinatarios_aleatorios(qtd=5):
    """
    Gera uma lista de destinatários aleatórios.

    Parâmetros:
    - qtd: Número de destinatários a serem gerados.

    Retorna:
    - Lista de dicionários com os destinatários.
    """
    nomes_empresas = [
        "Empório Bebidas LTDA", "Supermercado Econômico SA",
        "Adega do Norte LTDA", "Casa das Bebidas SA",
        "Mercado Bebidas Premium LTDA"
    ]
    destinatarios = []
    for i in range(qtd):
        nome = random.choice(nomes_empresas)
        cnpj = f"{random.randint(
            10_000_000, 99_999_999):08d}/{random.randint(1, 999):04d}-{random.randint(1, 99):02d}"
        destinatario = {"CNPJ": cnpj, "RazaoSocial": nome}
        destinatarios.append(destinatario)
    return destinatarios


# Exemplos de uso
produtos = gerar_produtos_aleatorios(15)
emitentes = gerar_emitentes_aleatorios(5)
destinatarios = gerar_destinatarios_aleatorios(5)

# Gerar dados fictícios
df = gerar_notas_fiscais_ficticias(
    numero_registros=100000,
    produtos=produtos,
    emitentes=emitentes,
    destinatarios=destinatarios
)

# Salvar em arquivo CSV ou Excel
df.to_csv("notas_fiscais_exemplo.csv", index=False, sep=";")
# df.to_excel("notas_fiscais_exemplo.xlsx")
