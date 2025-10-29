#Dictionary

user={"name":"hassan","salary":50000,"avilabel":True}


print(user.keys())
print(user.values())
print(user.get("name"))
print(user.get("salary"))

if user.get("avilabel")==True:
    print(f"well come {user['name']}")


skills={"one":{"name":"html","progres":"90%"}}
skills2={"two":{"name":"css","progres":"85%"}}
print("*" *70)

print(skills)
print(skills.get("one").get("name"))
print(skills['one']['progres'])

allskills={"langOne":skills,"langTwo":skills2}

print(allskills)

#methods
allskills.clear()
print(allskills)
allskills.update({"one":"html"})
allskills['one']="css"
print(allskills)
allskills.update({"two":"html"})
print(allskills)

call=allskills.copy()
call.update({"three":"javascript"})
allskills.clear()
print(allskills)
print(call)


print(call.popitem())


print("*" *50)
a={"one":None,"t":15}
print(a)
print(a.setdefault("zizo",55))
print(a)

print("*" *50)

viw={"one":"lst1","two":"lst2"}
lls=viw.items()
viw['three']="lst3"
print(lls)
print(viw)

for ls in lls:
    print(f"key: {ls[0]} value is {ls[1]}")

va=("one","two","three")
b="x"
print(dict.fromkeys(va,b))

print(bool(''))
print(bool('1'))


age=10
cun="EG"
rank=10

print(cun=="EG" and age >5 and rank >3)
print(cun=="EG" and age >5 and rank >11)

print(cun=="EG" or age >5 or rank >3)
print(cun=="EG" or age >15 or rank >11)

print(not age >50)

x=10
x+=10
print(str(x))