S = []
c = 'y'

while c == 'y' or c == 'Y':
    print("1. Push")
    print("2. POP")
    print("3. Traversal")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        a = input("Enter an element: ")
        S.append(a)
        
    elif choice == 2:
        if S == []:
            print("Empty Stack, Underflow")
        else:
            print("Deleted element is:", S.pop())
            
    elif choice == 3:
        L = len(S)
        if L == 0:
            print("Stack is empty")
        else:
            for i in range(L - 1, -1, -1):
                print(S[i])
                
    else:
        print("Wrong statement")
        
    c = input("Do you want to continue Y/N: ")
