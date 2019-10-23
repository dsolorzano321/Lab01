#Lab04
#Daniel Solorzano
#Data Structures fall 2019

import numpy as np
import time
import math


class BTree(object):
    # Constructor
    def __init__(self, data, child=[], isLeaf=True, max_data=5):  
        self.data = data #array
        self.child = child 
        self.isLeaf = isLeaf
        if max_data <3: #max_data must be odd and greater or equal to 3
            max_data = 3
        if max_data%2 == 0: #max_data must be odd and greater or equal to 3
            max_data +=1
        self.max_data = max_data

def InsertBTree(T, wordemb):
    if not IsFull(T):
        InsertInternal(T, wordemb)
    else: #if full, split
        m, l, r = Split(T)
        T.data =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,wordemb)  
        InsertInternal(T.child[k],wordemb)

def InsertInternal(T,wordemb):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,wordemb)
    else:
        k = FindChild(T,wordemb)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.data.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,wordemb)  
        InsertInternal(T.child[k],wordemb)

def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_data//2
    if T.isLeaf:
        leftChild = BTree(T.data[:mid],max_data=T.max_data) 
        rightChild = BTree(T.data[mid+1:],max_data=T.max_data) 
    else:
        leftChild = BTree(T.data[:mid],T.child[:mid+1],T.isLeaf,max_data=T.max_data) 
        rightChild = BTree(T.data[mid+1:],T.child[mid+1:],T.isLeaf,max_data=T.max_data) 
    return T.data[mid], leftChild, rightChild 

def InsertLeaf(T,i):
    T.data.append(i)
    T.data.sort(key=lambda obj: obj.word)

def IsFull(T):
    return len(T.data) >= T.max_data
    
