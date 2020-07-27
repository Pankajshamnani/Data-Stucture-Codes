#implementing stack using list
max_size=int(input("enter size of stack"))
stack=[]    #create an empty stack

def push(element):
    if(len(stack)==max_size):
        print("sorry stack full")
    else:
        stack.append(element)
def pop():
    if(len(stack)==0):
        print("sorry stack empty")
    else:
        x=stack.pop()
        print("element poped= ",x)

while(1):
    print("Menu")
    print("1.Push")
    print("2.Pop")
    print("3.Display stack")
    print("4.exit")
    op=int(input())
    if op==1:
        element=int(input("enter element to be inserted"))
        push(element)
    elif op==2:
        pop()
    elif op==3:
        print("stack:")
        for i in stack:
            print(i,end=" ")
    elif op==4:
        break
    else:
        print("wrong selection")
