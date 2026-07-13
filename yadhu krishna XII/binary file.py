import pickle

List1 = []

while True:
    roll = int(input("Enter student roll No: "))
    s = input("Enter student name: ")
    student = {"roll No": roll, "Name": s}
    List1.append(student)
    
    choice = input("Do you want to add more record Y/N: ")
    if choice == 'n' or choice == 'N':
        break

file = open("student.dat", "wb")
pickle.dump(List1, file)
file.close()

file = open("student.dat", "rb")
rollNo = int(input("Enter Roll No that you want to search: "))
l1 = pickle.load(file)
file.close()

found = False
for x in l1:
    if x['roll No'] == rollNo:
        print("Name of the student is", x['Name'])
        found = True
        break

if not found:
    print("Record not found")
