import pandas as pd
data = pd.read_csv("D:/ProgParalela/resultados.csv")
# Excluir coluna "Concurso" e "Data"
data = data.drop(columns=["Concurso", "Data"])
# convete para matriz
data = data.values


# vetor = [2,1,3,4,5,61,7,8,9,10,11,12,13,14,15]
# vetor2 = [2,1,3,4,5,61,7,8,9,10,11,12,13,14,16]
seq = []
for aux in range(0,15):
    seq.append(0)


def sequencia(matriz,j,i,cont):
    for num in matriz[j]:
        if i == len(matriz[j])-1:
            break
        # print(f"Numero: {num+1}/ Vetor: {matriz[j][i+1]}")
        if num+1 == matriz[j][i+1]:
            cont=cont+1
            i=i+1
        else:
            if cont > 0:
                seq[cont] = seq[cont]+1
                # print(seq)
                cont=0
            i=i+1
            cont=0
    if cont > 0:
        seq[cont]=seq[cont]+1

def aplica_sequencia(matriz, fim, inicio=0 ):
    for j in range(inicio,fim):
        sequencia(matriz,j,0,0)
       

#[0, 4833, 2891, 1687, 940, 454, 213, 88, 35, 25, 5, 3, 0, 1, 0]
aplica_sequencia(data,round(len(data)/3))
print("Final: ",seq)
aplica_sequencia(data,round(len(data)/3*2),round(len(data)/3))
print("Final: ",seq)
aplica_sequencia(data,round(len(data)),round(len(data)/3*2))
print("Final: ",seq)