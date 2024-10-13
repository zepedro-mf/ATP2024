# TPC5

## Data 2024/10/07

## Autor: José Pedro Machado Ferreira 

## Resumo do que foi feito:
O TPC5 teve como objetivo a realização de uma aplicação para gerir um cinema.

- A aplicação consistia em:
    - Desenvolver uma aplicação para a gestão de um conjunto de salas de cinema de um centro comercial.
    - Nesse centro comercial, existem várias salas de cinema (que poderão estar a exibir filmes ou não). Cada sala tem uma determinada lotação, uma lista com a referência dos bilhetes vendidos (lugares ocupados, onde cada lugar é identificado por um número inteiro), e cada sala tem um filme associado.

- O programa desta aplicação devia conter as seguintes características:
    - Uma função para exibir todos os filmes em exibição;
    - Uma função para indicar se um lugar de uma determinada sala está ocupado ou não;
    - Uma função para vender bilhetes e que, por consequência, altere o número de lugares disponíveis e impeça a compra em salas sem filme;
    - Uma função para mostrar a disponibilidade de todo o cinema;
    - Uma interface para controlar o programa.

- Na realização deste programa, o mais importante foi:
    - Descobrir como codificar cada função pedida pelo enunciado;
    - Juntar a função de indicar se um certo lugar está disponível na função que mostra a disponibilidade total do cinema;
    - Implementar a "projeção" da sala de cinema para facilitar a escolha do lugar desejado;
    - Implementar uma função que permite editar as salas, ou seja, mudar o nome do filme e interditar lugares;
    - Organizar o código utilizando funções.