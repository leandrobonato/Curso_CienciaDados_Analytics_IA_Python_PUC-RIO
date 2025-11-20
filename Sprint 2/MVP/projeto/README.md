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

3.1.1. Único link para a fonte de dados, que já está compilado em um único arquivo: https://datas.carbonmonitor.org/API/downloadFullDataset.php?source=carbon\_global



3.1.2. Local no repositório de arquivos coletados: 

\\projeto\\Data\\Carbon Monitor\\



3.1.3. Arquivos de dados

3.1.3.1. carbonmonitor-global\_datas\_2025-11-18.csv



3.1.4. Documentação dos campos: 

3.1.4.1. Country / País - refere-se ao país da informação

3.1.4.2. Date / Data - refere-se à data no formato: DD/MM/YYYY que o dado foi coletado

3.1.4.3. Sector / Setor - refere-se ao setor da informação	

3.1.4.4. Value / Valor - refere-se ao valor de CO2 emitidos por dia em metros

3.1.4.5  Há um país no final de cada dia que chama-se WORLD que irá servir para se referir à quantidade de emissão de CO2 no mundo inteiro para o respectivo dia





3.2. Climate Watch: https://www.climatewatchdata.org

3.2.1. Link para download da fonte de dados: 

https://www.climatewatchdata.org/data-explorer/historical-emissions?historical-emissions-data-sources=climate-watch\&historical-emissions-gases=all-ghg\&historical-emissions-regions=All%20Selected\&historical-emissions-sectors=total-including-lulucf\&page=1

3.2.1.1. Clique em Download Bulk Data

3.2.1.2. Baixe dois arquivos, sendo eles: Agriculture Profile e GHG Emissions

3.2.1.3. Ao clicar nos links das fontes de dados será direcionado para um cadastro de newslatter, bem simples, basta preencher o cadastro e o download será iniciado.

3.2.1.4. Ainda na tela de historical emissions, faça os seguintes filtros para realizar o donwload de todo o histórico de emissões de gás de dióxido de carbono:

3.2.1.4.1. Data Sources - All Selected

3.2.1.4.2. Parties and Regions - All Selected

3.2.1.4.3. Sectors - All Selected

3.2.1.4.4. Gases - CO2

3.2.1.4.5. Start Year - 1950

3.2.1.4.6. End Year - 2023

3.2.1.4.7. Bem abaixo do gráfico há um botão chamado: Download Historical Data, clique para realizar o download.



3.2.2. Local no repositório de arquivos coletados: 

\\projeto\\Data\\Climate Watch\\



3.2.3. Arquivos de dados



3.2.3.1. CW\_Agriculture\_area.csv

3.2.3.1.1. Documentação dos campos

3.2.3.1.1.1. Area - Sigla do país

3.2.3.1.1.2. Short Name - nome curto do tipo dado ou sigla do campo nas referências, com referência de valor de: 1000 ha (hectares)

3.2.3.1.1.2.1. share\_in\_agricultural\_area\_1 - Arable land - Terra arável

3.2.3.1.1.2.2. share\_in\_agricultural\_area\_2 - Permanent cropland - Terras agrícolas permanentes

3.2.3.1.1.2.3. share\_in\_agricultural\_area\_3 - Permanent meadows and pastures  prados e pastagens permanentes

3.2.3.1.1.2.4. share\_in\_land\_area\_1 - Total Land Area - área total do terreno

3.2.3.1.1.2.5. share\_in\_land\_area\_2 - Share in Land Area, Agricultura Area - área agrícola do terreno compartilhada

3.2.3.1.1.2.6. share\_in\_land\_area\_3 - Share in Land Area, Other Land - outras áreas do terreno compartilhada

3.2.3.1.1.2.7. share\_in\_land\_area\_4 - Share in Land Area, Forest - áreas do terreno compartilhada com florestas

3.2.3.1.1.3. Years - Anos - estará os valores de anos no restantes das colunas com os dados da quantidade de hectares dividido por 1000 ha  



3.2.3.2. CW\_Agriculture\_emissions.csv

3.2.3.2.1. Documentação dos campos

3.2.3.2.1.1. Area - Sigla do país

3.2.3.2.1.2. Short Name - nome curto do tipo dado ou sigla do campo nas referências, aqui é para a intensidade de emissões agrícolas e a referências de valores de: kg CO2eq/kg de produto

3.2.3.2.1.2.1. emission\_intensity\_cereals - Cereals excluding rice - Cereais (excluindo arroz) 

