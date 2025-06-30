# Pipeline de Fusão de Dados de Empresas

Este repositório contém um projeto de processamento e fusão de dados de duas empresas fictícias, utilizando arquivos JSON e CSV, com objetivo de unificar as informações de produtos de diferentes fontes.

## Estrutura do Projeto

```
├── data_raw/
│   ├── dados_empresaA.json
│   └── dados_empresaB.csv
├── data_processed/
│   └── dados_combinados.csv
├── processamento_dados.py
├── fusao_mercado_fev.py
├── exploration.ipynb
└── README.md
```

## Descrição dos Arquivos

- `dados_empresaA.json`: Dados no formato JSON da Empresa A.
- `dados_empresaB.csv`: Dados no formato CSV da Empresa B.
- `processamento_dados.py`: Contém a classe `Dados`, responsável por leitura, transformação, renomeação e exportação de dados.
- `fusao_mercado_fev.py`: Script que executa a leitura, renomeação, fusão e exportação dos dados combinados.
- `exploration.ipynb`: Notebook Jupyter para exploração dos dados.
- `dados_combinados.csv`: Resultado final da fusão dos dados das empresas.

## Como Executar

1. Certifique-se de que os arquivos da pasta `data_raw/` estão corretamente posicionados.
2. Execute o script `fusao_mercado_fev.py` para gerar o arquivo de saída combinado.
```bash
python fusao_mercado_fev.py
```

## Dependências

- Python 3.10+
- Nenhuma biblioteca externa é necessária (usa apenas módulos nativos: `json`, `csv`, `logging`)

## Observações

- As colunas do arquivo CSV são renomeadas para se unificar com as do JSON antes da fusão.
- O arquivo de saída é salvo em `data_processed/dados_combinados.csv`.

## Autor

Projeto desenvolvido como exercício de integração de dados.
