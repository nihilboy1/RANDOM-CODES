"""
Retornando uma função com uma função
"""

def f(var):
    print(var)


def kk():
    return f

v = kk()
print(v('opa'))
