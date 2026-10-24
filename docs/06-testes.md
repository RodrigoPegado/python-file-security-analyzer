# Testes automatizados — Python File Security Analyzer

## 1. O que são testes automatizados?

Testes automatizados são códigos desenvolvidos para verificar se determinadas funcionalidades de um programa apresentam os resultados esperados.

No Python File Security Analyzer, utilizamos a biblioteca nativa `unittest`.

O objetivo é identificar possíveis problemas durante o desenvolvimento e reduzir o risco de que alterações futuras prejudiquem funcionalidades já implementadas.

Um teste aprovado não garante que o programa esteja completamente livre de erros. Ele confirma apenas o comportamento verificado naquele cenário.

## 2. Organização dos testes

A pasta `tests/` contém os seguintes arquivos principais:

| Arquivo | Responsabilidade | Quantidade |
|---|---|---:|
| `test_hashing.py` | Verificar o cálculo SHA-256. | 1 |
| `test_rules.py` | Verificar a regra de dupla extensão. | 5 |
| `test_reporting.py` | Verificar a geração de relatórios. | 1 |
| `test_main.py` | Verificar a continuidade da análise após um erro de permissão. | 1 |
| **Total** | | **8** |

## 3. Estrutura básica de um teste

Exemplo:

```python
import unittest

class TesteExemplo(unittest.TestCase):

    def test_soma(self):
        resultado = 2 + 2

        self.assertEqual(resultado, 4)
```

Explicação:

- `import unittest`: importa o módulo de testes.
- `class TesteExemplo`: cria uma classe para organizar os testes.
- `unittest.TestCase`: disponibiliza métodos de verificação.
- `def test_soma(self)`: define um método que será identificado como teste.
- `self.assertEqual(resultado, 4)`: verifica se o resultado corresponde ao valor esperado.

O prefixo `test_` é importante para a descoberta automática dos métodos de teste.

## 4. Testando o hashing

Arquivo: `tests/test_hashing.py`

Criamos um arquivo vazio dentro de uma pasta temporária e calculamos seu SHA-256 utilizando nossa função `calcular_hash()`.

Depois, comparamos o resultado com o hash esperado.

```python
resultado = calcular_hash(caminho)

esperado = hashlib.sha256(b"").hexdigest()

self.assertEqual(resultado, esperado)
```

Esse teste verifica se nossa função calcula corretamente o hash de um arquivo vazio.

A expressão `b""` representa uma sequência vazia de bytes.

## 5. Testando as regras de análise

Arquivo: `tests/test_rules.py`

Criamos cinco testes para verificar o comportamento de `verificar_extensao()`.

| Entrada | Resultado esperado |
|---|---|
| `comprovante.pdf.exe` | `True` |
| `relatorio.pdf.bat` | `True` |
| `documento.pdf` | `False` |
| `programa.exe` | `False` |
| `FOTO.JPG.EXE` | `True` |

Exemplo:

```python
def test_dupla_extensao_exe(self):
    resultado = verificar_extensao("comprovante.pdf.exe")

    self.assertTrue(resultado)
```

O método `assertTrue()` verifica se o resultado é verdadeiro.

Já `assertFalse()` verifica se o resultado é falso.

**Importante:** um retorno `False` significa apenas que a regra atual não identificou o padrão configurado. Não representa uma confirmação de segurança.

## 6. Testando a geração de relatórios

Arquivo: `tests/test_reporting.py`

O teste fornece resultados fictícios à função `gerar_relatorio()`.

Depois, verifica se o relatório foi criado e se contém determinadas informações esperadas.

Utilizamos uma pasta temporária para evitar misturar arquivos de teste com os relatórios reais do projeto.

Exemplos de verificações:

```python
self.assertTrue(caminho.exists())

conteudo = caminho.read_text(encoding="utf-8")

self.assertIn("comprovante.pdf.exe", conteudo)
```

