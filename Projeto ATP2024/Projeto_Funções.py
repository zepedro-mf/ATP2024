import PySimpleGUI as sg
from datetime import datetime
import webbrowser
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Função para carregar os dados do ficheiro
def carregar(caminho_ficheiro):
    try:
        with open(caminho_ficheiro, 'r', encoding ='utf-8') as file:
            return json.load(file)
    except Exception as e:
        sg.popup_error(f"Error loading file: {e}")
        return None
    
# Função para guardar os dados no ficheiro
def guardar(caminho_ficheiro, dados):
    try:
        with open(caminho_ficheiro, 'w', encoding='utf-8') as file:
            json.dump(dados, file, indent=4)
            sg.popup("File saved successfully!")
    except Exception as e:
        sg.popup_error(f"Error saving file: {e}")


# Função para adicionar palavras-chave
def adicionar_keywords(window=None, keywords=""):
    layout_add_keyword = [
        [sg.Text("Keyword:", size=(20, 1)), sg.Input(key="-ADD_KEYWORD-")],
        [sg.Button("Cancel", key="-CANCEL-"), sg.Button("Confirm", key="-CONFIRM-")]
    ]

    window_add_keyword = sg.Window("Add Keywords", layout_add_keyword, modal=True)
    new_keywords = []

    running = True
    while running:
        event, values = window_add_keyword.read()
        if event in (sg.WINDOW_CLOSED, "-CANCEL-"):
            running = False

        elif event == "-CONFIRM-":
            keyword = values["-ADD_KEYWORD-"].strip()
            if keyword:
                existing_keywords = keywords.split(", ") if keywords else []
                if keyword in existing_keywords:
                    sg.popup("Keyword already exists in the list!")
                else:
                    new_keywords.append(keyword)
                window_add_keyword["-ADD_KEYWORD-"].update("")
            else:
                sg.popup("Please enter a keyword!")
            running = False

    window_add_keyword.close()
    
    if new_keywords:
        new_keyword = ", ".join(new_keywords)
        if window:  
            if keywords:
                keywords_list = keywords.split(", ")
                if new_keyword not in keywords_list:
                    keywords_list.extend(new_keywords)  
                    keywords = ", ".join(keywords_list)
            else:
                keywords = new_keyword
                keywords_list = new_keywords
            
            window["-KEYWORDS-"].update(values=keywords_list)  
            return keywords
        return new_keyword
    return keywords if window else ""


# Função para remover palavras-chave
def remover_keywords(window, values, keywords):
    selected_keywords = values["-KEYWORDS-"]
    if selected_keywords:
        if sg.popup_yes_no("Confirm", "Are you sure you want to remove the selected keywords?", 
                          icon=sg.SYSTEM_TRAY_MESSAGE_ICON_WARNING) == "Yes":
            keywords_list = keywords.split(", ")
            for keyword in selected_keywords:
                if keyword in keywords_list:
                    keywords_list.remove(keyword)
            keywords = ", ".join(keywords_list)
            window["-KEYWORDS-"].update(keywords_list)
    else:
        sg.popup("Please select a keyword to remove", title="No Selection")
    return keywords


# Função para adicionar autores
def adicionar_autores(window=None, autores=None):
    if autores is None:
        autores = []
        
    layout_add_author = [
        [sg.Text("Author name:", size=(20,1)), sg.Input(key="-AUTHOR_NAME-", size=(20,1))],
        [sg.Text("Affiliation name:", size=(20,1)), sg.Input(key="-AFFILIATION_NAME-", size=(20,1))],
        [sg.Text("ORCID:", size=(20,1)), sg.Input(key="-ORCID-", size=(20,1))],
        [sg.Button("Cancel", key="-CANCEL-"), sg.Button("Confirm", key="-CONFIRM-")]
    ]
    
    window_add_author = sg.Window("Add Authors", layout_add_author, modal=True)
    novos_autores = []
    
    running = True
    while running:
        event, values = window_add_author.read()
        if event in (sg.WINDOW_CLOSED, "-CANCEL-"):
            running = False
            
        elif event == "-CONFIRM-":
            author_name = values["-AUTHOR_NAME-"].strip()
            author_orcid = values["-ORCID-"].strip()
            
            if not author_name:
                sg.popup("Author name is required!")
                continue
            
            name_exists = any(autor["name"] == author_name for autor in autores)
            orcid_exists = any(autor.get("orcid") == author_orcid for autor in autores if autor.get("orcid"))
            
            if name_exists or orcid_exists:
                if name_exists:
                    sg.popup("Author name already exists in the list!")
                if orcid_exists:
                    sg.popup("ORCID already exists in the list!")
            else:
                autor = {
                    "name": author_name,
                    "affiliation": values["-AFFILIATION_NAME-"].strip(),
                    "orcid": author_orcid
                }
                novos_autores.append(autor)
                running = False
    
    window_add_author.close()
    
    if novos_autores and window:
        autores.extend(novos_autores)
        authors_info = [f"Name: {autor['name']}; Affiliation: {autor['affiliation']}" for autor in autores]
        window["-AUTHORS-"].update(authors_info)
        return autores
        
    return novos_autores if novos_autores else autores


# Função para remover autores
def remover_autores(window_popup, autores, selected_authors):
    for author in selected_authors:
        for autor in autores:
            if f"Name: {autor['name']}; Affiliation: {autor['affiliation']}" == author:
                autores.remove(autor)
    authors_info = [f"Name: {autor['name']}; Affiliation: {autor['affiliation']}" for autor in autores]
    window_popup["-AUTHORS-"].update(authors_info)
    return autores


