global Queue, Head, Tail
Queue = [None for x in range(10)]
Head = -1 #points to the first element in the queue
Tail = -1 #points to the last element in the queue

def Enqueue(value):
    global Queue, Head, Tail
    if Tail == 9:
        return False
    else:
        if Head == -1:
            Head = 0
        Tail += 1
        Queue[Tail] = value
        return True
    
for x in range(11):
    value = int(input("Input: "))
    status = Enqueue(value)
    if status == False:
        print("Queue is full.")
        
print(Queue)

def Dequeue():
    global Queue, Head, Tail
    if Head == -1 or Head > Tail:
        return -1
    else:
        ToReturn = Queue[Head]
        Head +=1
        return ToReturn