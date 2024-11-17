# Relatório TPC7

## Data 2024/10/21

## Autor: José Pedro Machado Ferreira 

## Resumo do que foi feito:
O TPC7 teve como objetivo a realização de uma aplicação para um modelo onde fosse possível guardar e aplicar algumas funções a registos de temperatura e precipitação ao longo de vários dias.

- A aplicação consistia em:
    - Desenvolver uma aplicação com várias funções que utilizem os dados de meteorologia fornecidos;
    - Adicionar dados de meteorologia e, posteriormente, guardá-los num documento para poderem ser carregados mais tarde.

- O programa desta aplicação devia conter as seguintes características:
    - A variável interna seria "TabMeteo", uma lista com tuplos onde cada tuplo contém um tuplo para a data (ano, mês, dia) e as informações de temperatura mínima, temperatura máxima e precipitação do dia. Exemplo: TabMeteo = [((ano, mês, dia), tempMin, tempMax, prec)];
    - Uma função para guardar a tabela num ficheiro;
    - Uma função para guardar a tabela num ficheiro;
    - Uma função para calcular a temperatura média;
    - Uma função para determinar a temperatura mínima mais baixa;
    - Uma função para encontrar o valor mais alto de precipitação;
    - Uma função para contar o número de dias com precipitação superior a "x";
    - Uma função para o maior número de dias consecutivos com precipitação abaixo de "x";
    - Uma função para representar um gráfico de temperatura máxima e mínima e um gráfico de pluviosidade;
    - Uma interface para controlar o programa.

- Na realização deste programa, o mais importante foi:
    - Desenvolver um código para converter as listas em texto para guardar no ficheiro .txt;
    - Desenvolver um código para ler cada linha do ficheiro e separar devidamente as informações para atualizar a lista interna (TabMeteo);
    - Desenvolver o código para a representação gráfica das informações de meteorologia;
    - Organizar o código utilizando funções.
