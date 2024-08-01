def find_sum(a,b):
    sum = a+b
    print(sum)
    return sum 

find_sum (5,10)

find_sum (12,19)

find_sum (14,1)

def average_num(a,b,c):
    average_num= ((a+b+c)/3)
    print(average_num)
    return(average_num)

average_num (1,2,3)

average_num (13,1512,2525)

average_num (141467, 1471849 , 14781984)

def cal_sum (a=4 , b=5):
    print (a+b)
    return a+b


cal_sum()

fruits = ("apple", "mango", "banana", "gauva" , "orange" , "lichi")

print(len(fruits))

def print_list(fruits):
    for item in fruits:
        print(item , end = " ")

print_list(fruits)

def show (n): 
    if (n==0):
        return
    print(n)
    show(n-1)

show(7)















