def ver_itens(listas,option):
    if not listas[option]:
        print("\nA lista está vazia.")
    else:
        for itens in listas[option]:
            print(f"- {itens}")
    return
