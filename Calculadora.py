"""
calculadora
autor: Arauttho
Função: fazer contas: soma, subtração, multiplicação e divisão.
"""

print(f'{"=-="*3} {"CALCULADORA v2.0"} {"=-="*3}')
while True:
    num1 = int(input('Digite um número: '))
    while True:
        opera = str(input('operador:[+, -, *, /] '))
        if opera == '+' or opera == '-' or opera == '/' or opera == '*':
            break
        else:
            print('Digite um operador válido.')
    num2 = int(input('Digite outro valor: '))
    if opera == '+':
        res = num1 + num2
    elif opera == '-':
        res = num1 - num2
    elif opera == '*':
        res = num1 * num2
    else:
        res = num1 / num2
    print(f'o resultado de {num1} {opera} {num2} é {res}!')
    retor = str(input('Deseja Continuar?[s/n] ').strip().upper())
    print(retor)
    if retor[0] == 'N':
        print('Finalizando... Até mais!')
        break