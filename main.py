import re
inp_email=input("write your email : ")
seEmail=re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.[A-z]+",inp_email)
lst=[]

if seEmail !=[]:
    lst.append(seEmail)
    print("Email Added")
else:
    print("Invalid mail")

for m in lst:
    print(m)