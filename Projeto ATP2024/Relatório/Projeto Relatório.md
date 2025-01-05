# Relatório do Projeto: Sistema de Gestão de Publicações Científicas

## Autores
José Ferreira, A107278  
Filipa Figueiredo, A107239  
Andreia Ferreira, A107234

## Data
03/03/2025

## Visão Geral
No âmbito da unidade curricular de Algoritmos e Técnicas de Programação, foi-nos proposto o desenvolvimento de um sistema de gestão de publicações científicas em Python.

## Requisitos do Sistema
Em relação ao sistema que nos foi proposto desenvolver, havia alguns requisitos essenciais que o sistema devia cumprir para analisar com eficiência uma base de dados fornecida com as publicações científicas.  
Requisitos:

### 1. Carregar Base de Dados
O programa deve ser capaz de carregar para a memória interna o conjunto de dados presente num ficheiro JSON com a seguinte estrutura:

```json
[
    {
        "title": "Título da publicação",
        "abstract": "Resumo do conteúdo da publicação",
        "keywords": "Palavras-chave relacionadas com a publicação",
        "authors": [
            {
                "name": "Nome do autor",
                "affiliation": "Nome da afiliação do autor",
                "orcid": "Identificador aberto de investigador e contribuidor"
            }
        ],
        "doi": "Identificador de objeto digital",
        "pdf": "Caminho do ficheiro PDF da publicação",
        "publish_date": "Data da publicação (AAAA-MM-DD)",
        "url": "Endereço web da publicação"
    }
]
```
O dataset consiste numa lista de dicionários, e cada um corresponde a uma publicação. Estes incluem "keys" para título, resumo, palavras-chave, autores, DOI, PDF, data de publicação e URL. Relativamente aos autores, estes são representados por uma lista de dicionários, onde cada dicionário contém informações sobre nome, afiliação e ORCID.

### 2. Criar Publicações
O programa deve permitir que o utilizador crie uma nova publicação, especificando título, resumo, palavras-chave, DOI, autores (com nome, afiliação e ORCID), caminho para o PDF, data da publicação e URL da publicação.

### 3. Atualizar Publicações
O programa deve permitir que o utilizador atualize as informações de uma dada publicação. Estas informações incluem título, resumo, palavras-chave, autores (nome, afiliação e ORCID), DOI, caminho para o PDF, data da publicação e URL da publicação.

### 4. Consultar Publicações
O programa deve permitir que o utilizador consulte as publicações através de filtros por título, autor, afiliação, data de publicação e palavras-chave. Após encontrar as publicações, deve ser possível ordená-las pelos títulos ou pelas datas de publicação.

### 5. Analisar Publicações por Autor
O programa deve listar os autores, permitindo ao utilizador visualizar as publicações correspondentes a um dado autor. Esta listagem deve ser ordenada pela frequência de publicações e/ou por ordem alfabética.

### 6. Analisar Publicações por Palavras-Chave
O programa deve permitir a visualização das palavras-chave existentes no conjunto de dados, possibilitando que o utilizador visualize as publicações correspondentes a uma dada palavra-chave. As palavras-chave devem ser ordenadas pela sua frequência e/ou por ordem alfabética.

### 7. Estatísticas das Publicações
O programa deve exibir estatísticas referentes às publicações presentes no conjunto de dados, apresentando gráficos para os seguintes tópicos:
- Distribuição de publicações por ano.
- Distribuição de publicações por mês de um determinado ano.
- Número de publicações por autor (top 20 autores).
- Distribuição de publicações de um autor por anos.
- Distribuição de palavras-chave pela sua frequência (top 20 palavras-chave).
- Distribuição de palavras-chave mais frequentes por ano.

### 8. Armazenamento dos Dados
O programa deve guardar as informações alteradas ou adicionadas em memória no ficheiro de suporte.

### 9. Importação de Dados
O programa deve permitir que, a qualquer momento, seja possível importar novos registos de outro conjunto de dados com a mesma estrutura mencionada anteriormente.

### 10. Exportação Parcial de Dados
O programa deve permitir exportar os registos resultantes de uma pesquisa para um ficheiro.

## Interface
### 1. Gestão de Publicações
#### 1.1 Adicionar novas publicações
Para adicionar novas publicações desenolvemos uma interface clara onde é possivel inserir todas as informações da publicação tendo como obrigatoriedade o título e o DOI, uma vez que são parametros importantes para a identificação da publicação como no exemplo a seguir:

<p align="center">
    <img src="Fotos%20Projeto/Add%20Publication%20.png" alt="logo" width="600"/>
</p>

Para adicionar novas palavras-chave e novos autores, as seguintes janelas são apresentadas ao utilizador:
<p align="center">
    <img src="Fotos%20Projeto/Add%20Keyword.png" alt="Descrição da Imagem" width="400"/>
    <img src="Fotos%20Projeto/Add%20Author.png" alt="Descrição da Imagem" width="400"/>
