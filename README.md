# 🛡️ Python File Security Analyzer

Ferramenta defensiva desenvolvida em **Python** para analisar arquivos em diretórios autorizados, calcular hashes SHA-256 e identificar determinados indicadores suspeitos por meio de regras heurísticas.

O projeto foi desenvolvido com foco no aprendizado prático de Python e segurança da informação, aplicando conceitos como manipulação de arquivos, hashing, organização modular, tratamento de exceções, testes automatizados e documentação técnica.

> **Aviso:** este é um projeto educacional. Os indicadores identificados não representam uma confirmação de malware e não substituem soluções profissionais de segurança.

---

## Funcionalidades

- Análise dos arquivos presentes em um diretório informado pelo usuário.
- Coleta de informações como nome, extensão e tamanho dos arquivos.
- Cálculo de hashes SHA-256.
- Identificação de determinados padrões de dupla extensão.
- Geração automática de relatórios em formato `.txt`.
- Tratamento de erros individuais de leitura, permitindo continuar a análise dos demais arquivos.
- Testes automatizados utilizando `unittest`.
- Documentação técnica e educacional.

### Exemplo de indicador suspeito

Um dos padrões analisados pela ferramenta é a combinação de uma extensão de documento ou imagem seguida por uma extensão configurada como potencialmente executável.

Exemplo:

```text
comprovante.pdf.exe
```

Nesse caso, a ferramenta sinaliza o nome do arquivo para uma possível investigação adicional.

**Importante:** a presença de uma dupla extensão não comprova que um arquivo seja malicioso. Da mesma forma, a ausência desse padrão não garante que o arquivo seja seguro.

---

## Tecnologias utilizadas

O projeto utiliza Python e módulos de sua biblioteca padrão, sem necessidade de instalar dependências externas.

| Tecnologia | Aplicação |
|---|---|
| Python | Linguagem principal |
| `pathlib` | Manipulação de caminhos e diretórios |
| `hashlib` | Cálculo de hashes SHA-256 |
| `datetime` | Data e horário dos relatórios |
| `unittest` | Testes automatizados |
| `tempfile` | Criação de ambientes temporários para testes |
| `unittest.mock` | Simulação de comportamentos e exceções |

---

## Estrutura do projeto

```text
python-file-security-analyzer/
│
├── analyzer/
│   ├── __init__.py
│   ├── hashing.py
│   ├── reporting.py
│   └── rules.py
│
├── docs/
│   ├── 01-visao-geral.md
│   ├── 02-bibliotecas.md
│   ├── 03-hashing.md
│   ├── 04-regras.md
│   ├── 05-relatorios.md
│   ├── 06-testes.md
│   └── 07-tratamento-erros.md
│
├── reports/
│   └── .gitkeep
│
├── samples/
│   └── .gitkeep
│
├── tests/
│   ├── test_hashing.py
│   ├── test_main.py
│   ├── test_reporting.py
│   └── test_rules.py
│
├── .gitignore
├── main.py
└── README.md
```

*Estrutura simplificada: arquivos gerados automaticamente e materiais de experimentação local foram omitidos.*

### Organização dos módulos

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Controla o fluxo principal da ferramenta |
| `hashing.py` | Calcula o SHA-256 dos arquivos |
| `rules.py` | Aplica a regra heurística de dupla extensão |
| `reporting.py` | Gera os relatórios textuais |
| `tests/` | Contém os testes automatizados |
| `docs/` | Contém a documentação técnica e educacional |

---

## Como executar

### 1. Pré-requisitos

É necessário possuir o **Python 3.8 ou superior** instalado no computador.

Verifique sua instalação pelo terminal:

```bash
python --version
```

### 2. Clonar o repositório

```bash
git clone https://github.com/Rodrigopegado/python-file-security-analyzer.git
```

Entre na pasta do projeto:

```bash
cd python-file-security-analyzer
```

Não é necessário instalar bibliotecas externas.

### 3. Executar a ferramenta

Na raiz do projeto, execute:

```bash
python main.py
```

O programa solicitará o caminho do diretório que deseja analisar.

Informe um diretório de sua propriedade ou para o qual você possua autorização de análise.

### 4. Consultar o relatório

