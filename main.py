import pathlib
from analyzer.rules import verificar_extensao
from analyzer.hashing import calcular_hash
total_files = 0
print("=== PYTHON FILE SECURITY ANALYZER ===")
file_path = input("Informe o caminho do diretório: ")
directory = pathlib.Path(file_path)
if directory.is_dir():
    print('\n[+] Diretório encontrado!:')
    print('Arquivos encontrados:')
    for item in directory.iterdir():
        if item.is_file() and item.name != '.gitkeep':
            print(f'  - {item.name} ')
            print(f'    extensão: {item.suffix}')
            print(f'    tamanho: {item.stat().st_size} bytes')
            print(f'    caminho: {item.resolve()}')
            print(f'    hash SHA-256: {calcular_hash(item)}')
            if verificar_extensao(item):
                print('[!] Arquivo suspeito! Possível dupla extensão.')
            else:
                print('[i] Nenhum indicador identificado pela regra atual.')
            print('-'*40)
            total_files += 1
    print(f'[+] Total de arquivos encontrados: {total_files}')
else:
    print('\n[-] Diretório não encontrado!')    