</p>

Caso o utilizador deseje remover alguma das palavras-chave ou autores que tenham adicionado, as seguintes janelas são apresentadas ao utilizador:
<p align="center">
    <img src="Fotos%20Projeto/Remove%20Keyword.png" alt="Descrição da Imagem" width="400"/>
    <img src="Fotos%20Projeto/Remove%20Author.png" alt="Descrição da Imagem" width="400"/>
</p>

Em caso do utilizador tentar guardar a publicação sem título ou DOI, um aviso será mostrado como no exemplo a seguir:
<p align="center">
    <img src="Fotos%20Projeto/Title%20or%20DOI.png" alt="logo" width="300"/>
</p>

Se porventura for inserido um título ou um DOI já existente, um aviso será mostrado como no exemplo a seguir:
<p align="center">
    <img src="Fotos%20Projeto/Duplicated%20Title.png" alt="Descrição da Imagem" width="300"/>
    <img src="Fotos%20Projeto/Duplicated%20DOI.png" alt="Descrição da Imagem" width="300"/>
</p>

Após inserir as informações corretamente e guardar a nova publicação, a janela seguinte será exposta:
<p align="center">
    <img src="Fotos%20Projeto/File%20Saved.png" alt="logo" width="300"/>
</p>

#### 1.2 Atualizar publicações existentes
Para atualizar as informações de uma publicação já existente no dataset desenvolvemos uma interface clara onde serão exibidos todos os parâmentros devidamente preenchidos com as informações da publicação mas com a possibilidade de mudar. Apesar da estrutura e de funções muito semelhante à janela de adicionar publicação, esta apresenta dois novos botões: "Edit" para editar autores já existentes, e "Delete Post" para apagar a publicação do dataset.
<p align="center">
    <img src="Fotos%20Projeto/Edit%20Publication.png" alt="logo" width="600"/>
</p>

No caso do utilizador querer editar os autores ja existentes ao selecionar essa opção, o seguinta janela será exibida:
<p align="center">
    <img src="Fotos%20Projeto/Edit%20Author.png" alt="logo" width="600"/>
</p>

Na hipótese do utilizador querer apagar a publicação do dataset, o seguinte aviso será mostrado:
<p align="center">
    <img src="Fotos%20Projeto/Delete%20Post.png" alt="logo" width="400"/>
</p>

### 2. Capacidades de Pesquisa
#### 2.1 Pesquisa com filtros
O programa é capaz de encontrar publicações utilizando vários filtros, tais como, palavra-chave, autor, afiliação, intervalo de tempo. Para realizar a pesquisa a seguinte janela é exibida:
<p align="center">
    <img src="Fotos%20Projeto/Search%20Filters.png" alt="logo" width="500"/>
</p>

Se não existir nenhuma publicação com os parâmetros submetidos, esta será apresentada:
<p align="center">
    <img src="Fotos%20Projeto/No%20Filter%20Search.png" alt="logo" width="400"/>
</p>

Após o programa procurar as publicações que apresentem os parâmentros preenchidos, será mostrada na seguinte janela as informações todas das publicações, os links que dão para interagrir direcionando diretamente para a Web
<p align="center">
    <img src="Fotos%20Projeto/Document%20Information.png" alt="logo" width="500"/>
</p>

O botão "Save Search" aprsentado na janela serve para o utilizador poder guardar a pesquisa em ficheiro txt ou em um ficheiro json com a mesma estrutura do dataset.
<p align="center">
    <img src="Fotos%20Projeto/Save%20Search.png" alt="Descrição da Imagem" width="200"/>
</p>
<p align="center">
    <img src="Fotos%20Projeto/Txt%20File.png" alt="Descrição da Imagem" width="500"/>
    <img src="Fotos%20Projeto/JSON%20File.png" alt="Descrição da Imagem" width="500"/>
</p>

#### 2.2 Pesquisa por título
O programa tem a funcionalidade de apresentar uma lista com todos os títulos das publicações presentes no dataset, com a possibilidade de os organizar por ordem alfabética ou por data de publicação.
<p align="center">
    <img src="Fotos%20Projeto/Title%20List.png" alt="Descrição da Imagem" width="600"/>
</p>

Se o utilizador selecionar um dos títulos apresentados, uma janela igual à função anterior aparecerá com as informações da publicação e com o botão para salvar a pesquisa.

#### 2.3 Pesquisa por autor
O programa tem a funcionalidade de apresentar uma lista com todos os autores das publicações presentes no dataset, com a possibilidade de os organizar por ordem alfabética ou pela sua frequencia.
<p align="center">
    <img src="Fotos%20Projeto/Author%20List.png" alt="Descrição da Imagem" width="400"/>
