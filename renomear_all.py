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
from time import sleep


pasta_alvo = None  # None = pasta atual
padrao_de_nomes = 'wallpaper_'
tipos_para_renomear = ['.png', '.jpg', '.jpeg']


if pasta_alvo:
    ...
else:
    pasta_alvo = str(aqui())


lista = listar(pasta_alvo)
lista_aux_0 = []


def mudar_nome(tipo_nome, lista_de_arquivos):
    aux = 1
    for arquivo in lista_de_arquivos:
        extensao = None
        if tipo_nome == 'novo_nome':
            if isfile(f'{pasta_alvo}/{arquivo[1]}'):
                extensao = arquivo[1].lower().split('.')[-1]
                if len(extensao) > 1:
                    extensao = '.' + extensao
                else:
                    continue
            if extensao and extensao in tipos_para_renomear:
                novo_nome = padrao_de_nomes + str(aux) + extensao
                valor_alvo = f'{pasta_alvo}/{arquivo[1]}'
                novo_valor = f'{pasta_alvo}/{novo_nome}'
                renomear(valor_alvo, novo_valor)
                print(f'{arquivo[0]} agora se chama {novo_nome}')
                aux += 1
                sleep(.1)
        if tipo_nome == 'nome_provisorio':
            if isfile(f'{pasta_alvo}/{arquivo}'):
                extensao = arquivo.lower().split('.')[-1]
                if len(extensao) > 1:
                    extensao = '.' + extensao
                else:
                    continue
            if extensao and extensao in tipos_para_renomear:
                data_de_modificacao = str(stat(f'{pasta_alvo}/{arquivo}')[8])
                nome_provisorio = data_de_modificacao + extensao
                valor_alvo = f'{pasta_alvo}/{arquivo}'
                novo_valor = f'{pasta_alvo}/{nome_provisorio}'
                renomear(valor_alvo, novo_valor)
                lista_aux_0.append((arquivo, nome_provisorio))
                aux += 1


mudar_nome('nome_provisorio', lista)
lista_aux_0.sort()
mudar_nome('novo_nome', lista_aux_0)
