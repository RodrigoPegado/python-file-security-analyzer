import pathlib
totalfiles = 0
print("=== PYTHON FILE SECURITY ANALYZER ===")
file_path = input("Informe o caminho do diretório: ")
directory = pathlib.Path(file_path)
if directory.is_dir():
    print('[+] Diretório encontrado!:')
    print('Arquivos encontrados:')
    for item in directory.iterdir():
        if item.is_file() and item.name != '.gitkeep':
            print(f'  - {item.name}')
            totalfiles += 1
    print(f'[+] Total de arquivos encontrados: {totalfiles}')
else:
    print('[-] Diretório não encontrado!')    