</p>

Se o utilizador selecionar um dos autores apresentados, uma janela igual à função anterior aparecerá com as informações da publicação e com o botão para salvar a pesquisa.

#### 2.4 Pesquisa por afiliação
O programa tem a funcionalidade de apresentar uma lista com todas as afiliações das publicações presentes no dataset, com a possibilidade de os organizar por ordem alfabética ou pela sua frequencia.
<p align="center">
    <img src="Fotos%20Projeto/Afilliation%20List.png" alt="Descrição da Imagem" width="600"/>
</p>

Se o utilizador selecionar uma das afiliações apresentados, uma janela igual à função anterior aparecerá com as informações da publicação e com o botão para salvar a pesquisa.

#### 2.5 Pesquisa por palavras-chave
O programa tem a funcionalidade de apresentar uma lista com todas as palavras-chave das publicações presentes no dataset, com a possibilidade de os organizar por ordem alfabética ou pela sua frequencia.
<p align="center">
    <img src="Fotos%20Projeto/Keyword%20List.png" alt="Descrição da Imagem" width="600"/>
</p>

Se o utilizador selecionar uma das palavras-chave apresentados, uma janela igual à função anterior aparecerá com as informações da publicação e com o botão para salvar a pesquisa.

#### 2.6 Pesquisa por intervalo de datas
O programa tem a funcionalidade de procurar publicações num dado intervalo de tempo.
<p align="center">
    <img src="Fotos%20Projeto/Search%20Date.png" alt="Descrição da Imagem" width="300"/>
</p>

Após inserida as datas uma janela igual à função anterior aparecerá com as informações da publicação e com o botão para salvar a pesquisa. Se não houver nenhuma publicação no dado intervalo de tempo a seguinte janela será exibida:
<p align="center">
    <img src="Fotos%20Projeto/No%20Search%20Date.png" alt="Descrição da Imagem" width="400"/>
</p>

### 3. Análise Estatística
#### 3.1 Distribuição de publicações por ano
O programa é capaz de exibir um gráfico com a distribuição de publicações por ano.
<p align="center">
    <img src="Fotos%20Projeto/Post%20Distribution%20Year.png" alt="Descrição da Imagem" width="600"/>
</p>

#### 3.2 Distribuição mensal de publicações
O programa é capaz de exibir um gráfico com a distribuição mensal de publicações num dado ano.
<p align="center">
    <img src="Fotos%20Projeto/Publication%20Year.png" alt="Descrição da Imagem" width="350"/>
    <img src="Fotos%20Projeto/Post%20Distribution%20Month.png" alt="Descrição da Imagem" width="500"/>
</p>

#### 3.3 Número de publicação por autor (Top20)
O programa é capaz de exibir um gráfico com o número de publicações de um autor, mas apenas o Top20 
<p align="center">
    <img src="Fotos%20Projeto/Number%20Post%20Author.png" alt="Descrição da Imagem" width="700"/>
</p>

#### 3.4 Distribuição de publicações por ano de um dado autor
O programa é capaz de exibir um gráfico com a distribuição de publicações por ano após ser selecionado um autor especifico.
<p align="center">
    <img src="Fotos%20Projeto/Select%20Author.png" alt="Descrição da Imagem" width="300"/>
    <img src="Fotos%20Projeto/Post%20Distribution%20Year%20Author.png" alt="Descrição da Imagem" width="600"/>
</p>

#### 3.5 Distribuição de palavras-chave pela sua frequência
O programa é capaz de exibir um gráfico com a distribuição das palavras-chave pela sua frequência.
<p align="center">
    <img src="Fotos%20Projeto/TOP20%20Keywords.png" alt="Descrição da Imagem" width="800"/>
</p>

#### 3.6 Número de palavras-chave num dado ano (Top20)
O programa é capaz de exibir um gráfico com o número de palavras-chave após ser selecionado um determinado ano 
<p align="center">
    <img src="Fotos%20Projeto/Publication%20Year.png" alt="Descrição da Imagem" width="300"/>
    <img src="Fotos%20Projeto/Top20%20Keywords%20Year.png" alt="Descrição da Imagem" width="700"/>
</p>

### 4. Menus
#### 4.1 Menu Principal
A primeira janela que aparece ao utilizador quando inicia o programa é a que se encontra a baixo. É a partir deste menu que se tem acesso a todas as funcionalidades do programa.
<p align="center">
    <img src="Fotos%20Projeto/Main%20Menu.png" alt="Descrição da Imagem" width="300"/>
</p>

Quando o utilizador carregar o ficheiro a seguinte mensagem será exposta para ele:
<p align="center">
    <img src="Fotos%20Projeto/Uploaded%20File.png" alt="Descrição da Imagem" width="200"/>
</p>

