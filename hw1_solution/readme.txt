minCost(cost, m, n):
1)initialize memory[m][n] for memoization

2)fill in the first column :
 for i in range(1, m):
	memory[i][0] = memory[i-1][0] + cost[i][0]

3)fill in the first raw:
for j in range(1, n):
        memory[0][j] = memory[0][j-1] + cost[0][j]

4)fill in the rest by considering 4 cases:

a) i<2 and j<2: (then you can move by only one cell)
 memory[i][j] = min(memory[i-1][j-1], memory[i-1][j], memory[i][j-1], ) + cost[i][j]

b) i>=2 and j<2: (then you can move by 2 across i)
 memory[i][j] = min(memory[i-1][j-1], memory[i-1][j], memory[i][j-1], memory[i-2][j]) + cost[i][j]

c) i<2 and j>=2: (then you can move by 2 across j)
  memory[i][j] = min(memory[i-1][j-1], memory[i-1][j], memory[i][j-1], memory[i][j-2]) + cost[i][j]

d) i>=2 and j>=2:  (you can move by 2 vertically and horizontally):

 memory[i][j] = min(memory[i-1][j-1], memory[i-1][j], memory[i][j-1], memory[i-2][j],  memory[i][j-2]) + cost[i][j]

5) return memory[m-1][n-1]
