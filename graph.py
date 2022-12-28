import math
import random
from re import X


def euclid(p,q):
    x = p[0]-q[0]
    y = p[1]-q[1]
    return math.sqrt(x*x+y*y)
                
class Graph:

    # Complete as described in the specification, taking care of two cases:
    # the -1 case, where we read points in the Euclidean plane, and
    # the n>0 case, where we read a general graph in a different format.
    # self.perm, self.dists, self.n are the key variables to be set up.
    def __init__(self,n,filename):
        self.n = n

        f = open(filename, 'r')
        filelines = []
        for l in f:
            filelines.append(l.split())
            for y in range (len(filelines[-1])):
                filelines[-1][y] = int(filelines[-1][y])

        #for metric files
        if(n != -1):
            self.n = n
            self.dists = [[0 for j in range(self.n)] for i in range(self.n)]
            for i in range(0, len(filelines)):
                self.dists[filelines[i][0]][filelines[i][1]] = filelines[i][2]
                self.dists[filelines[i][1]][filelines[i][0]] = filelines[i][2]
        #for euclidean files
        else:
            self.n = len(filelines)
            self.dists = [[0 for j in range (len(filelines))] for i in range(len(filelines))]
            for i in range (0, len(filelines)):
                for j in range (0, len(filelines)):
                    self.dists[i][j] = euclid(filelines[i], filelines[j])
        #list of length self.n
        self.perm = [x for x in range(self.n)]


    # Complete as described in the spec, to calculate the cost of the
    # current tour (as represented by self.perm).
    def tourValue(self):
        val = 0
        for i in range (0, len(self.perm) -1):
            val = val + self.dists[self.perm[i]][self.perm[i+1]]
        val = val + self.dists[self.perm[len(self.perm)-1]][self.perm[0]]

        #print(val)
        return val


    # Attempt the swap of cities i and i+1 in self.perm and commit
    # commit to the swap if it improves the cost of the tour.
    # Return True/False depending on success.
    def trySwap(self,i):
        originalDist = self.dists[(self.perm[(i-1) % self.n])][self.perm[i]] + self.dists[self.perm[(i+1) % self.n]][self.perm[(i+2) % self.n]] 
        swappedDist = self.dists[self.perm[(i-1) % self.n]][self.perm[(i+1) % self.n]] + self.dists[self.perm[i]][self.perm[(i+2) % self.n]]

        if originalDist > swappedDist:
            temp = self.perm[i]
            self.perm[i] = self.perm[(i+1) % self.n]
            self.perm[(i+1) % self.n] = temp
            return True
        else:
            return False

    # Consider the effect of reversiing the segment between
    # self.perm[i] and self.perm[j], and commit to the reversal
    # if it improves the tour value.
    # Return True/False depending on success.              
    def tryReverse(self,i,j):
        
        originalDist = self.dists[self.perm[(i-1) % self.n]][self.perm[i]] + self.dists[self.perm[j]][self.perm[(j+1) % self.n]]
        swappedDist = self.dists[self.perm[(i-1) % self.n]][self.perm[j]] + self.dists[self.perm[i]][self.perm[(j+1) % self.n]]

        if originalDist > swappedDist:
            self.perm[i:j+1]=self.perm[i:j+1][::-1]
            return True
        else:
            return False




    def swapHeuristic(self,k):
        better = True
        count = 0
        while better and (count < k or k == -1):
            better = False
            count = count + 1
            for i in range(self.n):
                if self.trySwap(i):
                    better = True

    def TwoOptHeuristic(self,k):
        better = True
        count = 0
        while better and (count < k or k == -1):
            better = False
            count += 1
            for j in range(self.n-1):
                for i in range(j):
                    if self.tryReverse(i,j):
                        better = True

                        
    # Implement the Greedy heuristic which builds a tour starting
    # from node 0, taking the closest (unused) node as 'next'
    # each time.
    def Greedy(self):
        unusedNodes = [i for i in range(1, self.n)]
        for i in range(self.n -1):
            #list holding the node and the distance
            currentDist = map(lambda x: (x, self.dists[self.perm[i]][x]), unusedNodes)
            #finding minimum of the distance
            minDist = min(currentDist, key = lambda x: x[1])
            self.perm[i+1]=minDist[0]
            unusedNodes.remove(minDist[0])
        
    
    def getFurtherstNode(self, currentNode, unusedNodes):
        #method which finds the furthest node of the unused nodes, from the one passed in
        currentDist = []
        for x in (unusedNodes):
                currentDist.append(self.dists[currentNode][x])
        maxDist = currentDist[0]
        maxNode = unusedNodes[0]
        
        for y in range(1, len(currentDist)):
            if (currentDist[y] > maxDist):
                maxDist = currentDist[y]
                maxNode = unusedNodes[y]
        return maxNode

    def bestPlacement(self, node, subtour):
        #compares palcing a node in between each of the nodes in the subtour, then choses the tuple to go in between based on it adding the minimal length to tour value
        distFromNode = []
        for x in range(len(subtour)):
            distFromNode.append(self.dists[node][x])
        minTuple = [0,1]
        for y in range(len(distFromNode)-1):
            distWithNode = (distFromNode[y]+distFromNode[y+1] - self.dists[y][y+1])
            minDist = (distFromNode[minTuple[0]] + distFromNode[minTuple[1]]) - self.dists[minTuple[0]][minTuple[1]]
            if( distWithNode < minDist):
                minTuple = [y, y+1]

        subtour.insert(minTuple[1], node)
        return subtour


    def furthestInsertion(self):
        unusedNodes = self.perm
        startingNode = random.choice(unusedNodes) #random node as starting point
        unusedNodes.remove(startingNode)
        subtour = [startingNode]

        furthestNode = self.getFurtherstNode(startingNode, unusedNodes)
        unusedNodes.remove(furthestNode)
        subtour.append(furthestNode)
        subtour.append(startingNode) #creates subtour as [starting node, furthest node, starting node]

        for i in range(0, len(unusedNodes)): #for each node not in tour
            currentNode = subtour[i]
            furthestNode = self.getFurtherstNode(currentNode, unusedNodes) # find its furthest node

            subtour = self.bestPlacement(furthestNode, subtour) # then find its best position, based on adding the minimal distance to the tour

            unusedNodes.remove(furthestNode)
        subtour.pop() #remove starting node from the end of the tour
        self.perm = subtour
        



    def Greedys(self):
        usedNodes = []
        currentLowest = 0
        for i in range(0,self.n):
            usedNodes.append(self.perm[currentLowest])
            if(i == 0):
                    currentLowest = 1            
            else:
                currentLowest = 0            
            for j in range(1,self.n -1):                
                if(j != i):
                    if ( usedNodes.__contains__(self.perm[j]) == False) :                        
                        if (self.dists[usedNodes[-1]][self.perm[currentLowest]] > self.dists[usedNodes[-1]][self.perm[j]]):
                        #if ( usedNodes.__contains__(self.perm[j]) == False):
                            currentLowest = j   
        self.perm = usedNodes



