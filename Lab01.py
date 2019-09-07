#Daniel Solorzano
#lab01
#sep 6th, 2019
#data Structures fall 2019
import time

#converts from list of chars to string
def convertToString(s): 
    # initialization of string to "" 
    new = "" 
  
    # traverse in the string  
    for x in s: 
        new += x  
  
    # return string  
    return new 
      
def convertToList(s):
    new = []
    
    for i in s:
        new += s[i]
    
    return new



def print_p(chosen, left, n, words):
    if n==0:
        # convert the word, check if it is a word against set
        # print if it is in the set
        
        word = convertToString(chosen)
        if word in words:
            print(word)
        # print(chosen)
    else:
        b = len(left)
        for i in range(b):
           c = chosen+[left[i]] # [] + ['a']
           d = left[:i]+left[i+1:] # ['a'] + ['b','c']
           print_p(c, d, n-1, words)


    
   
    
if __name__ == '__main__':
    condition = True
    newSet = set(line.strip()for line in open('words_alpha.txt')) #open the text file back and read the content
    while condition:
           
        word = input("enter a word or an ampty string to finish: ")
        if len(word) == 0:
            condition = False
        print('Word: ' + word)
        print("The word " + word + " has the following anagrams:")
        
        start = time.time() # start timer
        print_p([], word, len(word), newSet)
        
        end = time.time() # end timer
        total = end - start
        print('it took' , total , 'seconds to find the anagrams')
    print("Bye, thanks for using this program")
        
    
    

