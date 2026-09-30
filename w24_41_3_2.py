#items are added at the front of the linked list
#important to study
LinkedList = [[None for x in range(2)] for x in range(20)] #do not write [[]*2]*20 as inserting items get 
FirstEmpty = 0
FirstNode = -1
for x in range (20):
    LinkedList[x][0] = -1
    LinkedList[x][1] = x + 1
LinkedList[19][1] = -1

def InserData():
    global LinkedList, FirstEmpty, FirstNode
    for x in range (5):
        value = int(input("Input a number"))
        if FirstEmpty != -1:
            #inserting first item to the list:
            if FirstEmpty == 0:
                LinkedList[0][0] = value
                LinkedList[0][1] = -1
                FirstEmpty = 1
                FirstNode = 0
            else: #all the pointers and items have to be shifted first have to be shifted first
                ShiftedPointer = FirstEmpty - 1
                while ShiftedPointer >=0:    
                    LinkedList[ShiftedPointer+1][0] = LinkedList[ShiftedPointer][0]
                    ShiftedPointer-=1
                LinkedList[0][1] = -1
                LinkedList[0][0] = value
                x = 1
                while LinkedList[x][0] != -1 :
                    LinkedList[x][1] = x-1 #decreases the pointer value that will point backwards till the first element in the linked list array
                    x+=1
                FirstNode = x-1
                FirstEmpty = x
                if FirstEmpty == 20:
                    FirstEmpty = -1
        print(LinkedList)

def OutputLinkedList():
    global LinkedList, FirstEmpty, FirstNode
    CurrentPointer = FirstNode
    while CurrentPointer >= 0:
        if LinkedList[CurrentPointer][1]<=FirstNode:
            print(LinkedList[CurrentPointer][0])
        CurrentPointer-=1

def RemoveData(value):
    global LinkedList, FirstEmpty, FirstNode
    CurrentPointer = FirstNode
    while LinkedList[CurrentPointer][0] != value: #while loop means one instance
        CurrentPointer-=1
    CurrentEmptyListPointer = 0
    while LinkedList[CurrentEmptyListPointer][0] != -1:
        CurrentEmptyListPointer+=1
    LinkedList[CurrentPointer][1] = CurrentEmptyListPointer
    LinkedList[CurrentPointer+1][1] = CurrentPointer - 1
    if FirstNode == 0:
        FirstNode = -1 #if the only element in the list is removed, the node should become empty.
    FirstEmpty = CurrentEmptyListPointer
    print(LinkedList)
    print(FirstNode)

def InsertData(): #better simplified algorithm
    global LinkedList, FirstEmpty, FirstNode
    for x in range(5):
        if FirstEmpty != -1:
            NextEmpty = LinkedList[FirstEmpty][1]
            LinkedList[FirstEmpty][0] = int(input("Value: "))
            LinkedList[FirstEmpty][1] = FirstNode
            FirstNode = FirstEmpty
            FirstEmpty = NextEmpty

def RemData(ItemToRemove): #better simplified algorithm
    global LinkedList
    global FirstNode
    global FirstEmpty
    if LinkedList[FirstNode][0] == ItemToRemove:
        NewFirst = LinkedList[FirstNode][1]
        LinkedList[FirstNode][1] = FirstEmpty
        FirstEmpty = FirstNode
        FirstNode = NewFirst
    else:
        if FirstNode != -1:
            CurrentPointer = FirstNode
            PreviousNode = -1
        while(ItemToRemove != LinkedList[CurrentPointer][0] and CurrentPointer != -1):
            PreviousNode = CurrentPointer
            CurrentPointer = LinkedList[CurrentPointer][1]
        if ItemToRemove == LinkedList[CurrentPointer][0]:
            LinkedList[PreviousNode][1] = LinkedList[CurrentPointer][1]
            LinkedList[CurrentPointer][0] = -1
            LinkedList[CurrentPointer][1] = FirstEmpty
            FirstEmpty = CurrentPointer

InserData()
OutputLinkedList()
RemoveData(5)
OutputLinkedList()