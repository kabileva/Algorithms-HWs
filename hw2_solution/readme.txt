Environment: Python 2.7

Algorithm:

1) Run Dijkstra's for all permutations of start-stopover sities-targets
2) Insert results of 1 to heap to see if we have several shortest pathes
3) Pop first results with the smallest weight from the heap

Analysis:

V - number os cities
E - number of edges between cities
k - number of stops

1) - O(ElogV) - with heap
   #of permutations = k! , so we have
	O(k!*ElogV) 
2) Insertion is made k! times and it gives:
   O(log1)+O(log2)+...+O(log(k!))
3)Popping is O(log(k!))

So, considering number of stops as constant and small enough (V > k!) we can ignore it, however we should 
take it into account otherwise

Another approach:
- Compute all pathes with Floyd-Warshall
it will give better result if we have small number of stops. otherwise it is useless because we 
won't use the most part of pathes it computes