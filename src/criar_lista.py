def criar_lista(listas):
    while True:
        nome_lista = input("Qual o nome da lista que você deseja criar?\n")

        if nome_lista in listas.items():
            print("Essa lista já existe.")
        else:
            listas[nome_lista] = []
            print(f"A lista '{nome_lista}' foi criada com sucesso")
            break
