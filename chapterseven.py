f =open("sample.txt", "r")

line1= f.readline()
print(line1)

line2= f.readline()
print(line2)

line3 = f.readline()
print(line3)

f = open("sample.text" , "a")
f.write("\n I love from friends and family. They are the best. I hope everyone is doing their best and achieve what they wish to.")

import os
os.remove("sample.txt")








