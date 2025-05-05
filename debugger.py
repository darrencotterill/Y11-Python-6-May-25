

word = "Hello"

for i in range (len(word)):
    print (i)
    letter = word[i]
    print (letter)

def sum(a, b):
    print("Summing ", a, " and", b)
    return (a + b)

for i in range(0,10):
    result = sum(i, i+1)
    print(result)
    

