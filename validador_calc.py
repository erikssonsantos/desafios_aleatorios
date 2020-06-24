# Principais variáveis usadas
expressao = input('Digite a expressão: ').strip()
quant_parenteses_abrir = expressao.count('(')
quant_parenteses_fechar = expressao.count(')')
parenteses_para_fechar = 0
distancia_entre_parenteses = 0 # Para verificar a quantidade de caracteres dentro
# dos parentese: erro se a distância entre o a abertura e o fechamento for 1
diferenca = 0 # vai guardar a diferença na quantidade de tipos de parênteses
erros = [] # lista que vai guardar todos os erros previstos e interceptados
validade = True


# Condicionais de verificação.
# Dois tipos de erros:
# erros com número igual de parêntese em if
# erros com número diferente de parênteses em else
if quant_parenteses_abrir == quant_parenteses_fechar:
    caracter_anterior = ''
    for caracter in expressao:
        if caracter == ')' and parenteses_para_fechar == 0:
            validade = False
            erros.append('Você fechou parentese antes de abrir.')
            break
        if caracter == '(':
            parenteses_para_fechar += 1
            distancia_entre_parenteses += 1
            continue
        if caracter != ')':
            distancia_entre_parenteses += 1
            caracter_anterior = caracter
            continue
        else:
            if distancia_entre_parenteses == 1:
                validade = False
                erros.append('Parênteses vazio.')
                break
            if caracter_anterior in '*-+/':
                validade = False
                erros.append('Operador em posição errada.')
                break
            parenteses_para_fechar -= 1
            distancia_entre_parenteses = 0
else:
    validade = False
    erros.append('A quantidade de parenteses abrindo é diferente da quantidade de parenteses fechando')
    if quant_parenteses_abrir > quant_parenteses_fechar:
        diferenca = quant_parenteses_abrir - quant_parenteses_fechar
        erros.append(f'Você esqueceu de fechar {diferenca} parentese(s)')
    elif quant_parenteses_abrir < quant_parenteses_fechar:
        diferenca = quant_parenteses_fechar - quant_parenteses_abrir
        erros.append(f'Você esqueceu de abrir {diferenca} parentese(s)')


# Condicional de impressão
if validade == True:
    print(f'A expressão {expressao} está válida!')
else:
    print(f'A expressão {expressao} está errada!')
    for erro in erros: # for para printar os erros acumulados na lista de erros
        print(erro)
