a = int(input("Enter rows : "))

if a%2 == 0:
    abc = int(a/2)
else:
    abc = int(a/2)+1
d = abc-1
for i in range(1,abc+1):
    for t in range(1,d+1):
        print(end=" ")
    d = d -1
    num =1
    for t in range(2*i-1):
        print(end=str(num)+" ")
        num = num +1
    print("\n")