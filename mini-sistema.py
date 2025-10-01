from colorama import Fore, Back, init
init(autoreset=True)
import time
import random
lista = []
def remover():
    time.sleep(0.5)
    for i, n in enumerate(lista, start=1):
        print(f"{i} - {n}")
        time.sleep(0.5)
        print()
    usuario = input(Fore.GREEN + "Digite a tarefa que deseja remover: ").strip()
    if usuario in lista:
        lista.remove(usuario)
        print(Fore.RED + Back.WHITE + f"Você tirou {usuario} da lista")
    else:
        print(Fore.RED + Back.WHITE + "essa tarefa não existe")
def adicionar():
    usuario = input(Fore.CYAN + "Qual tarefa deseja adicionar: ").strip()
    time.sleep(0.3)
    print()
    lista.append(usuario.strip() + "\n")
    print(f"Você adicionou {usuario}")                         
    time.sleep(0.2)
def listar():
    for i, n in enumerate(lista, start=1):
        print(f"{i} - {n.strip()}")
        time.sleep(0.5)
        print()
def ler_e_salvar():
    try:
      linha = lista
      for l, n in enumerate(lista, start=1):
          print(f"{l} - {n.strip()}")
      usuario = input("Digite o arquivo para entrar nele: ")
      with open(usuario, "a", encoding="utf-8") as f:    
          f.writelines(linha)             
          print(f"tudo salvo em {usuario}")
    except FileNotFoundError:
        print("Arquivo não foi encontrado")
def remover_tudo():
    lista.clear()
    return(Fore.WHITE + Back.GREEN + "Você removeu tudo da sua lista!")
def ler_conteudo():    
    try:
        usuario = input("Digite qual arquivo deseja abrir para ler: ")
        with open(usuario, "r", encoding="utf-8") as ler:
            conteudo = ler.readlines()
            for linha in conteudo:
                print(linha.strip()) 
    except FileNotFoundError:
        print("Esse arquivo não existe!") 
def deletar_arquivo():
    try:
        delete = input("Digite o nome do arquivo para deletar: ")
        with open(delete, "r", encoding="utf-8") as f:
            print("Antes:")
            print(f.read())
        with open(delete, "w", encoding="utf-8") as f:
            print("depois:")
            f.write("")
            print("Arquivo deletado com sucesso!")
    except FileNotFoundError:
        print("ops, esse arquivo não existe tente outro")   

def menu_lista():
    while True:
        print(Fore.BLACK + Back.WHITE + "==== Menu DE Tarefas ====")
        time.sleep(1)
        print("1 - Adicionar")    
        print("2 - listar")    
        print("3 - salvar e ler arquivo")
        print("4 - sair")    
        print("5 - remover")    
        print("6 - remover tudo")   
        print("7 - ler arquivo")
        print("8 - deletar tudo de um arquivo")
        time.sleep(1)
        try:
            escolha = int(input("Digite sua escolha: "))
            if escolha == 1:
                print(adicionar())
            elif escolha == 2:
                print(listar())
            elif escolha == 3:
                print(ler_e_salvar())
            elif escolha == 4:
            
                try:
                    usuario = int(input(Fore.GREEN + "Você deseja realmente sair (aperte /1/ para sair /2/ continuar)"))
                    time.sleep(0.5)
                    if usuario == 1:
                        print(Fore.WHITE + Back.GREEN + "usuario escolheu sair")
                        break
                    elif usuario == 2:
                        print("voltando")
                except ValueError:
                    print(Fore.RED + "Digite apenas numeros!")
            elif escolha == 5: 
                print(remover())
            elif escolha == 6:
                print(remover_tudo())
            elif escolha == 7:
                print(ler_conteudo())
            elif escolha == 8:
                print(deletar_arquivo())
        except ValueError:
            print(Fore.YELLOW + Back.BLACK + "Digite apenas números")
            exit()
        except KeyboardInterrupt:
            print(Fore.YELLOW + Back.BLACK + "Conexão encerrada pelo usuario")  
            exit()
def menu_matematica():
    while True:
        print(Fore.WHITE + Back.GREEN + "=== Menu De Matematica ===")
        print("Escolha o modo da soma exemplo: +, -, /, x,")
        usuario = input("Escolha o modo de soma ou 'sair': ")
        if usuario == "+":
            try:
                nmr1 = int(input("Digite o primeiro numero: "))
                nmr2 = int(input("Agora digite o segundo: "))
                print(f"Resultado: {nmr1 + nmr2}")
            except ValueError:
                print(Fore.WHITE + Back.YELLOW + "Erro digite apenas numeros")
        elif usuario == "-":
            try:
                nmr1 = int(input("Digite o primeiro numero: "))
                nmr2 = int(input("Agora digite o segundo: "))
                print(f"Resultado: {abs(nmr1 - nmr2)}")
            except ValueError:
                print(Fore.WHITE + Back.YELLOW + f"Digite apenas números")
        elif usuario == "x":
            try:
                nmr1 = int(input("Digite o primeiro numero: "))
                nmr2 = int(input("Agora digite o segundo: "))
                print(f"Resultado: {nmr1 * nmr2}")
            except ValueError:
                print(Fore.WHITE + Back.YELLOW + f"Digite apenas números")        
        elif usuario == "/":          
            try:
                nmr1 = int(input("Digite o primeiro numero: "))
                nmr2 = int(input("Agora digite o segundo: "))
                print(f"Resultado: {nmr1 / nmr2}")
            except ZeroDivisionError:
                print(Fore.WHITE + Back.YELLOW + "Não é possivel dividir por 0")
        elif usuario == "sair":
            print("Voltando ao menu principal aguarde..")
            break
            time.sleep(2)
