#creating a blank linked list
list = []
for i in range (5):
    list.append(["",i+1])
list[len(list)-1][1] = -1 #setting the pointer of the last index to be the null pointer
StartPointer = -1  #-1 indicates an empty linked list
FreeListPointer = 0 #0 indicates the next available space in which the item could be stored

def display():
    global list
    for row in list:
        print(row) #prints each row of the linked list, consisting of a node value and a pointer to the next node of the list

def InsertOrder(Node): #adds the elements in the linked list in ascending order of numbers
    global StartPointer, FreeListPointer, list
    #step 1: modify the free list pointer and add the node to the linked list
    if FreeListPointer == -1:
        print("Linked list is full.")
    else:
        NewNodePointer = FreeListPointer #takes the value of the first free node available
        FreeListPointer = list[FreeListPointer][1] #updates the freelistpointer to be the next space available, this could be done after adding the node to the list as well
        list[NewNodePointer][0]= Node #adds the node to the list
    
    #step 2: modify the start pointer, in case it is empty
        if StartPointer == -1:
            list[NewNodePointer][1] = -1 #end of the linked list marked at the first available space from the first freelistpointer
            StartPointer = NewNodePointer #marks the startpointer of the linked list to be the first space used up for the first node
        elif Node < list[StartPointer][0]: # adds in ascending order
            list[NewNodePointer][1] = -1 #end of the linked list marked at the first available space from the first freelistpointer
            StartPointer = NewNodePointer #as the node to be added is less than what is already there at the startpointer location, the node is added before that, so the startpointer has to be modified
        else: #other case scenario where the node can be anywhere in between (the loop inside is usually applicable for 3rd node onwards)
            PreviousPointer = StartPointer #in case 2nd node is being added, previous pointer becomes startpointer (before adding)
            currentPointer = list[StartPointer][1] #current pointer is the one pointed by the startpointer
            while currentPointer != -1 and Node > list[currentPointer][0]: #in case the node is larger than what is present at the start pointer, it uses insertion sort to move the larger number to the end
                PreviousPointer = currentPointer #previous pointer becomes current pointer
                currentPointer = list[currentPointer][1] #current pointer is modified to be the one pointed
            list[NewNodePointer][1] = currentPointer #after insertion sort, the pointer new node points to is the next available free space determined by the insertion sort algorithm
            list[PreviousPointer][1] = NewNodePointer #the node before that points to the new node
        return("added")
    
InsertOrder(23)
InsertOrder(22)
InsertOrder(26)
InsertOrder(21)
InsertOrder(39)
InsertOrder(44)
display()




