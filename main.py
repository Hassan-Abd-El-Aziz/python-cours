h="I love you Hassan"

print(h.index("n"))
print(h.startswith("H",11))
print(h.endswith("n",16))
print(h.swapcase())

print(h.split())
print(h.rsplit(" ",2))

print(h.center(50,"#"))
print(h.find("ss"))

print("*" *50)

a,b,c,z="1","11","111","1111"
print(a.zfill(4))
print(b.zfill(4))
print(a.zfill(4))
print(a.zfill(4))

print("*" *50)

name="zizo"

print(name.ljust(10,"@"))
print(name.rjust(10,"#"))


e='''hi hassan,
ilove python
and i love js
'''
print(e.splitlines())
s=e.splitlines()
for a in s :
    print(a)

print("*" *50)

txt="heloo\thassan\tilove\tyou"
print(txt)
print(txt.expandtabs(2))

print("*" *50)

tst="I Need 5G"
print(tst.istitle())#true
tst="I need 5g"
print(tst.istitle())#false
print("*" *50)

sps=" "
print(sps.isspace())
print("*" *50)


l="ilove"
print(l.islower())
print(l.isalpha())


idn="hass_n"
idn2="hass-n"
print(idn.isidentifier())
print(idn2.isidentifier())

alln="h33loz1zo"

print(alln.isalnum())


var="one two one two three two three one "

print(var.replace("one","1"))
print(var.replace("two","2",1))
print(var.replace("three","3",2))

lst=["one","two","three","four"]
print(lst)
print("-".join(lst))
print(" ".join(lst))
print("*" *50)

nam="hassan"
age=62
rate=1.5458

# old_formating
print("wellcome %s" % nam)
print("Hello %s your age is %d" % (nam,age))
print("hi %.3s age is %d" % (nam,age))
print("hi %.3s age is %d rate is %.2f" % (nam,age,rate))

# new_formating
print("wellcom {:s}".format(nam))
print("Hello {:s} your age is {:d}".format(nam,age))
print("hi {:.3s} your age is {:d} rate is {:.3f}".format(nam,age,rate))


format_mony=15454654654564
print("your mony in bank is {:,d}" .format(format_mony))

a,b,c="one","two","three"
print("{2:s}, {1:s} , {0:s}" .format(a,b,c))

# last New Formating
skill=["Html","css","js"]

for k,s in enumerate(skill):
    print(f"skill {k + 1} => is {s.capitalize()}")