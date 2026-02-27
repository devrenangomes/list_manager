from src.functions.criar_lista import criar_lista
from src.menus.acessar_lista import acessar_lista

listas = {}

while True:
    print(f"\n=== Gerenciador de listas ===")
    print("1. Criar Lista")
    print("2. Acessar Lista")
    print("3. Sair")

    option = int(input("\nEscolha uma das opções acima:\n"))
    match option:
        case 1: criar_lista(listas)
        case 2: acessar_lista(listas)
        case 3: 
            print("Encerrando...")
            break
            



