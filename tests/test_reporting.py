import unittest
import tempfile
import os
from pathlib import Path
from unittest.mock import patch

from analyzer.reporting import gerar_relatorio


class TesteReporting(unittest.TestCase):

    def test_gerar_relatorio(self):
        resultados = [
            {
                "nome": "comprovante.pdf.exe",
                "extensao": ".exe",
                "tamanho": 25,
                "caminho": "comprovante.pdf.exe",
                "sha256": "hash_ficticio",
                "suspeito": True
            }
        ]

        with tempfile.TemporaryDirectory() as pasta_temporaria:
            with patch.dict(os.environ, {}, clear=False):
                diretorio_original = Path.cwd()

                try:
                    os.chdir(pasta_temporaria)
                    caminho = gerar_relatorio(resultados)
                    caminho = Path(caminho).resolve()
                finally:
                    os.chdir(diretorio_original)

                self.assertTrue(caminho.exists())

                conteudo = caminho.read_text(encoding="utf-8")

                self.assertIn("comprovante.pdf.exe", conteudo)
                self.assertIn("hash_ficticio", conteudo)