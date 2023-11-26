"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    a = 0
    array = []
    while a < len(result): #len se usa para tomar el tamaño de la entrada
        array.append(result[a])
        array.append("@")
        a += 1

    return array
print(fn_hack_9())