from libs.calculadora import Calculadora
from libs.jogo import pense_num_numero, pense_num_numero2

c= Calculadora()
r1 = c.soma(2,2)
print(r1)

v1 = pense_num_numero(5)
v2 = pense_num_numero(4)
v3 = pense_num_numero2(15)
v4 = pense_num_numero2(65)

print(f'Resultados v1={v1}, v2={v2}, v3={v3}, v4={v4}')
