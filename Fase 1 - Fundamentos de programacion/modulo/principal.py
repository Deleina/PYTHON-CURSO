#como se puede evitar que si se importa un modulo  de una clase 
# se ejecute un codigo de testeo que se hizo?
# es posible gracias al atributo name
import mi_modulo
print('VALOR DE __name__ en principal.py=',__name__)

print("hola desde principal.py")
mi_modulo.hacer_algo()
print("adios desde principal.py")

