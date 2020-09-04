#!/usr/bin/env python
# -*- coding: utf-8 -*-


from os import listdir as listar
from os import getcwd as aqui
from os import rename as renomear
from os.path import isfile


pasta_alvo = None # None = pasta atual
padrao_de_nomes = 'w_'
tipos_para_renomear = ['.png', '.jpg', '.jpeg', '.webp']
padrao_antes = True
numero = 1


if pasta_alvo:
    ...
else:
    pasta_alvo = str(aqui())


lista = listar(pasta_alvo)


def mudar_nome(lista_de_arquivos):

    for arquivo in lista_de_arquivos:
        extensao = None
        if isfile(f'{pasta_alvo}/{arquivo}'):
            extensao = arquivo.lower().split('.')[-1]
            if len(extensao) > 1:
                extensao = '.' + extensao
            else:
                continue

        if extensao in tipos_para_renomear:
            global numero
            if padrao_antes:
                novo_nome = padrao_de_nomes + str(numero) + extensao
            else:
                novo_nome = str(numero) + padrao_de_nomes + extensao
            renomear(f'{pasta_alvo}/{arquivo}', f'{pasta_alvo}/{novo_nome}')
            print(f'{arquivo} agora se chama {novo_nome}')
            numero += 1

    numero = 1


mudar_nome(lista)

