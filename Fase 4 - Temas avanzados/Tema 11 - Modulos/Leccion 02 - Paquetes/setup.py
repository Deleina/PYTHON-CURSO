from ensurepip import version
#en este fichero vamos a definir imformacion basica con 
# imformacion sobre el paquete 

from setuptools import setup

setup(
    name="paquete",
    version="0.1",
    description="este es un paquete de ejemplo",
    author="marta deleina",
    author_email="marta.deleina@gmail.com",
    url="http://m.inmfo",
    scripts=[],
    packages=["paquete", "paquete.adios","paquete.hola"]
)
