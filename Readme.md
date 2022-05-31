# Algoritmo de Busca A*

	def: É um algoritmo para Busca de Caminho. Ele busca o caminho em um grafo de um vértice 
	inicial até um vértice final. Ele é a combinação de aproximações heurísticas como do algoritmo
	Breadth First Search (Busca em Largura) e da formalidade do Algoritmo de Dijkstra.

	*Nós (N)= conjunto de nós a serem pesquisados;
	*Inicio(I) = o estado inicial da busca

	#Faça:

	> Inicialize N com o nó de busca (I) como única entrada;
	> Se N está vazio, interrompa. Se não, escolha o melhor elemento de N;
	> Se o estado (n) é um objetivo, retorne n;
	> (De outro modo) Remova n de N;
	>  Encontre os descendentes do estado (n) que não estão em visitados e crie todas as extensões de n para cada descendente;
	> Adicione os caminhos estendidos a N e vá ao passo 2;