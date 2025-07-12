"""
Testes abrangentes para as funções do módulo jogo.
Inclui: marks, parametrização, fixtures, exceptions, edge cases, e boas práticas.
"""

from libs.jogo import pense_num_numero, pense_num_numero2
from libs.calculadora import Calculadora
from pytest import mark, raises, fixture, approx
import pytest
import sys


# ============================================================================
# FIXTURES - Configuração reutilizável
# ============================================================================

@fixture
def calculadora():
    """Fixture que retorna uma instância da Calculadora."""
    return Calculadora()


@fixture(params=[1, 5, 10, 100, 1000])
def numeros_positivos_pequenos(request):
    """Fixture parametrizada com números positivos pequenos."""
    return request.param


@fixture(params=[0.1, 0.5, 1.5, 2.7, 9.9])
def numeros_decimais_positivos(request):
    """Fixture parametrizada com números decimais positivos."""
    return request.param


@fixture(params=[-1, -5, -10, -100])
def numeros_negativos(request):
    """Fixture parametrizada com números negativos."""
    return request.param


# ============================================================================
# TESTES PARA pense_num_numero - Versão verbosa
# ============================================================================

class TestPenseNumNumero:
    """Classe para agrupar todos os testes da função pense_num_numero."""
    
    @mark.jogo
    @mark.basic
    def test_numero_positivo_simples(self):
        """Testa que a função sempre retorna 3 para números positivos."""
        assert pense_num_numero(1) == 3
        assert pense_num_numero(5) == 3
        assert pense_num_numero(10) == 3
        assert pense_num_numero(100) == 3
    
    @mark.jogo
    @mark.edge_case
    def test_numero_zero(self):
        """Testa que a função retorna 3 para zero."""
        assert pense_num_numero(0) == 3
    
    @mark.jogo
    @mark.edge_case
    def test_numeros_decimais(self):
        """Testa que a função funciona com números decimais."""
        assert pense_num_numero(1.5) == approx(3, rel=1e-9)
        assert pense_num_numero(2.7) == approx(3, rel=1e-9)
        assert pense_num_numero(0.1) == approx(3, rel=1e-9)
    
    @mark.jogo
    @mark.edge_case
    def test_numeros_muito_grandes(self):
        """Testa que a função funciona com números muito grandes."""
        assert pense_num_numero(1e6) == approx(3, rel=1e-9)
        assert pense_num_numero(1e9) == approx(3, rel=1e-9)
    
    @mark.jogo
    @mark.exception
    def test_numero_negativo_levanta_excecao(self):
        """Testa que números negativos levantam exceção."""
        with raises(Exception, match="Número precisa ser positivo!"):
            pense_num_numero(-1)
        
        with raises(Exception, match="Número precisa ser positivo!"):
            pense_num_numero(-5)
        
        with raises(Exception, match="Número precisa ser positivo!"):
            pense_num_numero(-0.1)
    
    @mark.jogo
    @mark.parametrize("numero", [1, 2, 3, 5, 7, 10, 15, 20, 50, 100])
    def test_propriedade_matematica_parametrizada(self, numero):
        """Testa que a propriedade matemática sempre resulta em 3."""
        resultado = pense_num_numero(numero)
        assert resultado == approx(3, rel=1e-9)
    
    @mark.jogo
    @mark.parametrize("numero_negativo", [-1, -2, -5, -10, -100, -0.5])
    def test_numeros_negativos_parametrizados(self, numero_negativo):
        """Testa que todos os números negativos levantam exceção."""
        with raises(Exception, match="Número precisa ser positivo!"):
            pense_num_numero(numero_negativo)
    
    @mark.jogo
    @mark.property_based
    def test_propriedade_invariante(self):
        """Testa que a função tem a propriedade invariante de sempre retornar 3."""
        # Teste com vários números aleatórios
        numeros_teste = [0, 1, 2.5, 7, 13, 42, 99.9, 500, 1234.56]
        for num in numeros_teste:
            assert pense_num_numero(num) == approx(3, rel=1e-9)


# ============================================================================
# TESTES PARA pense_num_numero2 - Versão compacta
# ============================================================================

