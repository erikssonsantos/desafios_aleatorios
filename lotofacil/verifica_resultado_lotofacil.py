import requests
import re
import os.path
from os import remove

# dicionário que conterá resultados: 
# número do concurso, data e números sorteados:
resultados = {}
atualizacao = ""


def get_dict_from_json():
    import json
    
    dados = open("dictall.json", 'r', encoding="utf8")
    all_conteudo = dados.read()
    dados.close()
    
    return json.loads(all_conteudo)


def atualiza_json():
    import json
    criar_dict_resultados()
    dados = open("dictall.json", 'w', encoding="utf8") 
    json.dump(resultados, dados, indent = 4, sort_keys = False) 
    dados.close()


resultados = get_dict_from_json()



# cria dicionário personalizado a partir de arquivo local
def criar_dict_resultados():
    
    resultados.clear()
    i = 0
    concurso = 0
    data = ""
    numero = 0
    
    dados = open("todos_resultados_txt.txt", 'r', encoding="utf8")
    
    for linha in dados:
        d = re.search("(\d\d/\d\d/\d\d\d\d)", linha)
        n = re.search("(>\d\d\d)", linha)
        
        if d != None:
            concurso += 1
            data = f"{d.group()}"
            resultados[concurso] = [[data],[]]
            i = 0
        
        if n != None and i < 15:
            n = n.group()
            resultados[concurso][1].append(int(n.replace(">", "")))
            i += 1
        
    dados.close()


def verifica_se_dados_locais_estao_atualizados():
    if os.path.isfile("todos_resultados_txt.txt"):
        from datetime import datetime
        now = datetime.now()
        keys = []
        for i in resultados.keys():
            keys.append(int(i))
        ultimo_concurso = str(max(keys))
        del keys
        
        dia_ultimo_concurso = re.search("(\d\d)", resultados[ultimo_concurso][0][0])
        dia_ultimo_concurso = dia_ultimo_concurso.group()
        dia_ultimo_concurso = int(dia_ultimo_concurso)
        
        mes_ultimo_concurso = re.search("(/\d\d)", resultados[ultimo_concurso][0][0])
        mes_ultimo_concurso = mes_ultimo_concurso.group()
        mes_ultimo_concurso = int(mes_ultimo_concurso.replace('/', ''))
        
        ano_ultimo_concurso = re.search("(/\d\d\d\d)", resultados[ultimo_concurso][0][0])
        ano_ultimo_concurso = ano_ultimo_concurso.group()
        ano_ultimo_concurso = int(ano_ultimo_concurso.replace('/', ''))

        hoje = f"{now.day}/{now.month}/{now.year}"
        data_ultimo_concurso = f"{dia_ultimo_concurso}/{mes_ultimo_concurso}/{ano_ultimo_concurso}"
        
        a = ano_ultimo_concurso < now.year
        b = ano_ultimo_concurso == now.year
        c = mes_ultimo_concurso < now.month
        d = mes_ultimo_concurso == now.month
        e = dia_ultimo_concurso < now.day
        f = now.hour > 20
        g = now.minute > 30

        z1 = a and (f and g)
        z2 = (b and c) and (f and g)
        z3 = (b and (d and e)) and (f and g)
        z = z1 or z2 or z3

        if z:
            import shutil
            source=r"todos_resultados_txt.txt"
            if os.path.isfile("todos_resultados_txt_bp.txt"):
                os.remove("todos_resultados_txt_bp.txt")
            destination=r"todos_resultados_txt_bp.txt"
            shutil.copyfile(source, destination)
            os.remove("todos_resultados_txt.txt")
            atualiza_dados_locais(1)
    else:
        atualiza_dados_locais()
    
    atualizacao = "Atualizado"
    
    

# if not os.path.isfile("todos_resultados_txt.txt"):

def atualiza_dados_locais(caso=0):
    
    link_todos_resultados = "http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotofacil/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbz8vTxNDRy9_Y2NQ13CDA0sTIEKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wBmoxN_FydLAGAgNTKEK8DkRrACPGwpyQyMMMj0VAcySpRM!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0K85260Q5OIRSC42046/res/id=historicoHTML/c=cacheLevelPage/=/"
    
    try:
        # busca resultados na internet
        resposta = requests.get(link_todos_resultados)
        
        # cria arquivo local com todos os resultados
        dados = open("todos_resultados_txt.txt", 'w', encoding="utf8")
        dados.write(resposta.text)
        dados.close()
        
        # cópia json
        atualiza_json()
        
        atualizacao = "Atualizado"
    except:
        if caso == 0:
            print("Não foi possível atualizar dados.")
        elif caso == 1:
            import shutil
            source=r"todos_resultados_txt_bp.txt"
            destination=r"todos_resultados_txt.txt"
            shutil.copyfile(source, destination)
            print("Não foi possível atualizar dados.")
        else:
            print("Não foi possível atualizar dados. [Caso não interceptado.]")




def quantidade_acertos(numeros_jogados, n_concurso):
    n_quantidade_acertos = 0
    concurso_analisado = resultados[n_concurso]
    numeros_sorteados = resultados[n_concurso][1]
    # data_concurso_analisado = resultados[n_concurso][0]
    
    for i in range(15):
        if len(numeros_jogados) == len(numeros_sorteados):
            verificado = numeros_jogados[i] in numeros_sorteados
            if verificado:
                n_quantidade_acertos += 1
        else:
            if len(numeros_jogados) != 15:
                print("Sua aposta não tem 15 números!")
            elif len(numeros_sorteados) != 15:
                print("Numeros sorteados devem ser na quantidade de 15!")
    
    return n_quantidade_acertos


def um_jogo_em_todos_resultados(numeros_jogados):
    for key, value in resultados.items():
        acertos = quantidade_acertos(numeros_jogados, key)
        print(f"{key} - {value[0]} - {acertos}")
        if acertos == 15:
            break


def vezes_numero(numero):
    vezes = 0
    for i in resultados.keys():
        if numero in resultados[i][1]:
            vezes += 1
    
    return vezes


def rank_vezes():
    rank = {}
    
    for i in range(1, 26):
        rank[i] = vezes_numero(i)
    
    rank_temp = rank.copy()
    value_list = list(rank.values())
    value_list.sort(reverse=True)
    
    for i in value_list:
    
        for k, v in rank_temp.items():
            if v == i:
                rank[value_list.index(i) + 1] = [k, v]
    
    return rank
        

verifica_se_dados_locais_estao_atualizados()
# print(vezes_numero(22))
'''
for k, v in rank_vezes().items():
    print(f"{k}º -> {v}")
'''
# a = quantidade_acertos([2,3,4,5,6,7,8,10,13,17,18,19,20,21,24], int(max(resultados.keys())))
# print(a)
# jogo_bom = [2,3,4,5,6,7,8,10,13,17,18,19,20,21,24]
# um_jogo_em_todos_resultados([10, 13, 24, 11, 25, 3, 23, 18, 5, 1, 19, 2, 14, 4, 20])

# print(get_dict_from_json())

um_jogo_em_todos_resultados([2,3,4,5,6,7,8,10,13,17,18,19,20,21,24])

print(f"\n\n{atualizacao}")