O método `assertIn()` verifica se determinado valor está presente no conteúdo analisado.

## 7. O que é tempfile?

A biblioteca `tempfile` permite criar arquivos e diretórios temporários.

Exemplo:

```python
import tempfile

with tempfile.TemporaryDirectory() as pasta:
    print(pasta)
```

Ao sair do bloco `with`, o gerenciador de contexto tenta remover o diretório temporário e seu conteúdo.

Isso permite executar testes sem depender de arquivos pessoais do usuário.

## 8. Testando o tratamento de erros

Arquivo: `tests/test_main.py`

Criamos um teste que simula uma falha de permissão durante a análise.

O cenário contém dois arquivos fictícios:

- `arquivo_bloqueado.txt`: provoca um `PermissionError` simulado.
- `documento.txt`: pode ser analisado normalmente.

O objetivo é confirmar que o erro em um arquivo não impede que o outro seja processado.

Para isso, utilizamos `unittest.mock.patch()`.

## 9. O que é patch?

O `patch()` permite substituir temporariamente uma função ou outro objeto durante um teste.

Exemplo:

```python
from unittest.mock import patch

with patch("builtins.input", return_value="samples"):
    caminho = input("Informe o diretório: ")
```

Nesse exemplo, o `input()` retorna automaticamente `"samples"`.

Isso permite testar funções interativas sem precisar digitar informações manualmente.

### return_value e side_effect

| Recurso | Finalidade |
|---|---|
| `return_value` | Define o valor retornado por uma função simulada. |
| `side_effect` | Permite provocar uma exceção ou executar um comportamento personalizado. |

No nosso oitavo teste, utilizamos `side_effect` para simular um erro de permissão.

```python
def hash_simulado(caminho):
    if caminho.name == "arquivo_bloqueado.txt":
        raise PermissionError("Acesso negado (simulação)")

    return "hash_ficticio"
```

O comando `raise` provoca uma exceção intencionalmente.

Dessa forma, podemos testar o tratamento de erros sem modificar as permissões reais dos arquivos no Windows.

## 10. Executando os testes

Para executar todos os testes, abra o terminal na raiz do projeto e utilize:

```powershell
python -m unittest discover -s tests -v
```

Explicação:

| Parte | Significado |
|---|---|
| `python -m unittest` | Executa o módulo de testes. |
| `discover` | Procura testes automaticamente. |
| `-s tests` | Define a pasta onde os testes serão procurados. |
| `-v` | Ativa uma saída mais detalhada. |

Para executar somente os testes das regras:

```powershell
python -m unittest discover -s tests -p "test_rules.py" -v
```

## 11. Interpretando os resultados

| Resultado | Significado |
|---|---|
| `OK` | Os testes executados passaram. |
| `FAIL` | Uma verificação produziu um resultado diferente do esperado. |
| `ERROR` | Ocorreu uma exceção durante a execução do teste. |
| `Ran 0 tests` | Nenhum teste foi encontrado ou executado. |

Durante o desenvolvimento, encontramos um problema porque alguns arquivos haviam sido nomeados com o prefixo `teste_`, enquanto nosso padrão de descoberta procurava `test_`.

Também aprendemos a importância de salvar os arquivos no VS Code antes de executar novamente os testes.

## 12. Limitações da cobertura atual

Os oito testes verificam funcionalidades importantes, mas não cobrem todos os possíveis cenários.

Ainda podemos adicionar testes para:

- Diretórios inexistentes.
- Falhas ao listar diretórios.
- Arquivos modificados durante a análise.
- Falhas durante a gravação dos relatórios.
- Diferentes tamanhos e conteúdos de arquivos.

## 13. Conclusão

Os testes automatizados ajudam a verificar o comportamento do Python File Security Analyzer durante seu desenvolvimento.

Além de identificar possíveis problemas, eles facilitam futuras modificações, pois permitem conferir se funcionalidades anteriormente testadas continuam apresentando os resultados esperados.