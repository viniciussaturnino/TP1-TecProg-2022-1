Este documento tem como objetivo realizar a entrega do TP3, documentando os requisitos solicitados no enunciado. As 5 características escolhidas pelo grupo foram:

1. Boa documentação;
2. Ausência de duplicidades;
3. Simplicidade;
4. Idiomático;
5. Modularidade (baixo acoplamento e alta coesão).

# 1. Boa documentação

## 1.1 Descrição

Esta característica possui como efeito no código, a melhoria na claridade do projeto e do código, visto que uma boa documentação serve como guia para os desenvolvedores e interessados no sistema.

## 1.2 Relação com mau-cheiros

Esta característica possui relação com o mau-cheiro comentários, visto que este mau-cheiro diz respeito em como o código explica sobre si mesmo, que é justamente o objetivo de uma boa documentação, explicar o código.

## 1.3 Operação de refatoração

Como operação de refatoração para esta característica, o README do projeto foi refatorado para uma melhor explicação sobre o projeto, como pode ser visto nas imagens abaixo:

![Boa Documentação 1](./assets/boa-documentacao-1.png)
![Boa Documentação 2](./assets/boa-documentacao-2.png)
![Boa Documentação 3](./assets/boa-documentacao-3.png)

# 2. Ausência de duplicidades

## 2.1 Descrição

Esta característica visa a diminuição de código duplicado, duplicidade esta também conhecida como boilerplate, e os efeitos dessa característica no código é a melhora na manutenibilidade do mesmo, visto que as duplicidades são centralizadas em um lugar só, e também melhora a visibilidade, visto que o código fica mais compactado.

## 2.2 Relação com mau-cheiros

Esta característica tem completa relação com o mau-cheiro código duplicado, já que os dois visam o mesmo problema, que é trechos de código iguais em lugares distindos, que poderiam muito bem ser centralizados em uma única função, classe, objeto ou outra estrutura de programação.

## 2.3 Operação de refatoração

Uma refatoração que visa essa característica pode ser vista a seguir:

![Ausência de duplicidade](./assets/ausencia-de-duplicidades.png)

Nesta refatoração, foi identificado uma duplicação de código, que dificulta muito a manutenção desta funcionalidade, visto que se for ter uma alteração deve-se alterar a mesma coisa em vários pontos, e com isso, foi criada uma função centralizando a funcionalidade e eliminando a duplicidade.

# 3. Simplicidade

## 3.1 Descrição

Uma das boas práticas na programação consiste em construir um código legível e bem descritivo. E quando uma classe, por exemplo, acaba tento muitas responsabilidades, o entendimento acaba sendo prejudicado e ela acaba tornando-se, muitas vezes em uma classe com pouca ou nenhuma simplicidade.

## 3.2 Relação com mau-cheiros

A característica ou mau cheiro que foi identificado no projeto e onde a simplicidade poderia ser aplicada é a característica de Classe Inchada ou Grande.

## 3.3 Operação de refatoração

Uma exemplo de operação de refatoração que evidencia o ponto da simplicidade está presente em um dos Pull Requests feitos no projeto. No PR em questão é possível perceber abaixo o quanto a classe tinha muitas operações e responsabilidades:

![Pull Request](./assets/simplicidade.png)

# 4. Idiomático

## 4.1 Descrição

Escrever código de maneira idiomática significa respeitar as regras e convenções da linguagem que está sendo utilizada. Além disso, também é necessário nomear as estruturas e variáveis do código de maneira breve e clara, passando o entendimento para quem estiver lendo.

## 4.2 Relação com mau-cheiros

Um mau-cheiro relacionado à falta desta técnica é a Generalidade especulativa, pois um código não escrito de maneira idiomática se torna um projeto difícil de entender, e, consequentemente, um projeto difícil de manter.

## 4.3 Operação de refatoração

![Idiomático](./assets/idiomatico.png)

Nessa refatoração onde removemos os números mágicos, criamos variáveis seguindo as regras e convenções da linguagem Python, além de nomeá-las de forma breve e clara, deixando dessa maneira, um código fácil de entender e manter.

# 5. Modularidade (baixo acoplamento e alta coesão)

## 5.1 Descrição

Esta característica visa evitar classes com múltiplas responsabilidades, e que possuem muito acoplamento entre si, melhorando a estrutura do código, a coesão e o acoplamento.
## 5.2 Relação com mau-cheiros

O mau-cheiro que mais se relaciona com esta característica é o de classe inchada, que é um mau-cheiro que indica uma coestão baixa, evidenciando que uma classe está com mais responsabilidades do que deveria.

## 5.3 Operação de refatoração

Uma operação de refatoração feita no projeto que visa esta característica, pode ser vista abaixo:

![Modularidade 1](./assets/modularidade-1.png)
![Modularidade 2](./assets/modularidade-2.png)

Na operação acima, o método ```get_parking_access_price_by_time``` estava dentro da classe ```payloads```, dando a esta classe uma responsabilidade que não deveria ser dela, e com isso, foi criada uma nova classe com um escopo que se adequa a esta função.