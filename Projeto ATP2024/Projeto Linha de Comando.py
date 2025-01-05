import json
import os
from datetime import datetime

#C:\Users\ze05p\OneDrive\Documentos\Licenciatura em Engenharia Biomédica\2º Ano\1º Semestre\Algoritmos e Técnicas de Programação\Projeto\ata_medica_papers.json
def carregar_arquivo(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading file: {e}")
        return []

def guardar_arquivo(publications, path):
    try:
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(publications, file, indent=4, ensure_ascii=False)
        print(f"Data saved successfully to {path}")
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

def criar_publicacao(publications, current_path=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n=== Create New Publication ===")
    publication = {
        "title": input("Title: "),
        "abstract": input("Abstract: "),
        "keywords": adicionar_keywords(),
        "authors": adicionar_autores(),
        "doi": input("DOI: "),
        "publish_date": validar_data(),
        "url": input("URL: ")
    }
    publications.append(publication)
    
    if current_path:
        guardar_arquivo(publications, current_path)
    
    return publications

def adicionar_keywords():
    keywords = []
    print("Enter keywords (press Enter with empty input to finish):")
    while True:
        keyword = input("Keyword: ").strip()
        if not keyword:
            break
        keywords.append(keyword)
    return ', '.join(keywords)

def validar_data():
    while True:
        date_str = input("Publication date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Invalid date format! Please use YYYY-MM-DD")
    
def adicionar_autores():
    authors = []
    while True:
        name = input("Author name (or ENTER to finish): ")
        if not name:
            break
        affiliation = input("Affiliation: ")
        authors.append({"name": name, "affiliation": affiliation})
    return authors

def titulo_por_data(publications, newest_first=True):
    pub_dates = []
    for p in publications:
        date_str = p.get("publish_date", "")
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d") if date_str else datetime.min
        except ValueError:
            date = datetime.min
        pub_dates.append((p, date))
    
    sorted_pubs = [pub for pub, _ in sorted(pub_dates, key=lambda x: x[1], reverse=newest_first)]
    display_paginated(sorted_pubs)
    return sorted_pubs

def titulo_por_alfabetica(publications):
    sorted_pubs = sorted(publications, key=lambda x: x.get("title", "N/A"))
    display_paginated(sorted_pubs)
    return sorted_pubs

def procurar_titulo(publications):
    search = input("Enter title to search: ")
    results = [p for p in publications if search.lower() in p.get("title", "").lower()]
    
    if not results:
        print(f"No publications found with title containing '{search}'")
        return None
    
    print(f"\nFound {len(results)} publications:")
    mostrar_publicacao(results)
    return results

def autor_por_frequencia(publications):
    author_pubs = {}
    for pub in publications:
        for author in pub.get("authors", []):
            name = author.get("name", "N/A")
            if name not in author_pubs:
                author_pubs[name] = []
            if pub not in author_pubs[name]:
                author_pubs[name].append(pub)
    
    sorted_authors = sorted(author_pubs.items(), 
                          key=lambda x: len(x[1]), 
                          reverse=True)
    
    display_items = [f"{author} ({len(pubs)})" for author, pubs in sorted_authors]
    display_paginated(display_items)
    return sorted_authors

def autor_por_alfabetica(publications):
    authors = set()
    for pub in publications:
        for author in pub.get("authors", []):
            authors.add(author.get("name", "N/A"))
    
    sorted_authors = sorted(authors)
    display_paginated(sorted_authors)
    return sorted_authors

def procurar_autor(publications):
    author = input("Enter author name: ")
    results = [p for p in publications if any(author.lower() in a.get("name", "").lower() for a in p.get("authors", []))]
    if not results:
        print(f"No publications found with author '{author}'")
        return None
    
    print(f"\nFound {len(results)} publications:")
    mostrar_publicacao(results)
    return results

def affiliation_por_frequencia(publications):
    affiliation_pubs = {}
    for pub in publications:
        for author in pub.get("authors", []):
            aff = author.get("affiliation", "N/A")
            if aff not in affiliation_pubs:
                affiliation_pubs[aff] = []
            if pub not in affiliation_pubs[aff]:
                affiliation_pubs[aff].append(pub)
    
    sorted_affiliations = sorted(affiliation_pubs.items(), 
                               key=lambda x: len(x[1]), 
                               reverse=True)
    
    display_items = [f"{aff} ({len(pubs)})" for aff, pubs in sorted_affiliations]
    display_paginated(display_items)
    return sorted_affiliations

def affiliation_por_alfabetica(publications):
    affiliations = set()
    for pub in publications:
        for author in pub.get("authors", []):
            affiliations.add(author.get("affiliation", "N/A"))
    
    sorted_affiliations = sorted(affiliations)
    display_paginated(sorted_affiliations)
    return sorted_affiliations

def procurar_affiliation(publications):
    affiliation = input("Enter affiliation: ")
    results = [p for p in publications 
              if any(affiliation.lower() in a.get("affiliation", "").lower() 
                    for a in p.get("authors", []))]
    
    if not results:
        print(f"No publications found with affiliation '{affiliation}'")
        return None
    
    print(f"\nFound {len(results)} publications:")
    mostrar_publicacao(results)
    return results

def keywords_por_frequencia(publications):
    keyword_freq = {}
    keyword_pubs = {}
    for pub in publications:
        keywords = pub.get("keywords", "").split(",")
        for keyword in keywords:
            keyword = keyword.strip()
            if keyword:
                keyword_freq[keyword] = keyword_freq.get(keyword, 0) + 1
                if keyword not in keyword_pubs:
                    keyword_pubs[keyword] = []
                keyword_pubs[keyword].append(pub)
    
    sorted_keywords = sorted(keyword_freq.items(), key=lambda x: x[1], reverse=True)
    display_paginated([keyword for keyword, _ in sorted_keywords])
    return sorted_keywords

def keywords_por_alfabetica(publications):
    keyword_pubs = {}
    for pub in publications:
        for keyword in pub.get("keywords", "").split(","):
            keyword = keyword.strip()
            if keyword:
                if keyword not in keyword_pubs:
                    keyword_pubs[keyword] = []
                keyword_pubs[keyword].append(pub)
    
    sorted_keywords = sorted(keyword_pubs.keys())
    display_paginated(sorted_keywords)
    return sorted_keywords

def procurar_keyword(publications):
    keyword = input("Enter keyword: ")
    results = [p for p in publications if keyword.lower() in p.get("keywords", "").lower()]
    
    if not results:
        print(f"No publications found with keyword '{keyword}'")
        return None
    
    print(f"\nFound {len(results)} publications:")
    mostrar_publicacao(results)
    return results

def procurar_data(publications):
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Use YYYY-MM-DD")
        return None

    results = []
    for pub in publications:
        pub_date_str = pub.get("publish_date", "")
        try:
            pub_date = datetime.strptime(pub_date_str, "%Y-%m-%d")
            if start <= pub_date <= end:
                results.append(pub)
        except ValueError:
            continue
    
    if not results:
        print(f"No publications found between {start_date} and {end_date}")
        return None
        
    print(f"\nFound {len(results)} publications:")
    mostrar_publicacao(results)
    return results

def editar_keywords(keywords_str):
    # Convert string to list
    keywords = [k.strip() for k in keywords_str.split(',') if k.strip()] if keywords_str else []
    
    while True:
        print("\nCurrent keywords:")
        for i, keyword in enumerate(keywords, 1):
            print(f"{i}. {keyword}")
            
        print("\nOptions:")
        print("1. Add new keyword")
        print("2. Edit keyword")
        print("3. Delete keyword")
        print("0. Return")
        
        choice = input("Choose option: ")
        
        if choice == "0":
            return ', '.join(keywords)
        elif choice == "1":
            new_keyword = input("New keyword: ").strip()
            if new_keyword:
                keywords.append(new_keyword)
        elif choice == "2":
            try:
                idx = int(input("Keyword number to edit: ")) - 1
                if 0 <= idx < len(keywords):
                    print(f"\nCurrent keyword: {keywords[idx]}")
                    keywords[idx] = input("New keyword: ").strip()
                else:
                    print("Invalid keyword number!")
            except ValueError:
                print("Invalid input!")
        elif choice == "3":
            try:
                idx = int(input("Keyword number to delete: ")) - 1
                if 0 <= idx < len(keywords):
                    del keywords[idx]
                    print("Keyword deleted!")
                else:
                    print("Invalid keyword number!")
            except ValueError:
                print("Invalid input!")
        else:
            print("Invalid option!")

def editar_autores(authors):
    while True:
        print("\nCurrent authors:")
        for i, author in enumerate(authors, 1):
            print(f"{i}. {author.get('name', 'N/A')} ({author.get('affiliation', 'N/A')})")
            
        print("\nOptions:")
        print("1. Add new author")
        print("2. Edit author")
        print("3. Delete author")
        print("0. Return")
        
        choice = input("Choose option: ")
        
        if choice == "0":
            return authors
        elif choice == "1":
            name = input("Name: ")
            affiliation = input("Affiliation: ")
            authors.append({"name": name, "affiliation": affiliation})
        elif choice == "2":
            try:
                idx = int(input("Author number to edit: ")) - 1
                if 0 <= idx < len(authors):
                    print("\nCurrent values:")
                    print(f"Name: {authors[idx].get('name', 'N/A')}")
                    print(f"Affiliation: {authors[idx].get('affiliation', 'N/A')}")
                    authors[idx]["name"] = input("\nNew name: ")
                    authors[idx]["affiliation"] = input("New affiliation: ")
                else:
                    print("Invalid author number!")
            except ValueError:
                print("Invalid input!")
        elif choice == "3":
            try:
                idx = int(input("Author number to delete: ")) - 1
                if 0 <= idx < len(authors):
                    del authors[idx]
                    print("Author deleted!")
                else:
                    print("Invalid author number!")
            except ValueError:
                print("Invalid input!")
        else:
            print("Invalid option!")

def atualizar_publicacao(publications, current_path=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n=== Update Publication ===")
    if not publications:
        print("No publications loaded!")
        return publications
    print("\nSearch publication by:")
    print("1. Title")
    print("2. DOI")
    option = input("Choose option: ")
    
    if option == "1":
        search = input("Enter title: ")
        pub_list = [p for p in publications if search.lower() in p.get("title", "").lower()]
    elif option == "2":
        search = input("Enter DOI: ")
        pub_list = [p for p in publications if search == p.get("doi", "")]
    else:
        print("Invalid option!")
        return publications
        
    if not pub_list:
        print("Publication not found!")
        return publications
        
    if len(pub_list) > 1:
        print("\nMultiple publications found:")
        for i, pub in enumerate(pub_list, 1):
            print(f"{i}. {pub.get('title', 'N/A')} (DOI: {pub.get('doi', 'N/A')})")
        try:
            idx = int(input("\nSelect publication number: ")) - 1
            pub = pub_list[idx]
        except (ValueError, IndexError):
            print("Invalid selection!")
            return publications
    else:
        pub = pub_list[0]
    
    while True:
        print("\nUpdate options:")
        print("1. Title")
        print("2. Abstract")
        print("3. Keywords")
        print("4. Authors")
        print("5. DOI")
        print("6. Publication date")
        print("7. URL")
        print("8. Delete publication")
        print("0. Return to menu")
        
        choice = input("Choose field to update: ")
        
        if choice == "0":
            if current_path:
                guardar_arquivo(publications, current_path)
                break
        elif choice == "1":
            print(f"Current title: {pub.get('title', 'N/A')}")
            pub["title"] = input("New title: ")
        elif choice == "2":
            print(f"Current abstract: {pub.get('abstract', 'N/A')}")
            pub["abstract"] = input("New abstract: ")
        elif choice == "3":
            pub["keywords"] = editar_keywords(pub.get("keywords", ""))
        elif choice == "4":
            pub["authors"] = editar_autores(pub.get("authors", []))
        elif choice == "5":
            print(f"Current DOI: {pub.get('doi', 'N/A')}")
            pub["doi"] = input("New DOI: ")
        elif choice == "6":
            print(f"Current date: {pub.get('publish_date', 'N/A')}")
            pub["publish_date"] = validar_data()
        elif choice == "7":
            print(f"Current URL: {pub.get('url', 'N/A')}")
            pub["url"] = input("New URL: ")
        elif choice == "8":
            if input("Type 'DELETE' to confirm: ").upper() == "DELETE":
                publications.remove(pub)
                print("Publication deleted!")
                if current_path:
                    guardar_arquivo(publications, current_path)
                return publications
        else:
            print("Invalid option!")
                    
    return publications

def buscar_publicacao(publications):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n=== Search Publication ===")
    running = True
    while running:
        print("\nSearch by:")
        print("1. Title")
        print("2. Author")
        print("3. Affiliation")
        print("4. Keywords")
        print("5. Date")
        print("0. Close")
        
        option = input("Choose an option: ")
        
        if option == "0":
            running = False
            
        elif option == "1":
            submenu_running = True
            while submenu_running:
                print("\nTitle options:")
                print("1. Sort by newest first")
                print("2. Sort by oldest first")
                print("3. Sort alphabetically")
                print("4. Search specific title")
                print("0. Close")
                
                title_option = input("Choose an option: ")
                
                if title_option == "0":
                    submenu_running = False
                elif title_option == "1":
                    titulo_por_data(publications, newest_first=True)
                elif title_option == "2":
                    titulo_por_data(publications, newest_first=False)
                elif title_option == "3":
                    titulo_por_alfabetica(publications)
                elif title_option == "4":
                    procurar_titulo(publications)
                else:
                    print("Invalid title option!")
        
        elif option == "2":
            submenu_running = True
            while submenu_running:
                print("\nAuthor options:")
                print("1. Sort by frequency")
                print("2. Sort alphabetically")
                print("3. Search specific author")
                print("0. Close")
                
                author_option = input("Choose an option: ")
                
                if author_option == "0":
                    submenu_running = False
                elif author_option == "1":
                    autor_por_frequencia(publications)
                elif author_option == "2":
                    autor_por_alfabetica(publications)
                elif author_option == "3":
                    procurar_autor(publications)
                else:
                    print("Invalid author option!")

        elif option == "3":
            submenu_running = True
            while submenu_running:
                print("\nAffiliation options:")
                print("1. Sort by frequency")
                print("2. Sort alphabetically")
                print("3. Search specific affiliation")
                print("0. Close")

                affiliation_option = input("Choose an option: ")
                
                if affiliation_option == "0":
                    submenu_running = False
                elif affiliation_option == "1":
                    affiliation_por_frequencia(publications)
                elif affiliation_option == "2":
                    affiliation_por_alfabetica(publications)
                elif affiliation_option == "3":
                    procurar_affiliation(publications)
        
        elif option == "4":
            submenu_running = True
            while submenu_running:
                print("\nKeyword options:")
                print("1. Sort by frequency")
                print("2. Sort alphabetically") 
                print("3. Search specific keyword")
                print("0. Close")
                
                keyword_option = input("Choose an option: ")
                
                if keyword_option == "0":
                    submenu_running = False
                elif keyword_option == "1":
                    keywords_por_frequencia(publications)
                elif keyword_option == "2":
                    keywords_por_alfabetica(publications)
                elif keyword_option == "3":
                    procurar_keyword(publications)
                else:
                    print("Invalid keyword option!")
        
        elif option == "5":
            procurar_data(publications)
        
        else:
            print("Invalid option!")
            
    return []

def mostrar_publicacao(publications, items_per_page=1):
    if isinstance(publications, dict):
        publications = [publications]
    
    total_items = len(publications)
    total_pages = (total_items + items_per_page - 1) // items_per_page
    current_page = 1
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        start_idx = (current_page - 1) * items_per_page
        end_idx = start_idx + items_per_page
        
        print(f"\nPublication {current_page}/{total_pages}")
        print("-" * 50)
        
        for pub in publications[start_idx:end_idx]:
            print(f"\nTitle: {pub.get('title', 'N/A')}")
            print(f"Abstract: {pub.get('abstract', 'N/A')}")
            print(f"Keywords: {pub.get('keywords', 'N/A')}")
            print("\nAuthors:")
            authors = pub.get('authors', [])
            if authors:
                for author in authors:
                    name = author.get('name', 'N/A')
                    affiliation = author.get('affiliation', 'N/A')
                    print(f"- {name} ({affiliation})")
            else:
                print("- N/A")
            print(f"DOI: {pub.get('doi', 'N/A')}")
            print(f"Date: {pub.get('publish_date', 'N/A')}")
            print(f"URL: {pub.get('url', 'N/A')}")
            
        if total_pages > 1:
            print("\nNavigation:")
            print("n - Next publication")
            print("p - Previous publication")
            print("q - Return to menu")
            
            choice = input("\nEnter choice: ").lower()
            
            if choice == 'n' and current_page < total_pages:
                current_page += 1
            elif choice == 'p' and current_page > 1:
                current_page -= 1
            elif choice == 'q':
                break
        else:
            input("\nPress Enter to continue...")
            break

def gerar_estatisticas(publications):
    if not publications:
        print("No publications to analyze!")
        return
        
    running = True
    while running:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== Statistics Menu ===")
        print("1. Publications by year")
        print("2. Publications by author")
        print("3. Most common keywords")
        print("0. Return to menu")
        
        option = input("\nChoose an option: ")
        
        if option == "0":
            running = False
        
        elif option == "1":
            years = {}
            for pub in publications:
                date = pub.get("publish_date", "N/A")
                if date != "N/A":
                    year = date.split("-")[0]
                    years[year] = years.get(year, 0) + 1
            
            stats = [f"{year}: {qty} publications" for year, qty in sorted(years.items())]
            display_paginated(stats)
            
        elif option == "2":
            authors = {}
            for pub in publications:
                for author in pub.get("authors", []):
                    name = author.get("name", "N/A")
                    authors[name] = authors.get(name, 0) + 1
            
            stats = [f"{author}: {qty} publications" for author, qty in 
                    sorted(authors.items(), key=lambda x: x[1], reverse=True)]
            display_paginated(stats)
            
        elif option == "3":
            keywords = {}
            for pub in publications:
                keywords_str = pub.get("keywords", "")
                if keywords_str:
                    for kw in keywords_str.split(","):
                        kw = kw.strip()
                        if kw:
                            keywords[kw] = keywords.get(kw, 0) + 1
            
            stats = [f"{kw}: {qty} occurrences" for kw, qty in 
                    sorted(keywords.items(), key=lambda x: x[1], reverse=True)]
            display_paginated(stats)
            
        else:
            print("Invalid option!")

def display_paginated(items, items_per_page=10):
    total_items = len(items)
    total_pages = (total_items + items_per_page - 1) // items_per_page
    current_page = 1
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        start_idx = (current_page - 1) * items_per_page
        end_idx = start_idx + items_per_page
        
        print(f"\nPage {current_page}/{total_pages} (Total items: {total_items})")
        print("-" * 50)
        
        for i, item in enumerate(items[start_idx:end_idx], start=start_idx + 1):
            if isinstance(item, dict):
                print(f"{i}. {item.get('title', 'N/A')}")
            else:
                print(f"{i}. {item}")
                
        print("\nNavigation:")
        print("n - Next page")
        print("p - Previous page")
        print("q - Return to menu")
        
        choice = input("\nEnter choice: ").lower()
        
        if choice == 'n' and current_page < total_pages:
            current_page += 1
        elif choice == 'p' and current_page > 1:
            current_page -= 1
        elif choice == 'q':
            break

def merge_publications(existing_pubs, new_pubs):
    dois = {pub.get('doi') for pub in existing_pubs if pub.get('doi')}
    merged = existing_pubs.copy()
    
    for pub in new_pubs:
        if pub.get('doi') not in dois:
            merged.append(pub)
    return merged

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    publications = []
    current_path = ""
    while True:
        print("\n=== Main Menu ===")
        print("1. Upload file")
        print("2. Add publication") 
        print("3. Update publication")
        print("4. Search publications")
        print("5. View Docuemnt")
        print("6. Publication Statistics")
        print("0. Exit")
        
        option = input("\nChoose an option: ")
        
        if option == "1":
            path = input("JSON file path: ")
            loaded_pubs = carregar_arquivo(path)
            if loaded_pubs:
                if publications:  # If existing publications
                    choice = input("Merge with existing publications? (y/n): ").lower()
                    if choice == 'y':
                        publications = merge_publications(publications, loaded_pubs)
                        print(f"Merged! Total publications: {len(publications)}")
                    else:
                        publications = loaded_pubs  # Replace existing
                else:
                    publications = loaded_pubs  # First load
                current_path = path
                input("\nPress Enter to continue...")

        elif option == "2":
            if not publications:
                print("No publications loaded!")
            else:
                publications = criar_publicacao(publications, current_path)

        elif option == "3":
            if not publications:
                print("No publications loaded!")
            else:
                publications = atualizar_publicacao(publications, current_path)

        elif option == "3":
            if not publications:
                print("No publications loaded!")
            else:
                buscar_publicacao(publications)

        elif option == "4":
            if not publications:
                print("No publications loaded!")
            else:
                buscar_publicacao(publications)

        elif option == "5":
            if not publications:
                print("No publications loaded!")
            else:
                print(f"\nTotal publications: {len(publications)}")
                mostrar_publicacao(publications)
            
        elif option == "6":
            if not publications:
                print("No publications loaded!")
            else:
                gerar_estatisticas(publications)
        elif option == "0":
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    menu()