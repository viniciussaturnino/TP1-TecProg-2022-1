# Introdução

Essa é uma aplicação com o objetivo de ser utilizada para o controle de estacionamento de estabelecimentos. Com o intuito de desenvolver de forma rápida e com qualidade, o grupo decidiu construir o software utilizando Python por ser familiar para os membros. Com os conhecimentos adquiridos durante o decorrer da disciplina, conseguimos alcançar um bom resultado, seguindo boas práticas e com uma base sólida para implementação de novas funcionalidades no futuro.

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 180106821  |  [Mateus Gomes do Nascimento](https://github.com/matgomes21) |
| 180129058  |  [Paulo Victor da Silva](https://github.com/twistershark) |
| 180138545  |  [Thiago Mesquita Peres Nunes de Carvalho](https://github.com/thiagompc) |
| 180132245  |  [Vinicius de Sousa Saturnino](https://github.com/viniciussaturnino) |

# Características

O sistema de gerenciamento tem como premissa ajudar o estabelecimento a ter uma visão da entrada de dinheiro, quantidade de veículos que estão transitando pelo estacionamento, além de ajudar o mesmo a tomar melhores decisões no futuro.

Através da classe de estacionamento(ParkingLot), o responsável tem acesso as informações de entrada e saída do veículo no estacionamento, além de permitir a definição dos custos e taxas relacionadas ao estacionamento.

Já a classe de acesso ao estacionamento(ParkingAccess), fornece o valor de entrada baseado no período em que o veículo esteve presente no estacionamento.


# Requisitos para utilização: 

1. Ter o Python3 instalado na máquina.
2. Clonar o projeto para sua máquina.
3. Acessar a pasta do projeto clonado com o terminal.
4. Executar o seguinte comando no terminal para instalar as dependências do projeto: `pip install -r requirements.txt`

# Descrição de classes

## ParkingLot (Atributos)


| Nome                          | Tipo   | Obrigatório | Descrição                               | Exemplo  |
|-------------------------------|--------|-------------|-----------------------------------------|----------|
| name                          | String | S           | Nome do estabelecimento                 | Estac. 1 |
| fraction_value                | Number | S           | Valor da fração do tempo                | 30       |
| fulltime_value                | Number | N           | Valor da hora cheia                     | 15       |
| daily_value_daytime           | Number | S           | Valor da diária                         | 120      |
| daily_value_overnight         | Number | S           | Valor da diária noturna                 | 45       |
| daily_overnight_initial_hour  | String | S           | Horário de início do período noturno    | 19:00:00 |
| daily_overnight_end_hour      | String | S           | Horário de término do período noturno   | 08:00:00 |
| subscription_access_value     | Number | S           | Valor da mensalidade                    | 600      |
| event_access_value            | Number | S           | Valor de acesso durante evento          | 50       |
| opening_hour                  | String | S           | Horário de abertura                     | 08:00:00 |
| closing_hour                  | String | S           | Horário de término                      | 19:00:00 |
| capacity                      | Number | S           | Capacidade máxima do estacionamento     | 300      |
| contractor_percentage_revenue | Number | S           | Porcentagem de lucro do estabelecimento | 50       |

## ParkingLot (Métodos)

| Nome                                | Atributos       | Descrição                                                                       |
|-------------------------------------|-----------------|---------------------------------------------------------------------------------|
| to_dict                             | this            | Transforma dado em dicionário                                                   |
| validate_if_variable_is_a_valid_str | variable, name  | Verifica se a variável é uma string e se o tamanho dela é igual a 8 caracteres. |
| validate_if_variable_is_a_valid_int | variable, field | Verifica se a variável é um número inteiro e se o seu valor é maior que 0       |
| register_parking_access             | parking_access  | Cadastra novo estacionamento no sistema                                         |
| parking_access_data_is_valid        | parking_access  | Valida os dados relacionados ao estabelecimento                                 |
| get_parking_accesses                | this            | Retorna todas as entradas no estacionamento                                     |
| get_parking_access_price            | parking_access  | Retorna o valor de uma entrada no estacionamento                                |

---

## ParkingSystem (Atributos)


| Nome                          | Tipo   | Obrigatório | Descrição                               |
|-------------------------------|--------|-------------|-----------------------------------------|
| parking_lots                  | Dicionário | S       | Dados do estabelecimento            |


## ParkingSystem (Métodos)

| Nome                                | Atributos       | Descrição                                                                       |
|-------------------------------------|-----------------|---------------------------------------------------------------------------------|
| to_dict                             | this            | Transforma dado em dicionário                                                   |
| register_parking_lot | parking_lot  | Adiciona um novo estacionamento ao sistema. |

---

## ParkingAccess (Métodos)

| Nome                                | Atributos       | Descrição                                                                       |
|-------------------------------------|-----------------|---------------------------------------------------------------------------------|
| to_dict                             | this            | Transforma dado em dicionário                                                   |
| get_price_by_time | parking_access, parking_lot  | Calcula o valor de uma entrada no estacionamento através do horário de entrada e saída. |