# Função para verificar duplicados
def verificar_duplicados(publicacoes, title, doi, current_pub=None):
    for publicacao in publicacoes:
        if publicacao != current_pub: 
            if title and title.strip() == publicacao.get("title", ""):
                sg.popup("Title already exists in dataset")
                return True
            
            if doi and doi.strip() == publicacao.get("doi", ""):
                sg.popup("DOI already exists in dataset") 
                return True
                
    return False


# Função para criar publicações
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
        "abstract": abstract,
        "keywords": keywords,
        "authors": autores,
        "doi": doi,
        "pdf": pdf,
        "publish_date": publish_date,
        "title": title,
        "url": url,
    }

    publicacoes.append(nova_publicacao)
    return True


# Função para formatar as informações das publicações
def gerar_informacoes_publicacoes(dados):
    if dados is None:
        return ""

    info_total = ""
    for publicacao in dados if isinstance(dados, list) else [dados]:
        title = publicacao.get("title", "N/A")
        publish_date = publicacao.get("publish_date", "N/A")
        abstract = publicacao.get("abstract", "N/A")
        keywords = publicacao.get("keywords", "N/A")
        doi = publicacao.get("doi", "N/A")
        pdf = publicacao.get("pdf", "N/A")
        url = publicacao.get("url", "N/A")

        autores_info = ""
        for author in publicacao.get("authors", []):
            name = author.get("name", "N/A")
            afiliação = author.get("affiliation", "N/A")
            orcid = author.get("orcid", "N/A")
            autores_info += f"\nAuthor: {name}\nAffiliation: {afiliação}\nORCID: {orcid}\n"

        info = f"""Title: {title}

Publish Date: {publish_date}

Abstract: {abstract}

Keywords: {keywords}

Authors:{autores_info}
----
 
DOI: {doi}

PDF: {pdf}

URL: {url}

////\n""" 
        
        info_total += info
    return info_total


# Função para atualizar os elementos da interface gráfica com base no índice
def atualizar_elementos(index, publicacoes_links, window, current_links):
    publicacao = publicacoes_links[index][0]
    links = publicacoes_links[index][1]
    window['-PUBLICACAO-'].update(publicacao)
    window['-INDEX-'].update(f'{index + 1}/{len(publicacoes_links)}')
    window['-INDEX2-'].update(f'{index + 1}/{len(publicacoes_links)}')
    
    if "DOI: " in links:
        current_links["DOI"] = links.split('DOI: ')[1].split()[0]
        window['-DOI-'].update(f"DOI: {current_links['DOI']}")
    else:
        current_links["DOI"] = "N/A"
        window['-DOI-'].update(f"DOI: {current_links['DOI']}")
        
    if "PDF: " in links:
        current_links["PDF"] = links.split('PDF: ')[1].split()[0]
        window['-PDF-'].update(f"PDF: {current_links['PDF']}")
    else:
        current_links["PDF"] = "N/A"
        window['-PDF-'].update(f"PDF: {current_links['PDF']}")
        
    if "URL: " in links:
        current_links["URL"] = links.split('URL: ')[1].split()[0]
        window['-URL-'].update(f"URL: {current_links['URL']}")
    else:
        current_links["URL"] = "N/A"
        window['-URL-'].update(f"URL: {current_links['URL']}")


# Função para atualizar os elementos da janela
def mostrar_informacoes(dados):
    info_total = gerar_informacoes_publicacoes(dados)
    if not info_total:
        return

    publicacoes = [publicacao.strip() for publicacao in info_total.split("////") if publicacao.strip()]
    publicacoes_links = [publicacao.split("----") for publicacao in publicacoes]
    index = 0

    current_links = {"DOI": "", "PDF": "", "URL": ""}

    layout = [
        [sg.Multiline(size=(100, 30), key='-PUBLICACAO-', disabled=True)],
        [sg.Text("", enable_events=True, key='-DOI-', text_color='blue')],
        [sg.Text("", enable_events=True, key='-PDF-', text_color='blue')],
        [sg.Text("", enable_events=True, key='-URL-', text_color='blue')],
        [
            sg.Button('Previous', key='-PREVIOUS-'), sg.Text(f'{index + 1}/{len(publicacoes)}', key='-INDEX-'), 
            sg.Push(), sg.Button('Exit', key='-EXIT-'), sg.Push(), 
            sg.Text(f'{index + 1}/{len(publicacoes)}', key='-INDEX2-'), sg.Button('Next', key='-NEXT-')
        ]
    ]

    window = sg.Window('Document Information', layout)
    window.finalize()

    atualizar_elementos(index, publicacoes_links, window, current_links)

    running = True
    while running:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "-EXIT-"):
            running = False
        elif event == '-NEXT-':
            index = (index + 1) % len(publicacoes)
            atualizar_elementos(index, publicacoes_links, window, current_links)
        elif event == '-PREVIOUS-':
            index = (index - 1) % len(publicacoes)
            atualizar_elementos(index, publicacoes_links, window, current_links)
        elif event == '-DOI-':
            webbrowser.open(current_links["DOI"])
        elif event == '-PDF-':
            webbrowser.open(current_links["PDF"])
        elif event == '-URL-':
            webbrowser.open(current_links["URL"])

    window.close()


# Função para encontrar publicações
def encontrar_publicacao(publicacoes, titulo, doi):
    for publicacao in publicacoes:
        if publicacao.get("title") == titulo.strip():
            sg.popup("Publication found!")
            return publicacao
        elif doi:
            doi_stored = publicacao.get("doi", "")
            if doi_stored.endswith(doi):
                sg.popup("Publication found!")
                return publicacao
    sg.popup("No Publication Title!")
    return None


