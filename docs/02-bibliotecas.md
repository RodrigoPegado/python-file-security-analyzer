# Bibliotecas utilizadas — Python File Security Analyzer

## 1. Introdução

Durante o desenvolvimento do Python File Security Analyzer, utilizamos diferentes bibliotecas nativas do Python.

Uma biblioteca disponibiliza funcionalidades que podemos reutilizar sem precisar desenvolver tudo do zero.

Por exemplo, não precisamos implementar manualmente o algoritmo SHA-256: a biblioteca `hashlib` já oferece essa funcionalidade.

As bibliotecas utilizadas neste projeto fazem parte da biblioteca padrão do Python (*Standard Library*), portanto não precisamos instalar pacotes externos para utilizá-las.

---

## 2. pathlib — Manipulação de caminhos

A biblioteca `pathlib` permite trabalhar com arquivos e diretórios de maneira organizada.

**Utilização no projeto:** identificar diretórios, percorrer arquivos, consultar extensões e manipular caminhos.

### Exemplo

```python
from pathlib import Path

arquivo = Path("documento.pdf")

print(arquivo.name)
print(arquivo.suffix)
```

Resultado:

```text
documento.pdf
.pdf
```

### Métodos e propriedades importantes

| Recurso | Função |
|---|---|
| `Path()` | Cria um objeto que representa um caminho. |
| `.is_dir()` | Verifica se o caminho representa um diretório existente. |
| `.is_file()` | Verifica se representa um arquivo regular existente. |
| `.iterdir()` | Percorre os itens presentes diretamente em um diretório. |
| `.name` | Retorna o nome do arquivo. |
| `.suffix` | Retorna a última extensão. |
| `.suffixes` | Retorna uma lista das extensões identificadas. |
| `.stat().st_size` | Consulta o tamanho do arquivo em bytes. |
| `.relative_to()` | Representa um caminho em relação a outro caminho. |
| `.resolve()` | Obtém um caminho absoluto, resolvendo seus componentes. |

**Exemplo aplicado ao Analyzer:**

```python
directory = Path(file_path)

if directory.is_dir():
    for item in directory.iterdir():
        if item.is_file():
            print(item.name)
```

Esse código verifica se o diretório informado existe e percorre seus arquivos.

---

## 3. hashlib — Cálculo de hashes

A biblioteca `hashlib` oferece implementações de algoritmos de hash criptográfico.

No nosso projeto, utilizamos SHA-256.

Um hash é um valor calculado a partir de determinados dados. Alterações no conteúdo normalmente produzem um hash diferente.

### Exemplo

```python
import hashlib

mensagem = b"Python"

resultado = hashlib.sha256(mensagem).hexdigest()

print(resultado)
```

O prefixo `b` indica que estamos trabalhando com bytes.

### Recursos importantes

| Recurso | Função |
|---|---|
| `hashlib.sha256()` | Cria um objeto para calcular SHA-256. |
| `.update()` | Adiciona bytes ao cálculo do hash. |
| `.hexdigest()` | Retorna o resultado como texto hexadecimal. |

**Aplicação no Analyzer:** calcular uma identificação SHA-256 para cada arquivo analisado.

O SHA-256 não determina se um arquivo contém malware. Ele é útil para identificação e verificação de integridade, especialmente quando temos um valor de referência confiável para comparação.

---

## 4. datetime — Datas e horários

A biblioteca `datetime` permite trabalhar com datas e horários.

**Utilização no projeto:** registrar quando um relatório foi gerado e criar nomes de arquivos com marcação temporal.

### Exemplo

```python
from datetime import datetime

agora = datetime.now()

print(agora.strftime("%Y-%m-%d_%H-%M-%S"))
```

### Recursos importantes

| Recurso | Função |
|---|---|
| `datetime.now()` | Obtém a data e a hora locais atuais. |
| `.strftime()` | Formata uma data ou horário como texto. |

Alguns códigos de formatação:

