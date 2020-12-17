#Given: Two positive integers a and b (a<b<10000).
#Return: The sum of all odd integers from a through b, inclusively.

a = int(input('enter value a: '))
b = int(input('enter value b: '))
mysum = 0
for num in range(a,b):
    if num % 2 == 1:
        mysum = mysum + num
     
    print(mysum)