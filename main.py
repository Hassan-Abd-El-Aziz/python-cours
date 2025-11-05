a="hassan"
d=["one",2,"two"]
c=("a","b","c")
b={1,2,3}
e={"a":"one","b":"two"}
q=100

print(list(a))
print(list(b))
print(list(c))
print(list(e))
# print(list(q))#error

print(tuple(a))
print(tuple(b))
print(tuple(e))

# user input
print("*" * 50)
f_name=input("enter your first name :")
l_name=input("enter your last name :")
age=input("enter your age :")

print(f"Hello {f_name} {l_name[0]} your age is {age}")

# *************************************************************
name=input("enter your name").strip().capitalize()
email=input("enter mail ").strip()

mailname=email[:email.index("@")]
domin=email[email.index("@")+1:]
print(f"hi {name} name in mail is :{mailname} your domain is: {domin}")

# -----------------------------------------------
age=int(input("enter your age :").strip())

month=age*12
week=month*4
days=week*365

print(f"age in month is {month}")
print(f"age in week is {week}")
print(f"age in days is {days:,}")

# -------------------------------------------------
name="hassan"
cuntry=input("enter your cuntry : ").strip()
price=1500
if cuntry=="ksa":
    print(f"Hello {name} from {cuntry} your price is {price-50}")
elif cuntry=="egypt":
    print(f"Hello {name} from {cuntry} your price is {price-500}")
elif cuntry=="Kwit":
    print(f"Hello {name} from {cuntry} your price is {price-100}")
else:
    print(f"Hello {name} from {cuntry} your price is {price-10}")
    

trnary if
name="hassan"
age=19
movierate=18
print(f"welcome {name}" if age >movierate else "out of rate")

# **********************
age=int(input("enter your age :"))
month=age*12
week=month*4
days=week*365
inp=input("enter what do you want : m,w,d")

print(f"heloo zizo {month}" if inp == "m" else "error"   )
print(f"heloo zizo {week}" if inp == "w" else "error"   )
print(f"heloo zizo {days}" if inp == "d" else "error"   )
# ********************

my_frinds=["hassan","zizo","mido"]

print("zizo" in my_frinds)

name="mido"
print("d" in name)

# /////////////////\\\\\\\\\\\\\\\\\
cuntries=["Eg","ks","sa"]
cun=input("enter your cuntry : ")
if cun in cuntries:
    print(f"helooo figo")
else:
    print("goooo")

admins=["Hassan","Hhmed"]
login_name=input("enter your name").strip().capitalize()

if login_name in admins:
    delete_update=input("inter what do you want delete, or update or d or m").capitalize()
    if delete_update =="Update" or delete_update=="U":
        newval=input("enter new value").strip().capitalize()
        admins[admins.index(login_name)]=newval
        print(admins)
    elif delete_update =="Delete" or delete_update=="D":
        admins.remove(login_name)
        print(admins)
    else:
        print("wrong option")
else:
    print("your are not admin add you")
    newadmin=input("select y,n")
    if newadmin =="y":
        admins.append(login_name)
        print(admins)
    else:
        print("your are not added")

# ******************************
a=["a","b","c","d"]
s=0
while s<len(a):
    print(f"number {str(s+1) } {a[s]}")
    s +=1
else:
    print("all printed")

print("*" *100)

my_webs=[]
maximum=5
while maximum > 0:
    web=input("enter your web").strip().lower()
    my_webs.append(web)
    maximum -=1
    print(f"https:// {my_webs}")
    print(f"you have {maximum} tries left")
else:
    print("full")

print("*" *100)

tries=4
mainpqssword="zizo"
password=input("enter your passwersd : ")

while password != mainpqssword:
    tries -=1
    print(f"wrong password you have {'last' if tries==0 else tries} left")
    password=input("enter your passwersd : ")

    if tries==0:
        print("all tries is finshed")
        break
else:
    print("correct passward")

print("*" *100)
for r in range(1,11):
    print(f"number {r}")