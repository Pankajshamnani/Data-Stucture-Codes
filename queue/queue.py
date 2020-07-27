#implementing queue using list
max_size=int(input("enter size of queue"))
queue=[]    #create an empty queue

def enqueue(element):
    if(len(queue)==max_size):
        print("sorry queue full")
    else:
        queue.append(element)
def dequeue():
    if(len(queue)==0):
        print("sorry queue empty")
    else:
        x=queue.pop(0)
        print("element dequeued= ",x)

while(1):
    print("Menu")
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Display queue")
    print("4.exit")
    op=int(input())
    if op==1:
        element=int(input("enter element to be inserted"))
        enqueue(element)
    elif op==2:
        dequeue()
    elif op==3:
        print("queue:")
        for i in queue:
            print(i,end=" ")
    elif op==4:
        break
    else:
        print("wrong selection")
