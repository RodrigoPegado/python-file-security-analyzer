from pathlib import Path

def verificar_extensao(caminho):
    arquivo = Path(caminho)
    extensoes = arquivo.suffixes
    extensoes_disfarce = [".pdf", ".txt", ".png", ".jpg"]
    extensoes_executaveis = [".exe", ".bat", ".cmd", ".com", ".msi"]
    if len(extensoes) >= 2:
        if extensoes[-1].lower() in extensoes_executaveis:
            if extensoes[-2].lower() in extensoes_disfarce:
                return True
            
    return False        
