import re
my_string="I Love pythone"
search_string=re.split(r"\s",my_string,1)
print(search_string)

strng_two="I_Love-you_pythone-and_A-js"
search_two=re.split(r"-|_",strng_two)
print(search_two)

for count,word in enumerate(search_two,1):
    if len(word)==1:
        continue
    print(f"word num: {count} is {word}")

print("*" *70)

string_three="I_love_you_somuch"
search_three=re.sub(r"_"," $ ",string_three)

print(search_three)