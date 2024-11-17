def menu():
    MyFaceBook = [
    {   
        'id': 'p1',
        'conteudo': 'A tarefa de avaliação é talvez a mais ingrata das tarefas que um professor tem de realizar...',
        'autor': 'jcr',
        'dataCriacao': '2023-07-20',
        'comentarios': [
            {
                'comentario': 'Completamente de acordo...',
                'autor': 'prh'
            },
            {
                'comentario': 'Mas há quem goste...',
                'autor': 'jj'
            }
        ]
    },
    {
        'id': 'p2',
        'conteudo': 'Conteúdo da segunda postagem',
        'autor': 'Ana',
        'dataCriacao': '2023-07-21',
        'comentarios': [
            {
                'comentario': 'Ola, tudo bem',
                'autor': 'prh'
            },
            {
                'comentario': 'Gosto muito!!',
                'autor': 'Ana'
            }
        ]
    },
    {
        "id": "p3",
        "conteudo": "Conteúdo da segunda postagem",
        "autor": "Paulo",
        "dataCriacao": "2023-06-21",
        "comentarios": []
    },
    {
        "id": "p4",
        "conteudo": "Conteúdo da segunda postagem",
        "autor": "Paulo",
        "dataCriacao": "2023-07-28",
        "comentarios": []
    }
    ]

    v = True 
    while v == True:
        print("""\n===== Menu =====
(1): Número de Posts;
(2): Procurar por Autor;
(3): Ordenar Posts por ordem alfabética de autores;
(4): Criar um Post;
(5): Remover Post por ID;
(6): Distribuição do Posts por autor;
(7): Posts comentados por Autor;
(0): Sair da aplicação""") 
        modo = int(input("Que modo deseja? "))

        if modo == 1:
            quantosPost(MyFaceBook)
        elif modo == 2:
            postsAutor(MyFaceBook, input("Que autor deseja procurar? "))
        elif modo == 3:
            autores(MyFaceBook)
        elif modo == 4:
            insPost(MyFaceBook, input("Descrição do Post. "), input("Nome do Autor. "), input("Data da publicação. "), [])
        elif modo == 5:
            remPost(MyFaceBook, input("Qual é o ID do post?"))
        elif modo == 6:
            postsPorAutor(MyFaceBook)
        elif modo == 7:
           comentadoPor(MyFaceBook, input("Que Autor deseja procura? "))
        elif modo == 0: 
            print("Programa Encerrado.")
            v = False
        else:
            print("Insira um modo válido!")

def quantosPost(redeSocial):
    return print(f" Atualmente há {len(redeSocial)} posts.")

def postsAutor(redeSocial, autor):
    res = [post for post in redeSocial if post.get("autor") == autor]
    if res: 
        for post in res:
            print(f"""\nID: {post["id"]}
Conteúdo: {post["conteudo"]}
Autor: {post["autor"]}
Data: {post["dataCriacao"]}
Comentários:""")
            if post["comentarios"]:
                for comentario in post["comentarios"]:
                    print(f"  - {comentario['autor']}: {comentario['comentario']}")
            else:
                print("  Nenhum comentário")
    else:
        print(f"O autor {autor} não tem posts.")

def autores(redeSocial):
    x = sorted(redeSocial, key = lambda post: post["autor"].lower())
    for post in x:
        print(f"""\nID: {post["id"]}
Conteúdo: {post["conteudo"]}
Autor: {post["autor"]}
Data : {post["dataCriacao"]}
Comentarios:""")
        if post["comentarios"]:
            for comentario in post["comentarios"]:
                print(f"  - {comentario['autor']}: {comentario['comentario']}")
        else:
            print("  Nenhum comentário")

def insPost(redeSocial, conteudo, autor, dataCriacao, comentarios):
    redeSocial.append({"id": f"p{len(redeSocial) + 1}",
                       "conteudo": conteudo, 
                       "autor": autor,
                       "dataCriacao": dataCriacao,
                       "comentarios": comentarios,})
    for post in redeSocial:
        print(f"""\nID: {post["id"]}
Conteúdo: {post["conteudo"]}
Autor: {post["autor"]}
Data : {post["dataCriacao"]}
Comentarios:""")
        if post["comentarios"]:
            for comentario in post["comentarios"]:
                print(f"  - {comentario['autor']}: {comentario['comentario']}")
        else:
            print("  Nenhum comentário")

def remPost(redeSocial, id):
    for post in redeSocial:
        if post["id"] == id:
            redeSocial.remove(post)
    for post in redeSocial:
        print(f"""\nID: {post["id"]}
Conteúdo: {post["conteudo"]}
Autor: {post["autor"]}
Data : {post["dataCriacao"]}
Comentarios:""")
        if post["comentarios"]:
            for comentario in post["comentarios"]:
                print(f"  - {comentario['autor']}: {comentario['comentario']}")
        else:
            print("  Nenhum comentário")

def postsPorAutor(redeSocial):
    distribuicao = {} 
    
    for post in redeSocial:
        autor = post["autor"]
        if autor in distribuicao:
            distribuicao[autor].append(post)
        else:
            distribuicao[autor] = [post]
    for autor, posts in distribuicao.items():
        print(f"\nAutor: {autor}")
        for post in posts:
            print(f"  - ID: {post['id']}, Conteúdo: {post['conteudo']}")

def comentadoPor(redeSocial, autor):
    comentarios_do_autor = []
    
    for post in redeSocial:
        for comentario in post["comentarios"]:
            if comentario["autor"] == autor:
                comentarios_do_autor.append(comentario["comentario"])
    if comentarios_do_autor:
        print(f"Comentários feitos por {autor}:")
        for comentario in comentarios_do_autor:
            print(f"- {comentario}")
    else:
        print(f"O autor {autor} não fez nenhum comentário.")


menu()