Caso contrário, ou seja, o utilizador nao carregue nehum ficheiro e tente selecionar outra opção que necessite do ficheiro um aviso será exibido para o mesmo:
<p align="center">
    <img src="Fotos%20Projeto/No%20File.png" alt="Descrição da Imagem" width="250"/>
</p>

#### 4.2 Menu de Pesquisa
Este menu é exibido quando o utilizador deseja procurar por publicações. É apartir daqui que o mesmo consegue selecionar o método para realizar a sua pesquisa.
<p align="center">
    <img src="Fotos%20Projeto/Search%20Menu.png" alt="Descrição da Imagem" width="200"/>
</p>

#### 4.3 Menu de Estatística
Quando o utlizador selecionar o botão para visualizar as estatística o menu abaixo será apresentado. Aqui o utilizador pode escolher que tipo de estátisca quer ver.
<p align="center">
    <img src="Fotos%20Projeto/Statistic%20Menu.png" alt="Descrição da Imagem" width="300"/>
</p>

## Algoritmo
### Tecnologias Utilizadas
- Python
- PySimpleGUI
- Matplotlib
- JSON

### Importação de Bibliotecas e Módulos
Para o desenvolvimento de sistema foi necessária a importação de bibliotecas e módulos de modo a conseguir realizar o programa da forma mais efeciente possível. As bibliotecas e os módulos em questão são:
- ```import PySimpleGUI as sg```
    - PySimpleGUI é uma biblioteca que simplifica a criação de interfaces gráficas em Python. 
    - No contexto de projeto esta biblioteca foi utilizada para desenvolver toda a interface do sistema de forma clara e objetiva.
- ```from datetime import datetime```
    - datetime é um módulo da biblioteca padrão do Python que fornece classes para manipulação de datas e horas.
    - No contexto do projeto este módulo foi utilizado para uma melhor manipulação das datas de forma a tornar o código mais efeciente.
- ```import webbrowser```
    - webbrowser é um módulo da biblioteca padrão do Python que permite a interação com URL para abrir diretamente na Web.
    - No contexto do projeto foi utilizado para ser possível ter uma interação com os links fornecidos nas publicações.
- ```import json```
    - json é um módulo da biblioteca padrão do Python que fornece uma maneira simples de codificar e decodificar dados no formato JSON (JavaScript Object Notation). Ele é usado para ler e escrever dados em arquivos JSON.
    - No contexto do programa, uma vez que o dataset se encontrava guardado em um ficheiro JSON, esta biblioteca foi usada para conseguir ler e escrever os dados das publicações
- ```import matplotlib.pyplot as plt```
    - matplotlib.pyplot é um módulo da biblioteca Matplotlib que fornece uma interface de estilo MATLAB para a criação de gráficos e visualizações. 
    - No contexto do programa este módulo da biblioteca Matplotlib foi usado para representar gráficamente as estatísticas requeridas pela inunciado.
- ```from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg```
    - FigureCanvasTkAgg é uma classe do módulo matplotlib.backends.backend_tkagg que permite integrar gráficos Matplotlib em interfaces Tkinter. Ele é usado para desenhar gráficos em um widget Tkinter Canvas
    - No contexto do programa este módulo foi necessário para apresentar os gráficos na interface da melhor forma possível.

### 1. Gestão de Ficheiros
#### 1.1 Carregar ficheiros JSON
Para carregar o dataset presente no ficheiro JSON, com a estrutura anterior mente mencionada, foi utilizado código já desenvolvido nas aulas com algumas adaptações para a interface.
``` py
def carregar(caminho_ficheiro):
    try:
        with open(caminho_ficheiro, 'r', encoding ='utf-8') as file:
            return json.load(file)
    except Exception as e:
        sg.popup_error(f"Error loading file: {e}")
        return None 
```

#### 1.2 Guardar publicações
Para guardar as publicações atualizadas ou criadas foi necessário desenvolver uma função para guardar os dados no mesmo ficheiro que foram carregados.
``` py
def guardar(caminho_ficheiro, dados):
    try:
        with open(caminho_ficheiro, 'w', encoding='utf-8') as file:
            json.dump(dados, file, indent=4)
            sg.popup("File saved successfully!")
    except Exception as e:
        sg.popup_error(f"Error saving file: {e}")
```

#### 1.3 Exportar resultados de pesquisa
Para exportar resultados de uma pesquisa desenvolvemos duas maneiras possíveis para o fazer.
- Uma que permite exportar em formato txt com uma estrutura defenida por nós
```py
def guardar(caminho_ficheiro, dados):
    try:
        with open(caminho_ficheiro, 'w', encoding='utf-8') as file:
            json.dump(dados, file, indent=4)
            sg.popup("File saved successfully!")
    except Exception as e:
        sg.popup_error(f"Error saving file: {e}")
```
- Outra que permite exportar em formato de json com a mesma estrutura do dataset

