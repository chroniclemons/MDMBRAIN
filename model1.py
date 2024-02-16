import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import random
import networkx as nx

global n
global k
global adjmatrix

n = 10
k = 1
adjmatrix = np.zeros(shape=(n,n))
def AdjMatrix(n, mode):          
            if mode == 'random':
                count = 0
                while count < random.randrange(n, n * (n - 1)):
                    ran1 = random.randrange(0, n)
                    ran2 = random.randrange(ran1, n)
                    if adjmatrix[ran1][ran2]==1:
                        continue
                    elif ran1 == ran2:
                        continue
                    else:
                        adjmatrix[ran1][ran2] = 1
                        count += 1
            elif mode == 'circular':
                j = 0
                adjmatrix[0][n-1] = 1
                while j < n - 2:
                    adjmatrix[j][j + 1] = 1
        
                    j += 1
                adjmatrix[n - 2][n - 1] = 1
            else:
                return
            
            ## to make sure the adjmatrix makes sense (upper triangular form and no selfnections)
            i = 0
            while i < n:
                j = 0
                while j < n:
                    if i == j:
                        adjmatrix[i][i] = 0
                    else:
                        adjmatrix[j][i] = adjmatrix[i][j]
                    j += 1
                i +=1
            return adjmatrix
       
        
def dx_dt(x, t):
    nodes = np.zeros(shape=(n,))   
    
    
    def gen_dx_dt(nodes):
        edges = []
        j = 0
        out = []
        while j < len(adjmatrix):
            i = j
            while i < len(adjmatrix):
                if adjmatrix[j][i] == 1:
                    edges.append([i,j])
                    i += 1
                else:
                    i += 1
                    continue
            j += 1
                
        for _ in range(n):
            a_n = []
            for con in edges:
                if con[0] == _:
                    a_n.append(con[1])                
            out.append(a_n)
            
        return out
    
   
    output = np.zeros(shape=(n,))   
    i = 0
    while i < n:
        output[i] += (- k * x[i])
        for num in (gen_dx_dt(nodes))[i]:
            output[i] += x[num]
        i += 1
        
    
    return output
            
def draw_graph():
    graph = nx.Graph()
    count = 0
    color_map = []
    while count < n:
        graph.add_node(count)
        if count == 0:          
            color_map.append('green')
        else:
            color_map.append('cyan')
        count += 1
    j = 0
    while j < n:
        i = j
        while i < n:
            if adjmatrix[i][j] == 1:
                graph.add_edge(i, j)
                i += 1
            else:
                i += 1
        j += 1
    plt.figure(nx.draw(graph, node_color=color_map , with_labels=True, font_weight='bold'))

    




#setting initial conditions    
x = np.zeros(shape=(n,))
x[0] = 100
time = 0
AdjMatrix(n, 'circular')
value_matrix = []
time_values = np.zeros(shape=(101,))
c = 0
while time < 10:
    sol = odeint(dx_dt, x, (0, time))
    value_matrix.append(sol[:][1])
    time_values[c] = time
    time += 0.1
    c += 1

draw_graph()
plt.plot(time_values, value_matrix[:])  
plt.show()

