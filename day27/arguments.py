def add(*args):
    print(args)
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,2,3,4,5,6))
#**kwargs

def calculator(**kwargs):
    print(kwargs)
    print(kwargs.get("add"))
    print(kwargs.get("sub"))
    print(kwargs.get("mul"))
    print(kwargs.get("div"))
calculator(add=5,sub=3,mul=2,div=1  )