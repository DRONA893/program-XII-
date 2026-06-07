f=open("book.txt")
s=f.read()
c=0
for i in s:
    if i=='a'or i=='e'or i=='i'or i=='o'or i=='u'or i=='A'or i=='E'or i=='I'or i=='O'or i=='U':
       c=c+1
print("the no of vowels is",c)
f.close
