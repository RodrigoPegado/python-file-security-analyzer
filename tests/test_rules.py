import unittest

from analyzer.rules import verificar_extensao


class TesteRegras(unittest.TestCase):

    def test_dupla_extensao_exe(self):
        resultado = verificar_extensao("comprovante.pdf.exe")

        self.assertTrue(resultado)

    def test_dupla_extensao_bat(self):
        resultado = verificar_extensao("relatorio.pdf.bat")

        self.assertTrue(resultado)

    def test_arquivo_comum(self):
        resultado = verificar_extensao("documento.pdf")

        self.assertFalse(resultado)

    def test_extensao_unica_exe(self):
        resultado = verificar_extensao("programa.exe")

        self.assertFalse(resultado)

    def test_extensao_maiuscula(self):
        resultado = verificar_extensao("FOTO.JPG.EXE")

        self.assertTrue(resultado)