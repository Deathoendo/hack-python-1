"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    a = 5
    while a <= 5:
        result.append(a)
        a -=1
        if a == -1:
            break
    
    return result  

print(fn_hack_7())