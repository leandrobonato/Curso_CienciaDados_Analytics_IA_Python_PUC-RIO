## EXERCÍCIO 01 ##

*Aplicação: Plataforma de aluguel de imóvel por temporada*

Os proprietários se cadastram na plataforma fornecendo o cpf (que será o identificador único), o nome completo, data de nascimento, telefone celular e e-mail. Todos os campos são obrigatórios. Somente são aceitos proprietários maiores de 18 anos. 
O proprietário deve cadastrar pelo menos um imóvel para ter seu cadastro aceito. 

Este imóvel só poderá pertencer a um proprietário. O proprietário pode cadastrar quantos imóveis desejar. 

Para cada imóvel deve ser informado: endereço completo, número de quartos, número de banheiros, se tem ou não vaga na garagem, se aceita ou não animais. Além disto, também é necessário informar o valor mínimo da diária para uma pessoa, o valor adicional da diária por pessoa e o número máximo de pessoas. Todos os campos são obrigatórios e cada imóvel recebe como identificação um número sequencial chamado ID. O proprietário também pode registrar em um único campo de observações uma descrição do imóvel assim como outras questões particulares para a locação. 

Os interessados também devem realizar um cadastro na plataforma. No cadastro devem fornecer o cpf (que será o identificador único), o nome completo, data de nascimento, telefone celular e e-mail. Todos os campos são obrigatórios. Somente são aceitos interessados maiores de 18 anos.
Os interessados poderão consultar a lista de imóveis disponíveis no período desejado por endereço (estado, cidade, bairro e cep) e também filtrar por critérios como número de quartos, número de banheiros, se tem ou não vaga na garagem, se aceita ou não animais, número máximo de pessoas e faixa de valores. 

Os interessados podem fazer a reserva do imóvel, mas devem realizar o pagamento pela plataforma para garantir o aluguel no período desejado. Em caso de reservas, a plataforma irá registrar a locação do imóvel com as datas de início e fim previstas, o valor a ser pago e o número de pessoas. Cada interessado só pode alugar um imóvel por período. Com esta operação o imóvel fica indisponível para outras locações no período. Até 48 horas antes do início previsto o interessado pode solicitar o cancelamento e a plataforma providenciará o reembolso de 70% do valor pago e disponibilizará o imóvel novamente para outros interessados. 
Ao entrar no imóvel, no dia agendado o locatário deve realizar o check-in na plataforma. Ao sair do imóvel, o locatário deve realizar o check-out. Ao longo da estadia o locatário poderá registrar observações no acompanhamento do aluguel para relatar algum problema. 
Um mesmo imóvel pode ser alugado pelo mesmo locatário mais de uma vez em períodos diferentes. Após concluir cada locação, o locatário poderá realizar uma avaliação do imóvel em até 30 dias. 

Considerando esta descrição, identifique e represente através de um DER

    • as entidades
    • os atributos de cada entidade
    • os identificadores de cada entidade
    • os relacionamentos
    • os atributos dos relacionamentos, se houverem
    • as cardinalidades mínimas/máximas

Crie e registre em um Dicionário de Dados outras informações relevantes extraídas desta descrição.

## EXERCÍCIO 02 ##

Neste exercício você irá praticar a transformação do modelo de dados da aplicação Plataforma de aluguel de imóvel por temporada em um banco de dados relacional. 

O primeiro passo é  gerar o Modelo Lógico na 3FN aplicando as regras de mapeamento e depois as técnicas de Normalização apresentadas na Aula 02 no seu DER gerado na prática da Aula 01. 

*Mas atenção!* Caso você utilize o brModelo para gerar o Modelo Lógico a partir do DER é necessário verificar a qualidade do modelo gerado. Realize os ajustes pertinentes, aplicando as regras de mapeamento e as técnicas de normalização.

Em seguida você precisará elaborar: 

    • Comandos de Criação de Tabelas com Atributos e Restrições de Integridade
    • Comandos de Consulta ao Dicionário de Dados do SGBD para verificar os objetos criados
    
*Mas atenção!!* Caso você utilize o brModelo para gerar o script de criação das tabelas (modelo físico) a partir do Modelo Lógico, é necessário, antes de executar no sqlite, ajustar os comandos DDL gerados da seguinte forma:

    • Alterar os comandos CREATE TABLE de modo a incluir todas as constraints necessárias (PRIMARY KEY, FOREIGN KEY, NOT NULL, CHECK, DEFAULT e UNIQUE);
    • Remover os comandos ALTER TABLE;
    • Revisar e alterar a ordem de criação de tabelas com base na precedência para tabelas referenciadas por FOREIGN KEY e
    • Opcionalmente, nomear todas as constraints.
