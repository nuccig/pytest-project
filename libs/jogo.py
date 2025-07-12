from libs.calculadora import Calculadora

c= Calculadora()

def pense_num_numero(num):
    if num <0:
        raise Exception('Número precisa ser positivo!')
    else:
        passo_0 = c.soma(num,5)
        passo_1 = c.multiplicacao(passo_0,2)
        passo_2 = c.subtracao(passo_1,4)
        passo_3 = c.divisao(passo_2,2)
        passo_4 = c.subtracao(passo_3,num)
    return passo_4    # sempre será igual a 4

def pense_num_numero2(num):
    return c.subtracao(c.divisao(c.subtracao(c.multiplicacao(c.soma(num,5),2),4),2),num)
