#Creating a new file
print("New")
print("Jeevan jyoti Sahoo")

# Biggest Sum

handler = open("bigsum.txt")

lines = handler.readlines()
ar = lines[1].split(' ')

for i in range(len(ar)):
    ar[i] = int(ar[i])
    
print(sum(ar))