# Função para editar a informação de um dado autor 
def editar_autores(window_editar, values, autores):
    selected_authors = values["-AUTHORS-"]
    if not selected_authors:
        sg.popup("Please select an author to edit")
        return autores
        
    for author_entry in selected_authors:
        name, affiliation = author_entry.split("; ")
        name = name.split(": ")[1]
        affiliation = affiliation.split(": ")[1]
        autor = next((a for a in autores if a["name"] == name), None)
        
        if autor:
            layout_edit_author = [
            [sg.Text("Author name:", size=(20, 1)), sg.Input(default_text=autor.get("name", ""), key="-AUTHOR_NAME-", size=(40, 1))],
            [sg.Text("Affiliation name:", size=(20, 1)), sg.Input(default_text=autor.get("affiliation", ""), key="-AFFILIATION_NAME-", size=(40, 1))],
            [sg.Text("ORCID:", size=(20, 1)), sg.Input(default_text=autor.get("orcid", ""), key="-ORCID-", size=(40, 1))],
            [sg.Button("Save", key="-SAVE_AUTHOR-"), sg.Button("Cancel", key="-CANCEL_AUTHOR-")]
        ]
            window_edit_author = sg.Window("Edit Author", layout_edit_author, modal=True)
            
            running_editor_author = True
            while running_editor_author:
                event_author, values_author = window_edit_author.read()
                if event_author in (sg.WINDOW_CLOSED, "-CANCEL_AUTHOR-"):
                    running_editor_author = False
                    
                elif event_author == "-SAVE_AUTHOR-":
                    if not values_author["-AUTHOR_NAME-"].strip():
                        sg.popup("Author name is required!")
                        continue
                        
                    autor["name"] = values_author["-AUTHOR_NAME-"].strip()
                    autor["affiliation"] = values_author["-AFFILIATION_NAME-"].strip()
                    autor["orcid"] = values_author["-ORCID-"].strip()
                    running_editor_author = False
            
            window_edit_author.close()
            
            authors_info = [f"Name: {autor['name']}; Affiliation: {autor['affiliation']}" 
                        for autor in autores]
            window_editar["-AUTHORS-"].update(authors_info)
    
    return autores


# Função para atualizar as informações de uma dada publicação
def atualizar_publicacao(values, keywords, autores, publicacao_encontrada, caminho_ficheiro, publicacoes):
    title = values["-EDIT_TITLE-"].strip()
    doi = values["-EDIT_DOI-"].strip()

    if verificar_duplicados(publicacoes, title, doi, publicacao_encontrada):
        return False
    
    updated_publication = {
        "title": title,
        "abstract": values["-EDIT_ABSTRACT-"].strip(),
        "publish_date": values["-EDIT_DATE-"].strip(),
        "doi": doi,
        "pdf": values["-EDIT_PDF-"].strip(),
        "url": values["-EDIT_URL-"].strip(),
        "keywords": keywords,
        "authors": autores
    }

    for key, value in updated_publication.items():
        publicacao_encontrada[key] = value
    
    return True

# Função para remover publicação          
def remover_publicacao(publicacao_encontrada, caminho_ficheiro, publicacoes):
    publicacoes.remove(publicacao_encontrada)
    sg.popup("Publication removed successfully!")
    guardar(caminho_ficheiro, publicacoes)


# Função para mostrar na interface as informações com botão "save search"
def mostrar_informacoes_consultar(dados):
    info_total = gerar_informacoes_publicacoes(dados)
    if not info_total:
        return

    publicacoes = [publicacao.strip() for publicacao in info_total.split("////") if publicacao.strip()]
    publicacoes_links = [publicacao.split("----") for publicacao in publicacoes] 
    index = 0

    current_links = {"DOI": "", "PDF": "", "URL": ""}

    layout = [
        [sg.Multiline(size=(100, 30), key='-PUBLICACAO-', disabled=True)],
        [sg.Text("", enable_events=True, key='-DOI-', text_color='blue')],
        [sg.Text("", enable_events=True, key='-PDF-', text_color='blue')],
        [sg.Text("", enable_events=True, key='-URL-', text_color='blue')],
        [
            sg.Button('Previous', key='-PREVIOUS-'), sg.Text(f'{index + 1}/{len(publicacoes)}', key='-INDEX-'), 
            sg.Push(), sg.Button('Save Search', key='-SAVE_SEARCH-'), 
            sg.Button('Exit', key='-EXIT-'), sg.Push(), 
            sg.Text(f'{index + 1}/{len(publicacoes)}', key='-INDEX2-'), sg.Button('Next', key='-NEXT-')
        ]
    ]

    window = sg.Window('Document Information', layout, modal=True)
    window.finalize()

    atualizar_elementos(index, publicacoes_links, window, current_links)

    running = True
    while running:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "-EXIT-"):
            running = False
        elif event == '-NEXT-':
            index = (index + 1) % len(publicacoes)
            atualizar_elementos(index, publicacoes_links, window, current_links)
        elif event == '-PREVIOUS-':
            index = (index - 1) % len(publicacoes)
            atualizar_elementos(index, publicacoes_links, window, current_links)
        elif event == '-DOI-':
            if current_links["DOI"]:
                webbrowser.open(current_links["DOI"])
        elif event == '-PDF-':
            if current_links["PDF"]:
                webbrowser.open(current_links["PDF"])
        elif event == '-URL-':
            if current_links["URL"]:
                webbrowser.open(current_links["URL"])
        elif event == '-SAVE_SEARCH-':
            layout_save = [
                [sg.Button("Save as Text", key="-SAVE_TEXT-")],
                [sg.Button("Save as JSON", key="-SAVE_JSON-")],
                [sg.Button("Close", key="-CLOSE-")]
            ]

            window_save = sg.Window("Save Search", layout_save, modal=True)

            save_running = True
            while save_running:
                event_save, values_save = window_save.read()
                if event_save in (sg.WINDOW_CLOSED, "-CLOSE-"):
                    save_running = False

                elif event_save == "-SAVE_TEXT-":
                    caminho_arquivo = sg.popup_get_file("Save as", save_as=True, no_window=True, file_types=(("Text Files", "*.txt"),))
                    if caminho_arquivo:
                        with open(caminho_arquivo, 'a', encoding='utf-8') as f:
                            f.write(info_total)
                        sg.popup("Search saved successfully!")

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

            window_save.close()

    window.close()
    

