def resta(a,b):
    return a-b
def mensaje (x):
    print("ALERTA: ",x)
def producto(a: int,b: int) -> int:
    return a*b
def saludo(a: str )-> str:
    x="Hola "+a
    return x
def despedida(a:str)->None:
    x="Chao "+a
    print(x)


###    
c=5
d: int = 2
print(resta(c,d))
despedida("Carlos")
print(saludo("Carlos"))
print(producto(5,2))
print(resta(5,2))
mensaje ("enemigo acercandose")