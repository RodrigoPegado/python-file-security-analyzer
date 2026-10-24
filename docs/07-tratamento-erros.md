# Tratamento de erros — Python File Security Analyzer

## 1. Objetivo

O tratamento de erros permite que um programa lide com determinadas situações inesperadas sem necessariamente interromper toda a execução.

No Python File Security Analyzer, implementamos esse recurso para que uma falha durante a análise de um arquivo não impeça automaticamente a análise dos demais.

## 2. O que são exceções?

Uma exceção é um evento que interrompe o fluxo normal de execução de um programa quando não é tratado.

Exemplo:

```python
numero = int("Python")
```

Esse código provoca um `ValueError`, porque a palavra `"Python"` não pode ser convertida em um número inteiro.

Podemos utilizar `try` e `except` para tratar esse tipo de situação.

## 3. Entendendo try e except

Exemplo:

```python
try:
    numero = int(input("Digite um número: "))
    print(numero)

except ValueError:
    print("Você precisa digitar um número válido.")
```

O funcionamento é simples:

- `try`: contém o código que tentaremos executar.
- `except`: define o que fazer caso uma exceção correspondente aconteça.

Se o usuário digitar `25`, o programa apresenta o número normalmente.

Se digitar `abc`, o programa apresenta a mensagem definida no `except ValueError`.

## 4. Exceções utilizadas no Analyzer

Durante a análise dos arquivos, utilizamos principalmente duas exceções:

| Exceção | Significado |
|---|---|
| `PermissionError` | Indica um problema relacionado à permissão de acesso. |
| `OSError` | Representa diferentes problemas associados a operações do sistema operacional. |

`PermissionError` é uma subclasse de `OSError`.

Por isso, quando utilizamos os dois tratamentos separadamente, colocamos o tratamento específico de `PermissionError` primeiro.

## 5. Tratamento implementado no main.py

O trecho abaixo representa a estrutura utilizada durante a análise:

```python
try:
    hash_arquivo = calcular_hash(item)

    # Continua a análise do arquivo.
    # Consulta informações e registra os resultados.

except PermissionError:
    print(f"[-] Permissão negada para acessar: {item.name}")
    continue

except OSError as error:
    print(f"[-] Erro ao analisar {item.name}: {error}")
    continue
```

### Explicação

**`hash_arquivo = calcular_hash(item)`**

Tenta abrir o arquivo e calcular seu SHA-256.

**`except PermissionError:`**

Captura especificamente uma falha de permissão.

**`except OSError as error:`**

Captura outros problemas associados às operações de arquivo.

A expressão `as error` permite acessar o objeto da exceção e apresentar detalhes do problema.

**`continue`**

Interrompe a iteração atual do laço e passa para o próximo item.

Dessa forma, um arquivo que não pôde ser analisado não impede necessariamente o processamento dos demais.

## 6. Diferença entre continue e break

Ambos podem ser utilizados dentro de laços de repetição, mas apresentam comportamentos diferentes.

### continue

```python
for numero in range(1, 6):
    if numero == 3:
        continue

    print(numero)
```

Resultado:

```text
1
2
4
5
```

O número 3 foi ignorado, mas o laço continuou.

### break

```python
for numero in range(1, 6):
    if numero == 3:
        break

    print(numero)
```

Resultado:

```text
1
2
```

Nesse caso, o laço foi encerrado quando o número 3 foi encontrado.

No Analyzer, utilizamos `continue` porque queremos tentar analisar os arquivos restantes.

## 7. O que é raise?

O comando `raise` permite provocar uma exceção intencionalmente.

Exemplo:

```python
raise PermissionError("Acesso negado (simulação)")
```

Durante nossos estudos, utilizamos esse recurso para simular uma falha de leitura.

Não foi necessário alterar as permissões reais do Windows.

## 8. Simulando um erro de leitura

Criamos um exercício com três nomes fictícios:

```python
arquivos = [
    "documento.pdf",
    "arquivo_bloqueado.txt",
    "foto.png"
]

for arquivo in arquivos:

    try:
        if arquivo == "arquivo_bloqueado.txt":
            raise PermissionError("Acesso negado (simulação)")

        print(f"[OK] Arquivo analisado: {arquivo}")

    except PermissionError as erro:
        print(f"[-] Erro: {erro}")
        continue
```

Resultado esperado:

```text
[OK] Arquivo analisado: documento.pdf
[-] Erro: Acesso negado (simulação)
[OK] Arquivo analisado: foto.png
```

Esse exercício demonstra que uma falha tratada não precisa interromper toda a análise.

## 9. Testando o tratamento de erros com mock

No arquivo `tests/test_main.py`, criamos um teste automatizado que simula um `PermissionError`.

Utilizamos `unittest.mock.patch()` para substituir temporariamente a função de hashing.

Exemplo simplificado:

```python
def hash_simulado(caminho):
    if caminho.name == "arquivo_bloqueado.txt":
        raise PermissionError("Acesso negado (simulação)")

    return "hash_ficticio"
```

Assim, conseguimos verificar se o programa continua processando outro arquivo mesmo quando ocorre uma falha.

O teste não modifica permissões reais e não executa arquivos suspeitos.

## 10. O que é finally?

O bloco `finally` pode ser utilizado com `try` para executar uma operação de finalização, independentemente de ocorrer ou não uma exceção.

Exemplo:

```python
try:
    print("Executando uma operação")

finally:
    print("Finalizando a operação")
```

Durante nossos testes de relatórios, utilizamos esse conceito para restaurar o diretório de trabalho original após uma alteração temporária.

É importante lembrar que `finally` não captura exceções por conta própria. Sua finalidade é executar operações de finalização.

## 11. Limitações atuais

O tratamento implementado melhora a resistência do programa a determinadas falhas durante a análise individual dos arquivos.

Entretanto, ainda existem situações que podem exigir melhorias futuras:

- Falhas ao percorrer o diretório selecionado.
- Problemas ao criar ou gravar o relatório.
- Arquivos que desaparecem durante a análise.
- Registro separado dos arquivos que não puderam ser analisados.

Não devemos afirmar que o programa consegue tratar todos os erros possíveis.

## 12. Resumo para consulta

| Recurso | Função |
|---|---|
| `try` | Define um bloco de código que será executado. |
| `except` | Trata exceções correspondentes. |
| `PermissionError` | Representa falhas relacionadas à permissão de acesso. |
| `OSError` | Representa diferentes erros de operações do sistema. |
| `as error` | Permite acessar o objeto da exceção. |
| `continue` | Passa para a próxima iteração do laço. |
| `break` | Encerra o laço. |
| `raise` | Provoca uma exceção intencionalmente. |
| `finally` | Executa operações de finalização. |
| `patch()` | Substitui temporariamente objetos durante testes. |

## 13. Conclusão

O tratamento de erros tornou o Python File Security Analyzer mais resistente a falhas individuais durante a leitura de arquivos.

Além disso, sua implementação permitiu praticar conceitos importantes de Python, como exceções, controle de fluxo, simulação de falhas e testes automatizados.