# Função para ordeanr os títulos alfabéticamente e por data de publicação
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


# Função para procurar publicação com filtros 
def pesquisar_com_filtros(publicacoes):
    keywords_list, _ = contar_frequencia_palavras_chave(publicacoes)
    authors_list, _ = contar_frequencia_autores(publicacoes)
    affiliations_list, _ = contar_frequencia_afiliacoes(publicacoes)
    
    layout_filter_search = [
        [sg.Text("Search Publications with Filters", font=('Helvetica', 16), justification='center')],
        [sg.Text("Keyword:", size=(15, 1)), sg.Combo(values=list(keywords_list), key="-FILTER_KEYWORD-", size=(40, 1))],
        [sg.Text("Author:", size=(15, 1)), sg.Combo(values=list(authors_list), key="-FILTER_AUTHOR-", size=(40, 1))],
        [sg.Text("Affiliation:", size=(15, 1)), sg.Combo(values=list(affiliations_list), key="-FILTER_AFFILIATION-", size=(40, 1))],
        [sg.Text("Start Date:", size=(15, 1)), sg.Input(key="-FILTER_START_DATE-", size=(20, 1)), sg.CalendarButton("Select", target="-FILTER_START_DATE-", format="%Y-%m-%d")],
        [sg.Text("End Date:", size=(15, 1)), sg.Input(key="-FILTER_END_DATE-", size=(20, 1)), sg.CalendarButton("Select", target="-FILTER_END_DATE-", format="%Y-%m-%d")],
        [sg.Button("Search", key="-SEARCH-"), sg.Button("Exit", key="-EXIT-")]
    ]
    
    window_filter_search = sg.Window("Search with Filters", layout_filter_search, modal=True)

    filter_search_running = True
    while filter_search_running:
        event_filter_search, values_filter_search = window_filter_search.read()

        if event_filter_search in (sg.WINDOW_CLOSED, "-EXIT-"):
            filter_search_running = False

        elif event_filter_search == "-SEARCH-":
            keyword = values_filter_search["-FILTER_KEYWORD-"]
            author = values_filter_search["-FILTER_AUTHOR-"]
            affiliation = values_filter_search["-FILTER_AFFILIATION-"]
            start_date = values_filter_search["-FILTER_START_DATE-"]
            end_date = values_filter_search["-FILTER_END_DATE-"]

            filtered_publications = publicacoes

            if keyword:
                filtered_publications = [pub for pub in filtered_publications if keyword.lower() in pub.get("keywords", "").lower()]

            if author:
                filtered_publications = [pub for pub in filtered_publications if any(author.lower() in a.get("name", "").lower() for a in pub.get("authors", []))]

            if affiliation:
                filtered_publications = [pub for pub in filtered_publications if any(affiliation.lower() in a.get("affiliation", "").lower() for a in pub.get("authors", []))]

            try:
                if start_date:
                    start_date = datetime.strptime(start_date, "%Y-%m-%d")
                if end_date:
                    end_date = datetime.strptime(end_date, "%Y-%m-%d")

                if start_date and end_date:
                    filtered_publications = [
                        pub for pub in filtered_publications
                        if "publish_date" in pub and pub["publish_date"]
                        and start_date <= datetime.strptime(pub["publish_date"][-10:], "%Y-%m-%d") <= end_date
                    ]
            except ValueError:
                sg.popup_error("Invalid date format. Please use YYYY-MM-DD.")

            if filtered_publications:
                mostrar_informacoes_consultar(filtered_publications)
            else:
                sg.popup("No publications found matching the criteria.")

    window_filter_search.close()


# Função para encontrar um publicação de um dado título da "listbox"
def consultar_por_titulo(publicacoes):
    ordered_title_list, ordered_title_date, ordered_title_date_rev = ordenar_titulos(publicacoes)

    layout_consultar_title = [
        [sg.Text("Title List", justification="center", font=('Helvetica', 16))],
        [sg.Listbox(values=ordered_title_list, size=(150, 40), key="-TITLE_LIST-", select_mode="single", enable_events=True)],
        [
            sg.Button("Exit", key="-EXIT-"),
            sg.Button("Latest", key="-SORT_LATEST_TITLE-"),
            sg.Button("Oldest", key="-SORT_OLDEST_TITLE-"),
            sg.Button("Alphabetical", key="-ALPHABETICAL_TITLE-"),
        ],
    ]

    window_consultar_title = sg.Window("Search by Title", layout_consultar_title, modal=True)

    title_running = True
    while title_running:
        event_title, values_title = window_consultar_title.read()

        if event_title in (sg.WINDOW_CLOSED, "-EXIT-"):
            title_running = False

        elif event_title == "-TITLE_LIST-":
            selected_title = values_title["-TITLE_LIST-"]
            if selected_title:
                selected_title = selected_title[0]
                publicacao_selecionada = next((p for p in publicacoes if p.get("title") == selected_title), None)
                if publicacao_selecionada:
                    mostrar_informacoes_consultar(publicacao_selecionada)
                else:
                    sg.popup("Could not find the selected publication.")

        elif event_title == "-SORT_LATEST_TITLE-":
            window_consultar_title["-TITLE_LIST-"].update(values=ordered_title_date_rev)

        elif event_title == "-SORT_OLDEST_TITLE-":
            window_consultar_title["-TITLE_LIST-"].update(values=ordered_title_date)

        elif event_title == "-ALPHABETICAL_TITLE-":
            window_consultar_title["-TITLE_LIST-"].update(values=ordered_title_list)

    window_consultar_title.close()


