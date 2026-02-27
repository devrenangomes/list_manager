def criar_lista(listas):
    while True:
        nome_lista = input("\nQual o nome da lista que você deseja criar?\n")

        if nome_lista in listas:
            print("Essa lista já existe.")
        else:
            listas[nome_lista] = []
            print(f"\nA lista '{nome_lista}' foi criada com sucesso!")
            break

    return