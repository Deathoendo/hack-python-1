"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    resultado = []
    for i in result:
        if i == "o" :
            i = "0"
        if i == "i":
            i = "1"
        if i == "a":
           i = "@"
        i = i.upper()
        resultado.append(i)
        
    return resultado

print(fn_hack_10())