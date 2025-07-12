"""
Testes abrangentes para a classe Calculadora.
Inclui: marks, parametrização, fixtures, exceptions, edge cases, e boas práticas.
"""

from libs.calculadora import Calculadora
from pytest import mark, raises, fixture, approx
import pytest
import sys
import math

# ============================================================================
# FIXTURES - Configuração reutilizável
# ============================================================================

@fixture
def calculadora():
    """Fixture que retorna uma instância da Calculadora."""
    return Calculadora()


@fixture(params=[1, 2, 5, 10, 100])
def numeros_positivos(request):
    """Fixture parametrizada com números positivos."""
    return request.param


@fixture(params=[-1, -5, -10, -100])
def numeros_negativos(request):
    """Fixture parametrizada com números negativos."""
    return request.param


# ============================================================================
# TESTES DE SOMA - Casos básicos e edge cases
# ============================================================================

class TestSoma:
    """Classe para agrupar todos os testes da operação soma."""
    
    @mark.soma
    @mark.basic
    def test_soma_numeros_positivos(self, calculadora):
        """Testa soma de números positivos."""
        assert calculadora.soma(2, 3) == 5
        assert calculadora.soma(10, 15) == 25
    
    @mark.soma
    @mark.basic
    def test_soma_numeros_negativos(self, calculadora):
        """Testa soma de números negativos."""
        assert calculadora.soma(-2, -3) == -5
        assert calculadora.soma(-10, -5) == -15
    
    @mark.soma
    @mark.basic
    def test_soma_positivo_negativo(self, calculadora):
        """Testa soma de número positivo com negativo."""
        assert calculadora.soma(5, -3) == 2
        assert calculadora.soma(-5, 3) == -2
    
    @mark.soma
    @mark.edge_case
    def test_soma_com_zero(self, calculadora):
        """Testa soma com zero (elemento neutro)."""
        assert calculadora.soma(0, 5) == 5
        assert calculadora.soma(5, 0) == 5
        assert calculadora.soma(0, 0) == 0
    
    @mark.soma
    @mark.edge_case
    def test_soma_numeros_decimais(self, calculadora):
        """Testa soma com números decimais."""
        resultado = calculadora.soma(0.1, 0.2)
        assert resultado == approx(0.3, rel=1e-9)
    
    @mark.soma
    @mark.parametrize("a,b,esperado", [
        (1, 1, 2),
        (5, 5, 10),
        (-1, 1, 0),
        (100, -50, 50),
        (0.5, 0.5, 1.0),
        (1e6, 1e6, 2e6),  # Números grandes
    ])
    def test_soma_parametrizada(self, calculadora, a, b, esperado):
        """Testa soma com múltiplos casos parametrizados."""
        assert calculadora.soma(a, b) == approx(esperado, rel=1e-9)
    
    @mark.soma
    @mark.property_based
    def test_soma_propriedades_matemáticas(self, calculadora):
        """Testa propriedades matemáticas da soma."""
        a, b = 5, 3
        # Propriedade comutativa: a + b = b + a
        assert calculadora.soma(a, b) == calculadora.soma(b, a)
        
        # Propriedade associativa com c = 2
        c = 2
        assert calculadora.soma(calculadora.soma(a, b), c) == calculadora.soma(a, calculadora.soma(b, c))


# ============================================================================
# TESTES DE SUBTRAÇÃO
# ============================================================================