```py
elif event_save == "-SAVE_JSON-":
    caminho_arquivo_save = sg.popup_get_file("Save as", save_as=True, no_window=True, file_types=(("JSON Files", "*.json"),))
    if caminho_arquivo_save:
        try:
            with open(caminho_arquivo_save, 'r', encoding='utf-8') as file:
                dados_existentes = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            dados_existentes = []

        if isinstance(dados, list):
            dados_existentes.extend(dados)
        else:
            dados_existentes.append(dados)

        guardar(caminho_arquivo_save, dados_existentes)
```
### 2. Gestão de Publicações
#### 2.1 Adicionar novas publicações
Para adicionar novas publicações ao dataset desenvolvemos a seguinte função que recebe como arguentos ```publicacoes```, que se refere à memoria interna do dataset onde estão armazenadas todas as publicações, ```values```, que são os dados obtidos pelo input do utilizador na interface, ```autores```, que é uma lista de autores gerada por uma outra função, e ```keywords```, que é uma string tambem criada por uma outra função onde as palavras-chave estão serparas por vírgulas.

```py
def criar_publicacoes(publicacoes, values, autores, keywords):
    title = values["-TITLE-"].strip()
    abstract = values["-ABSTRACT-"].strip()
    doi = values["-DOI-"].strip()
    pdf = values["-PDF-"].strip()
    url = values["-URL-"].strip()
    publish_date = values["-PUBLISH_DATE-"].strip()

    if verificar_duplicados(publicacoes, title, doi):
        return False 
    
    nova_publicacao = {
        "title": title,
        "abstract": abstract,
        "doi": doi,
        "pdf": pdf,
        "url": url,
        "publish_date": publish_date,
        "autores": autores,
        "keywords": keywords
    }

    publicacoes.append(nova_publicacao)
    return True
```

Primeiro, extrai os dados necessários dos ```values``` correspondentes, com a utilização do métoddo ```strip()``` para remover quaisquer espaços em branco desnecessários. Em seguida, verifica se já existe alguma publicação com o mesmo título ou DOI através da função ```verificar_duplicados```. Caso encontre duplicados, retorna ```False``` para indicar que esta publicação não pode ser adicionada. 

Se não houver duplicados, cria um novo dicionário ```nova_publicacao``` com todos os dados fornecidos, incluindo os autores e palavras-chave. Este dicionário é então adicionado à lista de publicações existentes através do método ```append()```. Por fim, retorna ```True``` para indicar que a publicação pode ser adicionada.

```py
elif event == "-SAVE-":
    if not values["-TITLE-"].strip() and not values["-DOI-"].strip():
        sg.popup("Title or DOI is required!")
    else:
        if criar_publicacoes(publicacoes, values, autores, keywords):
            if caminho_ficheiro:
                guardar(caminho_ficheiro, publicacoes)
                sg.popup("Publication successfully saved!")
                popup_running = False
            else:
                sg.popup("No file selected.")
```
Este trexo de código mostra como o valor booleano é interpretado para guardar ou não a publicação dependo se esta tem ou nao um título ou DOI repetido. Também aqui tem uma verificação caso o utilizador não insira título nem DOI.

#### 2.2 Atualizar Publicação
Para ser possivel atualizar as informações de uma dada publicação existente no dataset nós desenvolvemos a seguinte função que recebe como argumentos ```values```, que são os dados obtidos pelo input do utilizador na interface, ```keywords```, que é uma string tambem criada por uma outra função onde as palavras-chave estão serparas por vírgulas, ```autores```, que é uma lista de autores gerada por uma outra função, ```publicacao_encontrada```, que são as informações de uma publicação que foi encontrada por uma outra função dados os dados de título ou DOI, ```caminho_ficheiro```, que é o caminho guardado em memória onde as publicações com a publicação atualizada serão guardadas, e ```publicacoes```, que se refere à memoria interna do dataset onde estão armazenadas todas as publicações.

```py
def atualizar_publicacao(values, keywords, autores, publicacao_encontrada, caminho_ficheiro, publicacoes):
    title = values["-EDIT_TITLE-"].strip()
    doi = values["-EDIT_DOI-"].strip()

    if verificar_duplicados(publicacoes, title, doi, publicacao_encontrada):
        return
    
    updated_publication = {
        "title": values["-EDIT_TITLE-"].strip(),
        "abstract": values["-EDIT_ABSTRACT-"].strip(),
        "publish_date": values["-EDIT_DATE-"].strip(),
        "doi": values["-EDIT_DOI-"].strip(),
        "pdf": values["-EDIT_PDF-"].strip(),
        "url": values["-EDIT_URL-"].strip(),
        "keywords": keywords,
        "authors": autores
    }

    for key, value in updated_publication.items():
        publicacao_encontrada[key] = value

    if caminho_ficheiro:
        guardar(caminho_ficheiro, publicacoes)
        sg.popup("Publication successfully updated!")
    else:
        sg.popup("No file selected for saving")
```

