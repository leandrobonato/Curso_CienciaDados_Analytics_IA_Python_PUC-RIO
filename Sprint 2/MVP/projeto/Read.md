MVP PUC-RIO - Engenharia de Dados

Autor: Leandro Miozzo Bonato





Título: Emissão de CO² no planeta





1. Introdução

Com base nos grandes problemas climáticos atuais, este é um projeto aberto de coleta de alguns dados públicos encontrados na internet para tentar entender a emissão de dióxido carbono (CO²) no mundo, sendo explorado a evolução disso nos últimos anos, setores, países e continentes que mais possuem emissões de carbonos, e tentar responder uma das perguntas que mais gera debates no planeta.





O que será do futuro da humanidade quanto ao meio ambiente?





2\. Objetivos

Esta pergunta é muito ampla para ser respondida, e poderíamos escrever inúmeras páginas de livros para tentar (talvez nem conseguir) responder de forma definitiva, então para este projeto foi dividido em novas pequenas perguntas que podem ser respondidas com os dados públicos coletados, e com isso, chegar em uma breve conclusão sobre alguns dos problemas que o nosso planeta enfrenta e como entender e poder ajudar de alguma forma.



2.1. Neste século (2001 à 2100) a emissão de carbono no planeta.

2.1.1. Qual foi a emissão de carbono no planeta por ano?

2.1.2. Qual foi a emissão de carbono no planeta por década?



2.2. Emissão de carbono no planeta por país.

2.2.1. Qual foi a emissão de carbono no planeta por país por ano?

2.2.2. Qual foi a emissão de carbono no planeta por país por década?



2.3. Emissão de carbono no planeta por continente.

2.3.1. Qual foi a emissão de carbono no planeta por continente por ano?

2.3.2. Qual foi a emissão de carbono no planeta por continente por década?



2.4. Sobre alguns dados coletados estarem negativos.

2.4.1 Quais são os países que possuem emissão negativa?

2.4.2 Quais são os continentes que possuem emissão negativa? 4.3 Quais são os anos que possuem emissão negativa?

2.4.4 Quais são as décadas que possuem emissão negativa?



2.5. Sobre o efeito estufa.

2.5.1. Quais são os países que contribuíram para diminuir o efeito estufa?

2.5.2. Quais são os continentes que contribuíram para diminuir o efeito estufa?

2.5.3. Quais são os anos que contribuíram para diminuir o efeito estufa?

2.5.4. Quais são as décadas que contribuíram para diminuir o efeito estufa?



2.6. Sobre projeções.

2.6.1. Qual é a projeção de emissão de carbono no planeta por ano?

2.6.2. Qual é a projeção de emissão de carbono no planeta por década?

2.6.3. Qual é a projeção de emissão de carbono no planeta por país?

2.6.4. Qual é a projeção de emissão de carbono no planeta por continente?

2.6.5. Qual é a projeção de emissão de carbono no planeta por país por ano?

2.6.6. Qual é a projeção de emissão de carbono no planeta por continente por ano?

2.6.7. Qual é a projeção de emissão de carbono no planeta por país por década?



2.7. Sobre o crédito de carbono.

2.7.1. O que é o crédito de carbono?

2.7.2. Como ele poderá ajudar a diminuir o efeito estufa?

2.7.3. Quem patrocina o crédito de carbono?





3\. Dados Coletados

As seguintes fontes de dados foram usadas para a coleta dos dados, são elas: Carbon Monitor, Climate Watch (CW), International Energy Agency (IEA), National Aeronautics and Space Administration (NASA), Organização das Nações Unidas (ONU), Our World in Data, World Bank Group.



Todas as organizações listadas anteriormente, possuem dados públicos que foram cuidadosamente baixados, interpretados e verificados para a organização deste projeto. Abaixo os links para dos dados.



3.1. Carbon Monitor: https://carbonmonitor.org

Único link para a fonte de dados, que já está compilado em um único arquivo: https://datas.carbonmonitor.org/API/downloadFullDataset.php?source=carbon\_global



3.2. Climate Watch: https://www.climatewatchdata.org

Link para download da fonte de dados: https://www.climatewatchdata.org/data-explorer/historical-emissions?historical-emissions-data-sources=climate-watch\&historical-emissions-gases=all-ghg\&historical-emissions-regions=All%20Selected\&historical-emissions-sectors=total-including-lucf%2Ctotal-including-lucf\&page=1

\*\* Ao clicar no link da fonte de dados será direcionado para um cadastro de newslatter, bem simples, assim que feito o download o arquivo zip, o mesmo terá outros arquivos e com isso vários arquivos CSV´s e XLS´s. Neste repositório foram convertidos os arquivos XLS´s para CSV´s, um para cada aba do seu respectivo XLSX.



3.3. International Energy Agency (IEA): https://www.iea.org

Link para download direto, onde será um arquivo XLSX e terá que fazer um cadastro gratuito no site para conseguir realizar o download da fonte de dados: https://www.iea.org/data-and-statistics/data-product/global-energy-review-co2-emissions-in-2021#