- `%Y`: ano com quatro dígitos.
- `%m`: mês.
- `%d`: dia.
- `%H`: hora.
- `%M`: minuto.
- `%S`: segundo.

---

## 5. unittest — Testes automatizados

A biblioteca `unittest` permite criar testes para verificar se determinadas partes do programa funcionam conforme o esperado.

**Utilização no projeto:** testar o cálculo de hashes, as regras de análise, a geração de relatórios e o tratamento de erros.

### Exemplo

```python
import unittest

class TesteExemplo(unittest.TestCase):

    def test_soma(self):
        resultado = 2 + 2

        self.assertEqual(resultado, 4)
```

### Métodos importantes

| Método | O que verifica |
|---|---|
| `assertEqual(a, b)` | Se dois valores são iguais. |
| `assertTrue(valor)` | Se o valor é verdadeiro. |
| `assertFalse(valor)` | Se o valor é falso. |
| `assertIn(a, b)` | Se determinado elemento está presente em outro objeto. |

Os métodos de teste começam com `test_` para permitir sua identificação automática pelo `unittest`.

---

## 6. tempfile — Arquivos e pastas temporárias

A biblioteca `tempfile` permite criar arquivos e diretórios temporários.

**Utilização no projeto:** criar ambientes isolados para executar testes sem depender de arquivos pessoais do computador.

### Exemplo

```python
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as pasta:
    arquivo = Path(pasta) / "teste.txt"

    arquivo.write_text("Exemplo", encoding="utf-8")

    print(arquivo.exists())
```

Ao encerrar o bloco `with`, o gerenciador de contexto tenta remover o diretório temporário e seu conteúdo.

Isso ajuda a evitar que os testes deixem arquivos desnecessários no computador.

---

## 7. unittest.mock — Simulação de comportamentos

O módulo `unittest.mock` permite substituir temporariamente funções e outros objetos durante os testes.

Utilizamos principalmente `patch`.

### Exemplo

```python
from unittest.mock import patch

with patch("builtins.input", return_value="samples"):
    caminho = input("Informe o diretório: ")

print(caminho)
```

Nesse exemplo, o `input()` retorna automaticamente `"samples"`.

Não precisamos digitar nada no terminal.

### Recursos importantes

| Recurso | Função |
|---|---|
| `patch()` | Substitui temporariamente um objeto durante o teste. |
| `return_value` | Define um valor que a função simulada deve retornar. |
| `side_effect` | Permite definir um comportamento personalizado ou provocar uma exceção. |

No Analyzer, utilizamos mocks para simular erros de permissão sem precisar modificar as permissões reais do Windows.

---

## 8. os — Interação com o sistema operacional

A biblioteca `os` permite realizar diferentes operações relacionadas ao sistema operacional.

Durante os testes de relatórios, utilizamos recursos para trabalhar com o diretório de execução.

### Exemplo

```python
import os

diretorio_atual = os.getcwd()

print(diretorio_atual)
```

### Recursos importantes

| Recurso | Função |
|---|---|
| `os.getcwd()` | Retorna o diretório de trabalho atual. |
| `os.chdir(caminho)` | Altera o diretório de trabalho do processo. |

**Atenção:** alterar o diretório de trabalho afeta a resolução de caminhos relativos durante a execução. Por isso, nos testes, precisamos restaurar o diretório original.

---

## 9. Resumo para consulta rápida

| Biblioteca | Responsabilidade no projeto |
|---|---|
| `pathlib` | Manipular caminhos, arquivos e diretórios. |
| `hashlib` | Calcular hashes SHA-256. |
| `datetime` | Registrar datas e horários nos relatórios. |
| `unittest` | Executar testes automatizados. |
| `tempfile` | Criar ambientes temporários de teste. |
| `unittest.mock` | Simular funções e situações de erro. |
| `os` | Interagir com o diretório de trabalho do processo. |

## 10. Observações finais

Todas essas bibliotecas fazem parte da biblioteca padrão do Python.

O objetivo de utilizá-las separadamente é manter o projeto organizado e facilitar sua manutenção, seus testes e sua evolução.
