from libs.jogo import *
from pytest import mark, raises
import pytest

def test_quando_func_pense_num_numero_recebe_qualquer_valor_1_entao_retorna_3():
    qualquer = 65
    resposta = pense_num_numero(qualquer)
    assert resposta == 3

def test_quando_func_pense_num_numero_recebe_qualquer_valor_2_entao_retorna_3():
    qualquer =11
    resposta = pense_num_numero(qualquer)
    assert resposta == 3

def test_quando_func_pense_num_numero_recebe_qualquer_valor_3_entao_retorna_3():
    qualquer = 9
    resposta = pense_num_numero(qualquer)
    assert resposta == 3

def test_quando_func_pense_num_numero_recebe_qualquer_valor_4_entao_retorna_3():
    qualquer = 1
    resposta = pense_num_numero(qualquer)
    assert resposta == 3

# Estudo das Exceptions
@mark.retorno
def test_quando_func_pense_num_numero_recebe_valor_negativo_entao_retorna_except():
    qualquer = -1
    resposta = pense_num_numero(qualquer)
    assert resposta == 3

# Função para testar o Exception
@mark.retorno2
def test_avalia_exception_da_func_pense_num_numero():
    qualquer = -4
    with pytest.raises(Exception):
        retorno = pense_num_numero(qualquer)
        assert retorno