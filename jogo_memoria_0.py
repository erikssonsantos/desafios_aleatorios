from random import randint


class Jogo:
	
	def __init__(self):
        
		self.loop_do_jogo = True
		self.numero_de_opcoes = 10
		self.opcoes_descobertas = []
		self.cartas = [randint(1, 1000) for i in range(self.numero_de_opcoes // 2)]
		self.cartas += self.cartas
		self.carta1 = None
		self.carta2 = None
		self.indice_carta1 = None
		self.indice_carta2 = None
	
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
			opcoes_descobertas.append(self.indice_carta1)
			opcoes_descobertas.append(self.indice_carta2)
			return True
		else:
			return False
			
	def mostrar_opcoes(self, escolhida1=None, escolhida2=None):
        
		for i in range(self.numero_de_opcoes):
			if escolhida1 and escolhida1 == i:
				print(self.cartas[escolhida1], end=' ')
				continue
			if escolhida2 and escolhida2 == i:
				print(self.cartas[escolhida2], end=' ')
				continue
			print('*', end=' ')
		print()
		
	def fim(self):
		return
		

jogo = Jogo()


while jogo.loop_do_jogo:
    
	jogo.mostrar_opcoes()
	escolhido = int(input('Escolha uma opção: '))


jogo.fim()

