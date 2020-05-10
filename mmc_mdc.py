#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:21:02 2020

@author: eriksson
"""


def kprimes(comeco_intervalo: int, fim_intervalo: int, /, *, next_prime: bool = False):
    
    primo: bool = True

    if comeco_intervalo <= 2:
        primos_no_intervalo: dict = {1: 2}
        yield 2
        quant_primos = 1
        comeco_intervalo = 3
    else:
        primos_no_intervalo = {1: 2, 2: 3}
        yield 2
        yield 3
        quant_primos = 2
        for numero_analisado in range(5, comeco_intervalo + 1, 2):
            raiz_quadrada_numero_analisado = numero_analisado ** .5
            for candidato_a_divisor in primos_no_intervalo.values():
                if candidato_a_divisor > raiz_quadrada_numero_analisado:
                    break
                if numero_analisado % candidato_a_divisor == 0:
                    primo = False
                    break
            if primo:
                quant_primos += 1
                yield numero_analisado
                primos_no_intervalo[quant_primos] = numero_analisado
            primo = True

    if comeco_intervalo % 2 == 0:
        comeco_intervalo += 1
    for numero_analisado in range(comeco_intervalo, fim_intervalo + 1, 2):
        raiz_quadrada_numero_analisado = numero_analisado ** .5
        for candidato_a_divisor in primos_no_intervalo.values():
            if candidato_a_divisor > raiz_quadrada_numero_analisado:
                break
            if numero_analisado % candidato_a_divisor == 0:
                primo = False
                break
        if primo:
            quant_primos += 1
            yield numero_analisado
            primos_no_intervalo[quant_primos] = numero_analisado
        primo = True

    if next_prime:
        numero_analisado = fim_intervalo
        if numero_analisado >= 2:
            while True:
                numero_analisado += 1
                raiz_quadrada_numero_analisado = numero_analisado ** .5
                for candidato_a_divisor in primos_no_intervalo.values():
                    if candidato_a_divisor > raiz_quadrada_numero_analisado:
                        break
                    if numero_analisado % candidato_a_divisor == 0:
                        primo = False
                        break
                if primo:
                    quant_primos += 1
                    primos_no_intervalo[quant_primos] = numero_analisado
                    yield numero_analisado
                    break
                primo = True


def isprime(numero: int, /) -> bool:

    if not isinstance(numero, int):
        raise TypeError
    if numero < 2:
        return False

    for i in kprimes(0, numero):
        if numero == i:
            return True

    return False


def nextprime(numero: int, /) -> int:
    
    if not isinstance(numero, int):
        raise TypeError

    for i in kprimes(2, numero, next_prime=True):
        pass
    else:
        return i


def mdc(param_numeros: list):
    
    fator = nextprime(1)
    fatores = []
    quantidade_de_numeros = len(param_numeros)
    numero_temp = None
    fatores_temp = []
    
    for i in range(quantidade_de_numeros):
        numero_temp = param_numeros[i]
        while numero_temp != 1:
            if numero_temp % fator == 0:
                fatores_temp.append(fator)
                numero_temp //= fator
            else:
                fator = nextprime(fator)
        fatores.append(fatores_temp.copy())
        fatores_temp.clear()
        fator = nextprime(1)
    else:
        fatores_usados_primeiro_numero = tuple(set(fatores[0]))
        fatores_comuns = []
        ocorrencia_de_fator = 0
        expoentes = []
        for ii in range(len(fatores_usados_primeiro_numero)):
            for iii in fatores:
                if fatores_usados_primeiro_numero[ii] in iii:
                    ocorrencia_de_fator += 1
                    expoentes.append(iii.count(fatores_usados_primeiro_numero[ii]))
            if ocorrencia_de_fator == quantidade_de_numeros:
                fatores_comuns.append((fatores_usados_primeiro_numero[ii], min(expoentes)))
            ocorrencia_de_fator = 0
            expoentes.clear()
        else:
            produto_dos_fatores_comuns = 1
            for iv in fatores_comuns:
                produto_dos_fatores_comuns *= iv[0] ** iv[1]
            else:
                return produto_dos_fatores_comuns


def mmc(param_numeros: list):
    
    mmc_ = 1
    numeros_temp = []
    fator = nextprime(1)
    isfator = False
    fatores = []
    quantidade_de_parametros = len(param_numeros)
    soma_dos_parametros = sum(param_numeros)
    
    while soma_dos_parametros != quantidade_de_parametros:
        for i in param_numeros:
            if i % fator == 0:
                numeros_temp.append(i // fator)
                isfator = True
            else:
                numeros_temp.append(i)
        else:
            if isfator:
                fatores.append(fator)
                isfator = False
            else:
                fator = nextprime(fator)
        param_numeros = numeros_temp.copy()
        numeros_temp.clear()
        soma_dos_parametros = sum(param_numeros)
    else:
        for fator in fatores:
            mmc_ *= fator
        return mmc_
