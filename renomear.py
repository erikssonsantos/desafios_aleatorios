#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Renomeia arquivos.

Renomeia arquivos wallpapers de uma pasta alvo.
Pode ser alterado para renomear outros tipos de arquivos.
"""


from os import listdir as listar
from os import getcwd as aqui
from os import rename as renomear
from os import stat
from os.path import isfile
# from time import sleep


pasta_alvo = None  # None = pasta atual
padrao_de_nomes = 'wallpaper_'
tipos_para_renomear = ['.png', '.jpg', '.jpeg', '.webp']
# padrao_antes = True
numero_inicial = 1


if pasta_alvo:
    ...
else:
    pasta_alvo = str(aqui())


lista = listar(pasta_alvo)
lista_aux_0 = []


def extensao(arquivo):

    if isfile(f'{arquivo}'):
        extensao = arquivo.lower().split('.')
        if len(extensao) > 1:
            return '.' + extensao[-1]
        else:
            return None
    else:
        return 'directory'


def nome_de_transicao(lista_de_arquivos):

    for arquivo in lista_de_arquivos:

        ext = extensao(arquivo)

        if ext == None or ext == 'directory':
            continue

        if extensao(arquivo) in tipos_para_renomear:
            data_de_modificacao = str(stat(f'{pasta_alvo}/{arquivo}')[1])
            novo_nome = data_de_modificacao + ext
            valor_alvo = f'{pasta_alvo}/{arquivo}'
            novo_valor = f'{pasta_alvo}/{novo_nome}'
            renomear(valor_alvo, novo_valor)
            lista_aux_0.append((arquivo, novo_nome))


def nome_definitivo(lista_de_arquivos):
    aux = numero_inicial

    for arquivo in lista_de_arquivos:
        
        ext = extensao(arquivo[1])

        if ext == None or ext == 'directory':
            continue

        if extensao(arquivo[1]) in tipos_para_renomear:
            novo_nome = padrao_de_nomes + str(aux) + ext
            valor_alvo = f'{pasta_alvo}/{arquivo[1]}'
            novo_valor = f'{pasta_alvo}/{novo_nome}'
            renomear(valor_alvo, novo_valor)
            print(f'{arquivo[0]} agora se chama {novo_nome}')
            aux += 1
            # sleep(.1)


nome_de_transicao(lista)
lista_aux_0.sort()
nome_definitivo(lista_aux_0)