\*\* A observação da fonte de dados baixada é de as informações serem de 2019 à 2021 e apenas informações de alguns países, mundo, a quantidade de emissão do ano em metros de CO2, e a taxa de crescimento comparada com o ano anterior.



3.4. National Aeronautics and Space Administration (NASA): https://data.nasa.gov/dataset/

Link para download direto: https://acdisc.gsfc.nasa.gov/data/CMS/CMSFluxTotal.3

\*\* Os passsos são:

1\. Clique em Once Registered, you can click here.

2\. Caso não tenha um cadastro, crie um.

3\. Depois realize o login

4\. Volte na página do link direto para download

5\. Clique no arquivo CMSFluxTotal201001\_202212\_v3.nc

6\. Baixe o arquivo.

\*\*\* Os arquivos da NASA possuem mais de 500 mb, e o GitHub não aceita tais arquivos, então pra isso foi feito um algoritmo para separá-los em arquivos menores com no máximo 50 mb cada um. 



3.5. Organização das Nações Unidas (ONU): https://unfccc.int/

Link para os DataSets: https://di.unfccc.int/time\_series

\*\* São vários datasets e conforme vai navegando poderá ir baixando os dados, exemplo, se clicar em Flexible Queries > Preencher todas as informações relacionadas à carbbono (em inglês Carbon) ou CO² mostrará então um relatório em tabela para exportar para CSV, ou em Time Series - Annex I, poderá ir filtrando as informações relacionadas com estas palavras-chaves e então modificando o resultado da consulta da tabela, e com isso exportar para XLSX e posteriormente converter para CSV.



3.6. Our World in Data: https://ourworldindata.org

Link para os dados: https://ourworldindata.org/search?q=co2

\*\* Pesquisar por CO2 e então os que foram feitos downloads foram as seguintes informações:

 - CO₂ emissions per capita

 - Annual CO₂ emissions

 - Annual concentration of atmospheric carbon dioxide

 - Annual CO₂ emissions by world region

 - Share of global CO₂ emissions

 - Cumulative CO₂ emissions

 - Cumulative CO₂ emissions by world region

 - Share of global cumulative CO₂ emissions

 - Carbon dioxide emissions factors



3.7. World Bank Group: https://www.worldbank.org

Link para a fonte de dados: um dos arquivos está contido nesta página, e é XLSX, e a mesma foi aberta e convertida para CSV https://carbonpricingdashboard.worldbank.org/sites/default/files/carbon-pricing-dashboard-data/data\_08\_2025.xlsx



3.8. Explicação final dos arquivos e de todos os processamentos

3.8.1. Todos os arquivos estarão dentro de uma pasta com o nome da instituição / organização.

3.8.2. Os arquivos estarão no repositório do github na subpasta Data.

3.8.3. Cada organização / instituição tem uma forma de arquivar as informações e os dados, portanto, cada arquivo CSV tem uma formatação diferente, desta forma, cada pasta terá uma documentação explicando cada arquivo ali contido, onde será uma explicação breve e com todos os campos dos arquivos CSV, isso incluí até mesmo se a organização disponibiliza uma documentação oficial, a mesma será feita com um novo formato para estar mais legível.

3.8.4. Muitos dados não serão usados até o final do projeto, porém terão alguma explicação para este acontecimento.

3.8.5. Nos links disponibilizados para realizar o download dos arquivos, foi encontrado muitos arquivos com outros formatos, como o XLSX que por si só já possuí um conversor para CSV, entretanto foi encontrado também arquivos com o formato NC, que é um formato de dados de processamento pelo Python, desta forma foi criado um algoritmo em Python para realizar a leitura, conversão e a junção destes arquivos em um único arquivo CSV.



Conclusão

Para responder à pergunta "O que será do futuro da humanidade quanto ao meio ambiente?", deve-se imediatamente entender que não é apenas a emissão de carbono que está envolvida no impacto ambiental, mas com muitap pesquisa para este projeto entendemos que há muito mais que carbono, sendo alguns: gás metano, queima de combústiveis fósseis, desmatamento e o não plantio e preservação da natureza, agropecuária, processos indústriais, uso de fertilizantes, estilo de vida e consumo, transportes, entre muitos outros fatores unidos à esses mencionados e não mencionados.



Entretanto, sendo um dos principais vilões, o dióxido de carbono é: .....



Conclusão final, entendi nesse tema uma única pessoa tem um poder enorme de mudar muita coisa, e melhorar o mundo em que vivemos muito exponencialmente, veja os dados de produção de dióxido de carbono por pessoa, e não apenas plantando uma árvore em algum lugar qualquer, mas sim que com mais estudos (não sobre meio ambiente) sobre tecnologia, poderemos fazer mais e mais com muito menos, veja a pecuária de produção de leite dos Estados Unidos, conseguem produzir muito mais leite que o Brasil, que é o segundo colocado, e com muito menos vacas e consequentemente produzindo menos gás metano. Com isso, podemos concluir que é puro estudos e pura tecnologia que os favorecem.

