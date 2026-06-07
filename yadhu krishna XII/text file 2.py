f1=open("seperation.txt","w")
while True:
    line=input("enter data:")
    f1.write(line)
    f1.write("\n")
    choice=input("do you want to continue")
    if choice=="n":
                   break
f1.close()

f2=open("seperation.txt","r")
l1=f2.readlines()
s=""
for i in range(len(l1)):
    l=l1[i].split()
    for j in l:
        s=s+j
        s=s+"#"
    print(s)
f2.close()
