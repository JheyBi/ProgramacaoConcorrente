import pandas as pd
import threading
import time

seq = []
for aux in range(0,15):
    seq.append(0)

def le_entrada(path):
    data = pd.read_csv(path)
    # Excluir coluna "Concurso" e "Data"
    data = data.drop(columns=["Concurso", "Data"])
    # convete para matriz
    data = data.values
    return data

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

def aplica_sequencia(matriz, inicio, fim):
    #printa qual thread é
    print(f"Thread: {threading.current_thread().name} - Intervalo = ({inicio+1} - {fim})")
    # print(f"Matriz inicio = {matriz[inicio]}")
    for j in range(inicio,fim):
        sequencia(matriz,j,0,0)
    # print(f"Matriz fim = {matriz[fim-1]}")

def imprime_sequencia():
    
    for i in range(1,len(seq)):
        print(f"sequencia de {i+1} - {seq[i]}")
    

# def aplica_thread(data, num_thread):
    
#     intervalo = len(data)/num_thread

#     for num in range(0,num_thread):
#         t = Thread(target=aplica_sequencia, args=(data,int(intervalo*num),int(intervalo*(num+1))))
#         t.start()



       
#main
def main():
    data = le_entrada("resultados.csv")
    

    #[0, 4833, 2891, 1687, 940, 454, 213, 88, 35, 25, 5, 3, 0, 1, 0]
    tempo_inicial = time.time()
    aplica_sequencia(data,0,len(data))
    tempo_final = time.time()
    print(f"Tempo de execução 1 thread: {tempo_final - tempo_inicial}")
    imprime_sequencia()


    #thread
    #zera a seq
    for aux in range(0,15):
        seq[aux] = 0
    tempo_inicial = time.time()

    
    #cria as n threads
    num_thread = 4
    intervalo = int(len(data)/num_thread)

    tempo_inicial = time.time()
    threading.Thread(target=aplica_sequencia, args=(data,0,intervalo)).start()
    for num in range(1, num_thread):
        threading.Thread(target=aplica_sequencia, args=(data,(intervalo*num)+(num-1),intervalo*(num+1)+num)).start()
    tempo_final = time.time()
    print(f"Tempo de execução {num_thread} thread: {tempo_final - tempo_inicial}")
    imprime_sequencia()    

    # num = 0
    # print("tamanho da matriz",len(data))
    # intervalo = len(data)/num_thread
    # print(f"Intervalo = ({round(intervalo*num)} - {round(intervalo*(num+1))})",intervalo)
    # t1 = Thread(target=aplica_sequencia, args=(data,round(intervalo*num),round(intervalo*(num+1))))
    # num=num+1
    # print(f"Intervalo = ({round(intervalo*num)+1} - {round(intervalo*(num+1))})",intervalo)
    # t2 = Thread(target=aplica_sequencia, args=(data,round(intervalo*num)+1,round(intervalo*(num+1))))
    # num=num+1
    # print(f"Intervalo = ({round(intervalo*num)+1} - {round(intervalo*(num+1))})",intervalo)
    # t3 = Thread(target=aplica_sequencia, args=(data,round(intervalo*num)+1,round(intervalo*(num+1))))
    # num=num+1
    # print(f"Intervalo = ({round(intervalo*num)+1} - {round(intervalo*(num+1))})",intervalo)
    # t4 = Thread(target=aplica_sequencia, args=(data,round(intervalo*num)+1,round(intervalo*(num+1))))

main()
