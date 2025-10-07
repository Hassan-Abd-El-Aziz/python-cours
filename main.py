def say_hello(name) -> str:
    print(f"Hello {name}")

say_hello("hassan")

def calc(n1,n2) -> int:
    print(n1+n2)

calc(10,20)

def lst(*nums) -> list:
    print(nums)


lst(list(["hassan","zizo"]))
print(type(lst))