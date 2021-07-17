import json
import re
from dateutil.relativedelta import relativedelta
from datetime import date
from os import path

db_arquivo = 'db.json'
db_temp = {}


def get_dict_from_json():
    if path.isfile(db_arquivo):
        dados = open(db_arquivo, 'r', encoding="utf8")
        todo_conteudo = dados.read()
        dados.close()
        return json.loads(todo_conteudo)
    else:
        return {}


def update_json():
    dados = open(db_arquivo, 'w', encoding="utf8")
    json.dump(db_temp, dados, indent=4, sort_keys=False)
    dados.close()


def add_pessoa():
    id_pessoa_nova = None
    nome_completo = None
    data_nascimento = None
    sexo = None
    fone = None
    email = None
    pais = None
    endereco = None
    idade = None

    today = date.today()

    if len(db_temp.keys()) == 0:
        id_pessoa_nova = 1
    else:
        id_pessoa_nova = max(db_temp.keys()) + 1

    nome_completo = input('Nome completo: ').strip().upper()

    while True:
        valido = False
        data_nascimento = input('Data de nascimento no seguinte padrão dd/mm/aaaa: ').strip()
        if re.fullmatch("(\d\d\/\d\d\/\d\d\d\d)", data_nascimento):
            dia_dn = int(data_nascimento[:2])
            mes_dn = int(data_nascimento[3:5])
            ano_dn = int(data_nascimento[6:])
            a = mes_dn < 13
            b = dia_dn < 32
            c = ano_dn < today.year + 1
            d = today.year - ano_dn == 0
            if a and b and c:
                if d:
                    e = mes_dn <= today.month
                    f = dia_dn <= today.day
                    g = today.month - mes_dn == 0
                    if e:
                        if g:
                            if f:
                                valido = True
                        else:
                            valido = True
                else:
                    valido = True

            if valido:
                break
            else:
                print('Data digitada não é válida!')
        else:
            print('Digite a data no seguinte padrão dd/mm/aaaa')

    while True:
        sexo = input('Sexo [M ou F]: ').strip().upper()
        if sexo in 'MF':
            break
        else:
            print('Digite M para masculino ou F para feminino.')

    fone = input('Fone: ').strip().lower()

    r = re.compile(
        r"^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$")  # https://pt.stackoverflow.com/questions/365442/fun%C3%A7%C3%A3o-de-valida%C3%A7%C3%A3o-de-email
    while True:
        email = input('E-mail: ')
        if r.match(email):
            break
        else:
            print('Digite um e-mail válido.')

    pais = input('País: ').strip().upper()

    endereco = input('Endereço: ').strip().upper()

    dn = date(int(data_nascimento[6:]), int(data_nascimento[3:5]), int(data_nascimento[:2]))
    idade = relativedelta(today, dn).years

    db_temp[id_pessoa_nova] = {
        'nome_completo': nome_completo,
        'data_nascimento': data_nascimento,
        'sexo': sexo,
        'fone': fone,
        'email': email,
        'pais': pais,
        'endereco': endereco,
        'idade': idade
    }

    update_json()

    print(f'\nO CADASTRO DE {nome_completo} FOI SALVO COM SUCESSO.')

    mostrar_menu_main()


def atualizar_cadastro(id_pessoa):
    ...


def listar_cadastros():
    print('-' * 5, end=' ')
    print('LISTA DE CLIENTES', end=' ')
    print('-' * 5, end='\n\n')

    db_temp = get_dict_from_json()

    for key, value in db_temp.items():
        print(f'{key} - {value["nome_completo"]} - {value["sexo"]} - {value["idade"]} anos')

    print('\n\n\n')

    if len(db_temp.values()) == 0:
        print('\n\nNENHUM CLIENTE CADASTRADO/ATIVO!\n\n')
        mostrar_menu_main()

    print('[ 1 ] ATUALIZAR CADASTRO')
    print('[ 2 ] DELETAR CADASTRO')
    print('[ 3 ] VOLTAR PARA O MENU PRINCIPAL')
    print('[ 4 ] SAIR DO APLICATIVO')

    while True:
        comando = int(input('>>> '))
        if comando in range(1, 5):
            break
        else:
            print('Digite uma opção válida!')

    if comando == 1:
        print('\n\nAtualizar ainda não foi implementado!\n\n')
        mostrar_menu_main()
    elif comando == 2:
        print('\n\nDeletar ainda não foi implementado!\n\n')
        mostrar_menu_main()
    elif comando == 3:
        mostrar_menu_main()
    elif comando == 4:
        import sys
        sys.exit('\nATÉ A PRÓXIMA!\n')


def mostrar_menu_main():
    print('-' * 5, end=' ')
    print('CLIENTES', end=' ')
    print('-' * 5, end='\n\n')

    print('[ 1 ] CADASTRAR NOVO CLIENTE')
    print('[ 2 ] VER CADASTROS SALVOS')
    print('[ 3 ] SAIR DO APLICATIVO')

    comando = int(input('>>> '))

    if comando == 1:
        add_pessoa()
    elif comando == 2:
        listar_cadastros()
    elif comando == 3:
        import sys
        sys.exit('\nATÉ A PRÓXIMA!\n')
    else:
        mostrar_menu_main()


if __name__ == '__main__':
    mostrar_menu_main()