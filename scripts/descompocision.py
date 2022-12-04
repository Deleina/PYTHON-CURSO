import sys
#recorriendo una cadena desde el final
if len(sys.argv) == 2:
	numero=int(sys.argv[1])
	if numero<0 or numero >9999:
		print('error - numero es  incorrecto')
		print('ejemplo : descomposocion.py[0-9999]')

	else:
		####logica
		cadena= str(numero)
		longitud= len(cadena)

		for i in range(longitud):
			print('{:04d}'.format( int(cadena[longitud-1-i])*10**i))

else:
	print('error - argumentos incorrectos')
	print('ejemplo : descomposocion.py[0-9999]')