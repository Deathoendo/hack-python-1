"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    resultado = ""
    for i in result:
        if i == "o" :
            i = "0"
        if i == "i":
            i = "1"
        if i == "a":
           i = "@"
        resultado = resultado + i
    return resultado

print(fn_hack_5())