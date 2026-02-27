def adcionar_item(listas,option):
    item = input("\nAdcione um item:\n")
    if item in listas[option]:
        print("Esse item já existe.")
    else:
        listas[option].append(item)
        print(f"\n'{item}' adicionado com sucesso!")
    return