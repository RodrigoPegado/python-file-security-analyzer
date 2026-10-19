import pathlib

from analyzer.rules import verificar_extensao
from analyzer.hashing import calcular_hash
from analyzer.reporting import gerar_relatorio

total_files = 0
resultados = []

print("=== PYTHON FILE SECURITY ANALYZER ===")

file_path = input("Informe o caminho do diretório: ")
directory = pathlib.Path(file_path)

if directory.is_dir():
    print('\n[+] Diretório encontrado!')
    print('Arquivos encontrados:')

    for item in directory.iterdir():

        if item.is_file() and item.name != '.gitkeep':

            print(f'  - {item.name}')
            print(f'    extensão: {item.suffix}')
            print(f'    tamanho: {item.stat().st_size} bytes')
            print(f'    caminho: {item.relative_to(directory)}')

            hash_arquivo = calcular_hash(item)
            print(f'    hash SHA-256: {hash_arquivo}')

            resultado_suspeito = verificar_extensao(item)

            if resultado_suspeito:
                print('[!] Indicador suspeito: possível dupla extensão.')
            else:
                print('[i] Nenhum indicador identificado pela regra atual.')

            resultado_arquivo = {
                "nome": item.name,
                "extensao": item.suffix,
                "tamanho": item.stat().st_size,
                "caminho": str(item.relative_to(directory)),
                "sha256": hash_arquivo,
                "suspeito": resultado_suspeito
            }

            resultados.append(resultado_arquivo)
            total_files += 1
            print("-" * 45)

    caminho_relatorio = gerar_relatorio(resultados)

    print(f"\n[+] Total de arquivos analisados: {total_files}")
    print("[+] Relatório gerado com sucesso!")
    print(f"[+] Local: {caminho_relatorio}")

else:
    print("[-] Diretório não encontrado!")