# Função para ordeanr os autores alfabéticamente e pela sua frequencia 
def contar_frequencia_autores(publicacoes):
    author_frequency = {}
    for publicacao in publicacoes:
        for autor in publicacao.get("authors", []):
            name = autor.get("name", "")
            if name:
                if name not in author_frequency:
                    author_frequency[name] = 0
                author_frequency[name] += 1
    
    author_list = sorted(author_frequency.keys())
    
    frequency_tuple_list = []
    for name in author_frequency.keys():
        count = author_frequency[name]
        frequency_tuple_list.append((name, count))
    
    ordered_author_frequency = sorted(frequency_tuple_list, key=lambda x: x[1], reverse=True)
    
    return author_list, ordered_author_frequency


# Função para encontrar um publicação de um dado autor da "listbox"
def consultar_por_autor(publicacoes):
    author_list, ordered_author_frequency = contar_frequencia_autores(publicacoes)

    layout_consultar_author = [
        [sg.Text("Author List", justification="center", font=('Helvetica', 16))],
        [sg.Listbox(values=author_list, size=(50, 30), key="-AUTHOR_LIST-", select_mode="single", enable_events=True)],
        [
            sg.Button("Exit", key="-EXIT-"),
            sg.Button("Alphabetical", key="-SORT_AUTHOR_NAME-"),
            sg.Button("Frequency", key="-SORT_AUTHOR_FREQUENCY-"),
        ],
    ]

    window_consultar_author = sg.Window("Search by Author", layout_consultar_author, modal=True)

    author_running = True
    while author_running:
        event_author, values_author = window_consultar_author.read()

        if event_author in (sg.WINDOW_CLOSED, "-EXIT-"):
            author_running = False

        elif event_author == "-AUTHOR_LIST-":
            select_author = values_author["-AUTHOR_LIST-"]
            if select_author:
                selected_author = select_author[0]
                publicacoes_autor = [publicacao for publicacao in publicacoes if any(autor.get("name") == selected_author for autor in publicacao.get("authors", []))]
                if publicacoes_autor:
                    mostrar_informacoes_consultar(publicacoes_autor)
                else:
                    sg.popup(f"No publications found for author '{selected_author}'.")

        elif event_author == "-SORT_AUTHOR_NAME-":
            window_consultar_author["-AUTHOR_LIST-"].update(values=author_list)

        elif event_author == "-SORT_AUTHOR_FREQUENCY-":
            author_sorted_by_frequency = [keyword for keyword, _ in ordered_author_frequency]
            window_consultar_author["-AUTHOR_LIST-"].update(values=author_sorted_by_frequency)

    window_consultar_author.close()


# Função para ordeanr as afiliações alfabéticamente e pela sua frequencia 
def contar_frequencia_afiliacoes(publicacoes):
    affiliation_frequency = {}
    for publicacao in publicacoes:
        for autor in publicacao.get("authors", []):
            affiliation = autor.get("affiliation", "")
            if affiliation:
                if affiliation not in affiliation_frequency:
                    affiliation_frequency[affiliation] = 0
                affiliation_frequency[affiliation] += 1

    affiliation_list = sorted(affiliation_frequency.keys())
    ordered_affiliation_frequency = sorted(affiliation_frequency.keys(), key=lambda affiliation: affiliation_frequency[affiliation], reverse=True)
    return affiliation_list, ordered_affiliation_frequency 


# Função para encontrar um publicação de uma dada afiliação da "listbox"
def consultar_por_afiliacao(publicacoes):
    affiliation_list, ordered_affiliation_frequency = contar_frequencia_afiliacoes(publicacoes)

    layout_consultar_affiliation = [
        [sg.Text("Affiliations List", justification="center", font=('Helvetica', 16))],
        [sg.Listbox(values=affiliation_list, size=(150, 40), key="-AFFILIATION_LIST-", select_mode="single", enable_events=True)],
        [
            sg.Button("Exit", key="-EXIT-"),
            sg.Button("Alphabetical", key="-SORT_AFFILIATION_NAME-"),
            sg.Button("Frequency", key="-SORT_AFFILIATION_FREQUENCY-"),
        ],
    ]

    window_consultar_affiliation = sg.Window("Search by Affiliation", layout_consultar_affiliation, modal=True)
    affiliation_running = True
    while affiliation_running:
        event_affiliation, values_affiliation = window_consultar_affiliation.read()

        if event_affiliation in (sg.WINDOW_CLOSED, "-EXIT-"):
            affiliation_running = False

        elif event_affiliation == "-AFFILIATION_LIST-":
            select_affiliation = values_affiliation["-AFFILIATION_LIST-"]
            if select_affiliation:
                selected_affiliation = select_affiliation[0]
                publicacoes_afiliacao = [publicacao for publicacao in publicacoes if any(autor.get("affiliation") == selected_affiliation for autor in publicacao.get("authors", []))]
                if publicacoes_afiliacao:
                    mostrar_informacoes_consultar(publicacoes_afiliacao)
                else:
                    sg.popup(f"No publications found for affiliation '{selected_affiliation}'.")

        elif event_affiliation == "-SORT_AFFILIATION_NAME-":
            window_consultar_affiliation["-AFFILIATION_LIST-"].update(values=affiliation_list)

        elif event_affiliation == "-SORT_AFFILIATION_FREQUENCY-":
            window_consultar_affiliation["-AFFILIATION_LIST-"].update(values=ordered_affiliation_frequency)

    window_consultar_affiliation.close()


