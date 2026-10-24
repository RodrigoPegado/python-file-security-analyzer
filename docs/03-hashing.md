# Hashing e SHA-256 — Python File Security Analyzer

## 1. O que é hashing?

Hashing é o processo de transformar dados de entrada em um valor de tamanho fixo por meio de uma função matemática.

No Python File Security Analyzer, utilizamos o algoritmo criptográfico SHA-256 para calcular o hash dos arquivos analisados.

O SHA-256 produz um resultado de 256 bits, normalmente representado por 64 caracteres hexadecimais.

## 2. Para que serve o SHA-256?

O SHA-256 pode ser utilizado para:

- Identificar o conteúdo de arquivos.
- Verificar a integridade de dados.
- Comparar arquivos com valores de referência conhecidos.
- Identificar alterações em arquivos entre diferentes análises.

**Importante:** calcular um hash não significa descobrir se um arquivo contém malware.

Para verificar a integridade, por exemplo, precisamos comparar o hash calculado com um valor de referência confiável.

## 3. Como implementamos o hashing?

Arquivo: `analyzer/hashing.py`

```python
import hashlib

def calcular_hash(caminho):
    with open(caminho, 'rb') as f:
        file_hash = hashlib.sha256()

        while chunk := f.read(8192):
            file_hash.update(chunk)

    return file_hash.hexdigest()
```

### Explicação linha por linha

**`import hashlib`**

Importa o módulo da biblioteca padrão do Python que disponibiliza algoritmos de hash criptográfico.

**`def calcular_hash(caminho):`**

Define uma função que recebe o caminho do arquivo que será analisado.

**`with open(caminho, 'rb') as f:`**

Abre o arquivo em modo de leitura binária.

- `r`: leitura (*read*).
- `b`: modo binário (*binary*).

Utilizamos leitura binária porque precisamos calcular o hash a partir dos bytes reais do arquivo, independentemente de ele ser um documento, imagem ou outro formato.

O `with` também ajuda a garantir o fechamento do arquivo ao sair do bloco, inclusive quando ocorre uma exceção.

**`file_hash = hashlib.sha256()`**

Cria um objeto responsável por calcular o hash SHA-256.

**`while chunk := f.read(8192):`**

Lê o arquivo em blocos de até 8192 bytes.

O operador `:=`, chamado de *walrus operator*, atribui o conteúdo lido à variável `chunk` e permite utilizá-lo na condição do `while`.

Enquanto houver bytes disponíveis, o laço continua. Quando a leitura retorna `b''`, o laço termina.

**`file_hash.update(chunk)`**

Adiciona o bloco de bytes ao cálculo do hash.

Cada bloco contribui para o resultado final.

**`return file_hash.hexdigest()`**

Retorna o hash calculado como uma sequência de caracteres hexadecimais.

## 4. Por que ler o arquivo em blocos?

Imagine um arquivo de 2 GB.

Se utilizássemos:

```python
conteudo = f.read()
```

O Python tentaria carregar todo o conteúdo restante do arquivo na memória de uma só vez.

Em nosso projeto, utilizamos:

```python
f.read(8192)
```

Dessa forma, processamos o arquivo em pequenos blocos, reduzindo a necessidade de memória durante a leitura.

O resultado SHA-256 final é o mesmo que obteríamos processando todos os bytes de uma vez, desde que o conteúdo e a ordem dos bytes sejam idênticos.

## 5. Experimento prático — Alterando o conteúdo

Durante o desenvolvimento, realizamos um experimento com três situações:

| Experimento | Conteúdo |
|---|---|
| 1 | Arquivo vazio |
| 2 | Arquivo contendo uma frase |
| 3 | Mesma frase, acrescentando um ponto final |

O hash SHA-256 de um arquivo completamente vazio é:

```text
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

Ao adicionar uma frase ao arquivo, seu hash muda.

Ao acrescentar apenas um ponto final à mesma frase, o hash também muda significativamente.

Esse comportamento ilustra o chamado **efeito avalanche**: uma pequena alteração na entrada pode produzir uma grande diferença no resultado de uma função de hash criptográfico.

### O que aprendemos?

O hash depende dos bytes do conteúdo, não apenas do nome ou da extensão do arquivo.

Portanto, dois arquivos com nomes diferentes e conteúdo binário idêntico produzem o mesmo SHA-256.

Da mesma forma, renomear um arquivo sem modificar seu conteúdo não altera o hash.

## 6. Hashing não é criptografia reversível

Hashing e criptografia não são a mesma coisa.

A criptografia reversível permite recuperar os dados originais utilizando os mecanismos e as chaves apropriadas.

Já uma função de hash criptográfico, como SHA-256, não foi projetada para permitir a reconstrução dos dados originais a partir do resultado.

## 7. Aplicação no Analyzer

Nosso programa calcula o SHA-256 de cada arquivo que consegue ler.

Depois, armazena o resultado em um dicionário:

```python
resultado_arquivo = {
    "nome": item.name,
    "sha256": hash_arquivo
}
```

Esse exemplo apresenta somente dois campos para facilitar a explicação. No programa real, o dicionário também contém extensão, tamanho, caminho relativo e indicador suspeito.

Posteriormente, o hash é incluído no relatório textual.

## 8. Limitações

O SHA-256 não substitui uma análise de segurança.

Um arquivo malicioso pode possuir um hash perfeitamente válido, assim como um arquivo legítimo.

Além disso, o Analyzer atualmente calcula os hashes, mas não realiza automaticamente consultas a bases externas de reputação nem compara os resultados com uma lista de hashes conhecidos.

## 9. Resumo para consulta

| Conceito | Significado |
|---|---|
| `hashlib` | Módulo Python utilizado para calcular hashes. |
| SHA-256 | Algoritmo que produz um resumo de 256 bits. |
| `rb` | Leitura binária de arquivos. |
| `read(8192)` | Leitura de até 8192 bytes por vez. |
| `update()` | Adiciona bytes ao cálculo. |
| `hexdigest()` | Retorna o hash em formato hexadecimal. |
| Efeito avalanche | Pequenas alterações na entrada podem causar grandes mudanças no hash. |

**Conclusão:** O SHA-256 é utilizado para identificar o conteúdo dos arquivos e registrar informações úteis para verificações posteriores de integridade, não para determinar isoladamente se um arquivo é seguro.