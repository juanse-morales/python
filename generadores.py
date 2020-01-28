# Generadores
# Son identicos a comprensión de lista pero no regresa una lista sino valores sobre los cuales se puede iterar

l = [1,2,3,-1,4]
s = ["H","o","l","a"]
l2 = (c * num for c in s for num in l if num > 0)

print(l)
print(l2.__next__())
print(l2.__next__())

print("Salto")

for letra in l2:
    print(letra)

def factorial(n):
    i = 1;
    while n > 1:
        i = n*i
        yield i
        n -= 1

for e in factorial(5):
    print(e)