# Função para ordeanr as palavras-chave alfabéticamente e pela sua frequencia 
def contar_frequencia_palavras_chave(publicacoes):
    keywords_frequency = {}
    for publicacao in publicacoes:
        keywords_string = publicacao.get("keywords", "")
        if keywords_string:
            for keyword in keywords_string.split(","):
                keyword = keyword.strip()
                if keyword:
                    if keyword not in keywords_frequency:
                        keywords_frequency[keyword] = 0
                    keywords_frequency[keyword] += 1

    keywords_list = sorted(keywords_frequency.keys())

    frequency_tuple_list = [(name, count) for name, count in keywords_frequency.items()]
    ordered_keywords_frequency = sorted(frequency_tuple_list, key=lambda x: x[1], reverse=True)

    return keywords_list, ordered_keywords_frequency


# Função para encontrar um publicação de uma dada palavra-chave da "listbox"
def consultar_por_palavras_chave(publicacoes):
    keywords_list, ordered_keywords_frequency = contar_frequencia_palavras_chave(publicacoes)

    layout_consultar_keywords = [
        [sg.Text("Keywords List", justification="center", font=('Helvetica', 16))],
        [sg.Listbox(values=keywords_list, size=(100, 30), key="-KEYWORDS_LIST-", select_mode="single", enable_events=True)],
        [
            sg.Button("Exit", key="-EXIT-"),
            sg.Button("Alphabetical", key="-SORT_KEYWORDS_NAME-"),
            sg.Button("Frequency", key="-SORT_KEYWORDS_FREQUENCY-"),
        ],
    ]

    window_consultar_keywords = sg.Window("Search by Keywords", layout_consultar_keywords, modal=True)

    keywords_running = True
    while keywords_running:
        event_keywords, values_keywords = window_consultar_keywords.read()

        if event_keywords in (sg.WINDOW_CLOSED, "-EXIT-"):
            keywords_running = False

        elif event_keywords == "-KEYWORDS_LIST-":
            select_keywords = values_keywords["-KEYWORDS_LIST-"]
            if select_keywords:
                selected_keywords = select_keywords[0]
                publicacoes_keywords = [publicacao for publicacao in publicacoes if selected_keywords in publicacao.get("keywords", [])]
                if publicacoes_keywords:
                    mostrar_informacoes_consultar(publicacoes_keywords)
                else:
                    sg.popup(f"No publications found for keyword '{selected_keywords}'.")

        elif event_keywords == "-SORT_KEYWORDS_NAME-":
            window_consultar_keywords["-KEYWORDS_LIST-"].update(values=keywords_list)

        elif event_keywords == "-SORT_KEYWORDS_FREQUENCY-":
            keywords_sorted_by_frequency = [keyword for keyword, _ in ordered_keywords_frequency]
            window_consultar_keywords["-KEYWORDS_LIST-"].update(values=keywords_sorted_by_frequency)

    window_consultar_keywords.close()


# Função para encontrar publicações num dado intervalo de tempo
def consultar_por_data(publicacoes):
    layout_consultar_date = [
        [sg.Text("Search for Date", justification="center", font=('Helvetica', 16))],
        [sg.Text("Start Date:"), sg.Input(key="-START_DATE-", size=(15, 1)), sg.CalendarButton("Select", target="-START_DATE-", format="%Y-%m-%d")],
        [sg.Text("End Date: "), sg.Input(key="-END_DATE-", size=(15, 1)), sg.CalendarButton("Select", target="-END_DATE-", format="%Y-%m-%d")],
        [sg.Button("Exit", key="-EXIT-"), sg.Button("Confirm", key="-DATE_CONFIRM-")],
    ]

    window_consultar_date = sg.Window("Search by Date", layout_consultar_date, modal=True)

    date_running = True
    while date_running:
        event_date, values_date = window_consultar_date.read()

        if event_date in (sg.WINDOW_CLOSED, "-EXIT-"):
            date_running = False

        elif event_date == "-DATE_CONFIRM-":
            start_date = values_date.get("-START_DATE-", "")
            end_date = values_date.get("-END_DATE-", "")

            valid_start_date = True
            valid_end_date = True

            # Verificar o formato das datas
            if start_date:
                try:
                    start_date = datetime.strptime(start_date, "%Y-%m-%d")
                except ValueError:
                    sg.popup_error("Invalid start date format. Please use YYYY-MM-DD.")
                    valid_start_date = False

            if end_date:
                try:
                    end_date = datetime.strptime(end_date, "%Y-%m-%d")
                except ValueError:
                    sg.popup_error("Invalid end date format. Please use YYYY-MM-DD.")
                    valid_end_date = False

            if valid_start_date and valid_end_date:
                if not start_date or not end_date:
                    sg.popup("Please select both dates.")
                else:
                    publicacoes_no_intervalo = []
                    for publicacao in publicacoes:
                        publish_date = publicacao.get("publish_date", "")

                        if publish_date:
                            try:
                                data_part = publish_date[-10:]
                                data_publicacao = datetime.strptime(data_part, "%Y-%m-%d")
                                if start_date <= data_publicacao <= end_date:
                                    publicacoes_no_intervalo.append(publicacao)
                            except ValueError:
                                sg.popup_error(f"Invalid publication date format for publication: {publicacao.get('title', 'Unknown Title')}")
                                
                    if publicacoes_no_intervalo:
                        mostrar_informacoes_consultar(publicacoes_no_intervalo)
                    else:
                        sg.popup("No publications found in the selected date range.")

    window_consultar_date.close()


