class Cidade ():
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


def a_estrela (cidade_inicial, cidade_final):
    cidade_atual = cidade_inicial
    distancia_percorrida = 0

    while cidade_atual != cidade_final:
        cidades = cidade_atual.lista_de_adjacencia
        distancias = []

        for i in cidades:
            nome_da_cidade = i
            distancia = i[0].distancia_em_linha_reta + i[1]
            tupla = (nome_da_cidade, distancia)
            print(tupla)

            if len(distancias) == 0:
                menor_caminho = tupla
            else:
                if menor_caminho[1] > tupla[1]:
                    menor_caminho = tupla
            
            distancias.append(tupla)
        
        cidade_atual = menor_caminho[0][0]
        distancia_percorrida = distancia_percorrida + menor_caminho[0][1]

    
    print(cidade_atual.nome, distancia_percorrida)


def main():
    ceilandia = Cidade("Ceilandia", 42)
    aguas_claras = Cidade("Aguas Claras", 47)
    samambaia = Cidade("Samambaia", 32)
    sobradinho = Cidade("Sobradinho", 0)
    taguatinga = Cidade("Taguatinga", 100)
    vicente_pires = Cidade("Vicente Pires", 42)

    taguatinga.adiciona_adjacente(ceilandia, 30)
    taguatinga.adiciona_adjacente(aguas_claras, 27)
    taguatinga.adiciona_adjacente(samambaia, 47)

    ceilandia.adiciona_adjacente(taguatinga, 30)
    ceilandia.adiciona_adjacente(samambaia, 22)

    samambaia.adiciona_adjacente(taguatinga, 47)
    samambaia.adiciona_adjacente(sobradinho, 32)
    samambaia.adiciona_adjacente(vicente_pires, 17)

    sobradinho.adiciona_adjacente(samambaia, 32)
    sobradinho.adiciona_adjacente(vicente_pires, 15)

    vicente_pires.adiciona_adjacente(samambaia, 17)
    vicente_pires.adiciona_adjacente(sobradinho, 15)

    aguas_claras.adiciona_adjacente(taguatinga, 27)


    a_estrela(aguas_claras, sobradinho)

if __name__ == '__main__':
    main()