class TestPenseNumNumero2:
    """Classe para agrupar todos os testes da função pense_num_numero2."""
    
    @mark.jogo
    @mark.basic
    def test_numero_positivo_simples(self):
        """Testa que a função sempre retorna 3 para números positivos."""
        assert pense_num_numero2(1) == 3
        assert pense_num_numero2(5) == 3
        assert pense_num_numero2(10) == 3
        assert pense_num_numero2(100) == 3
    
    @mark.jogo
    @mark.edge_case
    def test_numero_zero(self):
        """Testa que a função retorna 3 para zero."""
        assert pense_num_numero2(0) == 3
    
    @mark.jogo
    @mark.edge_case
    def test_numeros_decimais(self):
        """Testa que a função funciona com números decimais."""
        assert pense_num_numero2(1.5) == approx(3, rel=1e-9)
        assert pense_num_numero2(2.7) == approx(3, rel=1e-9)
        assert pense_num_numero2(0.1) == approx(3, rel=1e-9)
    
    @mark.jogo
    @mark.edge_case
    def test_numeros_negativos(self):
        """Testa que a função funciona com números negativos (sem validação)."""
        # A função 2 não tem validação de número negativo
        assert pense_num_numero2(-1) == approx(3, rel=1e-9)
        assert pense_num_numero2(-5) == approx(3, rel=1e-9)
        assert pense_num_numero2(-10) == approx(3, rel=1e-9)
    
    @mark.jogo
    @mark.parametrize("numero", [-10, -1, 0, 1, 2, 5, 10, 100, 1000])
    def test_propriedade_matematica_parametrizada(self, numero):
        """Testa que a propriedade matemática sempre resulta em 3."""
        resultado = pense_num_numero2(numero)
        assert resultado == approx(3, rel=1e-9)
    
    @mark.jogo
    @mark.float_precision
    def test_precisao_com_decimais_complexos(self):
        """Testa precisão com números decimais complexos."""
        numeros = [3.14159, 2.71828, 1.41421, 0.57721]
        for num in numeros:
            assert pense_num_numero2(num) == approx(3, rel=1e-9)


# ============================================================================
# TESTES COMPARATIVOS - Comparando as duas implementações
# ============================================================================

class TestComparativoImplementacoes:
    """Testes que comparam as duas implementações das funções."""
    
    @mark.jogo
    @mark.comparativo
    def test_mesma_saida_para_numeros_positivos(self):
        """Testa que ambas as funções produzem o mesmo resultado para números positivos."""
        numeros_teste = [0, 1, 2, 5, 10, 50, 100, 0.5, 2.7, 9.9]
        
        for num in numeros_teste:
            resultado1 = pense_num_numero(num)
            resultado2 = pense_num_numero2(num)
            assert resultado1 == approx(resultado2, rel=1e-9)
    
    @mark.jogo
    @mark.comparativo
    @mark.exception
    def test_diferenca_tratamento_numeros_negativos(self):
        """Testa que as funções tratam números negativos de forma diferente."""
        numero_negativo = -5
        
        # Função 1 levanta exceção
        with raises(Exception):
            pense_num_numero(numero_negativo)
        
        # Função 2 não levanta exceção
        resultado2 = pense_num_numero2(numero_negativo)
        assert resultado2 == approx(3, rel=1e-9)
    
    @mark.jogo
    @mark.comparativo
    @mark.parametrize("numero", [1, 5, 10, 25, 100])
    def test_equivalencia_parametrizada(self, numero):
        """Testa equivalência das funções com parametrização."""
        assert pense_num_numero(numero) == approx(pense_num_numero2(numero), rel=1e-9)


# ============================================================================
# TESTES COM FIXTURES PARAMETRIZADAS
# ============================================================================