Primeiro, assim com a função de adicionar uma nova publicação, extrai os dados necessários dos ```values``` correspondentes, com a utilização do métoddo ```strip()``` para remover quaisquer espaços em branco desnecessários. Em seguida, assim como a outra também verifica se já existe alguma publicação com o mesmo título ou DOI através da função ```verificar_duplicados```. Caso encontre duplicados, nao retorna nada e nehuma alteração é feita.

Se não houver duplicados, cria um novo dicionário ```updated_publication``` com todos os dados fornecidos, incluindo os autores e palavras-chave. Depois, a função atualiza a publicação original, substituindo cada campo pelos novos valores através de um ciclo que percorre todos os elementos do dicionário ```updated_publication```. Por fim, se existir um caminho de ficheiro definido, a função guarda todas as alterações no ficheiro através da função guardar.

Ainda relacionado com a atualização de publicações, também desenvolvemos uma função para remover uma publicação do dataset. Esta recebe apenas três argumentos: ```publicacao_encontrada```, ```caminho_ficheiro``` e ```publicacoes```, já exmplicados anteriormente

```py
def remover_publicacao(publicacao_encontrada, caminho_ficheiro, publicacoes):
    publicacoes.remove(publicacao_encontrada)
    sg.popup("Publication removed successfully!")
    guardar(caminho_ficheiro, publicacoes)
```
O seu funcionamento é direto e eficiente. Primeiro, utiliza o método ```remove()``` para eliminar a publicação selecionada da lista de publicações. Este método procura a publicação específica na lista e remove-a completamente. Por fim, a função guardar é chamada que atualiza o ficheiro guardado com a nova lista de publicações, já sem a publicação que foi removida.

#### 2.3 Listagem
Como visto anteriormente na interface, nós desenvolvemos códigos para listar títulos, autores, afiliações e palavras-chave e que podem ser ordenados por ordem alfabética por frequencia de ocorrencia nas publicações e no caso dos títulos até mesmo por data de publicação.

```py
def contar_frequencia_autores(publicacoes):
    author_frequency = {}
    for publicacao in publicacoes:
        for autor in publicacao.get("authors", []):
            name = autor.get("name", "")
            if name:
                if name not in author_frequency:
                    author_frequency[name] = 0
                author_frequency[name] += 1
    return author_frequency
```
Aqui tem um exemplo de como fizemos para calcular quastas vezes um dado autor aparece ao longo de todas as publicações. Esta função recebe como argumento ```publicacoes```, que se refere à memoria interna do dataset onde estão armazenadas todas as publicações e e retorna um dicionário com a contagem de publicações por autor.

O seu funcionamento começa com a criação de um dicionário vazio chamado author_frequency, que irá armazenar o nome de cada autor como chave e o número de publicações como valor. Para cada publicação, a função examina a lista de autores associada. Utiliza o método ```get()``` para aceder à lista de autores, retornando uma lista vazia caso não existam autores. Para cada autor encontrado, extrai nome também. Caso seja a primeira vez que encontra o autor, cria uma nova entrada no dicionário com contagem inicial zero. Depois, incrementa a contagem para esse autor em uma unidade. Depois é só criar uma variavel onde terá uma lista ordenada por frequencia se utilizarmos como parâmetro de comapração a contagem no dicionário e por ordem alfabética se o parâmetro for os nomes no método ```sorted()```.

Após calcular a frequência, são criadas duas estruturas adicionais. Uma lista com os nomes dos autores ordenada alfabeticamente, obtida com o método ```sorted()``` aplicado às chaves do dicionário. Outra lista de tuplos ```(nome, frequência)```, onde cada autor é associado ao número de publicações, ordenada de forma decrescente pela frequência. Esta lista é obtida utilizando o método ```sorted()``` com um critério de ordenação baseado na contagem. Sentimos a necessidade de criar esta lista de tuplos, uma vez que a contagem será util para a estatística do projeto.

Para as afiliações e palavras-chave o código é muito semelhante ao explicado aqui apenas com algumas alterações noamdamente as ```keys``` correspondetes no dicionário de cada elemento. No caso dos títulos uma vez que este não são ordenados por ordem albabética mas sim por data de publicação já existem diferenças significativas no código.

