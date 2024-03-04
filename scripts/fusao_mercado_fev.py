from processamento_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# Extract

dados_empresaA = Dados(path_json, 'json')
print(dados_empresaA.dados)
print(dados_empresaA.qdt_linhas)

dados_empresaB = Dados(path_json, 'csv')
print(dados_empresaB.dados)
print(dados_empresaB.qdt_linhas)


# Transform

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(dados_empresaB.nome_colunas)

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(dados_fusao)

# Load

path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(path_dados_combinados)