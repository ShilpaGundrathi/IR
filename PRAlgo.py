import numpy as np
import numpy.matlib as npm

print("Enter the path of the graph in matrix format, with three columns (I,j,k) as Integers: ")
data = input()
def pageRank(file, beta = .85, epsilon = .001):
    data = np.loadtxt(file, delimiter=" ",dtype=int)
    data_list = data.tolist()
    edge_u  = [item[0] for item in data_list]
    edge_v =  [item[1] for item in data_list]
    x =(edge_u+edge_v)
    no_nodes = len(set(x))
    n = len(set(x))+1
    adjMatrix = np.array( [[0 for i in range(n)] for k in range(n)])
    for i in range(len(edge_u)):
        u = edge_u[i]
        v = edge_v[i]
        adjMatrix[u][v] = 1
    adjMatrix = np.delete(adjMatrix, (0), axis=0)
    adjMatrix = np.delete(adjMatrix, (0), axis=1)
    size_matrix = len(adjMatrix)
    matSum = adjMatrix.sum(axis=1)
    sumMatrix = np.zeros((size_matrix,size_matrix))
    for i, (row,matSum) in enumerate(zip(adjMatrix,matSum)):
        if(matSum!=0):
            sumMatrix[i,:] = row / matSum
        else:
            sumMatrix[i,:] = row
    M = sumMatrix.transpose()
    np.savetxt('test.txt', M)
    print(M)
#     calculating (1-beta)e/n
    e = np.matlib.ones((no_nodes, 1), dtype=np.int)
    r0 = np.matlib.ones((no_nodes, 1), dtype=np.int)/no_nodes
    y = (1-beta) * e / no_nodes
    # calculating  beta*m*v+y
    x = beta*M
    # matrix format of all
    y = np.asmatrix(y)
    r0 = np.asmatrix(r0)
    print(r0)
    x = np.asmatrix(x)
    count = 0
    while (True):
        r = x*r0 + y
        if (np.sum(np.abs(r - r0)) > epsilon):
            r0 = r
        else:
            break
        count = count + 1
    print(r)
    print("Number of iterations are : ", count)

pageRank(data)

