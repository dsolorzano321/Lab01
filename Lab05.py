import numpy as np
import time
import math
import sys
choice = 1

class HashTableL(object):
    #builds a hash table of size 'size'
      
    def __init__ (self, size, num_items=0):
          self.item = [None] * size
          self.num_items = 0
          
class Word:
    def __init__(self, word, embedding):
        self.word = word
        self.embedding = embedding
      
def getWords(filename):
    words = []
    embeddings = []
    file = open((filename), 'r', encoding = 'utf8')  
    print("Retriving data from the file:" , filename, ".....")
    start = time.time() # start timer
    # importing words and embeddings from file
    for line in file:
        splitLine = line.split(sep = ' ')
        word = splitLine[0]
        words.append(word)
        embedding = np.array([float(val)for val in splitLine[1:]])
        embeddings.append(embedding)
    end = time.time() # end timer
    total = end - start
    print("Finished retrieving data.....")
    print("Time taken:", total)
    return words, embeddings     
        
     
def get2Words(file):
    print("Reading word file to determine similarities")
    print("\nWord similarities found")
    file = open(file, 'r', encoding = 'utf8')
    for line in file:
        splitLine = line.strip().split(sep = ' ')
        
        word1 = splitLine[0]
        word2 = splitLine[1]

        r1 = retrieve(word1)
        r2 = retrieve(word2)

        print("Similarity [", word1,",", word2,"] =", sim(r1, r2))

    
## Insert method
def Insert(H, w, e): 
    sum = 0
    word = Word(w, e) # create the object with the word w
    for i in w:
        asci = ord(i)
        sum = sum + asci
    #print('Ascii val:', sum)
    for i in range(len(H.item)):
        if choice is 1:
            
            pos = (len(w) + i) % len(H.item)
            if H.item[pos]  == None:
                H.item[pos] = word
                H.num_items += 1
                return None
            
        if choice is 2:
            pos = (ord(w[0]) + i) % len(H.item)
            if H.item[pos]  == None:
                H.item[pos] = word
                H.num_items += 1
                return None
        if choice is 3:
            pos = (ord(w[0]) * ord(w[-1]) + i) % len(H.item)
            if H.item[pos]  == None:
                H.item[pos] = word
                H.num_items += 1
                return None
        if choice is 4:
            pos = (sum + i) % len(H.item)
            if H.item[pos]  == None:
                H.item[pos] = word
                H.num_items += 1
                return None
        if choice is 5:
            pos = recursiveH(w, len(H.item))
            if H.item[pos]  == None:
                H.item[pos] = word
                H.num_items += 1
                return None
        if choice == 6:
            pos = int((len(w)*100/2 + i) % len(H.item))
            if H.item[pos]  == None:
                H.item[pos] = word
                H.num_items += 1
                return None
    return None    
    
def recursiveH(S, n):
    if len(S) == 1:
        return 1
    else:
        return(ord(S[0]) + 255 * recursiveH(S[1:],n) ) % n
    
def retrieve(word):
    if choice == 1:
            
        for i in range(len(H.item)):
            pos = (len(word)+i) % len(H.item)

            if H.item[pos] == None:
                pass
            else :
                if H.item[pos].word == word:
                    return H.item[pos].embedding
        print("word was not found")

    if choice == 2:
        for i in range(len(H.item)):
            pos = (ord(word[0]) + i) % len(H.item)

            if H.item[pos] == None:
                pass
            else :
                if H.item[pos].word == word:
                    return H.item[pos].embedding
        print("word was not found")
    
    if choice == 3:
        for i in range(len(H.item)):
            pos = (ord(word[0])* ord(word[-1]) + i) % len(H.item)

            if H.item[pos] == None:
                pass
            else :
                if H.item[pos].word == word:
                    return H.item[pos].embedding
        print("word was not found")
        
    if choice == 4:
        sum = 0
        for i in word:
            asci = ord(i)
            sum = sum + asci
            
        for i in range(len(H.item)):
            pos = (sum + i) % len(H.item)

            if H.item[pos] == None:
                pass
            else :
                if H.item[pos].word == word:
                    return H.item[pos].embedding
        print("word was not found")   
    if choice == 5:
        for i in range(len(H.item)):
            pos = (ord(word[0])+ ord(word[-1]) + i) % len(H.item)
            #print("Pos",pos,"Word", word)
            if H.item[pos] == None:
                pass
            else :
                if H.item[pos].word == word:
                    return H.item[pos].embedding
        print("word was not found")
        
    if choice == 6:
        for i in range(len(H.item)):
            pos = int((len(word)*100/2 + i) % len(H.item))

            if H.item[pos] == None:
                pass
            else :
                if H.item[pos].word == word:
                    return H.item[pos].embedding
        print("word was not found")

def mag(x): 
    return math.sqrt(sum(i**2 for i in x))
    
def sim(e0, e1):
    numer = np.dot(e0,e1)
    denom = mag(e0)* mag(e1)
    
    return numer/denom



def longestChain(H):
  count = 0
  temp = 0
  for i in range(len(H.item)*2):
    pos = (i) % len(H.item)
    if H.item[pos] != None :
      temp +=1
    else :
      if temp > count: 
        count = temp
      temp = 0
  return count


if __name__ == "__main__":
    
    words, embeddings = getWords("glove.6b.50d.txt")
    H = HashTableL(101) # set initial hash table size
    
    choice = int(input("Choose hash function 1 to 6 \n"))
    if choice > 6 or choice < 1:
        print("You chose a number that was not a hash function.... Aborting")
        sys.exit()
    print("Choice:", choice)
    print("Building hash table\n")
    start = time.time()
    for i in range(10000):
        LF = H.num_items / len(H.item)
        
        if LF >= 0.5: # increase table size if load factor is greater than 0.5
            #H.num_items = (H.num_items*2)+1
            #print("Load factor reached, doubling table size to:", len(H.item)*2)
            #start = time.time() # start timer
            for i in range(len(H.item)):
                H.item.append(None)
           
                
        Insert(H, words[i], embeddings[i])
    end = time.time() # end timer
    total = end - start
     
    print("Hash table stats:")
    print("Table size:", len(H.item))
    print("Load Factor:", H.num_items / len(H.item))
    print("Longest chain:", longestChain(H))
    print("Running time for table construction:",total)
    print()
    # print stats
    
    start = time.time() # start timer
    get2Words('words.txt')
    end = time.time() # start timer
    total = end - start
    print("Running time for query processing:" , total)