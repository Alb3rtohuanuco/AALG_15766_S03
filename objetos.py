import random


class Perro:
    def __init__(self, nombre="", color="", edad=0):
        self._nombre = nombre
        self._color = color
        self._edad = edad

    def Ladrar():
        print("Guau")
    def Saludo(self):
        return "Pata" if random.randint(0,1) == 0 else "Cola"
    def __str(self):
        return f"Perro: {self._nombre}, de color {self._color} y {self._edad}"
    
        
        
        

p = Perro("Fido", "Marron", 5)
p.Ladrar()
print(f"Me saludo con la {p.Saludo()}")
print(p)
print()

q=Perro()
p._nombre="Rambo"
print(q._nombre)
        