def FindChild(T, k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree   
    for i in range(len(T.data)):
        if k.word < T.data[i].word:
            return i
    return len(T.data)

def FindChild2(T, k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree   
    for i in range(len(T.data)):
        if k < T.data[i].word:
            return i
    return len(T.data)

## Retrieve words from glove.txt and imput them into a BST
def getWordsBTree(T, filename):
    file = open((filename), 'r', encoding = 'utf8')  
    print("Retrieving data from the file:" , filename, ".....")
    start = time.time() # start timer
    counter = 0
    for line in file:
        if counter > 400000: ## Stop running after specified number of insertions
            break
        splitLine = line.split(sep = ' ')
        word = splitLine[0]
        if not word.isalpha(): # ignore symbols
            continue
        embedding = np.array([float(val)for val in splitLine[1:]])
        wordemb = WordEmbedding(word, embedding)
        InsertBTree(T,wordemb)
        counter +=1
        
    end = time.time() # end timer
    total = end - start
    print("Finished retrieving data.....")
    print("Running time for B-tree construction (with max_items =",T.max_data ,"):", total)
    return T

def get2WordsBTree(root, file):
    print("Reading word file to determine similarities")
    print("\nWord similarities found")
    start = time.time()
    file = open(file, 'r', encoding = 'utf8')
    for line in file:
        splitLine = line.strip().split(sep = ' ')
        
        word1 = splitLine[0]
        word2 = splitLine[1]
        
        r1 = retrieveBTree(root, word1)
        r2 = retrieveBTree(root, word2)
        #print(r1,r2)

        print("Similarity [", word1,",", word2,"] =", sim(r1, r2))
    end = time.time() # end timer
    total = end - start
    print("Running time for B-tree query processing (with max items = ", root.max_data, "):", total)
def retrieveBTree(T, key):
    # Returns node where k is, or None if k is not in the tree

    for i in T.data:
        #print("key:",key,"i:", i.word)
        if key == i.word:
            #print("here--------------------")
            return i.emb

    #if key in T.data:
        #return T.word
    if T.isLeaf:
        #print("NONE--------------------------")
        return None
    return retrieveBTree(T.child[FindChild2(T,key)], key)

def Print(T):
    # Prints data in tree in ascending order
    if T.isLeaf:
        for t in T.data:
            print(t.word,end=' ')
    else:
        for i in range(len(T.data)):
            Print(T.child[i])
            print(T.data[i].word,end=' ')
        Print(T.child[len(T.data)])    
         
def PrintD(T,space):
    # Prints data and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.data)-1,-1,-1):
            print(space,T.data[i].word)
    else:
        PrintD(T.child[len(T.data)],space+'   ')  
        for i in range(len(T.data)-1,-1,-1):
            print(space,T.data[i].word)
            PrintD(T.child[i],space+'   ')



###################################################################################################
## BST Implementation


class WordEmbedding(object):
    def __init__(self, word, embedding, left = None, right = None):
        # word must be a string, embedding can be a list or and array of ints or floats
        self.word = word
        self.emb = np.array(embedding, dtype=np.float32) # For Lab 4, len(embedding=50)
        self.left = left 
        self.right = right

def InsertBST(T, word, embedding):  
    if T == None:
        T =  WordEmbedding(word, embedding)
    elif T.word > word:
        T.left = InsertBST(T.left, word, embedding)
    else:
        T.right = InsertBST(T.right, word, embedding)
    return T

def get2WordsBST(root, file):
    print("Reading word file to determine similarities")
    print("\nWord similarities found")
    start = time.time()
    file = open(file, 'r', encoding = 'utf8')
    for line in file:
        splitLine = line.strip().split(sep = ' ')
        
        word1 = splitLine[0]
        word2 = splitLine[1]

        r1 = retrieveBST(root, word1)
        r2 = retrieveBST(root, word2)

        print("Similarity [", word1,",", word2,"] =", sim(r1, r2))
    end = time.time() # end timer
    total = end - start
    print()
    print("Running time for BSTree query processing :", total)
def mag(x): 
    return math.sqrt(sum(i**2 for i in x))
    
def sim(e0, e1):
    numer = np.dot(e0,e1)
    denom = mag(e0)* mag(e1)
    
    return numer/denom

## Retrieve words from glove.txt and imput them into a BST
def getWordsBST(filename):
    file = open((filename), 'r', encoding = 'utf8')  
    print("Retrieving data from the file:" , filename, ".....")
    start = time.time() # start timer
    T = None
    counter = 0
    for line in file:
        if counter > 400000: ## Stop running after specified number of insertions
            break
        splitLine = line.split(sep = ' ')
        word = splitLine[0]
        if not word.isalpha(): # ignore symbols
            continue
        embedding = np.array([float(val)for val in splitLine[1:]])
        T = InsertBST(T, word, embedding)
        counter +=1
        
    end = time.time() # end timer
    total = end - start
    print("Finished retrieving data.....")
    print("Running time for binary search tree construction:", total)
    return T

def ShowBST(T,ind):
    # Display rotated BST in text form
    if T is not None:
        ShowBST(T.right,ind+'   ')
        print(ind, T.word)
        ShowBST(T.left,ind+'   ')
        
def retrieveBST(root, word):
    if root.word == word:
        #print(root.word, root.emb)
        return root.emb
    
    else:
        if root.word > word:
            return retrieveBST(root.left, word)
        else:
            return retrieveBST(root.right, word)
        
        
        
def heightBST(T):
    if T == None:
        return 0
    return 1 + max(heightBST(T.left), heightBST(T.right))

def HeightBtree(T):
    if T.isLeaf:
        return 1
    return 1 + HeightBtree(T.child[0])    

def NumItemsBtree(T):
    if T.isLeaf:
        return len(T.data)
    
    count = 0
    for i in range(len(T.child)):
        count += NumItemsBtree(T.child[i])
    
    return count + len(T.data)


def numOfNodesBST(T):
    if T == None:
        return 0
    return 1 + numOfNodesBST(T.left) + numOfNodesBST(T.right)


if __name__ == "__main__":
    print("Choose table implementation")
    choice = input("Type 1 for binary search tree or 2 B-tree")
    print("Choice:", choice)
    if choice == '1':
        bst = getWordsBST("glove.6b.50d.txt")
        print("Height:", heightBST(bst))
        print("Number of Nodes:", numOfNodesBST(bst))
        get2WordsBST(bst, "words.txt")

    else:
        maxsize = input("Please choose size of max number of items per node for the BTree")
        btree = BTree([],max_data=int(maxsize))
        
        getWordsBTree(btree, "glove.6b.50d.txt")
        print("Height:", HeightBtree(btree))
        print("Number of Nodes:", NumItemsBtree(btree))
        #Print(btree)
        get2WordsBTree(btree, "words.txt")

    


    



