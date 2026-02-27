from src.functions.adcionar_item import adcionar_item
from src.functions.ver_itens import ver_itens
from src.functions.remover_item import remover_item

def menu_lista(listas, option):
    while True:
        print(f"\nVocê está na lista '{option}'")
        print("1. Adcionar item")
        print("2. Remover item")
        print("3. Ver todos os itens")
        print("4. Sair")

        escolha = int(input("\nEscolha uma das opções acima:\n"))
        
        match escolha:
            case 1: adcionar_item(listas, option)
            case 2: remover_item(listas, option)
            case 3: ver_itens(listas, option)
            case 4: 
                break
    return