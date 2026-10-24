# Regras de análise — Python File Security Analyzer

## 1. Objetivo do módulo

O arquivo `analyzer/rules.py` contém as regras utilizadas para identificar determinados indicadores suspeitos nos nomes dos arquivos.

Atualmente, implementamos uma regra heurística simples que verifica padrões de dupla extensão.

Exemplo:

`comprovante.pdf.exe`

Esse nome apresenta duas extensões: `.pdf` e `.exe`.

A presença desse padrão pode justificar uma análise adicional, mas não comprova que o arquivo seja malicioso.

## 2. Código desenvolvido

```python
from pathlib import Path

def verificar_extensao(caminho):
    arquivo = Path(caminho)
    extensoes = arquivo.suffixes

    extensoes_disfarce = [".pdf", ".txt", ".png", ".jpg", ".docx", ".xlsx"]
    extensoes_executaveis = [".exe", ".bat", ".cmd", ".vbs", ".js", ".sh"]

    if len(extensoes) >= 2:
        if extensoes[-1].lower() in extensoes_executaveis:
            if extensoes[-2].lower() in extensoes_disfarce:
                return True

    return False
```

## 3. Explicação linha por linha

### Importação

`from pathlib import Path`

Importa a classe `Path`, utilizada para trabalhar com caminhos e nomes de arquivos.

### Definição da função

`def verificar_extensao(caminho):`

Cria uma função que recebe um caminho ou nome de arquivo para análise.

### Criando um objeto Path

`arquivo = Path(caminho)`

Transforma o valor recebido em um objeto `Path`.

### Identificando as extensões

`extensoes = arquivo.suffixes`

A propriedade `.suffixes` retorna uma lista contendo as extensões identificadas no nome do arquivo.

Exemplo:

```python
arquivo = Path("comprovante.pdf.exe")

print(arquivo.suffixes)
```

Resultado:

```text
['.pdf', '.exe']
```

### Listas de referência

`extensoes_disfarce` contém extensões que nossa regra considera como possíveis elementos de disfarce.

`extensoes_executaveis` contém extensões que configuramos como indicadores relevantes quando aparecem após uma extensão de disfarce.

Essas listas fazem parte da lógica definida para o projeto. Elas não representam uma classificação universal de arquivos maliciosos.

### Verificando a quantidade de extensões

```python
if len(extensoes) >= 2:
```

O programa verifica se foram identificadas pelo menos duas extensões.

Se houver somente uma, a regra não sinaliza o arquivo.

### Índices negativos

```python
extensoes[-1]
extensoes[-2]
```

Em Python, índices negativos permitem acessar elementos a partir do final de uma lista.

| Índice | Significado |
|---|---|
| `-1` | Último elemento |
| `-2` | Penúltimo elemento |

Para a lista `['.pdf', '.exe']`, temos:

- `extensoes[-1]` → `.exe`
- `extensoes[-2]` → `.pdf`

### Padronizando as letras

```python
.lower()
```

Converte o texto para letras minúsculas.

Isso permite reconhecer nomes como `FOTO.JPG.EXE`, mesmo que nossas listas de referência utilizem extensões minúsculas.

### Operador in

```python
if extensoes[-1].lower() in extensoes_executaveis:
```

Verifica se a última extensão está presente na lista configurada.

Em seguida, verificamos se a penúltima extensão está presente na lista de possíveis disfarces.

### Retorno da função

Se as duas condições forem atendidas, a função retorna `True`.

Caso contrário, retorna `False`.

## 4. Exemplos práticos

| Nome do arquivo | Resultado esperado |
|---|---|
| `comprovante.pdf.exe` | `True` |
| `relatorio.pdf.bat` | `True` |
| `FOTO.JPG.EXE` | `True` |
| `documento.pdf` | `False` |
| `programa.exe` | `False` |
| `imagem.png` | `False` |

O retorno `False` significa somente que o nome não correspondeu ao padrão definido pela regra atual.

Não significa que o arquivo é necessariamente seguro.

## 5. Por que essa regra é considerada heurística?

Uma heurística é um método de análise baseado em critérios ou padrões previamente definidos.

Nossa ferramenta procura uma combinação específica de extensões.

Ela não examina o comportamento do arquivo, não executa seu conteúdo e não realiza uma análise completa de malware.

Além disso, existem arquivos legítimos que podem apresentar nomes com múltiplas extensões.

## 6. Limitações da implementação

A regra atual possui algumas limitações:

- Verifica somente as extensões configuradas nas listas.
- Não analisa o conteúdo interno do arquivo.
- Não identifica todos os possíveis padrões de nomes enganosos.
- Não verifica assinaturas digitais.
- Não determina se o arquivo é malicioso.
- Não substitui ferramentas especializadas de segurança.

## 7. Resumo para consulta

| Recurso | Função |
|---|---|
| `Path()` | Representar o caminho recebido. |
| `.suffixes` | Obter uma lista das extensões identificadas. |
| `len()` | Consultar a quantidade de elementos. |
| `[-1]` | Acessar o último elemento. |
| `[-2]` | Acessar o penúltimo elemento. |
| `.lower()` | Converter texto para letras minúsculas. |
| `in` | Verificar se um elemento pertence a uma coleção. |
| `True` | A regra encontrou o padrão configurado. |
| `False` | A regra não encontrou o padrão configurado. |

**Conclusão:** o módulo `rules.py` aplica uma regra heurística simples para sinalizar determinados padrões de dupla extensão e auxiliar uma análise defensiva posterior.