def jogo_de_adivinhar():
    while True:
        print(Fore.WHITE + Back.RED + "==== Adivinhe e ganhe ====")
        print()
        print(Fore.BLACK + Back.YELLOW + "1 - 1 vs 1")
        print("or")
        print(Fore.BLACK + Back.YELLOW + "2 - computador x jogador")
        usuario = int(input("Digite sua opção ou digite 3 para sair: "))
        if usuario == 1:
            total1 = 0
            total2 = 0
            robo = random.randint(1, 500)
            while total1 <= 3 and total2 <= 3:
                input("JOGADOR 1 - aperte enter: ")
                usuario1 = random.randint(1, 500)
                print(Fore.BLACK + Back.RED + f"Jogador 1 tirou o numero: {usuario1}")
                input("JOGADOR 2 - aperte enter: ")
                usuario2 = random.randint(1, 500)
                print(Fore.BLACK + Back.RED + f"Jogador 2 tirou o numero: {usuario2}")
                us1 = abs(robo - usuario1)
                us2 = abs(robo - usuario2)
                if us1 == us2:
                    print("empate!")
                elif us1 > us2:
                    total1 += 1
                    print("Jogador 1 chegou mais perto")
                    print(Fore.BLACK + Back.YELLOW + f"pontos do jogador 1 aumentou para: {total1}")
                elif us2 > us1:
                    total2 += 1
                    print("Jogador 2 chegou mais perto")     
                    print(Fore.BLACK + Back.YELLOW + f"Pontos aumentou para: {total2}")
            if total1 == 3:
                print(Fore.WHITE + Back.GREEN + "Jogador 1 é o campeão!")
                break
            elif total2 == 3:
                print(Fore.WHITE + Back.GREEN + "Jogador 2 Foi o campeão!")
                break
        elif usuario == 2:
            comp1 = 0
            jgdr1 = 0
            numero_aleatorio = random.randint(1, 500)
            print(Fore.WHITE + Back.RED + "<<<<< Bem vindo Ao Inferno >>>>>")
            time.sleep(1)
            while comp1 <= 3 and jgdr1 <= 3:
                computador = random.randint(1, 500)
                print(f"Computador tirou o numero {computador}")
                time.sleep(1) 
                input("Jogador - aperte enter")
                jogador = random.randint(1, 500)
                print(f"Jogador tirou o numero {jogador}")
                time.sleep(1)
                dist1 = abs(jogador - numero_aleatorio)
                dist2 = abs(computador - numero_aleatorio)
                if dist1 > dist2:
                    jgdr1 += 1
                    print(Fore.YELLOW + Back.BLACK + "Jogador venceu a rodada")
                    print(Fore.BLACK + Back.WHITE + f"Pontos atual {jgdr1}")
                elif dist2 > dist1:
                    comp1 += 1
                    print(Fore.RED + Back.BLACK + "Computador vençeu a rodada!")
                    print(Fore.BLACK + Back.WHITE + f"pontos atual do computador {comp1}")
                elif dist1 == dist2:
                    print(Fore.WHITE + Back.YELLOW + "Empate!")
            if jgdr1 == 3:
                print(Fore.BLACK + Back.BLUE + "Jogador 1 vençeu!")
                break
            elif comp1 == 3:
                print(Fore.BLACK + Back.RED + "Computador vençeu")
                print(Fore.GREEN + Back.RED + "Defeat.")
                break  
        elif usuario == 3:
            print(Fore.BLACK + Back.WHITE + "<<< Voltando ao menu principal >>> ")
            break
while True:
    try:
        print(Fore.WHITE + Back.BLUE +"==== Menu Principal ====")
        print("1 - organizar tarefas")
        print("2 - jogo de matematica")
        print("3 - jogo de sorte")
        print("4 - sair")
        usuario_principal = int(input("Digite entre 1, 2, 3 ou 4: "))
        if usuario_principal == 1:
            menu_lista()  
        elif usuario_principal == 2:
            menu_matematica()
        elif usuario_principal == 3:
            jogo_de_adivinhar()
        elif usuario_principal == 4:
            print("Usuario escolheu encerrar a sessão")
            exit()
    except ValueError:
        print(Fore.BLACK + Back.YELLOW + f"Digite apenas números")
    except KeyboardInterrupt:
        print(Fore.RED + Back.BLACK + "Conexão encerrada pelo usuario apertando 'ctrl C'")
        exit()
 
        