class TestSubtracao:
    """Classe para agrupar todos os testes da operação subtração."""
    
    @mark.subtracao
    @mark.basic
    def test_subtracao_basica(self, calculadora):
        """Testa subtração básica."""
        assert calculadora.subtracao(5, 3) == 2
        assert calculadora.subtracao(10, 4) == 6
    
    @mark.subtracao
    @mark.edge_case
    def test_subtracao_resultado_negativo(self, calculadora):
        """Testa subtração que resulta em número negativo."""
        assert calculadora.subtracao(3, 5) == -2
        assert calculadora.subtracao(1, 10) == -9
    
    @mark.subtracao
    @mark.edge_case
    def test_subtracao_com_zero(self, calculadora):
        """Testa subtração com zero."""
        assert calculadora.subtracao(5, 0) == 5
        assert calculadora.subtracao(0, 5) == -5
        assert calculadora.subtracao(0, 0) == 0
    
    @mark.subtracao
    @mark.parametrize("a,b,esperado", [
        (10, 5, 5),
        (3, 3, 0),
        (-5, -3, -2),
        (0.5, 0.3, 0.2),
        (1000, 1, 999),
    ])
    def test_subtracao_parametrizada(self, calculadora, a, b, esperado):
        """Testa subtração com múltiplos casos."""
        assert calculadora.subtracao(a, b) == approx(esperado, rel=1e-9)


# ============================================================================
# TESTES DE MULTIPLICAÇÃO
# ============================================================================

class TestMultiplicacao:
    """Classe para agrupar todos os testes da operação multiplicação."""
    
    @mark.multiplicacao
    @mark.basic
    def test_multiplicacao_basica(self, calculadora):
        """Testa multiplicação básica."""
        assert calculadora.multiplicacao(3, 4) == 12
        assert calculadora.multiplicacao(7, 6) == 42
    
    @mark.multiplicacao
    @mark.edge_case
    def test_multiplicacao_por_zero(self, calculadora):
        """Testa multiplicação por zero (elemento absorvente)."""
        assert calculadora.multiplicacao(5, 0) == 0
        assert calculadora.multiplicacao(0, 10) == 0
        assert calculadora.multiplicacao(0, 0) == 0
    
    @mark.multiplicacao
    @mark.edge_case
    def test_multiplicacao_por_um(self, calculadora):
        """Testa multiplicação por um (elemento neutro)."""
        assert calculadora.multiplicacao(5, 1) == 5
        assert calculadora.multiplicacao(1, 7) == 7
    
    @mark.multiplicacao
    @mark.edge_case
    def test_multiplicacao_numeros_negativos(self, calculadora):
        """Testa multiplicação com números negativos."""
        assert calculadora.multiplicacao(-3, 4) == -12
        assert calculadora.multiplicacao(3, -4) == -12
        assert calculadora.multiplicacao(-3, -4) == 12
    
    @mark.multiplicacao
    @mark.parametrize("a,b,esperado", [
        (2, 3, 6),
        (-2, 3, -6),
        (-2, -3, 6),
        (0.5, 4, 2.0),
        (10, 0.1, 1.0),
        (1e3, 1e3, 1e6),  # Números grandes
    ])
    def test_multiplicacao_parametrizada(self, calculadora, a, b, esperado):
        """Testa multiplicação com múltiplos casos."""
        assert calculadora.multiplicacao(a, b) == approx(esperado, rel=1e-9)
    
    @mark.multiplicacao
    @mark.property_based
    def test_multiplicacao_propriedades(self, calculadora):
        """Testa propriedades matemáticas da multiplicação."""
        a, b = 4, 5
        # Propriedade comutativa: a * b = b * a
        assert calculadora.multiplicacao(a, b) == calculadora.multiplicacao(b, a)


# ============================================================================
# TESTES DE DIVISÃO - Incluindo tratamento de exceções
# ============================================================================

