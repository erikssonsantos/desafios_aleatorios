import requests
import re
import os.path
from os import remove

# dicionário que conterá resultados: 
# número do concurso, data e números sorteados:
resultados = {}
atualizacao = ""

# cria dicionário personalizado a partir de arquivo local
def criar_dict_resultados():
    
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
        criar_dict_resultados()
        ultimo_concurso = max(resultados.keys())
        
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
        
        if a or (b and c) or (b and (d and e)):
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
        import json
        dados = open("dictall.json", "w") 
        json.dump(resultados, dados, indent = 4, sort_keys = False) 
        dados.close()
        
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











verifica_se_dados_locais_estao_atualizados()
criar_dict_resultados()
# a = quantidade_acertos([2,3,4,5,6,7,8,10,13,17,18,19,20,21,24], int(max(resultados.keys())))
# print(a)
um_jogo_em_todos_resultados([2,3,4,5,6,7,8,10,13,17,18,19,20,21,24])


print(f"\n\n{atualizacao}")


'''
import json
dados = open("dictall.json", "w") 
json.dump(resultados, dados, indent = 4, sort_keys = False) 
dados.close()
'''

