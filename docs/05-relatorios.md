# Geração de relatórios — Python File Security Analyzer

## 1. Objetivo do módulo

O arquivo `analyzer/reporting.py` é responsável por transformar os resultados da análise em um relatório textual.

Em vez de mostrar as informações somente no terminal, o programa permite consultá-las posteriormente em um arquivo `.txt`.

Os relatórios são armazenados na pasta `reports/`.

## 2. Como os resultados são organizados?

Durante a análise, o `main.py` utiliza uma lista chamada `resultados`.

Cada arquivo analisado com sucesso é representado por um dicionário.

Exemplo simplificado:

```python
resultado_arquivo = {
    "nome": "comprovante.pdf.exe",
    "extensao": ".exe",
    "tamanho": 25,
    "caminho": "comprovante.pdf.exe",
    "sha256": "hash_ficticio",
    "suspeito": True
}
```

Um dicionário armazena informações por meio de pares de chave e valor.

Por exemplo:

```python
print(resultado_arquivo["nome"])
```

Resultado:

```text
comprovante.pdf.exe
```

Para armazenar vários arquivos, utilizamos uma lista:

```python
resultados = []

resultados.append(resultado_arquivo)
```

O método `.append()` adiciona um elemento ao final da lista.

## 3. Como o módulo recebe os resultados?

A função `gerar_relatorio()` recebe a lista criada durante a análise:

```python
caminho_relatorio = gerar_relatorio(resultados)
```

Isso permite separar duas responsabilidades:

- `main.py`: controla a análise e reúne os resultados.
- `reporting.py`: recebe os resultados e escreve o relatório.

Essa separação facilita a manutenção e os testes automatizados.

## 4. Criando a pasta de relatórios

A biblioteca `pathlib` permite representar e criar diretórios.

Exemplo:

```python
from pathlib import Path

pasta_relatorios = Path("reports")

pasta_relatorios.mkdir(exist_ok=True)
```

O método `.mkdir()` cria um diretório.

O argumento `exist_ok=True` evita que seja gerado um erro somente porque o diretório já existe.

## 5. Utilizando datetime

Para diferenciar os relatórios, utilizamos informações de data e horário.

Exemplo:

```python
from datetime import datetime

agora = datetime.now()

nome = agora.strftime("relatorio_%Y%m%d_%H%M%S.txt")
```

Um possível resultado seria:

```text
relatorio_20261023_221500.txt
```

A marcação temporal facilita a identificação de quando cada relatório foi produzido.

**Observação:** nomes baseados apenas em segundos podem coincidir caso dois relatórios sejam gerados no mesmo segundo. Uma melhoria futura seria utilizar microssegundos ou outro identificador único.

## 6. Escrevendo um arquivo de texto

O Python permite criar e escrever arquivos utilizando `open()`.

Exemplo:

```python
with open("exemplo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Relatório de exemplo")
```

Explicação:

| Elemento | Significado |
|---|---|
| `open()` | Abre um arquivo. |
| `"w"` | Modo de escrita. Cria o arquivo ou substitui seu conteúdo anterior. |
| `encoding="utf-8"` | Define a codificação do texto. |
| `with` | Gerencia a abertura e o fechamento do arquivo. |
| `.write()` | Escreve texto no arquivo. |

Utilizamos UTF-8 para lidar adequadamente com caracteres como acentos.

## 7. Percorrendo os resultados

Como `resultados` é uma lista, podemos utilizar `for` para acessar cada dicionário:

```python
for resultado in resultados:
    print(resultado["nome"])
    print(resultado["sha256"])
```

A cada repetição, a variável `resultado` representa um dos arquivos analisados.

Esse mesmo conceito permite escrever os dados individualmente no relatório.

## 8. Caminhos relativos e privacidade

Durante o desenvolvimento, percebemos que o relatório inicialmente poderia registrar caminhos absolutos do Windows.

Exemplo fictício de caminho absoluto:

```text
C:\Users\Usuario\Documents\Projeto\samples\arquivo.txt
```

Esse formato pode expor informações desnecessárias sobre a estrutura de diretórios do computador.

Por isso, no `main.py`, utilizamos:

```python
item.relative_to(directory)
```

O método `.relative_to()` representa o caminho de um item em relação ao diretório informado.

No nosso caso, como analisamos diretamente os arquivos presentes na pasta selecionada, o resultado normalmente corresponde ao nome do arquivo.

Exemplo:

```text
arquivo.txt
```

Isso reduz a exposição de caminhos pessoais nos relatórios.

Não significa que o relatório seja anônimo: nomes de arquivos e outras informações registradas ainda podem ser sensíveis.

## 9. Como os indicadores são apresentados?

A função de análise retorna um valor booleano:

- `True`: a regra identificou o padrão configurado.
- `False`: a regra não identificou o padrão.

O módulo de relatórios utiliza esse resultado para registrar uma mensagem correspondente.

Um indicador suspeito não deve ser apresentado como confirmação de malware.

## 10. Tratamento dos arquivos com erro

Quando um arquivo apresenta um erro de leitura tratado pelo `main.py`, utilizamos `continue` para passar ao próximo item.

Nesse caso, o arquivo problemático não é adicionado à lista `resultados`.

Consequentemente, o relatório atual reúne somente os arquivos que foram analisados com sucesso.

Uma possível melhoria futura seria incluir uma seção específica para arquivos não analisados e os respectivos erros encontrados.

## 11. Resumo para consulta

| Recurso | Finalidade |
|---|---|
| Dicionário `{}` | Armazenar as informações de um arquivo. |
| Lista `[]` | Reunir os resultados de vários arquivos. |
| `.append()` | Adicionar um resultado à lista. |
| `for` | Percorrer os resultados. |
| `Path()` | Trabalhar com caminhos. |
| `.mkdir()` | Criar um diretório. |
| `datetime.now()` | Obter a data e o horário atuais. |
| `.strftime()` | Formatar datas e horários. |
| `open(..., "w")` | Abrir um arquivo para escrita. |
| `.write()` | Escrever conteúdo textual. |
| `.relative_to()` | Representar um caminho em relação a outro. |

## 12. Conclusão

O módulo de relatórios permite registrar os resultados produzidos pelo Python File Security Analyzer para consulta posterior.