```py
def ordenar_titulos(publicacoes):
    title_list = []
    for publicacao in publicacoes:
        title = publicacao.get("title", "")
        publish_date = publicacao.get("publish_date", "")
        
        if publish_date:
            try:
                data_publicacao = datetime.strptime(publish_date, "%Y-%m-%d")
            except ValueError:
                data_publicacao = None  
        if data_publicacao:
            title_list.append((title, data_publicacao))
    ordered_title_list = [item[0] for item in sorted(title_list, key=lambda x: x[0])]
    ordered_title_date = [item[0] for item in sorted(title_list, key=lambda x: x[1])]
    ordered_title_date_rev = [item[0] for item in sorted(title_list, key=lambda x: x[1], reverse=True)]
    return ordered_title_list, ordered_title_date, ordered_title_date_rev
```
Aqui a função ```ordenar_titulos``` organiza os títulos das publicações de três formas diferentes. Recebe a lista de publicações e começa por criar uma lista temporária que guarda tupulos com o títulos e a data correspondente a esse título. Para cada publicação que tenha data, a função tenta converter a data (que está em formato texto) para um objeto datetime, usando o formato ```ano-mês-dia```. Se a conversão falhar, atribui None à data. Por fim cria listas com ordenadas ```ordered_title_list```: títulos ordenados alfabeticamente ```ordered_title_date```: títulos ordenados por data, do mais antigo para o mais recente ```ordered_title_date_rev```: títulos ordenados por data, do mais recente para o mais antigo.

#### 2.4 Gráficos de estatística
Para possibilitar a vizualização de gráficos criados pelo ```Matplotlib``` na nossa interface foi necessário que desenvolvessemos um função auxiliar.

```py
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg
```
Esta função recebe dois argumentos: ```canvas```, área de desenho, e ```figura matplotlib```. Ela vai criar uma área de desenho específica para gráficos matplotlib em janelas tkinter, desenha a figura e ajusta-a para preencher todo o espaço disponível.

Um exemplo de uma função que cria um gráfico é a apresentada abaixo. Esta função recebe apenas o argumento ```publicacoes``` e tem a capacidade de gerar um gráfico utilizando a biblioteca ```Matplotlib```.

```py
def mostrar_distribuicao_palavras_chave(publicacoes):
    _, ordered_keywords = contar_frequencia_palavras_chave(publicacoes)

    top_20_keywords = [keyword for keyword, _ in ordered_keywords[:20]]
    keyword_counts = [count for _, count in ordered_keywords[:20]]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_20_keywords, keyword_counts)
    ax.set_xlabel("Keywords Frequency")
    ax.set_ylabel("Keywords")
    ax.set_title("Distribution of keywords by frequency")
    plt.gca().invert_yaxis()
    plt.tight_layout()

    layout_keyword = [
        [sg.Text("Distribution of keywords by frequency", justification="center", size=(30, 1))],
        [sg.Canvas(key="-CANVAS-")],
        [sg.Button("Exit", key="-EXIT-")]
    ]

    window_keyword = sg.Window("Distribution of keywords by frequency", layout_keyword, modal=True, finalize=True)
    draw_figure(window_keyword["-CANVAS-"].TKCanvas, fig)
    
    keyword_running = True
    while keyword_running:
        event_keyword, values_keyword = window_keyword.read()

        if event_keyword in (sg.WINDOW_CLOSED, "-EXIT-"):
            keyword_running = False

    window_keyword.close()
```

A função ```mostrar_distribuicao_palavras_chave``` gera um gráfico de barras horizontal que exibe as 20 palavras-chave mais frequentes nas publicações. Inicialmente, ela utiliza a função ```contar_frequencia_palavras_chave``` para obter uma lista ordenada de palavras-chave por frequência. Em seguida, seleciona as 20 palavras-chave mais frequentes e cria o gráfico utilizando o Matplotlib. Este gráfico é então mostrado em uma interface gráfica usando a função ```draw_figure```, permitindo ao utilizador visualizar as palavras-chave mais comuns nas publicações.

## Linha de Comando
Foi também solicitado o desenvolvimento de uma linha de comandos com requisitos muito semelhantes aos anteriormente referidos, entre os quais:
- Criar Publicação
- Consultar Publicação
- Eliminar Publicação
- Relatório de Estatísticas
- Listar Autores
- Guardar Publicações

Tendo em conta que realizámos a maior parte da linha de comandos antes da interface gráfica, muitos dos códigos são semelhantes, com exceções, claro, uma vez que o algoritmo tem de ser ajustado quando os inputs são feitos na interface, mas toda a lógica geral das funções de ambos é idêntica.

Para manter o terminal mais limpo e facilitar a leitura da informação, utilizámos o módulo ```import os```, que é uma biblioteca padrão do Python e fornece funcionalidades para interagir com o sistema operativo. No contexto deste projeto, o módulo ```import os``` foi utilizado para realizar tarefas como limpar a tela do terminal e garantir que o sistema seja capaz de identificar e manipular caminhos de ficheiros de forma compatível com diferentes sistemas operativos (Windows, Linux, etc.).

