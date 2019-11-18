# Edge list representation of graphs
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d
import graph_AL as al
import graph_AM as am 

class Edge:
    def __init__(self, source, dest, weight=1):
        self.source = source
        self.dest = dest
        self.weight = weight
        
class Graph:
    # Constructor
    def __init__(self,  vertices, weighted=False, directed = False):
        self.vertices = vertices
        self.el = []
        self.weighted = weighted
        self.directed = directed
        self.representation = 'EL'
        
    def insert_edge(self,source,dest,weight=1):
        if(self.directed == True):
            temp = Edge(source, dest, weight)
            self.el.append(temp)
        else:
            temp = Edge(source, dest, weight)
            temp1 = Edge(dest, source, weight)
            self.el.append(temp)
            self.el.append(temp1)
    
    def delete_edge_(self,source,dest):
        i = 0
        for edge in self.el:
            if (edge.dest == dest) and (edge.source == source):
                self.el.pop(i)
                return True
            i+=1    
        return False
    
    def delete_edge(self,source,dest):
        if source >= len(self.el) or dest>=len(self.el) or source <0 or dest<0:
            print('Error, vertex number out of range')
        else:
            deleted = self.delete_edge_(source,dest)
            if not self.directed:
                print(source, dest)
                deleted = self.delete_edge_(dest,source)
        if not deleted:        
            print('Error, edge to delete not found')  
                
                                
        
    def display(self):
        print('[',end='')

        for edge in self.el:
            print('('+str(edge.source)+','+str(edge.dest)+ ','+str(edge.weight)+ ')',end='')
        #print(']',end=' ')    
        print(']') 
     
    def draw(self):
        g = self.as_AL()
        g.draw()
            
    def as_EL(self):
        return self
    
    def as_AM(self):
        g = am.Graph(self.vertices, self.weighted, self.directed)
        for edge in self.el:
            g.insert_edge(edge.source, edge.dest, edge.weight)
        
        return g
    
    def as_AL(self):
        g = al.Graph(self.vertices, self.weighted, self.directed)
        for edge in self.el:
            g.insert_edge(edge.source, edge.dest, edge.weight)
        return g

        