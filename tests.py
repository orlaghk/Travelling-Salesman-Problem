import math
import graph
import time
import random

g=graph.Graph(6,"sixnodes")

#g.swapHeuristic(-6)
#g.TwoOptHeuristic(6)
#g.Greedy()
g.furthestInsertion()

g.tourValue()

#to find an average tour value and runtime I will caculate each of the three sets of data given on each of the algorithms.




def results(num, name, alg):
    avgTourValue = 0
    timesTaken = 0
    for i in range(0,50):
        g=graph.Graph(num,name)
        startTime = time.time()
        if(alg == "swap"):
            g.swapHeuristic(num)
        elif(alg == "TwoOpt"):
            g.TwoOptHeuristic(num)
        elif(alg == "Greedy"):
            g.Greedy()
        elif(alg == "furthestInsertion"):
            g.furthestInsertion()
        timeTaken = time.time() - startTime
        timesTaken = timesTaken + timeTaken
        avgTourValue = avgTourValue + g.tourValue()

    avgTourValue = avgTourValue/50
    timesTaken = timesTaken/50

    return(avgTourValue, timesTaken)

#Firstly calculating the values for six nodes.
print("\n Six Node Results, (Average Tour Value, Average Time Taken)")
sixNoAlg = (results(6, "sixnodes", "none"))
print("No algorithm :", sixNoAlg)

sixSwap = (results(6, "sixnodes", "swap"))
print("Swap :", sixSwap)

sixTwoOpt = (results(6, "sixnodes", "TwoOpt"))
print("2-Opt Heuristic :", sixTwoOpt)

sixGreedy = (results(6, "sixnodes", "Greedy"))
print("Greedy :", sixGreedy)

sixFurthestInsertion = (results(6, "sixnodes", "furthestInsertion"))
print("Furthest Insertion :", sixFurthestInsertion)

#Calculating the values for twelve nodes.
print("\n Twelve Node Results, (Average Tour Value, Average Time Taken)")
twelveNoAlg = (results(12, "twelvenodes", "none"))
print("No algorithm :", twelveNoAlg)

twelveSwap = (results(12, "twelvenodes", "swap"))
print("Swap :", twelveSwap)

twelveTwoOpt = (results(12, "twelvenodes", "TwoOpt"))
print("2-Opt Heuristic :", twelveTwoOpt)

twelveGreedy = (results(12, "twelvenodes", "Greedy"))
print("Greedy :", twelveGreedy)

twelveFurthestInsertion = (results(12, "twelvenodes", "furthestInsertion"))
print("Furthest Insertion :", twelveFurthestInsertion)

#Calculating the values for cities50.
print("\n Cities50 Results, (Average Tour Value, Average Time Taken)")
cities50NoAlg = (results(-1, "cities50", "none"))
print("No algorithm :", cities50NoAlg)

cities50Swap = (results(-1, "cities50", "swap"))
print("Swap :", cities50Swap)

cities50TwoOpt = (results(-1, "cities50", "TwoOpt"))
print("2-Opt Heuristic :", cities50TwoOpt)

cities50Greedy = (results(-1, "cities50", "Greedy"))
print("Greedy :", cities50Greedy)

cities50FurthestInsertion = (results(-1, "cities50", "furthestInsertion"))
print("Furthest Insertion :", cities50FurthestInsertion)



#code which creates a file of euclidean values, given an starting and ending limit

def euclideanGenerator(node1, node2, n):
    
    for i in range(n):
        if i==0:
            file = open(f'cities{n}', "w")
        else:
            file = open(f'cities{n}', "a")
        
        node = (random.randint(0, node1), random.randint(0, node2))
        file.write(f' {node[0]} {node[1]}' + '\n')
        file.close()


print (euclideanGenerator(75, 75, 75))

#Calculating the values for cities60.
print("\n Cities60 Results, (Average Tour Value, Average Time Taken)")
cities75NoAlg = (results(-1, "cities75", "none"))
print("No algorithm :", cities75NoAlg)

cities75Swap = (results(-1, "cities75", "swap"))
print("Swap :", cities75Swap)

cities75TwoOpt = (results(-1, "cities75", "TwoOpt"))
print("2-Opt Heuristic :", cities75TwoOpt)

cities75Greedy = (results(-1, "cities75", "Greedy"))
print("Greedy :", cities75Greedy)

cities75FurthestInsertion = (results(-1, "cities75", "furthestInsertion"))
print("Furthest Insertion :", cities75FurthestInsertion)

