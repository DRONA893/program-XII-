print('\t\t\t...')
print('\t\t\t...')
f1 = open('Sample.txt', 'w')

while True:
    line = input('Enter data ')
    f1.write(line)
    f1.write('\n')
    
    choice = input('Do you want to enter more data ')
    if choice == 'n':
        break

f1.close()

f1 = open('Sample.txt', 'r')
data = f1.read()
f2 = open('Sample2.txt', 'w')
f2.write(data)

f1.close()
f2.close()