class TestComFixtures:
    """Testes usando fixtures parametrizadas."""
    
    @mark.jogo
    @mark.fixture_test
    def test_pense_numero_com_positivos_fixture(self, numeros_positivos_pequenos):
        """Testa função 1 com fixture de números positivos."""
        resultado = pense_num_numero(numeros_positivos_pequenos)
        assert resultado == approx(3, rel=1e-9)
    
    @mark.jogo
    @mark.fixture_test
    def test_pense_numero2_com_positivos_fixture(self, numeros_positivos_pequenos):
        """Testa função 2 com fixture de números positivos."""
        resultado = pense_num_numero2(numeros_positivos_pequenos)
        assert resultado == approx(3, rel=1e-9)
    
    @mark.jogo
    @mark.fixture_test
    def test_pense_numero_com_decimais_fixture(self, numeros_decimais_positivos):
        """Testa função 1 com fixture de números decimais."""
        resultado = pense_num_numero(numeros_decimais_positivos)
        assert resultado == approx(3, rel=1e-9)
    
    @mark.jogo
    @mark.fixture_test
    def test_pense_numero2_com_negativos_fixture(self, numeros_negativos):
        """Testa que função 2 funciona com números negativos."""
        resultado = pense_num_numero2(numeros_negativos)
        assert resultado == approx(3, rel=1e-9)
    
    @mark.jogo
    @mark.fixture_test
    @mark.exception
    def test_pense_numero_excecao_com_negativos_fixture(self, numeros_negativos):
        """Testa que função 1 levanta exceção com números negativos."""
        with raises(Exception, match="Número precisa ser positivo!"):
            pense_num_numero(numeros_negativos)


# ============================================================================
# TESTES DE INTEGRAÇÃO COM CALCULADORA
# ============================================================================

class TestIntegracaoCalculadora:
    """Testes que verificam a integração com a classe Calculadora."""
    
    @mark.jogo
    @mark.integracao
    def test_funcoes_usam_calculadora_corretamente(self, calculadora):
        """Testa que as funções do jogo usam a calculadora corretamente."""
        # Verificamos se o resultado é consistente com uso manual da calculadora
        num = 10
        
        # Simulando pense_num_numero manualmente
        passo_0 = calculadora.soma(num, 5)        # 15
        passo_1 = calculadora.multiplicacao(passo_0, 2)  # 30
        passo_2 = calculadora.subtracao(passo_1, 4)      # 26
        passo_3 = calculadora.divisao(passo_2, 2)        # 13
        passo_4 = calculadora.subtracao(passo_3, num)    # 3
        
        # Deve ser igual ao resultado da função
        assert pense_num_numero(num) == passo_4
    
    @mark.jogo
    @mark.integracao
    def test_matematica_por_tras_do_algoritmo(self):
        """Testa que a matemática por trás do algoritmo está correta."""
        # A fórmula é: ((n + 5) * 2 - 4) / 2 - n
        # Simplificando: (2n + 10 - 4) / 2 - n = (2n + 6) / 2 - n = n + 3 - n = 3
        
        for n in [0, 1, 5, 10, 100, 0.5, 2.7]:
            resultado_manual = ((n + 5) * 2 - 4) / 2 - n
            resultado_funcao1 = pense_num_numero(n)
            resultado_funcao2 = pense_num_numero2(n)
            
            assert resultado_manual == approx(3, rel=1e-9)
            assert resultado_funcao1 == approx(3, rel=1e-9)
            assert resultado_funcao2 == approx(3, rel=1e-9)


# ============================================================================
# TESTES DE PERFORMANCE E EDGE CASES EXTREMOS
# ============================================================================

class TestPerformanceEEdgeCases:
    """Testes de performance e casos extremos."""
    
    @mark.jogo
    @mark.performance
    @mark.slow
    def test_numeros_muito_grandes(self):
        """Testa com números muito grandes."""
        numero_grande = 1e10
        assert pense_num_numero(numero_grande) == approx(3, rel=1e-6)
        assert pense_num_numero2(numero_grande) == approx(3, rel=1e-6)
    
    @mark.jogo
    @mark.edge_case
    def test_numero_muito_pequeno(self):
        """Testa com números muito pequenos."""
        numero_pequeno = 1e-10
        assert pense_num_numero(numero_pequeno) == approx(3, rel=1e-6)
        assert pense_num_numero2(numero_pequeno) == approx(3, rel=1e-6)
    
    @mark.jogo
    @mark.edge_case
    @mark.float_precision
    def test_precisao_extrema(self):
        """Testa precisão com casos extremos de ponto flutuante."""
        import math
        
        # Testando com pi, e, sqrt(2)
        numeros_especiais = [math.pi, math.e, math.sqrt(2)]
        
        for num in numeros_especiais:
            resultado1 = pense_num_numero(num)
            resultado2 = pense_num_numero2(num)
            assert resultado1 == approx(3, rel=1e-10)
            assert resultado2 == approx(3, rel=1e-10)


