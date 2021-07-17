import re
# from dateutil.relativedelta import *
from datetime import date


def validar_data_nascimento(data_avaliada):
    today = date.today()
    valido = False
    data_avaliada = data_avaliada.strip()
    if re.fullmatch("(\d\d\/\d\d\/\d\d\d\d)", data_avaliada):
        dia_dn = int(data_avaliada[:2])
        mes_dn = int(data_avaliada[3:5])
        ano_dn = int(data_avaliada[6:])
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
                    return False
            else:
                valido = True
        if valido:
            return True
        else:
            return False
    else:
        return False
