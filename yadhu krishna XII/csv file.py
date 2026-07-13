import csv

def write():
    f = open("user.csv", "w", newline="")
    w1 = csv.writer(f)
    w1.writerow(["UID", "Password"])
    
    while True:
        UID = input("Enter user name: ")
        Password = input("Enter password: ")
        L1 = [UID, Password]
        w1.writerow(L1)
        
        choice = input("Do you want to continue Y/N: ")
        if choice in ['N', 'n']:
            break
            
    f.close()

def read():
    f = open('user.csv', 'r', newline="")
    R1 = csv.reader(f)
    for i in R1:
        print(i)
    f.close()

def search():
    f = open("user.csv", "r", newline="")
    found = 0
    r2 = csv.reader(f)
    Search_UID = input("Enter the UID whose password to be searched: ")
    
    for i in r2:
        if i[0] == Search_UID:
            print("its password is: ", i[1])
            found = 1
            
    if found == 0:
        print("no such record")
        
    f.close()

# Main execution calls
write()
read()
search()