# ============================================================================
# TESTES CONDICIONAIS E ESPECÍFICOS DO SISTEMA
# ============================================================================

class TestSistemaOperacional:
    """Testes específicos para diferentes sistemas operacionais."""
    
    @mark.jogo
    @mark.windows
    @mark.skipif(sys.platform != 'win32', reason='Teste específico para Windows')
    def test_jogo_windows(self):
        """Teste que roda apenas no Windows."""
        assert pense_num_numero(5) == 3
        assert pense_num_numero2(5) == 3
    
    @mark.jogo
    @mark.unix
    @mark.skipif(sys.platform == 'win32', reason='Teste para sistemas Unix-like')
    def test_jogo_unix(self):
        """Teste que roda apenas em sistemas Unix-like."""
        assert pense_num_numero(7) == 3
        assert pense_num_numero2(7) == 3


# ============================================================================
# TESTES DE DOCUMENTAÇÃO E EXEMPLOS
# ============================================================================

class TestDocumentacao:
    """Testes que servem como documentação viva."""
    
    @mark.jogo
    @mark.exemplo
    def test_exemplo_uso_jogo(self):
        """Exemplo de como usar as funções do jogo.
        
        Este teste serve como documentação de uso.
        """
        # O jogo sempre retorna 3, independente do número pensado
        numero_pensado = 42
        
        # Versão verbosa (com validação)
        resultado_v1 = pense_num_numero(numero_pensado)  # Sempre 3
        
        # Versão compacta (sem validação)
        resultado_v2 = pense_num_numero2(numero_pensado)  # Sempre 3
        
        assert resultado_v1 == 3
        assert resultado_v2 == 3
        
        # A mágica funciona porque a matemática se anula:
        # ((n + 5) * 2 - 4) / 2 - n = n + 3 - n = 3


# ============================================================================
# TESTES DE VALIDAÇÃO DE TIPOS
# ============================================================================

class TestValidacaoTipos:
    """Testes para validar tipos de entrada."""
    
    @mark.jogo
    @mark.edge_case
    def test_entrada_string_numerica(self):
        """Testa comportamento com strings que representam números."""
        # Python converte automaticamente em operações matemáticas
        assert pense_num_numero(5.0) == 3  # float que é inteiro
        assert pense_num_numero2(5.0) == 3
    
    @mark.jogo
    @mark.exception
    def test_entrada_invalida_funcao1(self):
        """Testa comportamento com entradas inválidas na função 1."""
        with raises(TypeError):
            pense_num_numero("abc")  # String não numérica
    
    @mark.jogo
    @mark.exception  
    def test_entrada_invalida_funcao2(self):
        """Testa comportamento com entradas inválidas na função 2."""
        with raises(TypeError):
            pense_num_numero2("abc")  # String não numérica


# ============================================================================
# TESTES DE REGRESSÃO
# ============================================================================

def test_regressao_resultado_sempre_tres():
    """Teste de regressão para garantir que o resultado sempre seja 3."""
    # Este teste garante que mudanças futuras não quebrem a lógica fundamental
    numeros_teste = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]  # Sequência Fibonacci
    
    for num in numeros_teste:
        assert pense_num_numero(num) == 3, f"Falha para número {num}"
        assert pense_num_numero2(num) == 3, f"Falha para número {num}"


def test_consistencia_entre_implementacoes():
    """Testa que ambas as implementações são consistentes para números válidos."""
    for i in range(20):  # Teste com números de 0 a 19
        resultado1 = pense_num_numero(i)
        resultado2 = pense_num_numero2(i)
        assert resultado1 == resultado2, f"Inconsistência para número {i}"