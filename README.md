<div>
<h2><strong>Iniciando com pipeline de Dados - Python</strong></h2>
</div>
<div>&nbsp;</div>
<div>Este projeto foi realizado com base no curso <em>Pipeline de dados: combinando Python e orienta&ccedil;&atilde;o a objeto</em> da plataforma <em>Alura</em>.</div>
<div>Neste curso projeto realizamos as seguintes a&ccedil;&otilde;es:</div>
<ul>
<li>Construimos um pipeline de dados com Python do zero;</li>
<li>Refatoramos o c&oacute;digo com orienta&ccedil;&atilde;o a objeto;</li>
<li>Transformamos dados utilizando apenas Python;</li>
<li>Aprendemos a respeito dos benef&iacute;cios de criar um pipeline reutiliz&aacute;vel;</li>
<li>Estruture c&oacute;digos Python em fun&ccedil;&otilde;es.</li>
</ul>
<div>&nbsp;</div>
<div><strong>Este projeto est&aacute; separado na seguinte estrutura:</strong></div>
<div>data_raw: Onde armazenamos os dados brutos</div>
<div>data_processed: Onde armazenamos os dados j&aacute; processados</div>
<div>notebooks: Onde criamos um arquivo de explora&ccedil;&atilde;o dos dados</div>
<div>scripts: Neta pasta criamos dois arquivos em Python, o <em>fusao_mercado_fev.py</em> que &eacute; o arquivo principal e o arquivo <em>processamento_dados.py</em>, onde criamos o objeto Dados e suas fun&ccedil;&otilde;es.</div>
<div>&nbsp;</div>
<div>
<div><strong>Criando estrutura de pastas utilizando terminal Linux:</strong></div>
<div>mkdir data_raw</div>
<div>mkdir data_processed</div>
<div>mkdir notebooks</div>
<div>mkdir scripts</div>
<br />
<div><strong>Alimentando a base de dados:</strong></div>
<div>cd data_raw</div>
<div>wget <a href="https://github.com/alura-cursos/Pipeline-de-dados-combinando-Python-e-orientcao-a-objeto/blob/main/data_raw/dados_empresaA.json">https://github.com/alura-cursos/Pipeline-de-dados-combinando-Python-e-orientcao-a-objeto/blob/main/data_raw/dados_empresaA.json</a></div>
<div>&nbsp;</div>
<div>wget <a href="https://raw.githubusercontent.com/alura-cursos/Pipeline-de-dados-combinando-Python-e-orientcao-a-objeto/main/data_raw/dados_empresaB.csv">https://raw.githubusercontent.com/alura-cursos/Pipeline-de-dados-combinando-Python-e-orientcao-a-objeto/main/data_raw/dados_empresaB.csv</a></div>
<div>&nbsp;</div>
<div><strong>Criando ambiente virtual:</strong></div>
<div>python -m venv .venv #. para deixar a pasta oculta</div>
<br />
<div><strong>Ativando venv no Windows:</strong></div>
<div>.venv\Scripts\activate.bat</div>
<div>&nbsp;</div>
<div>Pendencias:&nbsp;</div>
</div>