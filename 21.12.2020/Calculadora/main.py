from calculadora import soma, subtracao, divisao, multiplicacao
# which python3 -- comando para saber onde está o python

while True:
    opcao = input("    1. Soma\n    2. Subtração\n    3. Divisão\n    4. Multiplicação\n    0. Sair\nInsira uma opção: ")
    if opcao == '0':
        break
    else:
        while True:
            try:
                v1 = float(input("Insira o primeiro valor da operação: "))
                v2 = float(input("Insira o segundo valor da operação: "))
                break
            except:
                print("Os valores devem ser numéricos.")
        if opcao == '1':
            print(f"Total soma: {soma(v1, v2)}")
        elif opcao == '2':
            print(f"Total subtração: {subtracao(v1, v2)}")
        elif opcao == '3':
            print(f"Total divisão: {divisao(v1, v2)}")
        elif opcao == '4':
            print(f"Total multiplicação: {multiplicacao(v1, v2)}")
        elif opcao == '0':
            print('Saindo!!')
            break
        else:
            print("Opção inválida, tente novamente.")