Após a execução, a ferramenta gera um arquivo de texto na pasta:

```text
reports/
```

Os relatórios utilizam uma identificação baseada em data e horário, facilitando a consulta posterior.

---

## Exemplo de utilização

Considere um diretório contendo os seguintes arquivos fictícios:

```text
arquivos/
├── documento.pdf
├── foto.png
├── comprovante.pdf.exe
└── relatorio.pdf.bat
```

Durante a análise, a ferramenta coleta os metadados disponíveis, calcula o hash SHA-256 de cada arquivo acessível e aplica a regra heurística configurada.

Neste exemplo, os nomes `comprovante.pdf.exe` e `relatorio.pdf.bat` correspondem ao padrão de dupla extensão definido no módulo `rules.py`.

Os resultados são reunidos em um relatório textual.

A ferramenta **não executa os arquivos analisados** para realizar essa verificação.

---

## Testes automatizados

O projeto possui oito testes automatizados distribuídos entre os módulos de hashing, regras, relatórios e fluxo principal.

Para executar todos os testes, utilize o seguinte comando na raiz do repositório:

```bash
python -m unittest discover -s tests -v
```

Os testes verificam:

- O cálculo SHA-256 de um arquivo vazio.
- Diferentes cenários da regra de dupla extensão.
- A geração de um relatório.
- A continuidade da análise após um erro de permissão simulado.

Os testes utilizam recursos como `tempfile` e `unittest.mock`, permitindo verificar determinados comportamentos sem depender de alterações reais nas permissões dos arquivos do sistema.

---

## Documentação

Além do README, o projeto possui uma documentação educacional que explica os conceitos e as decisões de implementação.

| Documento | Conteúdo |
|---|---|
| [01 — Visão geral](docs/01-visao-geral.md) | Objetivo, funcionamento e limitações |
| [02 — Bibliotecas](docs/02-bibliotecas.md) | Módulos Python utilizados |
| [03 — Hashing](docs/03-hashing.md) | Funcionamento do SHA-256 |
| [04 — Regras](docs/04-regras.md) | Identificação heurística de dupla extensão |
| [05 — Relatórios](docs/05-relatorios.md) | Organização dos resultados e geração de arquivos |
| [06 — Testes](docs/06-testes.md) | Testes automatizados e simulação de comportamentos |
| [07 — Tratamento de erros](docs/07-tratamento-erros.md) | Exceções e continuidade da análise |

A documentação foi organizada para servir tanto como referência técnica quanto como material de estudo para iniciantes em Python.

---

## Limitações atuais

O Python File Security Analyzer é um projeto educacional e possui algumas limitações importantes:

- Realiza a análise dos arquivos diretamente presentes no diretório informado, sem percorrer subdiretórios recursivamente.
- Utiliza uma regra heurística específica de dupla extensão.
- Não realiza análise comportamental ou execução de arquivos.
- Não consulta automaticamente bases externas de reputação.
- Não determina se um arquivo contém malware.
- Arquivos cuja análise falha não são incluídos nos resultados do relatório atual.
- Não substitui antivírus, EDR ou outras ferramentas especializadas.

Um hash SHA-256 também não determina isoladamente se um arquivo é seguro ou malicioso.

---

## Possíveis melhorias futuras

- Implementação de novas regras heurísticas configuráveis.
- Opção de análise recursiva de diretórios.
- Exportação de relatórios em JSON.
- Registro separado de arquivos que não puderam ser analisados.
- Ampliação da cobertura dos testes automatizados.
- Desenvolvimento de uma interface web para facilitar a utilização da ferramenta.

Essas funcionalidades representam possibilidades de evolução e não fazem parte da implementação atual.

---

## Uso responsável

Esta ferramenta deve ser utilizada somente em arquivos e diretórios próprios ou em ambientes nos quais exista autorização para realizar análises.

Para experimentos, recomenda-se utilizar arquivos de teste inofensivos e ambientes controlados.

O objetivo do projeto é apoiar o aprendizado de programação defensiva e conceitos fundamentais de segurança da informação.

---

## Licença

Nenhuma licença de distribuição foi definida nesta versão. As condições de reutilização e contribuição poderão ser estabelecidas posteriormente.