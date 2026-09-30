LinkedList = [
    [9512,5],
    [5541,3],
    [1999,0],
    [6651,-1],
    [-1,6],
    [5612,1],
    [-1,-1],
    [-1,4]
]
StartLinkedList = 2
StartEmptyList = 7

def PrintListItems():
    global LinkedList, StartEmptyList, StartLinkedList
    CurrentPointer = StartLinkedList
    while CurrentPointer != -1:
        print(LinkedList[CurrentPointer][0])
        CurrentPointer = LinkedList[CurrentPointer][1]

def PrintEmptyList():
    global LinkedList, StartEmptyList, StartLinkedList
    CurrentPointer = StartEmptyList
    while CurrentPointer != -1:
        print(LinkedList[CurrentPointer][0])
        CurrentPointer = LinkedList[CurrentPointer][1]
    


def AddItem(value):
    global LinkedList, StartEmptyList, StartLinkedList
    if StartEmptyList == -1:
        print("Linked list is full")
    else:
        LinkedList[StartEmptyList][0] = value
        NextEmpty = StartEmptyList
        LinkedList[StartEmptyList][1] = -1
        LastNodePointer = StartEmptyList
        StartEmptyList = NextEmpty
        #now updating the end pointer of the linked list
        CurrentNode = LinkedList[0][0]
        CurrentPointer = 0
        while CurrentNode != -1 and CurrentPointer != -1:
            CurrentNode = LinkedList[CurrentPointer][0]
            PointerToUpdate = CurrentPointer
            CurrentPointer = LinkedList[CurrentPointer][1]
        LinkedList[PointerToUpdate][1] = LastNodePointer

AddItem(8451)

