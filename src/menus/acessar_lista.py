from src.menus.menu_lista import menu_lista

def acessar_lista(listas):
    while True:
        for lista in listas:
            print(f"- {lista}")
        option = input("\nEscolha uma das listas acima:\n")
        if option in listas:
            menu_lista(listas, option)
        else:
            print("Essa lista não existe.")
        break
    
    return      
