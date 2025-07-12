from libs.calculadora import Calculadora
from pytest import mark
import pytest

c=Calculadora()

@mark.skip
@mark.soma
def test_quando_soma_recebe_4_e_3_entao_retorna_7():
    entrada1 = 4  # Given
    entrada2 = 3  # Given
    resultado = c.soma(entrada1,entrada2) # when
    esperado = 7  # Then
    assert resultado == esperado # Then

@mark.soma
def test_quando_soma_recebe_3_e_3_entao_retorna_6():
    assert c.soma(3,3) == 6

@mark.soma
def test_quando_nova_recebe_2_2_entao_retorna_4():
    print("Soma nova... estou na func...")
    assert c.soma(2,2) == 4

# TDD - Kent Beck - One-step Test
def test_quando_subtracao_recebe_2_1_entao_retorna_1():
    print("estou na func...")
    assert c.subtracao(2,1) == 1

def test_quando_subtracao_recebe_3_1_entao_retorna_2():
    in_1 = 3
    in_2 = 1
    resultado = c.subtracao(in_1,in_2)
    esperado = 2
    print(f'Resultado = {resultado}, Esperado = {esperado}')
    assert resultado == esperado

@mark.skip(reason="Ainda não implementei a func.")
def test_quando_exponencial_base_2_de_2_retorna_4():
    assert False


@mark.parametro
@mark.parametrize(
    'entrada',
    [3,5,6,8,9,2]
)
def test_multiplas_somas(entrada):
    assert c.soma(entrada,entrada) == 4

# Parametrize - multiplas
@mark.parametro2
@mark.parametrize(
    'entrada,valor_esperado',
    [(2,4),(7,14),(1,2),(9,18)]
)
def test_multiplas_somas2(entrada,valor_esperado):
    assert c.soma(entrada,entrada) == valor_esperado

# Parametrize - 3 parametros
@mark.parametro3
@mark.parametrize(
    'entrada1,entrada2,valor_esperado',
    [(2,4,6),(7,14,21),(1,2,3),(9,18,27)]
)
def test_multiplas_somas3(entrada1,entrada2,valor_esperado):
    assert c.soma(entrada1,entrada2) == valor_esperado

# Uso do @mark.xfail() - testes para garantir falhas (sei q vai falhar)

@mark.falha
@mark.xfail
def test_soma_que_vai_falhar():
    assert c.soma(2,2) == 7

@mark.falha
@mark.xfail
def test_soma_que_vai_falhar_2():
    assert c.soma(2,2) == 4

# Avaliando Falhas a partir de Sistema Operacional
import sys

@mark.windows
@mark.xfail(sys.platform=='win32',reason='Só deve funcionar no Mac')
def test_soma_que_vai_falhar_3():
    print('Estamos no teste de falha windows')
    assert c.soma(2,2) == 7

#@pytest.mark
def test_meu_teste():
    assert 1==1

# @mark.skipif()

@pytest.mark.pula
@pytest.mark.skipif(sys.platform=='win32', reason='Pula no Wind')
def test_soma_que_vai_pular_wind():
    print('Estamos no teste de falha windows')
    assert c.soma(2,2) == 7

# Como remover Warnings

# Continuar estudando os @markers