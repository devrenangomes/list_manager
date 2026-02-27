def remover_item(listas, option):
    remover = input("\nQual item você deseja remover?\n")
    if remover not in listas[option]:
        print("Esse item não existe.")
    else:
        listas[option].remove(remover)
    return