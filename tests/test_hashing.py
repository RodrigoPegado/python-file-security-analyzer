import unittest
import hashlib
import tempfile
from pathlib import Path

from analyzer.hashing import calcular_hash

class TesteHashing(unittest.TestCase):

    def test_hash_arquivo_vazio(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "arquivo_teste.txt"
            caminho.write_bytes(b"")
            resultado = calcular_hash(caminho)
            esperado = hashlib.sha256(b"").hexdigest()
            self.assertEqual(resultado, esperado)
