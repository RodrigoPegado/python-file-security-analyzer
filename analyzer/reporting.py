from pathlib import Path
from datetime import datetime


def gerar_relatorio(resultados):
    pasta = Path("reports")
    pasta.mkdir(exist_ok=True)
    data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
    caminho = pasta / f"relatorio_{data_hora}.txt"
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write("=== PYTHON FILE SECURITY ANALYZER ===\n")
        arquivo.write(f"Data da análise: {datetime.now():%d/%m/%Y %H:%M:%S}\n")
        arquivo.write(f"Total de arquivos: {len(resultados)}\n")
        arquivo.write("=" * 45 + "\n\n")
        for resultado in resultados:
            arquivo.write(f"Nome: {resultado['nome']}\n")
            arquivo.write(f"Extensão: {resultado['extensao']}\n")
            arquivo.write(f"Tamanho: {resultado['tamanho']} bytes\n")
            arquivo.write(f"Caminho: {resultado['caminho']}\n")
            arquivo.write(f"SHA-256: {resultado['sha256']}\n")
            if resultado["suspeito"]:
                arquivo.write(
                    "Indicador: Possível dupla extensão suspeita\n"
                )
            else:
                arquivo.write(
                    "Indicador: Nenhum indicador identificado pela regra atual\n"
                )

            arquivo.write("-" * 45 + "\n\n")
    return caminho