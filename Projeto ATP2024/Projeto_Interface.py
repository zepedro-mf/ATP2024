import PySimpleGUI as sg
from Projeto_Funções import *

layout_menu = [
    [sg.Text("Welcome to JSON Document Reader!")],
    [sg.Button("Upload Document", key="-UPLOAD-")],
    [sg.Button("Add Publication", key="-ADD_PUBLICATION-")],
    [sg.Button("Update Publication", key="-UPDATE_PUBLICATION-")],
    [sg.Button("Search Publication", key="-SEARCH_PUBLICATION-")],
    [sg.Button("View Document", key="-VIEW_DOCUMENT-")],
    [sg.Button("Publication Statistics", key="-PUBLICATION_STATISTICS-")],
    [sg.Button("Exit", key="-EXIT-")],
]
window_menu = sg.Window("Main Menu", layout_menu)

publicacoes = []
caminho_ficheiro = None

running = True
while running:
    event, _ = window_menu.read()

    if event in (sg.WINDOW_CLOSED, "-EXIT-"):
        running = False

    elif event == "-UPLOAD-":
        caminho_ficheiro = sg.popup_get_file("Select the JSON file", file_types=(("JSON Files", "*.json"),), no_window=True)
        if caminho_ficheiro:
            publicacoes.extend(carregar(caminho_ficheiro))
            sg.popup("Uploaded File")
    
    elif event in ("-ADD_PUBLICATION-", "-UPDATE_PUBLICATION-", "-SEARCH_PUBLICATION-", "-VIEW_DOCUMENT-", "-PUBLICATION_STATISTICS-"):
        if not publicacoes:
            sg.popup("No file has been uploaded.")
        else:
            if event == "-VIEW_DOCUMENT-":
                mostrar_informacoes(publicacoes)
                
            elif event == "-ADD_PUBLICATION-":
                layout_popup = [
                    [sg.Text("Title:", font=("Helvetica", 14), size=(15, 1)), sg.Multiline(key="-TITLE-", size=(80, 5))],
                    [sg.Text("Abstract:", font=("Helvetica", 14), size=(15, 1)), sg.Multiline(size=(80, 10), key="-ABSTRACT-")],
                    [sg.Text("Publish Date:", font=("Helvetica", 14), size=(15, 1)), sg.Input(key="-PUBLISH_DATE-", size=(72, 1), readonly=True), sg.CalendarButton("Select", target="-PUBLISH_DATE-", format="%Y-%m-%d")],
                    [
                        sg.Column([
                            [sg.Text("Keywords:", font=("Helvetica", 14), size=(15, 1)), sg.Button("Add", key="-ADD_KEYWORDS-"), sg.Button("Remove", key="-REMOVE_KEYWORDS-")],
                            [sg.Listbox(values=[], key="-KEYWORDS-", size=(40, 5))]
                        ]),sg.Push(),
                        sg.Column([
                            [sg.Text("Authors:", font=("Helvetica", 14), size=(15, 1)), sg.Button("Add", key="-ADD_AUTHORS-"), sg.Button("Remove", key="-REMOVE_AUTHORS-")],
                            [sg.Listbox(values=[], key="-AUTHORS-", size=(40, 5))]
                        ])
                    ],
                    [sg.Text("DOI:", font=("Helvetica", 14), size=(15, 1)), sg.Input(key="-DOI-", size=(80, 1))],
                    [sg.Text("PDF (URL or path):", font=("Helvetica", 14), size=(15, 1)), sg.Input(key="-PDF-", size=(80, 1))],
                    [sg.Text("Article URL:", font=("Helvetica", 14), size=(15, 1)), sg.Input(key="-URL-", size=(80, 1))],
                    [sg.Button("Save", key="-SAVE-"), sg.Button("Cancel", key="-CANCEL-")],
                ]
                window_popup = sg.Window("Add Publication", layout_popup, modal=True)
                
                autores = []
                keywords = ""

                popup_running = True
                while popup_running:
                    event, values = window_popup.read()
                    if event in (sg.WINDOW_CLOSED, "-CANCEL-"):
                        popup_running = False
                    
                    elif event == "-ADD_KEYWORDS-":
                       keywords = adicionar_keywords(window_popup, keywords)
                    
                    elif event == "-REMOVE_KEYWORDS-":
                        keywords = remover_keywords(window_popup, values, keywords)
                        
                    elif event == "-ADD_AUTHORS-":
                        autores = adicionar_autores(window_popup, autores)
                                        
                    elif event == "-REMOVE_AUTHORS-":
                        selected_authors = values["-AUTHORS-"]
                        if selected_authors:
                            if sg.popup_yes_no("Confirm", "Are you sure you want to remove the selected authors?", 
                                            icon=sg.SYSTEM_TRAY_MESSAGE_ICON_WARNING) == "Yes":
                                autores = remover_autores(window_popup, autores, selected_authors)
                        else:
                            sg.popup("Please select an author to remove")

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
                            
                window_popup.close()
            
            elif event == "-UPDATE_PUBLICATION-":
                layout_update  = [
                    [sg.Text("Post title:", size = (20,1)), sg.Multiline(key= "-POST_TITLE-", size = (40,3))],
                    [sg.Text("Post DOI:", size = (20,1)), sg.Multiline(key= "-DOI-", size = (40,3))],
                    [sg.Button("Cancel", key = "-CANCEL-"), sg.Button("Confirm", key = "-CONFIRM-")],
                ]
                window_update = sg.Window("Post Update", layout_update, modal = True)
                
                publicacao_encontrada = []

                update_running = True 
                while update_running:
                    event, values = window_update.read()

                    if event in (sg.WINDOW_CLOSED, "-CANCEL-"):
                        update_running = False  

                    elif event == "-CONFIRM-":
                        titulo = values["-POST_TITLE-"]
                        doi = values["-DOI-"]
                        publicacao_encontrada = encontrar_publicacao(publicacoes, titulo, doi)
                        if publicacao_encontrada:
                            update_running = False

                window_update.close()
        
                if publicacao_encontrada:
                    layout_editar = [
                        [sg.Text("Title:", font=("Helvetica", 14), size=(15, 1)), sg.Multiline(default_text=publicacao_encontrada.get("title", ""), key="-EDIT_TITLE-", size=(100, 5))],
                        [sg.Text("Abstract:", font=("Helvetica", 14), size=(15, 1)), sg.Multiline(default_text=publicacao_encontrada.get("abstract", ""), size=(100, 10), key="-EDIT_ABSTRACT-")],
                        [sg.Text("Publish Date:", font=("Helvetica", 14), size=(15, 1)), sg.Input(default_text=publicacao_encontrada.get("publish_date", ""), key="-EDIT_DATE-", size=(92, 1), readonly=True), sg.CalendarButton("Select", target="-EDIT_DATE-", format="%Y-%m-%d")],
                        [
                            sg.Column([
                                [sg.Text("Keywords:", font=("Helvetica", 14), size=(15, 1)), sg.Button("Add", key="-ADD_KEYWORDS-"), sg.Button("Remove", key="-REMOVE_KEYWORDS-")],
                                [sg.Listbox(values=[keyword.strip() for keyword in publicacao_encontrada.get("keywords", "").split(",")], key="-KEYWORDS-", size=(60, 5))]
                            ]), sg.Push(),
                            sg.Column([
                                [sg.Text("Authors:", font=("Helvetica", 14), size=(15, 1)), sg.Button("Add", key="-ADD_AUTHORS-"), sg.Button("Remove", key="-REMOVE_AUTHORS-"), sg.Button("Edit", key="-EDIT_AUTHORS-")],
                                [sg.Listbox(values=[f"Name: {author['name']}; Affiliation: {author['affiliation']}" for author in publicacao_encontrada.get("authors", [])], key="-AUTHORS-", size=(60, 5))]
                            ])
                        ],
                        [sg.Text("DOI:", font=("Helvetica", 14), size=(15, 1)), sg.Input(default_text=publicacao_encontrada.get("doi", ""), key="-EDIT_DOI-", size=(100, 1))],
                        [sg.Text("PDF (URL or path):", font=("Helvetica", 14), size=(15, 1)), sg.Input(default_text=publicacao_encontrada.get("pdf", ""), key="-EDIT_PDF-", size=(100, 1))],
                        [sg.Text("Article URL:", font=("Helvetica", 14), size=(15, 1)), sg.Input(default_text=publicacao_encontrada.get("url", ""), key="-EDIT_URL-", size=(100, 1))],
                        [sg.Button("Save", key="-SAVE-"), sg.Button("Cancel", key="-CANCEL-"), sg.Button("Delete Post", key="-DELETE_POST-")]
                    ] 
                    window_editar = sg.Window("Edit Publication", layout_editar, modal=True)

                    keywords = publicacao_encontrada.get("keywords", "")
                    autores = publicacao_encontrada.get("authors", [])

                    edit_running = True
                    while edit_running:
                        event, values = window_editar.read()

                        if event in (sg.WINDOW_CLOSED, "-CANCEL-"):  
                            edit_running = False

                        elif event == "-ADD_AUTHORS-":
                            autores = adicionar_autores(window_editar, autores)

                        elif event == "-REMOVE_AUTHORS-":
                            selected_authors = values["-AUTHORS-"]
                            if selected_authors:
                                if sg.popup_yes_no("Confirm", "Are you sure you want to remove the selected authors?", 
                                                icon=sg.SYSTEM_TRAY_MESSAGE_ICON_WARNING) == "Yes":
                                    autores = remover_autores(window_editar, autores, selected_authors)
                            else:
                                sg.popup("Please select an author to remove")

                        elif event == "-EDIT_AUTHORS-":
                            autores = editar_autores(window_editar, values, autores)

                        elif event == "-ADD_KEYWORDS-":
                            keywords = adicionar_keywords(window_editar, keywords)

                        elif event == "-REMOVE_KEYWORDS-":
                            keywords = remover_keywords(window_editar, values, keywords)

                        elif event == "-SAVE-":
                            if not values["-EDIT_TITLE-"].strip() and not values["-EDIT_DOI-"].strip():
                                sg.popup("Title or DOI is required!")
                            else:
                                if atualizar_publicacao(values, keywords, autores, publicacao_encontrada, caminho_ficheiro, publicacoes):
                                    if caminho_ficheiro:
                                        guardar(caminho_ficheiro, publicacoes)
                                        sg.popup("Publication successfully updated!")
                                        edit_running = False
                                    else:
                                        sg.popup("No file selected.")

                        elif event == "-DELETE_POST-":
                            if sg.popup_yes_no("Confirm", "Are you sure you want to remove this publication?", 
                                            icon=sg.SYSTEM_TRAY_MESSAGE_ICON_WARNING) == "Yes":
                                remover_publicacao(publicacao_encontrada, caminho_ficheiro, publicacoes)
                                edit_running = False

                    window_editar.close()
                    
            elif event == "-SEARCH_PUBLICATION-":
                layout_consultar_menu = [
                    [sg.Button("Search with filters", key="-SEARCH_FILTER-")],
                    [sg.Button("Search by title", key="-SEARCH_TITLE-")],
                    [sg.Button("Search by author", key="-SEARCH_AUTHOR-")],
                    [sg.Button("Search for affiliation", key="-SEARCH_AFFILIATION-")],
                    [sg.Button("Search for keywords", key="-SEARCH_KEYWORDS-")],
                    [sg.Button("Search by date", key="-SEARCH_DATE-")],
                    [sg.Button("Exit", key="-EXIT-")],
                ]

                window_consultar_menu = sg.Window("Search Menu", layout_consultar_menu, modal=True)

                consultar_running = True
                while consultar_running:
                    event_consultar, values_consultar = window_consultar_menu.read()

                    if event_consultar in (sg.WINDOW_CLOSED, "-EXIT-"):
                        consultar_running = False
                    
                    elif event_consultar == "-SEARCH_FILTER-":
                        pesquisar_com_filtros(publicacoes)

                    elif event_consultar == "-SEARCH_TITLE-":
                        consultar_por_titulo(publicacoes)
                    
                    elif event_consultar == "-SEARCH_AUTHOR-":
                        consultar_por_autor(publicacoes)

                    elif event_consultar == "-SEARCH_AFFILIATION-":
                        consultar_por_afiliacao(publicacoes)
                    
                    elif event_consultar == "-SEARCH_KEYWORDS-":
                        consultar_por_palavras_chave(publicacoes)
                    
                    elif event_consultar == "-SEARCH_DATE-":
                        consultar_por_data(publicacoes)
                    
                window_consultar_menu.close()

            elif event == "-PUBLICATION_STATISTICS-":
                layout_statistics = [
                    [sg.Text("Publication Statistics", justification="center", size=(30, 1))],
                    [sg.Button("Distribution of publications by year.", key="-PUBLICATION_YEAR-")],
                    [sg.Button("Distribution of publications by month of a given year.", key="-PUBLICATION_MONTH-")],
                    [sg.Button("Number of publications per author", key="-AUTHOR_NUMBER-")],
                    [sg.Button("Distribution of an author's publications by years", key="-AUTHOR_PUBLICATION-")],
                    [sg.Button("Distribution of keywords by frequency", key="-KEYWORD_NUMBER-")],
                    [sg.Button("Most frequent keywords distribution per year", key="-KEYWORD_YEAR-")],
                    [sg.Button("Exit", key="-EXIT-")],
                ]
                window_statistics = sg.Window("Dataset Statistics", layout_statistics, modal=True)

                statistics_running = True
                while statistics_running:
                    event_statistics, values_statistics = window_statistics.read()

                    if event_statistics in (sg.WINDOW_CLOSED, "-EXIT-"):
                        statistics_running = False

                    elif event_statistics == "-PUBLICATION_YEAR-":
                        mostrar_distribuicao_publicacoes_por_ano(publicacoes)

                    elif event_statistics == "-PUBLICATION_MONTH-":
                        mostrar_distribuicao_publicacoes_por_mes(publicacoes)
                    
                    elif event_statistics == "-AUTHOR_NUMBER-":
                        mostrar_numero_publicacoes_por_autor(publicacoes)
                    
                    elif event_statistics == "-AUTHOR_PUBLICATION-":
                        mostrar_distribuicao_publicacoes_por_autor(publicacoes)
                    
                    elif event_statistics == "-KEYWORD_NUMBER-":
                        mostrar_distribuicao_palavras_chave(publicacoes)

                    elif event_statistics == "-KEYWORD_YEAR-":
                        mostrar_distribuicao_palavras_chave_por_ano(publicacoes)

                window_statistics.close()