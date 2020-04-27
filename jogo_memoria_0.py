from random import randint


class Jogo:
    
    def __init__(self):
        
        self.loop_do_jogo = True
        self.numero_de_opcoes = 10
        self.cartas = [randint(1, 1000) for i in range(self.numero_de_opcoes // 2)]
        self.cartas += self.cartas
        self.carta1 = None
        self.carta2 = None
        self.indice_carta1 = None
        self.indice_carta2 = None
        self.cartas_encontradas = []
        
    def mostrar_carta(self, val, carta):
        
        if carta == 1:
            self.carta1 = self.cartas[val]
            self.indice_carta1 = val
        elif carta == 2:
            self.carta2 = self.cartas[val]
            self.indice_carta2 = val
        return self.cartas[val]
        
    def comparar_cartas(self, carta1, carta2):
        
        if carta1 == carta2:
            return True
        else:
            return False
            
    def mostrar_opcoes(self, escolhida1=None, escolhida2=None):
        print()
        for i in range(0, self.numero_de_opcoes):
            if i in self.cartas_encontradas:
                print(self.cartas[i], end=' ')
                continue
            if escolhida1 == i:
                print(self.cartas[escolhida1], end=' ')
                continue
            elif escolhida2 == i:
                print(self.cartas[escolhida2], end=' ')
                continue
            else:
                print('*', end=' ')
        print()
        
    def fim(self):
        print('Jogo finalizado!')


jogo = Jogo()

vez = 2
escolhida1 = None
escolhida2 = None
while jogo.loop_do_jogo:
    
    if vez == 1: 
        vez = 2
    elif vez == 2:
        vez = 1
    
    jogo.mostrar_opcoes(escolhida1, escolhida2)
    
    if vez == 1:
        escolhida1 = int(input('Escolha a primeira opção: '))
    if vez == 2:
        while True:
            escolhida2 = int(input('Escolha a segunda opção: '))
            if escolhida2 == escolhida1:
                print('Você á escolheu esssa opção!')
            else:
                break
        if jogo.comparar_cartas(jogo.cartas[escolhida1], jogo.cartas[escolhida2]):
            jogo.cartas_encontradas.append(escolhida1)
            jogo.cartas_encontradas.append(escolhida2)
            escolhida1 = None
            escolhida1 = None

jogo.fim()
