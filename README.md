# 🧪 Pytest Project

## 📋 Descrição
Projeto educacional demonstrando o uso do framework pytest para testes unitários em Python, com implementação de calculadora básica e algoritmo de "pense em um número" com cobertura completa de testes.

## 🚀 Tecnologias Utilizadas
- **Python 3.x** - Linguagem principal
- **Pytest** - Framework de testes
- **Colorama** - Colorização de output
- **Pygments** - Syntax highlighting

## 📁 Estrutura do Projeto
```
├── libs/
│   ├── __init__.py
│   ├── calculadora.py          # Classe Calculadora com operações básicas
│   └── jogo.py                 # Funções do jogo "pense em um número"
├── tests/
│   ├── __init__.py
│   ├── test_calculadora.py     # Testes da calculadora (funções)
│   ├── test_calculadora_class.py # Testes da calculadora (classe)
│   ├── test_jogo.py            # Testes do jogo (funções)
│   └── test_jogo_class.py      # Testes do jogo (classe)
├── main.py                     # Arquivo principal de execução
├── pytest.ini                 # Configurações do pytest
├── requirements.txt            # Dependências do projeto
└── .gitignore                  # Arquivos ignorados pelo Git
```

## ⚡ Funcionalidades
### Calculadora
- **Soma** - Adição de dois números
- **Subtração** - Subtração entre dois números  
- **Multiplicação** - Produto de dois números
- **Divisão** - Divisão entre dois números

### Jogo "Pense em um Número"
- **pense_num_numero()** - Algoritmo matemático que sempre resulta em 3
- **pense_num_numero2()** - Versão compacta do mesmo algoritmo
- **Validação** - Verificação de números positivos
- **Tratamento de exceções** - Para valores inválidos

### Framework de Testes
- **Testes unitários** completos para todas as funções
- **Marcadores personalizados** (@mark.soma, @mark.skip)
- **Testes parametrizados** para múltiplos cenários
- **Testes de exceções** com pytest.raises
- **Configurações avançadas** via pytest.ini

## 🔧 Instalação e Execução
### Pré-requisitos
```bash
# Instalar Python 3.x
python --version

# Clonar o repositório
git clone <repository-url>
cd pytest-project
```

### Instalação de Dependências
```bash
# Instalar dependências
pip install -r requirements.txt
```

### Execução dos Testes
```bash
# Executar todos os testes
pytest

# Executar testes com verbose
pytest -v

# Executar testes específicos por marcador
pytest -m soma

# Executar testes de um arquivo específico
pytest tests/test_calculadora.py

# Executar com relatório de cobertura
pytest --cov=libs
```

### Execução da Aplicação
```bash
# Executar o programa principal
python main.py
```

## 🛠️ Configuração do Pytest
### Marcadores Personalizados
- `@mark.soma` - Testes de operações de soma
- `@mark.skip` - Testes temporariamente desabilitados

### Configurações (pytest.ini)
- **Filtros de warnings** configurados
- **Marcadores customizados** definidos
- **Configurações de execução** otimizadas

## 📊 Estrutura dos Testes
### Padrão Given-When-Then
```python
def test_quando_soma_recebe_4_e_3_entao_retorna_7():
    entrada1 = 4  # Given
    entrada2 = 3  # Given
    resultado = c.soma(entrada1,entrada2) # When
    esperado = 7  # Then
    assert resultado == esperado # Then
```

### Tipos de Testes Implementados
- **Testes de valor de retorno** - Verificação de resultados
- **Testes de exceções** - Validação de erros esperados
- **Testes parametrizados** - Múltiplos casos de teste
- **Testes de edge cases** - Cenários limites

## 📦 Dependências Principais
- **pytest==8.4.1** - Framework de testes
- **colorama==0.4.6** - Colorização de terminal
- **pygments==2.19.2** - Syntax highlighting
- **packaging==25.0** - Utilitários de empacotamento

## 🎯 Objetivos Educacionais
- **Aprender pytest** - Framework mais popular para testes em Python
- **Boas práticas de teste** - Estruturação e organização
- **TDD (Test-Driven Development)** - Desenvolvimento orientado a testes
- **Cobertura de código** - Garantir qualidade do software
- **Configuração de ambiente** - Setup profissional de testes

## 🏆 Casos de Uso
- **Projeto educacional** para aprendizado de testes
- **Template base** para novos projetos Python
- **Demonstração de conceitos** de qualidade de software
- **Referência** para configuração de pytest
