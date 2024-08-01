count= 1
while count <= 8:
    print(("Hello Guys. I hope you all are doing good. Remember that dawn always follows dusk."))
    count +=1 

    print(count)


count = 1
while count <= 100:
        print(count)
        count += 1

count = 100
while count >= 1:
        print(count)
        count -= 1


n=int(input("Enter number :  "))


a= 1
while a <=10:
    print(n*a)
    a+=1

a= 1
while a <=5:
    print(a)
    if(a==3):
        break
    a+=1

i=0
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1


list = {0,1,2,3}
print(3)

classes = ["one", "two", "three", "four" ]

for val in classes:
    print(val)


nums = [1,4,9,16,25,36,49,64,81,100]

for val in nums:
    print(val)

#question 2

nums= (1,4,9,16,25,36,49,64,81,100)
x=49

idx=0
for el in nums:
    if(el==x):
        print("number found at idx", idx)
        break
    
    idx+=1

for val in range(7):
    print(val)

for i in range (4,11):
        print(i)

for a in range (3,25,2):
    print(a)


n = int(input("Enter your number : "))

for i in range (1,11):
    print(n*i)

for z in range(10):
        pass

print("hey")

n=10

sum = 0
for a in range(1,n+1):
    sum+=a

print("Total sum is :  ",sum)

