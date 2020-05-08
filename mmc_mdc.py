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

    numeros_temp = []
    fator = nextprime(1)
    isfator = False
    fatores = []
    candidatos_mdc = []
    quandidade_de_dividendos = 0

    while sum(param_numeros) != len(param_numeros):

        for i in param_numeros:
            if i % fator == 0:
                numeros_temp.append(i // fator)
                isfator = True
                quandidade_de_dividendos += 1
            else:
                numeros_temp.append(i)
        else:
            if quandidade_de_dividendos == len(param_numeros):
                candidatos_mdc.append(fator)
            quandidade_de_dividendos = 0
            if isfator:
                fatores.append(fator)
                isfator = False
            else:
                fator = nextprime(fator)

        param_numeros = numeros_temp.copy()
        numeros_temp.clear()
    else:
        candidato_mdc_vencedor = min(candidatos_mdc)
        quandidade_de_repeticoes_do_vencedor = candidatos_mdc.count(candidato_mdc_vencedor)
        mdc_ = candidato_mdc_vencedor ** quandidade_de_repeticoes_do_vencedor
        return mdc_


def mmc(param_numeros: list):

    numeros_temp = []
    fator = nextprime(1)
    isfator = False
    fatores = []

    while sum(param_numeros) != len(param_numeros):
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
    else:
        mmc_ = 1
        for fator in fatores:
            mmc_ *= fator
        return mmc_