class TestDivisao:
    """Classe para agrupar todos os testes da operação divisão."""
    
    @mark.divisao
    @mark.basic
    def test_divisao_basica(self, calculadora):
        """Testa divisão básica."""
        assert calculadora.divisao(10, 2) == 5
        assert calculadora.divisao(15, 3) == 5
    
    @mark.divisao
    @mark.edge_case
    def test_divisao_por_um(self, calculadora):
        """Testa divisão por um."""
        assert calculadora.divisao(7, 1) == 7
        assert calculadora.divisao(-5, 1) == -5
    
    @mark.divisao
    @mark.edge_case
    def test_divisao_zero_por_numero(self, calculadora):
        """Testa divisão de zero por um número."""
        assert calculadora.divisao(0, 5) == 0
        assert calculadora.divisao(0, -3) == 0
    
    @mark.divisao
    @mark.exception
    def test_divisao_por_zero_levanta_excecao(self, calculadora):
        """Testa que divisão por zero levanta ZeroDivisionError."""
        with raises(ZeroDivisionError):
            calculadora.divisao(5, 0)
        
        with raises(ZeroDivisionError):
            calculadora.divisao(-3, 0)
        
        with raises(ZeroDivisionError):
            calculadora.divisao(0, 0)
    
    @mark.divisao
    @mark.edge_case
    def test_divisao_numeros_negativos(self, calculadora):
        """Testa divisão com números negativos."""
        assert calculadora.divisao(-10, 2) == -5
        assert calculadora.divisao(10, -2) == -5
        assert calculadora.divisao(-10, -2) == 5
    
    @mark.divisao
    @mark.parametrize("dividendo,divisor,esperado", [
        (8, 2, 4),
        (9, 3, 3),
        (1, 2, 0.5),
        (7, 4, 1.75),
        (-12, 3, -4),
        (15, -5, -3),
        (-20, -4, 5),
    ])
    def test_divisao_parametrizada(self, calculadora, dividendo, divisor, esperado):
        """Testa divisão com múltiplos casos."""
        assert calculadora.divisao(dividendo, divisor) == approx(esperado, rel=1e-9)
    
    @mark.divisao
    @mark.exception
    @mark.parametrize("dividendo", [1, -1, 5, -10, 0])
    def test_divisao_por_zero_parametrizada(self, calculadora, dividendo):
        """Testa que qualquer número dividido por zero levanta exceção."""
        with raises(ZeroDivisionError):
            calculadora.divisao(dividendo, 0)


# ============================================================================
# TESTES DE INTEGRAÇÃO E CENÁRIOS COMPLEXOS
# ============================================================================

class TestIntegracao:
    """Testes que combinam múltiplas operações."""
    
    @mark.integracao
    def test_operacoes_combinadas(self, calculadora):
        """Testa combinação de operações."""
        # (3 + 2) * 4 / 2 - 1 = 9
        soma = calculadora.soma(3, 2)  # 5
        mult = calculadora.multiplicacao(soma, 4)  # 20
        div = calculadora.divisao(mult, 2)  # 10
        resultado = calculadora.subtracao(div, 1)  # 9
        assert resultado == 9
    
    @mark.integracao
    @mark.parametrize("a,b", [(5, 3), (10, 2), (-4, 6)])
    def test_propriedade_soma_subtracao(self, calculadora, a, b):
        """Testa que (a + b) - b = a."""
        soma = calculadora.soma(a, b)
        resultado = calculadora.subtracao(soma, b)
        assert resultado == approx(a, rel=1e-9)
    
    @mark.integracao
    @mark.parametrize("a,b", [(4, 2), (9, 3), (15, 5)])
    def test_propriedade_multiplicacao_divisao(self, calculadora, a, b):
        """Testa que (a * b) / b = a."""
        mult = calculadora.multiplicacao(a, b)
        resultado = calculadora.divisao(mult, b)
        assert resultado == approx(a, rel=1e-9)


# ============================================================================
# TESTES DE PERFORMANCE E EDGE CASES EXTREMOS
# ============================================================================

class TestPerformanceEEdgeCases:
    """Testes de performance e casos extremos."""
    
    @mark.performance
    @mark.slow
    def test_operacoes_com_numeros_muito_grandes(self, calculadora):
        """Testa operações com números muito grandes."""
        grande = 1e100
        assert calculadora.soma(grande, grande) == 2e100
        assert calculadora.multiplicacao(grande, 2) == 2e100
    
    @mark.edge_case
    @mark.float_precision
    def test_precisao_ponto_flutuante(self, calculadora):
        """Testa casos onde precisão de ponto flutuante é importante."""
        # Caso clássico: 0.1 + 0.2 != 0.3
        resultado = calculadora.soma(0.1, 0.2)
        assert resultado == approx(0.3, rel=1e-9)
        
        # Divisão que resulta em dízima periódica
        resultado = calculadora.divisao(1, 3)
        assert resultado == approx(0.333333333, rel=1e-8)
    
    @mark.edge_case
    def test_operacoes_com_infinity(self, calculadora):
        """Testa operações com infinito."""
        inf = float('inf')
        assert calculadora.soma(inf, 1) == inf
        assert calculadora.multiplicacao(inf, 2) == inf
        assert math.isnan(calculadora.subtracao(inf, inf))


