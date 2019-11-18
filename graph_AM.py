# Adjacency matrix representation of graphs
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d
import graph_EL as el
import graph_AL as al

class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.am = np.zeros((vertices,vertices),dtype=int)-1
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AM'
        
    def insert_edge(self,source,dest,weight=1):
        if(self.directed==True):
            self.am[source][dest] = weight
        else:
            self.am[source][dest] = weight
            self.am[dest][source] = weight


        
    
    def delete_edge(self,source,dest):
        
        self.am[source][dest] = -1
                
        
    def display(self):
        for j in range(len(self.am)):
            print(self.am[j])
        print()
     
    def draw(self):
        g = self.as_AL()
        g.draw()
    
    def as_EL(self):
        g = el.Graph(len(self.am), self.weighted, self.directed)
        for i in range(len(self.am)):
            for j in range(len(self.am[i])):
                g.insert_edge(i,j,self.am[i][j])
                
        return g
    
    def as_AM(self):
        return self
    
    def as_AL(self):
        g = al.Graph(len(self.am), self.weighted, self.directed)
        for i in range(len(self.am)):
            for j in range(len(self.am[i])):
                if(self.am[i][j] != -1):
                    g.insert_edge(i, j,self.am[i][j])
                
        return g


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        

