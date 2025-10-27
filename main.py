i=100
f=100.7
com=5+6j

print(type(i))
print(type(f))
print(type(com))

print(com.real)
print(com.imag)

print(int(f))

# Arithmetic oprator
print(10+5)# addition
print(100-50)# subtraction
print(10*2)# multiplication
print(20/2)# division
print(9%2)# modulues
print(5**3)#exponent
print(140//20)# floor division

# lists

mylist=[1,"one",2,"two",3,"three"]
print(mylist)
mylist[0:2]=[1]
print(mylist)
mylist[1:2]=[2]
print(mylist)
mylist[2:3]=[3]
print(mylist)
mylist[3:4]=[4]
print(mylist)
mylist[4:]=["non"]
print(mylist)

print("#" *50)

lstone=["one","two","three"]
lstTwo=["four","five"]
lstone.append(1)
lstone.append(lstTwo)
print(lstone)
print(lstone[4][1])

a=[1,2,3]
b=[6,4,5]
c=["one","two"]

b.extend(c)

a.extend(b)
print(a)

x=["A","B","C","D","A"]
x.remove("A")
print(x)

d=[5,1,3,6,2,4,0]
d.sort()
print(d)
d.reverse()
print(d)
z=d.copy()
d.clear()
print(d)
print(z)
z.sort()
print(z)
z.reverse()
print(z)

nm=[1,2,1,3,4,1,2,1,2,3,4]
print(nm.count(1))

print(nm.index(4))

nm.insert(2,"test")
print(nm)

s=[1,2,"A","b"]
print(s.pop(2))