# ============================================================================
# TESTES CONDICIONAIS BASEADOS NO SISTEMA OPERACIONAL
# ============================================================================

class TestSistemaOperacional:
    """Testes específicos para diferentes sistemas operacionais."""
    
    @mark.windows
    @mark.skipif(sys.platform != 'win32', reason='Teste específico para Windows')
    def test_soma_especifica_windows(self, calculadora):
        """Teste que roda apenas no Windows."""
        assert calculadora.soma(2, 2) == 4
    
    @mark.unix
    @mark.skipif(sys.platform == 'win32', reason='Teste para sistemas Unix-like')
    def test_soma_especifica_unix(self, calculadora):
        """Teste que roda apenas em sistemas Unix-like."""
        assert calculadora.soma(3, 3) == 6
    
    @mark.xfail(sys.platform == 'win32', reason='Falha conhecida no Windows')
    def test_divisao_com_falha_conhecida(self, calculadora):
        """Teste que tem falha conhecida em determinado sistema."""
        # Este teste vai falhar propositalmente no Windows
        assert calculadora.divisao(1, 3) == 0.333333333333333333333333333


# ============================================================================
# TESTES DE DOCUMENTAÇÃO E EXEMPLOS
# ============================================================================

class TestDocumentacao:
    """Testes que servem como documentação viva."""
    
    @mark.exemplo
    def test_exemplo_uso_basico(self, calculadora):
        """Exemplo de uso básico da calculadora.
        
        Este teste serve como documentação de como usar a classe.
        """
        # Criando uma instância (já feito pela fixture)
        calc = calculadora
        
        # Operações básicas
        soma_resultado = calc.soma(10, 5)          # 15
        sub_resultado = calc.subtracao(10, 5)      # 5
        mult_resultado = calc.multiplicacao(10, 5)  # 50
        div_resultado = calc.divisao(10, 5)        # 2.0
        
        assert soma_resultado == 15
        assert sub_resultado == 5
        assert mult_resultado == 50
        assert div_resultado == 2.0


# ============================================================================
# TESTES COM FIXTURES PARAMETRIZADAS
# ============================================================================

class TestComFixturesParametrizadas:
    """Testes usando fixtures parametrizadas."""
    
    @mark.fixture_test
    def test_soma_com_numeros_positivos_fixture(self, calculadora, numeros_positivos):
        """Testa soma usando fixture de números positivos."""
        resultado = calculadora.soma(numeros_positivos, numeros_positivos)
        assert resultado == numeros_positivos * 2
        assert resultado > 0
    
    @mark.fixture_test
    def test_multiplicacao_com_numeros_negativos_fixture(self, calculadora, numeros_negativos):
        """Testa multiplicação usando fixture de números negativos."""
        resultado = calculadora.multiplicacao(numeros_negativos, -1)
        assert resultado == abs(numeros_negativos)
        assert resultado > 0


# ============================================================================
# TESTES DE CLEAN CODE E BOAS PRÁTICAS
# ============================================================================

def test_calculadora_eh_uma_classe():
    """Verifica que Calculadora é uma classe."""
    assert isinstance(Calculadora(), Calculadora)


def test_metodos_sao_estaticos():
    """Verifica que os métodos são estáticos (podem ser chamados sem instância)."""
    assert Calculadora.soma(1, 2) == 3
    assert Calculadora.subtracao(5, 3) == 2
    assert Calculadora.multiplicacao(3, 4) == 12
    assert Calculadora.divisao(8, 2) == 4