3.2.3.2.1.2.2. emission\_intensity\_rice - Rice paddy - arrozal

3.2.3.2.1.2.3. emission\_intensity\_meat\_cattle - Meat cattle - Carne de Gado

3.2.3.2.1.2.4. emission\_intensity\_meat\_goat - Meat goat - Carne de cabra 

3.2.3.2.1.2.5. emission\_intensity\_meat\_chicken - Meat chicken - Carne de frango

3.2.3.2.1.2.6. emission\_intensity\_meat\_pig - Meat pig - Carne de porco

3.2.3.2.1.2.7. emission\_intensity\_meat\_buffalo - Meat Buffalo - Carne de búfalo

3.2.3.2.1.2.1. emission\_intensity\_meat\_sheep - Meat Sheep - Carne de ovelha

3.2.3.2.1.2.2. emission\_intensity\_milk\_cow - Milk Cow - Leite de vaca

3.2.3.2.1.2.3. emission\_intensity\_milk\_goat - Milk Goat - Leite de cabra

3.2.3.2.1.2.4. emission\_intensity\_milk\_buffalo - Milk Buffalo - Leite de búfalo

3.2.3.2.1.2.5. emission\_intensity\_milk\_sheep - Milk Sheep - Leite de ovelha

3.2.3.2.1.2.6. emission\_intensity\_milk\_camel - Milk Camel - Leite de camelo

3.2.3.2.1.2.7. emission\_intensity\_eggs - Eggs - Ovos

3.2.3.2.1.3. Years - Anos - estará os valores de anos no restantes das colunas com os dados da quantidade de kg CO2eq/kg de produto



3.2.3.3. CW\_Agriculture\_employment.csv

3.2.3.3.1. Documentação dos campos

3.2.3.3.1.1. Area - Sigla do país

3.2.3.3.1.2. Short Name - nome curto do tipo dado para empregados/funcionários/colaboradores nas áreas agrícolas com os valores de referência em percentual

3.2.3.3.1.2.1. employment\_agri\_female - % of female employment - porcentagem de mulheres trabalhando

3.2.3.3.1.2.2. employment\_agri\_male - % of male employment - porcentagem de homens trabalhando

3.2.3.3.1.2.3. employment\_agri\_total - % of total employment - porcentagem total trabalhando

3.2.3.3.1.3. Years - Anos - estará os valores de anos no restantes das colunas com os dados percentuais



3.2.3.4. CW\_Agriculture\_meat\_consumption.csv

3.2.3.4.1. Documentação dos campos

3.2.3.4.1.1. Area - Sigla do país

3.2.3.4.1.2. Short Name - nome curto do tipo dado para de consumo de carne com os valores de referência em: 1000 t (toneladas) ou quilogramas per capita

3.2.3.4.1.2.1. meat\_consumption\_1 - Beef - carne de gado

3.2.3.4.1.2.2. meat\_consumption\_2 - Pork - carne de porco

3.2.3.4.1.2.3. meat\_consumption\_3 - Poultry - carne de aves

3.2.3.4.1.2.3. meat\_consumption\_4 - Sheep - carne de ovelha 

3.2.3.4.1.2.1. meat\_consumption\_per\_capita\_1 - Beef - carne de gado

3.2.3.4.1.2.2. meat\_consumption\_per\_capita\_2 - Pork - carne de porco

3.2.3.4.1.2.3. meat\_consumption\_per\_capita\_3 - Poultry - carne de aves

3.2.3.4.1.2.3. meat\_consumption\_per\_capita\_4 - Sheep - carne de ovelha

3.2.3.4.1.3. Years - Anos - estará os valores de anos no restantes das colunas com os dados percentuais



3.2.3.5. CW\_Agriculture\_pesticides\_fertilizers.csv

3.2.3.5.1. Documentação dos campos

3.2.3.5.1.1. Area - Sigla do país

