x=int(input("Enter Number for number of recursions: "))
def print1toten(n):
    if (n>x):
        return
    print(n)
    print1toten(n+1)
print1toten(1)