import csv 
import math 

file= open('data.csv',newline='')

reder=csv.reader(file)
fileData= list(reder)
dta=fileData[0]
l=len(dta)
print(l)
def mean(data):
    values=0
    for i in data:
        values=values+int(i)
    mean=values/l
    return(mean)
squares=[]
for i in dta:
    a=int(i)-mean(dta)
    a=a**2
    squares.append(a)
sum=0
for i in squares:
    sum=sum+i
result=sum/l
sd= math.sqrt(result)
print(sd)