### Funcionalidades
#### 1. Menu Principal
O menu principal é muito semelhante ao menu principal da interface gráfica como é possível ver na imagem a baixo.

<p align="center">
    <img src="Fotos%20Projeto/LC%20Main%20Menu.png" alt="Descrição da Imagem" width="300"/>
</p>

#### 2. Adicionar Publicação
O menu que desenvolvemos para adicionar uma publicação é o que se encontra abaixo. Neste menu, será pedido, por ordem, que cada parâmetro seja preenchido. No caso das palavras-chave e dos autores, pode-se adicionar quantos quisermos, e, quando não quisermos adicionar mais nenhum, basta pressionar ENTER.

<p align="center">
    <img src="Fotos%20Projeto/LC%20Add%20Publication.png" alt="Descrição da Imagem" width="400"/>
</p>

#### 3. Atualizar Publicação
O menu que desenvolvemos para atualizar as informações de uma publicação de forma clara é o seguinte. Primeiramente, será solicitado o título ou o DOI da publicação que deseja procurar. Após isso, várias opções aparecerão, e basta selecionar a que desejamos alterar. O conteúdo atual será impresso no terminal e, em seguida, será pedido que seja inserido o novo conteúdo.

<p align="center">
    <img src="Fotos%20Projeto/LC%20Update%20Publication.png" alt="Descrição da Imagem" width="500"/>
</p>

#### 4. Procurar Publicação
No menu de pesquisa de publicações, inicialmente o utilizador será questionado sobre qual parâmetro deseja utilizar para a pesquisa. Após isso, um segundo menu será exibido, permitindo que o utilizador escolha como deseja visualizar a listagem do parâmetro selecionado: por ordem alfabética, por frequência ou, no caso dos títulos, por data de publicação.

<p align="center">
    <img src="Fotos%20Projeto/LC%20Search%20Publication.png" alt="Descrição da Imagem" width="300"/>
</p>

A seguir, uma lista será impressa no terminal de acordo com a escolha do utilizador. Assim, o utilizador poderá ver os nomes disponíveis, selecionar a opção de pesquisa no menu anterior e inserir o que deseja procurar.

<p align="center">
    <img src="Fotos%20Projeto/LC%20Search%20Publication%202.png" alt="Descrição da Imagem" width="700"/>
</p>

#### 5. Vizualização das publicações
Existe uma opção no menu principal para visualizar todas as publicações do documento. No entanto, a estrutura em que elas aparecem é exatamente a mesma que é utilizada para visualizar, por exemplo, as publicações encontradas após uma pesquisa. Se houver mais de uma publicação, é possível navegar entre elas utilizando as opções apresentadas ao utilizador.

<p align="center">
    <img src="Fotos%20Projeto/LC%20View%20Document.png" alt="Descrição da Imagem" width="700"/>
</p>

#### 6. Estatística das Publicações
Por último, existe o menu para consultar as estatísticas, como o número de publicações por ano, o número de publicações por autor e as palavras-chave mais comuns no dataset.

<p align="center">
    <img src="Fotos%20Projeto/LC%20Statistic.png" alt="Descrição da Imagem" width="300"/>
</p>

Selecionando qualquer uma das opções, o seguinte relatório estatístico será exibido para o utilizador, permitindo-lhe navegar utilizando as opções do menu.

<p align="center">
    <img src="Fotos%20Projeto/LC%20Statistic%202.png" alt="Descrição da Imagem" width="300"/>
</p>

## Desafios e Soluções
Um dos primeiros desafios que nos deparamos foi perceber todas as possibilidades que o ```PySimpleGUI``` nos possibilitava para organizar da melhor maneira possível todas as funcionalidades que desenvolvemos. Em relação à parte do algoritmo em si, algumas dificuldades que encontramos foram nomeadamente adaptar o código que tinha sido desenvolvido para a linha de comando para os inputs e outputs da interface e descobiri qual seria a melhor maneira de inserir os gráficos criados pelo ```Matplotlib``` na interface. Foi necessário realizar alguma pesquisa e estudo para superar estes objetivos, mas no final o sistema ficou exatamente como pretendiamos.

## Conclusão
Neste projeto, não só aplicámos os conhecimentos e habilidades adquiridos ao longo das aulas da Unidade Curricular de Algoritmos e Técnicas de Programação, como também desenvolvemos a nossa capacidade de aprendizagem autónoma, uma vez que surgiram necessidades de investigar e pesquisar novos conteúdos e informações. Além disso, tivemos a oportunidade de aprimorar a nossa competência na resolução de problemas, aprendendo a aplicá-la em situações práticas. Em resumo, apesar dos desafios e dificuldades enfrentados durante o desenvolvimento do projeto, consideramos ter alcançado os requisitos e objetivos propostos.