# Função que desenha um gráfico matplotlib na janela da interface
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


# Função que apresenta um gráfico de barras com a distribuição de publicações por ano
def mostrar_distribuicao_publicacoes_por_ano(publicacoes):
    publication_years = {}
    for publicacao in publicacoes:
        publish_date = publicacao.get("publish_date", "Unknown")
        if publish_date != "Unknown":
            try:
                publish_date_clean = publish_date.split()[-1]
                year = datetime.strptime(publish_date_clean, "%Y-%m-%d").year
                publication_years[year] = publication_years.get(year, 0) + 1
            except ValueError:
                publication_years["Unknown"] = publication_years.get("Unknown", 0) + 1

    years = list(publication_years.keys())
    counts = list(publication_years.values())

    fig, ax = plt.subplots()
    ax.bar(years, counts)
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Publications")
    ax.set_title("Distribution of Publications by Year")

    layout_year = [
        [sg.Text("Publication Distribution by Year", justification="center", size=(30, 1))],
        [sg.Canvas(key="-CANVAS-")],
        [sg.Button("Exit", key="-EXIT-")]
    ]

    window_year = sg.Window("Publication Distribution by Year", layout_year, modal=True, finalize=True)

    draw_figure(window_year["-CANVAS-"].TKCanvas, fig)

    running = True
    while running:
        event_year, values_year = window_year.read()
        if event_year in (sg.WINDOW_CLOSED, "-EXIT-"):
            running = False

    window_year.close()

# Função que extrai e retorna uma lista ordenada de anos únicos das publicações
def extrair_anos_publicacao(publicacoes):
    publication_years = []
    for publicacao in publicacoes:
        publish_date = publicacao.get("publish_date", "Unknown")
        if publish_date != "Unknown":
            try:
                publish_date_clean = publish_date.split()[-1]
                year = datetime.strptime(publish_date_clean, "%Y-%m-%d").year
                publication_years.append(year)
            except ValueError:
                year = None
            if year:
                publication_years.append(year)
    return sorted(set(publication_years))


# Função que mostra um gráfico interativo da distribuição de publicações por mês para um ano selecionado
def mostrar_distribuicao_publicacoes_por_mes(publicacoes):
    publication_years = extrair_anos_publicacao(publicacoes)

    layout_year = [
        [sg.Text("Publication Years:", justification="center", size=(30, 1))],
        [sg.Listbox(values=publication_years, size=(20, 10), key="-PUBLICATION_YEARS-", select_mode="single", enable_events=True)],
        [sg.Button("Exit", key="-EXIT-")]
    ]

    window_year = sg.Window("Publication Distribution by Year", layout_year, modal=True)

    year_running = True
    while year_running:
        event_year, values_year = window_year.read()

        if event_year in (sg.WINDOW_CLOSED, "-EXIT-"):
            year_running = False

        elif event_year == "-PUBLICATION_YEARS-":
            selected_year = values_year["-PUBLICATION_YEARS-"]
            if selected_year:
                try:
                    selected_year = int(selected_year[0])
                    publication_months = [0] * 12
                    
                    for publicacao in publicacoes:
                        publish_date = publicacao.get("publish_date", "Unknown")
                        if publish_date != "Unknown":
                            try:
                                publish_date_clean = publish_date.split()[-1]
                                date = datetime.strptime(publish_date_clean, "%Y-%m-%d")
                                if date.year == selected_year:
                                    publication_months[date.month - 1] += 1
                            except ValueError:
                                pass
           
                    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                    fig, ax = plt.subplots()
                    ax.bar(months, publication_months)
                    ax.set_xlabel("Month")
                    ax.set_ylabel("Number of Publications")
                    ax.set_title(f"Distribution of Publications by Month for {selected_year}")
                    plt.tight_layout()

                    layout_month = [
                        [sg.Text(f"Publication Distribution by Month for {selected_year}", justification="center", size=(30, 1))],
                        [sg.Canvas(key="-CANVAS-")],
                        [sg.Button("Exit", key="-EXIT-")]
                    ]

                    window_month = sg.Window("Publication Distribution by Month", layout_month, modal=True, finalize=True)
                    draw_figure(window_month["-CANVAS-"].TKCanvas, fig)

                    month_running = True
                    while month_running:
                        event_month, values_month = window_month.read()
                        if event_month in (sg.WINDOW_CLOSED, "-EXIT-"):
                            month_running = False
                    window_month.close()
                                
                except ValueError:
                    sg.popup_error("Invalid year format")

    window_year.close()


# Função que apresenta um gráfico horizontal com o número de publicações dos 20 autores mais produtivos
def mostrar_numero_publicacoes_por_autor(publicacoes):
    _, ordered_authors = contar_frequencia_autores(publicacoes)

    top_20_authors = ordered_authors[:20]

    author_names = [author[0] for author in top_20_authors]
    publication_counts = [author[1] for author in top_20_authors]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(author_names, publication_counts)
    ax.set_xlabel("Number of Publications")
    ax.set_ylabel("Authors")
    ax.set_title("Number of Publications per Author")
    plt.gca().invert_yaxis()
    plt.tight_layout()

    layout_author = [
        [sg.Text("Number of publications per author", justification="center", size=(30, 1))],
        [sg.Canvas(key="-CANVAS-")],
        [sg.Button("Exit", key="-EXIT-")]
    ]

    window_author = sg.Window("Number of publications per author", layout_author, modal=True, finalize=True)
    draw_figure(window_author["-CANVAS-"].TKCanvas, fig)

    author_running = True
    while author_running:
        event_author, values_author = window_author.read()

        if event_author in (sg.WINDOW_CLOSED, "-EXIT-"):
            author_running = False

    window_author.close()


