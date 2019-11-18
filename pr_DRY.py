#!/usr/bin/env python
# -*- coding: utf-8 -*-
op = 5
while(op == 5):
    print('×===========================×')
    print('|1 - Adição.                |')
    print('|2 - Subtração.             |')
    print('|3 - Multiplicação.         |')
    print('|4 - Divisão.               |')
    print('|0 - Sair.                  |')
    print('×===========================×')
    # TENTA LER INTEIRO DE MENU, E FLOAT DE VALs
    try: 
        escolha = int(input('Escolha uma das opções: '))
        # VERIFICA SE A ESCOLHA É VALIDA SENÃO SAI:
        if escolha not in [1,2,3,4]:
            print('Fim da operação!')
            break
        # ENTRADA DE DADOS:
        val_1 = float(input('Digite o primeiro valor: '))
        val_2 = float(input('Digite o segundo valor: '))
        # DEFINE O OPERADOR E O RESULTADO CONFORME ESCOLHA
        if escolha == 1:
            operador = "+"
            resultado = val_1 + val_2
        elif escolha == 2:
            operador = "-"
            resultado = val_1 - val_2       
        elif escolha == 3:
            operador = "*"
            resultado = val_1 * val_2
        elif escolha == 4:
            operador = "÷"
            resultado = val_1 / val_2
        # APRESENTA RESULTADO:
        print('\n*============================*')
        print('|{} {} {} = {}.'.format(val_1, operador, val_2, resultado))
        print('*============================*\n')
    # CASO NÃO TENHA SIDO VALIDO:
    except ValueError: 
        print("\nOps... algo saiu errado... tente novamente...\n")
        continue
