

from json import load

cidades = {
		"Arad":0,
		"Bucharest":1,
		"Craiova":2,
		"Dobreta":3,
		"Eforie":4,
		"Fagaras":5,
		"Giurgiu":6,
		"Hirsova":7,
		"Lasi":8,
		"Lugoj":9,
		"Mehadia":10,
		"Neamt":11,
		"Oradea":12,
		"Pitesti":13,
		"Rimmicu Vilcea":14,
		"Sibiu":15,
		"Timisoara":16,
		"Urziceni":17,
		"Vaslui":18,
		"Zerind":19
	}


class Cidade:
    def __init__ (self, nome, distancia_em_linha_reta):
        self.nome = nome
        self.distancia_em_linha_reta = distancia_em_linha_reta
        self.lista_de_adjacencia = []

    def __str__ (self):
        return f'Nome: {self.nome}, Distância em linha reta do objetivo: {self.distancia_em_linha_reta}'


    def adiciona_adjacente (self, cidade, distancia):
        item = (cidade, distancia)
        self.lista_de_adjacencia.append(item)


    def mostra_adjacentes (self):
        print(f"Cidades adjacentes a {self.nome}:")
        for i in self.lista_de_adjacencia:
            print(i[0], f", Distância entre as cidades: {i[1]}")


def func_menor_caminho(root, cidades, distancias):
	distancia_percorrida = 0
	

	for i in cidades:
		nome_da_cidade = i
		if i[0] == root:
			continue

		distancia = i[0].distancia_em_linha_reta + i[1]		
		tupla = (nome_da_cidade, distancia)
        
		if len(distancias) == 0:
			menor_caminho = tupla
		else:
			if menor_caminho[1] > tupla[1]:
				menor_caminho = tupla

		distancias.append(tupla)
	
	return menor_caminho


def a_estrela (cidade_inicial, cidade_final):
    cidade_atual = cidade_inicial
    root = []
    root.append(cidade_inicial)
    distancia_percorrida = 0
    while cidade_atual != cidade_final:
        cidades = cidade_atual.lista_de_adjacencia
        root.append(cidade_atual)
        distancias = []
       	
        menor_caminho = func_menor_caminho(root[-2], cidades, distancias)
        cidade_atual = menor_caminho[0][0]
        
        distancia_percorrida = distancia_percorrida + menor_caminho[0][1]
        print(f'Distância percorrida Até {cidade_atual.nome}: {distancia_percorrida}')
       # x = input()
    print(cidade_atual.nome, distancia_percorrida)





def main():
	with open("cidades.json", "r") as file:
		dados = load(file)

	lst = []

	for i, j in enumerate(dados):
		cidade = j["cidade"]
		distancia_em_linha_reta = int(j["distancia_linha_reta"])
		lst.append(Cidade(cidade, distancia_em_linha_reta))

	for i, j in enumerate(dados):
		for adj in j["adjacentes"]:
			lst[i].adiciona_adjacente(lst[cidades[adj["cidade"]]], int(adj["distancia"]))

	a_estrela(lst[cidades["Oradea"]], lst[cidades["Bucharest"]])
	a_estrela(lst[cidades["Zerind"]], lst[cidades["Bucharest"]])
	a_estrela(lst[cidades["Vaslui"]], lst[cidades["Bucharest"]])
	a_estrela(lst[cidades["Lasi"]], lst[cidades["Bucharest"]])
	a_estrela(lst[cidades["Lugoj"]], lst[cidades["Bucharest"]])
	a_estrela(lst[cidades["Mehadia"]], lst[cidades["Bucharest"]])
	a_estrela(lst[cidades["Urziceni"]], lst[cidades["Bucharest"]])
	a_estrela(lst[cidades["Neamt"]], lst[cidades["Bucharest"]])
	a_estrela(lst[cidades["Timisoara"]], lst[cidades["Bucharest"]])
	a_estrela(lst[cidades["Hirsova"]], lst[cidades["Bucharest"]])
	# a_estrela(lst[cidades["Dobreta"]], lst[cidades["Oradea"]])
	# a_estrela(lst[cidades["Arad"]], lst[cidades["Vaslui"]])
	# a_estrela(lst[cidades["Arad"]], lst[cidades["Eforie"]])


if __name__ == '__main__':
	main()