3.2.3.5.1.1. Source - Código do FAOSTAT, que condiz o tipo de fertilizante, herbicida, pesticida e outros agrotóxicos que podem influenciar nos alimentos, conforme a Organização Mundial de Alimentos e Agricultura das Nações Unidas (fonte: https://www.fao.org/home/en)

3.2.3.5.1.2. Short Name - tipo do agrotóxico do dado, podendo ser pesticidas ou fertilizantes com valores em t (toneladas)

3.2.3.5.1.2.3. total\_fertilizers - Total Fertilizers - Uso total de fertilizantes na agricultura (N, P2O5, K2O)

3.2.3.5.1.2.3. total\_pesticides\_use - Total pesticides - Uso total de pesticidas 

3.2.3.5.1.3. Years - Anos - estará os valores de anos no restantes das colunas com os dados em toneladas



3.2.3.6. CW\_Agriculture\_value\_added.csv

3.2.3.6.1. Documentação dos campos

3.2.3.6.1.1. Area - Sigla do país

3.2.3.6.1.2. Short Name - nome curto do tipo do dado para o valor adicionado (agricultura) em porcentagem do PIB

3.2.3.6.1.2.1. value\_added\_Agr - valor agregado do PIB em porcentagem

3.2.3.6.1.3. Years - Anos - estará os valores de anos no restantes das colunas com os dados percentuais



3.2.3.7. CW\_Agriculture\_production\_trade.csv

3.2.3.7.1. Documentação dos campos

3.2.3.7.1.1. Area - Sigla do país

3.2.3.7.1.2. Short Name - nome curto do tipo dado para do produto agrícola em t (toneladas)
3.2.3.7.1.2.1. production\_Agr\_1 - Agriculture Prouction - Maize - produção agrícola de milho

3.2.3.7.1.2.2. production\_Agr\_2 - Agriculture Prouction - Rice - produção agrícola de arroz

3.2.3.7.1.2.3. production\_Agr\_3 - Agriculture Prouction - Soy - produção agrícola de soja

3.2.3.7.1.2.4. production\_Agr\_4 - Agriculture Prouction - Wheat - produção agrícola de trigo

3.2.3.7.1.2.5. production\_Agr\_5 - Agriculture Prouction - Cattle - produção agrícola de gado

3.2.3.7.1.2.6. production\_Agr\_6 - Agriculture Prouction - Pig - produção agrícola de porco

3.2.3.7.1.2.7. production\_Agr\_7 - Agriculture Prouction - Chicken - produção agrícola de frango

3.2.3.7.1.2.8. production\_Agr\_8 - Agriculture Prouction - Goat - produção agrícola de ovelha

3.2.3.7.1.2.9. production\_Agr\_9 - Agriculture Prouction - Milk Cow - produção agrícola de leite de vaca

3.2.3.7.1.2.10. production\_Agr\_10 - Agriculture Prouction - Milk Goat - produção agrícola de leite de cabra

3.2.3.7.1.2.11. trade\_export\_1 - Trade of agriculture commodities - Export - Rice - Comércio de produtos agrícolas exportação de arroz

3.2.3.7.1.2.12. trade\_export\_2 - Trade of agriculture commodities - Export - Wheat - Comércio de produtos agrícolas exportação de trigo

3.2.3.7.1.2.13. trade\_export\_3 - Trade of agriculture commodities - Export - Soybeans - Comércio de produtos agrícolas exportação de soja

3.2.3.7.1.2.14. trade\_export\_4 - Trade of agriculture commodities - Export - Maize - Comércio de produtos agrícolas exportação de milho

3.2.3.7.1.2.15. trade\_export\_5 - Trade of agriculture commodities - Export - Milk Cow - Comércio de produtos agrícolas exportação de leite de vaca

3.2.3.7.1.2.16. trade\_export\_6 - Trade of agriculture commodities - Export - Chicken - Comércio de produtos agrícolas exportação de frango

3.2.3.7.1.2.17. trade\_export\_7 - Trade of agriculture commodities - Export - Goat - Comércio de produtos agrícolas exportação de cabra 

3.2.3.7.1.2.18. trade\_export\_8 - Trade of agriculture commodities - Export - Pig - Comércio de produtos agrícolas exportação de porco

3.2.3.7.1.2.19. trade\_import\_1 - Trade of agriculture commodities - Import - Rice - Comércio de produtos agrícolas exportação de arroz

3.2.3.7.1.2.20. trade\_import\_2 - Trade of agriculture commodities - Import - Wheat - Comércio de produtos agrícolas exportação de trigo

3.2.3.7.1.2.21. trade\_import\_3 - Trade of agriculture commodities - Import - Soybeans - Comércio de produtos agrícolas exportação de soja

3.2.3.7.1.2.22. trade\_import\_4 - Trade of agriculture commodities - Import - Maize - Comércio de produtos agrícolas exportação de milho

3.2.3.7.1.2.23. trade\_import\_5 - Trade of agriculture commodities - Import - Milk Cow - Comércio de produtos agrícolas exportação de leite de vaca

3.2.3.7.1.2.24. trade\_import\_6 - Trade of agriculture commodities - Import - Chicken - Comércio de produtos agrícolas exportação de frango

3.2.3.7.1.2.25. trade\_import\_7 - Trade of agriculture commodities - Import - Goat - Comércio de produtos agrícolas exportação de cabra

3.2.3.7.1.2.26. trade\_import\_8 - Trade of agriculture commodities - Import - Pig - Comércio de produtos agrícolas exportação de porco

3.2.3.7.1.3. Years - Anos - estará os valores de anos no restantes das colunas com os dados em toneladas



3.2.3.8. CW\_Agriculture\_water.csv

3.2.3.8.1 Documentação dos campos

3.2.3.8.1.1. Area - Sigla do país

3.2.3.8.1.2. Short Name - nome curto do tipo do dado para o percentual de retirada de água total para áreas agrícolas

3.2.3.8.1.2.1. water\_withdrawal - Agricultural water withdrawal as % of total water withdrawal - Retirada de água para agricultura como % da retirada total de água

3.2.3.8.1.3. Years - Anos - estará os valores de anos no restantes das colunas com os dados em percentuais



3.2.3.9 CW\_HistoricalEmissions\_UNFCCC.csv

3.2.3.9.1. Documentação dos campos

3.2.3.9.1.1. country - Sigla do país

3.2.3.9.1.2. source - tecnologia que realizou a coleta de dados, nesse arquivo terá duas, sendo elas: UNFCCC\_AI (por inteligência artificial) e UNFCCC\_NAI (Refere-se aos países que não estão listados no Anexo I da Convenção-Quadro das Nações Unidas)

3.2.3.9.1.2. sector - Setor da emissão do gás que o dado está sendo verificado 

3.2.3.9.1.2. Gas - tipo do gás que está sendo verificado no dado

3.2.3.9.1.3. Years - Anos - estará os valores de anos no restantes das colunas com os dados dos valores em MtCO₂e (milhões de toneladas de dióxido de carbono equivalente).

3.2.3.9.2. Observações para este arquivo

3.2.3.9.2.1. Há dados com os valores de country (países) com a seguinte informação: ANNEXI, talvez seja o valor do arquivo para o planeta, pois não há essa Contry no arquivo, ao contrário dos demais arquivos, entretanto também não há evidências suficiente para afirmar isso, então, esses campos serão descartados.

3.2.3.9.2.2. Os valores do source também serão descartados, afinal não é interessante para essa pesquisa.

3.2.3.9.2.3. Há alguns setores que possuem valores agregados para vários tipos de gases, e outros de tipos de pesquisas que estão juntos, como o objetivo deste projeto é apenas de dióxido de carbono, estes valores serão descartados.



3.2.3.10 CW\_HistoricalEmissions\_PRIMAP.csv

3.2.3.10.1. Documentação dos campos

3.2.3.10.1.1. country - Sigla do país

3.2.3.10.1.2. sector - Setor da emissão do gás que o dado está sendo verificado

3.2.3.10.1.2. Gas - tipo do gás que está sendo verificado no dado

3.2.3.10.1.3. Years - Anos - estará os valores de anos no restantes das colunas com os dados dos valores em MtCO₂e (milhões de toneladas de dióxido de carbono equivalente).

3.2.3.10.1. Observações para este arquivo

3.2.3.10.2.1. Há alguns setores que possuem valores agregados e que são especificamente do gás que está seno pesquisado neste projeto, então será mantido.

3.2.3.10.2.2. A sigla LULUCF significa Land Use, Land-Use Change, and Forestry - Uso da Terra, Mudança no Uso da Terra e Florestas. Por este motivo será mantido.

3.2.3.10.2.3. Gases que não são CO2 serão descartados.



3.2.3.11 CW\_HistoricalEmissions\_GCP.csv

3.2.3.11.1. Documentação dos campos

3.2.3.11.1.1. country name - nome do país

3.2.3.11.1.2. country - Sigla do país

3.2.3.11.1.3. sector - Setor da emissão do gás que o dado está sendo verificado

3.2.3.11.1.4. source - sigla da instituição que realizou a coleta dos dados 

3.2.3.11.1.5. Gas - tipo do gás que está sendo verificado no dado

3.2.3.11.1.6. Years - Anos - estará os valores de anos no restantes das colunas com os dados dos valores em MtCO₂e (milhões de toneladas de dióxido de carbono equivalente).



3.2.3.12 CW\_historical\_emissions.csv

3.2.3.12.1. Documentação dos campos

3.2.3.12.1.1. ISO - Sigla do país

3.2.3.12.1.2. country - nome do país

3.2.3.12.1.3. data source - sigla da instituição que realizou a coleta dos dados

3.2.3.12.1.4. sector - Setor da emissão do gás que o dado está sendo verificado

3.2.3.12.1.5. Gas - tipo do gás que está sendo verificado no dado

3.2.3.12.1.6. Unit - unidade de medida do gás 

3.2.3.12.1.7. Years - Anos - estará os valores de anos no restantes das colunas com os dados dos valores em MtCO₂e (milhões de toneladas de dióxido de carbono equivalente).

3.2.3.12.2. Observações para este arquivo

3.2.3.12.2.1. Há alguns setores que possuem valores agregados e que são especificamente do gás que está seno pesquisado neste projeto, então será mantido.

3.2.3.12.2.2. A sigla LULUCF significa Land Use, Land-Use Change, and Forestry - Uso da Terra, Mudança no Uso da Terra e Florestas. Por este motivo será mantido.

3.2.3.12.2.3. Gases que não são CO2 serão descartados.

3.2.3.12.2.4. Há dados com os valores de ISO e country (países) com a seguinte informação: ANNEXI, talvez seja o valor do arquivo para o planeta, pois não há essa Contry no arquivo, ao contrário dos demais arquivos, entretanto também não há evidências suficiente para afirmar isso, então, esses campos serão descartados.

3.2.3.12.2.5. Os valores do source também serão descartados, afinal não é interessante para essa pesquisa.



3.2.3.13 CW\_HistoricalEmissions\_ClimateWatch.csv

3.2.3.13.1. Documentação dos campos

3.2.3.13.1.1. country - sigla do país

3.2.3.13.1.2. source - sigla da instituição que realizou a coleta dos dados

3.2.3.13.1.3. sector - Setor da emissão do gás que o dado está sendo verificado

3.2.3.13.1.4. Gas - tipo do gás que está sendo verificado no dado

3.2.3.13.1.5. Years - Anos - estará os valores de anos no restantes das colunas com os dados dos valores em MtCO₂e (milhões de toneladas de dióxido de carbono equivalente).

3.2.3.13.2. Observações para este arquivo

3.2.3.13.2.1. Há alguns setores que possuem valores agregados e que são especificamente do gás que está seno pesquisado neste projeto, então será mantido.

3.2.3.13.2.2. A sigla LULUCF significa Land Use, Land-Use Change, and Forestry - Uso da Terra, Mudança no Uso da Terra e Florestas. Por este motivo será mantido.

3.2.3.13.2.3. Gases que não são CO2 serão descartados.

3.2.3.13.2.5. Os valores do source também serão descartados, afinal não é interessante para essa pesquisa.





3.3. International Energy Agency (IEA): https://www.iea.org

3.3.1. Link para download direto, onde será um arquivo XLSX e terá que fazer um cadastro gratuito no site para conseguir realizar o download da fonte de dados: https://www.iea.org/data-and-statistics/data-product/global-energy-review-co2-emissions-in-2021#

3.3.2. A observação da fonte de dados baixada é de as informações serem de 2019 à 2021 e apenas informações de alguns países, mundo, a quantidade de emissão do ano em metros de CO2, e a taxa de crescimento comparada com o ano anterior.

3.3.3. Local no repositório de arquivos coletados:

\\projeto\\Data\\iea\\



3.3.4. Arquivos de dados

3.3.4.1. CO2 Emissions in 2021 - gas emissions.csv

3.3.4.1.1. Documentação dos campos

3.3.4.1.1. Type emission - tipo de emissão 

3.3.4.1.2. CO2 emissions - origem de emissão de CO2

3.3.4.2.3. Unit - unidade de medida da emissão de CO2

3.3.4.2.4. Year - ano da emissão de CO2 conforme a unidade de medida 

3.3.4.2.5. Grow rate % Year - taxa de variação em porcentagem entre os anos 1 e 2, 2 e 3



3.3.5.1. CO2 Emissions in 2021 - countries.csv

3.3.5.2.1. Documentação dos campos

3.3.5.2.1.1. Type emission - tipo de emissão

3.3.5.2.1.2. country - país de emissão de CO2

3.3.5.2.1.3. Unit - unidade de medida da emissão de CO2

3.3.5.2.1.4. Year - ano da emissão de CO2 conforme a unidade de medida

3.3.5.2.1.5. Grow rate % Year - taxa de variação em porcentagem entre os anos 1 e 2, 2 e 3





3.4. National Aeronautics and Space Administration (NASA): https://data.nasa.gov/dataset/

3.4.1. Link para download direto: https://acdisc.gsfc.nasa.gov/data/CMS/CMSFluxTotal.3

3.4.1.1. Os passos para download são: 

3.4.1.1.1. Clique em Once Registered, you can click here.

3.4.1.1.2. Caso não tenha um cadastro, crie um.

3.4.1.1.3. Depois realize o login

3.4.1.1.4. Volte na página do link direto para download

3.4.1.1.5. Clique no arquivo CMSFluxTotal201001\_202212\_v3.nc

3.4.1.1.6. Baixe o arquivo.

3.4.1.2. Observações sobre os arquivos

3.4.1.2.1. Os arquivos da NASA possuem mais de 500 mb, e o GitHub não aceita tais arquivos, então pra isso foi feito um algoritmo para separá-los em arquivos menores com no máximo 50 mb cada um.

3.4.1.2.2. Também há um arquivo no formato de PDF para a documentação completa oficial sobre o arquivo



3.4.2 Local no repositório dos arquivos

\\projeto\\Data\\NASA\\



3.4.3. Arquivos de dados

3.4.3.1. CMSFluxTotal201001\_202212\_v3\_part\_1.csv

3.4.3.2. CMSFluxTotal201001\_202212\_v3\_part\_2.csv

3.4.3.3. CMSFluxTotal201001\_202212\_v3\_part\_3.csv

3.4.3.4. CMSFluxTotal201001\_202212\_v3\_part\_4.csv

3.4.3.5. CMSFluxTotal201001\_202212\_v3\_part\_5.csv

3.4.3.6. CMSFluxTotal201001\_202212\_v3\_part\_6.csv

3.4.3.7. CMSFluxTotal201001\_202212\_v3\_part\_7.csv

3.4.3.8. CMSFluxTotal201001\_202212\_v3\_part\_8.csv

3.4.3.9. CMSFluxTotal201001\_202212\_v3\_part\_9.csv

3.4.3.10. CMSFluxTotal201001\_202212\_v3\_part\_10.csv

3.4.3.11. CMSFluxTotal201001\_202212\_v3\_part\_11.csv

3.4.3.12. Documentação dos campos

3.4.3.12.1. time - Data e hora da coleta dos dados, no formato: YYYY-MM-DD HH:MM:SS

3.4.3.12.2. latitude - é os graus de latitude do registro

3.4.3.12.3. longitude - é os graus de longitude do registro

3.4.3.12.4. total\_post - quantidade de CO2 emitido na área em g/m^2/day (gramas por metro quadrado por dia)

3.4.3.12.5. area - é a área em m2 (metros quadrados)





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

3.8.4. Muitos dados não serão usados até o final do projeto, porém terão alguma explicação para este acontecimento.

3.8.5. Nos links disponibilizados para realizar o download dos arquivos, foi encontrado muitos arquivos com outros formatos, como o XLSX que por si só já possuí um conversor para CSV, entretanto foi encontrado também arquivos com o formato NC, que é um formato de dados de processamento pelo Python, desta forma foi criado um algoritmo em Python para realizar a leitura, conversão e a junção destes arquivos em um único arquivo CSV.



Conclusão

Para responder à pergunta "O que será do futuro da humanidade quanto ao meio ambiente?", deve-se imediatamente entender que não é apenas a emissão de carbono que está envolvida no impacto ambiental, mas com muitap pesquisa para este projeto entendemos que há muito mais que carbono, sendo alguns: gás metano, queima de combústiveis fósseis, desmatamento e o não plantio e preservação da natureza, agropecuária, processos indústriais, uso de fertilizantes, estilo de vida e consumo, transportes, entre muitos outros fatores unidos à esses mencionados e não mencionados.



Entretanto, sendo um dos principais vilões, o dióxido de carbono é: .....



Conclusão final, entendi nesse tema uma única pessoa tem um poder enorme de mudar muita coisa, e melhorar o mundo em que vivemos muito exponencialmente, veja os dados de produção de dióxido de carbono por pessoa, e não apenas plantando uma árvore em algum lugar qualquer, mas sim que com mais estudos (não sobre meio ambiente) sobre tecnologia, poderemos fazer mais e mais com muito menos, veja a pecuária de produção de leite dos Estados Unidos, conseguem produzir muito mais leite que o Brasil, que é o segundo colocado, e com muito menos vacas e consequentemente produzindo menos gás metano. Com isso, podemos concluir que é puro estudos e pura tecnologia que os favorecem.

