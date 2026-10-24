# Visão Geral — Python File Security Analyzer

## 1. O que é o projeto?

O Python File Security Analyzer é uma ferramenta defensiva desenvolvida em Python para analisar arquivos presentes em diretórios autorizados.

O projeto foi criado com finalidade educacional, permitindo aplicar conhecimentos de programação, manipulação de arquivos, hashing, identificação de indicadores suspeitos e testes automatizados.

A ferramenta não executa os arquivos analisados.

## 2. Objetivo

O objetivo é identificar determinadas características dos arquivos e registrar os resultados de forma organizada.

Atualmente, a ferramenta permite:

- Selecionar um diretório para análise.
- Listar os arquivos presentes diretamente no diretório.
- Consultar informações como nome, extensão e tamanho.
- Calcular hashes SHA-256.
- Identificar determinados padrões de dupla extensão.
- Gerar um relatório textual com os resultados.
- Tratar erros de acesso a arquivos, permitindo continuar a análise.
- Executar testes automatizados das principais funcionalidades.

## 3. Como funciona?

O funcionamento geral segue este fluxo:

1. O usuário informa o caminho de um diretório.
2. O programa verifica se o diretório existe.
3. Os arquivos são percorridos individualmente.
4. Para cada arquivo, o programa tenta calcular seu hash SHA-256 e coletar informações.
5. Uma regra verifica se o nome apresenta um padrão de dupla extensão configurado.
6. Os resultados são armazenados em uma lista de dicionários.
7. Ao final, um relatório textual é gerado.

Caso um arquivo apresente um erro de acesso durante a análise, o programa informa o problema e tenta continuar com os demais.

## 4. Organização do código

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Controla o fluxo principal da ferramenta. |
| `analyzer/hashing.py` | Calcula o hash SHA-256 dos arquivos. |
| `analyzer/rules.py` | Aplica a regra de identificação de dupla extensão. |
| `analyzer/reporting.py` | Gera os relatórios textuais. |
| `tests/` | Contém os testes automatizados. |
| `samples/` | Diretório destinado a arquivos de teste inofensivos. |
| `reports/` | Diretório destinado aos relatórios gerados. |
| `docs/` | Contém a documentação técnica e didática do projeto. |

## 5. Limitações importantes

Esta ferramenta não é um antivírus e não confirma a presença ou ausência de malware.

A identificação de dupla extensão é apenas uma regra heurística simples. Um resultado suspeito indica que determinado padrão foi encontrado, não que o arquivo seja necessariamente malicioso.

Da mesma forma, um arquivo sem indicadores identificados não deve ser considerado automaticamente seguro.

A análise atual não é recursiva: apenas os arquivos presentes diretamente no diretório selecionado são processados.

O hash SHA-256 identifica o conteúdo de um arquivo, mas não determina, isoladamente, se ele é seguro ou malicioso.

## 6. Finalidade educacional

Este projeto foi desenvolvido para praticar Python e fundamentos de cibersegurança defensiva.

Os testes devem ser realizados em diretórios autorizados, preferencialmente utilizando arquivos fictícios e ambientes controlados.