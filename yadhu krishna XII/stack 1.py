vowels = ['a', 'e', 'i', 'o', 'u']
words = input("Enter the word to search the vowels: ")
stack = []

for letter in words:
    if letter in vowels:
        if letter not in stack:
            stack.append(letter)

print(stack)
print("The number of unique vowels present in words is:", len(stack))
