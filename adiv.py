import random

dificuldade = None
tentativas_max = 0
intervalo_max = 0

while True:
    print("=" * 50)
    print("       ESCOLHA A DIFICULDADE")
    print("=" * 50)
    print("1 - Fácil ")
    print("2 - Médio ")
    print("3 - Difícil ")
    print("4 - Sair ")


    try:
        opcao = int(input("Digite a opção desejada (1 a 4): "))
    except:
        print("Digita número seu animal, não letra!")
        continue

    if opcao == 1:
        dificuldade = "Fácil"
        intervalo_max = 20
        tentativas_max = 10
        print("Very ez... vai chorar quando perder fácil?")
        break

    elif opcao == 2:
        dificuldade = "Médio"
        intervalo_max = 50
        tentativas_max = 6
        print("Seu momento é agora!!! Não vacila hein...")
        break

    elif opcao == 3:
        dificuldade = "Difícil"
        intervalo_max = 100
        tentativas_max = 4
        print("Hardcore hard... vai ver o que é sofrimento de verdade")
        break

    elif opcao == 4:
        print("Desista mesmo seu bosta kkkkkkk")
        print("Tchau!")
        exit()

    else:
        print("Opção inválida, digita direito (1 a 4)")


numero = random.randint(0, intervalo_max)
tentativas = 1
errou = True

print(f"Tá na {dificuldade} hein...")
print(f"Vou sortear um número de 0 até {intervalo_max}")
print(f"Você tem {tentativas_max} tentativas. Boa sorte (você vai precisar)")

while tentativas <= tentativas_max:
    print(f"Tentativa {tentativas} de {tentativas_max}")
    
    try:
        chute = int(input("Digite seu chute: "))
    except:
        print("Número inteiro, por favor... não me faz perder tempo")
        continue

    if chute == numero:
        print("Parabéns, você é o bonzão mesmo!!! ")
        print(f"Acertou em {tentativas} tentativa(s)")
        errou = False
        break
    
    else:
        print("Errou :c")
        
        if chute < numero:
            print("Dica: é MAIOR ↑")
        else:
            print("Dica: é MENOR ↓")
    
    tentativas += 1
    print("-" * 40)

if errou:
    print(f"Se e ruim em número era {numero}")
    print("Le falta odio")

print(" PERDEU AI BTEA?")
print(" Sobrou nada pro BETA ")