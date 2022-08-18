# Write the solution for "Filter Vowels".

print("Enter the Name of File: ")
fileName = str(input())
fileHandle = open(fileName, "r")
tot = 0
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for char in fileHandle.read():
  if char in vowels:
    tot = tot+1
fileHandle.close()

print("\nTotal Vowels are:")
print(tot)