import logging
from processamento_dados import Dados


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'


dados_empresaA = Dados(path_json, 'json')
logging.info(f'Extraindo as colunas da empresa A com {dados_empresaA.qtd_linhas} linhas.')
logging.info(f'Colunas da Empresa A:\n{dados_empresaA.nome_colunas}')


dados_empresaB = Dados(path_csv, 'csv')
logging.info(f'Extraindo as colunas da empresa B com {dados_empresaB.qtd_linhas} linhas.')
logging.info(f'Colunas da Empresa B:\n{dados_empresaB.nome_colunas}')


key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

logging.info('Renomeando as colunas da Empresa B...')
dados_empresaB.rename_columns(key_mapping)
logging.info(f'Colunas da Empresa B após renomeação:\n{dados_empresaB.nome_colunas}')


dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
logging.info(f'Dados combinados. Total de linhas: {dados_fusao.qtd_linhas}')


path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
logging.info(f'Dados combinados salvos com sucesso em: {path_dados_combinados}')