# Função que mostra um gráfico interativo da distribuição de publicações por ano para um autor selecionado
def mostrar_distribuicao_publicacoes_por_autor(publicacoes):
    author_list, _ = contar_frequencia_autores(publicacoes)

    layout_author_selection = [
        [sg.Text("Select an Author:", justification="center", size=(30, 1))],
        [sg.Listbox(values=author_list, size=(50, 20), key="-AUTHOR_LIST-", select_mode="single", enable_events=True)],
        [sg.Button("Exit", key="-EXIT-")]
    ]

    window_author_selection = sg.Window("Select Author", layout_author_selection, modal=True)

    author_selection_running = True
    while author_selection_running:
        event_author_selection, values_author_selection = window_author_selection.read()

        if event_author_selection in (sg.WINDOW_CLOSED, "-EXIT-"):
            author_selection_running = False

        elif event_author_selection == "-AUTHOR_LIST-":
            selected_author = values_author_selection["-AUTHOR_LIST-"]
            if selected_author:
                selected_author = selected_author[0]

                author_publication_years = {}
                for publicacao in publicacoes:
                    publish_date = publicacao.get("publish_date", "Unknown")
                    if publish_date != "Unknown":
                        try:
                            publish_date_clean = publish_date.split()[-1]
                            year = datetime.strptime(publish_date_clean, "%Y-%m-%d").year
                            for autor in publicacao.get("authors", []):
                                if autor.get("name", "Unknown") == selected_author:
                                    author_publication_years[year] = author_publication_years.get(year, 0) + 1
                        except ValueError:
                            pass  
                
                years = list(author_publication_years.keys())
                counts = list(author_publication_years.values())

                fig, ax = plt.subplots(figsize=(10, 6))  
                ax.bar(years, counts)
                ax.set_xlabel("Year")
                ax.set_ylabel("Number of Publications")
                ax.set_title(f"Distribution of Publications by Year for {selected_author}")
                plt.tight_layout()

                layout_year_distribution = [
                    [sg.Text(f"Publication Distribution by Year for {selected_author}", justification="center", size=(40, 1))],
                    [sg.Canvas(key="-CANVAS-")],
                    [sg.Button("Exit", key="-EXIT-")]
                ]

                window_year_distribution = sg.Window("Publication Distribution by Year", layout_year_distribution, modal=True, finalize=True)
                draw_figure(window_year_distribution["-CANVAS-"].TKCanvas, fig)

                year_distribution_running = True
                while year_distribution_running:
                    event_year_distribution, values_year_distribution = window_year_distribution.read()

                    if event_year_distribution in (sg.WINDOW_CLOSED, "-EXIT-"):
                        year_distribution_running = False

                window_year_distribution.close()

    window_author_selection.close()


# Função que apresenta um gráfico horizontal com a frequência das 20 palavras-chave mais comuns
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


# Função que mostra um gráfico interativo das 20 palavras-chave mais frequentes para um ano específico
def mostrar_distribuicao_palavras_chave_por_ano(publicacoes):
    publication_years = extrair_anos_publicacao(publicacoes)

    layout_year_selection = [
        [sg.Text("Select a Year:", justification="center", size=(30, 1))],
        [sg.Listbox(values=publication_years, size=(20, 10), key="-YEAR_LIST-", select_mode="single", enable_events=True)],
        [sg.Button("Exit", key="-EXIT-")]
    ]

    window_year_selection = sg.Window("Select Year", layout_year_selection, modal=True)

    year_selection_running = True
    while year_selection_running:
        event_year_selection, values_year_selection = window_year_selection.read()

        if event_year_selection in (sg.WINDOW_CLOSED, "-EXIT-"):
            year_selection_running = False

        elif event_year_selection == "-YEAR_LIST-":
            selected_year = values_year_selection["-YEAR_LIST-"]
            if selected_year:
                selected_year = int(selected_year[0])

                publicacoes_filtradas = []
                for publicacao in publicacoes:
                    publish_date = publicacao.get("publish_date", "")
                    if publish_date.startswith(str(selected_year)):
                        publicacoes_filtradas.append(publicacao)
                
                _, ordered_keywords = contar_frequencia_palavras_chave(publicacoes_filtradas)

                top_20_keywords = [keyword for keyword, _ in ordered_keywords[:20]]
                keyword_counts = [count for _, count in ordered_keywords[:20]]

                fig, ax = plt.subplots(figsize=(10, 6))
                ax.barh(top_20_keywords, keyword_counts)
                ax.set_xlabel("Keywords Frequency")
                ax.set_ylabel("Keywords")
                ax.set_title(f"Top 20 Keywords in {selected_year}")
                plt.gca().invert_yaxis()
                plt.tight_layout() 

                layout_keyword_distribution = [
                    [sg.Text(f"Top 20 Keywords in {selected_year}", justification="center", size=(40, 1))],
                    [sg.Canvas(key="-CANVAS-")],
                    [sg.Button("Exit", key="-EXIT-")]
                ]

                window_keyword_distribution = sg.Window("Top 20 Keywords in Year", layout_keyword_distribution, modal=True, finalize=True)
                draw_figure(window_keyword_distribution["-CANVAS-"].TKCanvas, fig)

                keyword_distribution_running = True
                while keyword_distribution_running:
                    event_keyword_distribution, values_keyword_distribution = window_keyword_distribution.read()

                    if event_keyword_distribution in (sg.WINDOW_CLOSED, "-EXIT-"):
                        keyword_distribution_running = False

                window_keyword_distribution.close()

    window_year_selection.close()