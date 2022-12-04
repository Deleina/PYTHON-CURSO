print("hola desde mi modulo.py")
class hacer_algo():
    def __init__(self):
        print("soy una funcion y hago algo")


if __name__ == "__main__":
    print("ejecutando como programa principal")

hacer_algo()
print("adios desde mi modulo.py!")   # Debajo del condicional pero fuera del mismo

print('VALOR DE __name__ en mi_modulo.py=',__name__)