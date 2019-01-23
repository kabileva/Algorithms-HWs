def minCost(cost, m, n):
    memory = [[0 for i in range(m)] for i in range(n)]
 
    memory[0][0] = cost[0][0]
 
    for i in range(1, m):
        memory[i][0] = memory[i-1][0] + cost[i][0]
 
    for j in range(1, n):
        memory[0][j] = memory[0][j-1] + cost[0][j]
 
    for i in range(1, m):
        for j in range(1, n):
            if i<2 and j<2:
                memory[i][j] = min(memory[i-1][j-1], memory[i-1][j], memory[i][j-1], ) + cost[i][j]
            elif i<2 and j>=2:
                memory[i][j] = min(memory[i-1][j-1], memory[i-1][j], memory[i][j-1], memory[i][j-2]) + cost[i][j]
            elif i>=2 and j<2:
                memory[i][j] = min(memory[i-1][j-1], memory[i-1][j], memory[i][j-1], memory[i-2][j]) + cost[i][j]
            else:
                memory[i][j] = min(memory[i-1][j-1], memory[i-1][j], memory[i][j-1], memory[i-2][j],  memory[i][j-2]) + cost[i][j]
                
 
    return memory[m-1][n-1]

'''
cost = [[2,-1,-10,43,9],[1,3,15,3,8],[2,-2,12,6,5],[3,-10,3,3,3],[4,1,43,-8,1]]
print(minCost(cost, 5, 5))
cost = [[4, -10, 3], [9, -2, 4], [5,2,2]]
print(minCost(cost, 3, 3))
'''

#part below is for reading the input

def proceedInput():
    cases = []
    cost = []
    tests = int(raw_input())
    for test in range(tests):
        tmp = raw_input().split()
        m = int(tmp[0])
        n = int(tmp[1])
        for raw in range(m):
            tmp = tmp = raw_input().split()
            for i in range(len(tmp)):
                tmp[i] = int(tmp[i])     
            cost.append(tmp)
        
        case = cost, m, n
        cases.append(case)
        cost = []
       
    return cases, tests

cases, tests = proceedInput()


for i in range(tests):
    cost, m, n = cases[i]
    print(minCost(cost, m, n))
    