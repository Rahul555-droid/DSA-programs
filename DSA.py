######DSA########


def Log(n):
        i=1
        while i<=n:
                i=i*2
                print(i)

def Log2(n):
        for i in range(1,n+1):          #pytho for loop is different byotch.Prefer while for conditionals
                i=i*2
                print(i)

#Log(100) #executes logn times cos of while loop

#Log2(100) #executes n times complexity will be n
        
#i will traverse through whole 100 values and printing 2 through 200 in for loop


#approximation of Harmonic number summation
import math
s=0
for i in range(1,1000001):
        s=s+1/i
print("HM:",s)

print("APPROX:",math.log(1000000))

"""
#approximation for summation of log(k) where k goes from 1 to n
import math
s=0

for i in range(1,100001):
        s=s+math.log(i)
print("summation",s)

print("approx",100000*math.log(100000))
"""
"""
######approximation of ulta reimann zeta function#######
def power(a,b):
    s=1
    for i in range(1,b+1):
        s=s*a
    return s

p=int(input("Enter value of p:"))
n=int(input("Enter value of n:"))
s=0

for i in range(1,n+1):
    s=s+power(i,p)
print("Summantion:",s)

print("Approximation",power(n,p+1)/(p+1))
"""
"""
def fun(n):
	s=i=1
	while s<n:
		i=i+1
		s=s+i
		print("*",i,s)
fun(20)
"""
"""
with open("goal.txt") as file:
    for row in file:
        print(row)
"""
