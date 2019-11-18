import graph_AM as am
import graph_AL as al
import graph_EL as el
from queue import Queue
from math import *



'''

# BFS - use Queue
answer = []
q = []
q.append(0)
while q:
    index= q.pop(0)
    answer.append(index)

    #get all of the possible answer []
    for edge in g.al[index]:
        if edge.dest not in q:
            q.append(edge.dest)
print("Using BFS")
print(answer)

'''


def dfs():
    
    #DFS - use Stack
    print("Using DFS")
    answer = []
    previous = []
    rest = []
    q = []
    q.append(0)
    previous.append(0)
    split = False
    once = False
    while q:
        index= q.pop()
        if once:
            rest.append(index)
            once = False
        if len(g.al[index]) == 1 and not split:
            for edge in g.al[index]:
                if edge.dest not in q:
                    q.append(edge.dest)
                    previous.append(edge.dest)
        elif len(g.al[index]) == 1 and split:
            for edge in g.al[index]:
                if edge.dest not in q:
                    q.append(edge.dest)
                    rest.append(edge.dest)
        elif len(g.al[index]) > 1:
            # len = 2
            split = True
            rest = []
            once = True
            for edge in g.al[index]:
                if edge.dest not in q:
                    q.append(edge.dest)
    
        else:
            # len = 0
            answer.append(previous+rest)
            rest = []
            once = True
    
    print(answer)

def dfs2():
    # DFS for graph_EL using Stack


    d = {}
    for edge in g.el:
        if edge.source not in d.keys():
            d[edge.source] = [edge.dest]
        else:
            d[edge.source].append(edge.dest)
    print(d)
    
    
    order= []
    answer = []
    stack = []
    prev = []
    rest = []
    splitted = False

    stack.append(0)
    while stack:
        item = stack.pop()
        order.append(item)
    
        if item in d.keys():
            if len(d[item]) == 1 and not splitted:
                prev.append(item)
                for i in d[item]:
                    stack.append(i)
            elif len(d[item]) == 1 and splitted:
                if d[item] == 15:
                    answer.append(prev+rest)
                    rest = []
                else:
                    rest.append(item)
                    for i in d[item]:
                        stack.append(i)
            elif len(d[item]) > 1:
                splitted = True
                prev.append(item)
                rest = []
    
                for i in d[item]:
                    stack.append(i)
        else:
            answer.append(prev + rest + [15])
            rest = []
    
    
    print("DFS Ordering for graph_EL is :", order)
    print("Answer using DFS Search for graph_EL is :", answer)

# DFS for graph_EL using Stack
g = el.Graph(16, directed = True)
g.insert_edge(0,5)
g.insert_edge(5,4)
g.insert_edge(4,7)
g.insert_edge(4,13)
g.insert_edge(7,2)
g.insert_edge(2,11)
g.insert_edge(11,10)
g.insert_edge(10,15)
g.insert_edge(13,8)
g.insert_edge(8,11)
g.display()

#dfs() # change graph to al to use this
dfs2()

    
