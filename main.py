from src.criar_lista import criar_lista

listas = {}

while True:
    print("=== Sistema de Gerenciamento de Listas")
    print("1. Criar Lista")
    print("2. Acessar Lista")
    print("3. Sair")

    option = int(input("Escolha uma das opções acima:\n"))
    match option:
        case 1: criar_lista(listas)
        case 3: 
            print("Encerrando...")
            break



