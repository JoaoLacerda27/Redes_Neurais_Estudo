import numpy as np

entradas = np.array([[0,0],[0,1],[1,0],[1,1]]) ##Matriz operador lógico AND
saidas = np.array([0,0,0,1]) ##Saídas esperadas
pesos = np.array([0.0, 0.0]) ##Pesos iniciais de cada sinapse
taxaAprendizagem = 0.1

##Função step Function
def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

##Calcula a saída das entradas
def calculaSaida(registro):
    s = registro.dot(pesos) ##Pega os registros (entradas) multiplica e soma pelos pesos
    return stepFunction(s)

##Interage com as entradas e as saídas esperadas e ajusta os pesos
def treinar():
    erroTotal = 1
    while (erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print('Peso atualizado: ' + str(pesos[j]))
        print('Total de erros: ' + str(erroTotal))

treinar()




