#lab03
#DataStrucutres 
#10/04/19

class Node(object):
    # Constructor
    def __init__(self, data, next=None):  
        self.data = data
        self.next = next 
    
class List(object):   
    # Constructor
    def __init__(self,head = None,tail = None):    
        self.head = head
        self.tail = tail
   
    def Print(self):
        t = self.head
        while t is not None:
            print(t.data,end=' ')
            t = t.next
        print()
        
    def Append(self,x):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next
            
    def AppendList(self,python_list):
        for d in python_list:
            self.Append(d) 

    
    def Insert(self, i):
        if self.head is None: 
            i = self.head 
            self.head = i
  
        # Special case for head at end 
        elif self.head.data >= i: 
            i = self.head 
            self.head = i 
  
        else : 
  
            # Locate the node before the point of insertion 
            current = self.head 
            while(current.next is not None and
                 current.next.data < i): 
                current = current.next
              
            i = current.next
            current.next = i
  
    
    
    def Delete(self, x):
        if self is None :
            print("node being searched for does not exist")
        tempL = List()
        tempL.head = self.head.next
        tempL.tail = self.head
        while tempL.head != None:
            if tempL.head.data is x:
                tempL.tail.next = tempL.tail.next.next
                return
            tempL.head = tempL.head.next
            tempL.tail = tempL.tail.next
        

    
    def Index(self, i):
        if self.head is None:
            return -1
        T = self.head
        count = 1
        while T is not None:
            if T.data == i:
                return count    
            count += 1
                
            T = T.next
        return count


    def Clear(self):
        self.head = None

    def Min(self):
        return self.head.data

    def Max(self):
        return self.tail.data


    def Select(self, k):
        if self.head is None:
            return -1
        count = 0
        t = self.head
        while t is not None:
            if count == k:
                print(t.data)
            count += 1
            t = t.next
        


if __name__ == "__main__": 
    
    L1 = List()
    L1.AppendList([1,3,6,8,15,17,18,20,21])

    print("Question 1")
    print("printing the elements of the list")
    L1.Print()

    print("===============================================")
    print("Question 2")
    L1.Print()
    
    print("inserting 7 into list", L1.Insert(7))
    L1.Print()
    print("===============================================")
    
    print("Question 3")
    L1.Print()
    print("deleting 3 from list", L1.Delete(3))
    L1.Print()
    
    print("===============================================")
    
    print("Question 4")
    
    
    
    print("===============================================")
    
    print("Question 5")
    L1.Print()
    print("return the index of i in the list")
    
    print("the index of 18 is:", L1.Index(18))
    
    
    print("===============================================")
    
    print("Question 6")
    print("removing all the elements of the list")
    
    L1.Clear()
    
    L1.Print()
    
    print("===============================================")
    print("===============================================")
    #creating a new lst because of deletion of previous
    L2 = List()
    L2.AppendList([3,7,8,10,11,16,13,19])
    print("The new list is:")
    L2.Print()
    
    print("===============================================")
    print("===============================================")
    
    print("Question 7")
    print("The smallest element of the list is:", L2.Min())
    
    print("===============================================")
    
    print("Question 8")
    print("The largest element of the sorted list is:", L2.Max())
    
    print("===============================================")
    print("Question 10")
    
    print("using the self function to find the 4th element")
    
    L2.Select(3)
    
    #missing questions 4, 9 and 10
    