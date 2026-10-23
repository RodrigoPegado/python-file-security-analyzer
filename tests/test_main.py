import unittest
import tempfile

from pathlib import Path
from unittest.mock import patch

from main import main


class TesteMain(unittest.TestCase):

    def test_continua_apos_erro_de_permissao(self):

        with tempfile.TemporaryDirectory() as pasta:
            diretorio = Path(pasta)

            (diretorio / "arquivo_bloqueado.txt").write_text("teste")
            (diretorio / "documento.txt").write_text("conteudo seguro")

            resultados_capturados = []

            def hash_simulado(caminho):
                if caminho.name == "arquivo_bloqueado.txt":
                    raise PermissionError("Acesso negado (simulação)")

                return "hash_ficticio"

            def relatorio_simulado(resultados):
                resultados_capturados.extend(resultados)
                return "relatorio_teste.txt"

            with patch("builtins.input", return_value=str(diretorio)), \
                 patch("main.calcular_hash", side_effect=hash_simulado), \
                 patch("main.gerar_relatorio", side_effect=relatorio_simulado):

                main()

            self.assertEqual(len(resultados_capturados), 1)

            self.assertEqual(
                resultados_capturados[0]["nome"],
                "documento.txt"
            )