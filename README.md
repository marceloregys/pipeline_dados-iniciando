# pipeline_dados-iniciando

Criando estrutura de pastas utilizando terminal Linux:
mkdir data_raw
mkdir data_processed
mkdir notebooks
mkdir scripts

Alimentando a base de dados:
cd data_raw
wget https://github.com/alura-cursos/Pipeline-de-dados-combinando-Python-e-orientcao-a-objeto/blob/main/data_raw/dados_empresaA.json
wget https://raw.githubusercontent.com/alura-cursos/Pipeline-de-dados-combinando-Python-e-orientcao-a-objeto/main/data_raw/dados_empresaB.csv

Criando ambiente virtual:
python -m venv .venv #. para deixar a pasta oculta 

Ativando no Windows
.venv\Scripts\activate.bat

