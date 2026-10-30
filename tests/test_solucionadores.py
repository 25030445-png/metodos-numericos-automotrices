"""Batería unitaria de validación."""
import unittest
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from casos import CASOS
from solucionadores import METODOS,validar,residuo,jacobi

class Pruebas(unittest.TestCase):
    def test_casos(self):
        self.assertEqual(len(CASOS),18)
        for c in CASOS:
            with self.subTest(id=c["id"]):
                r=METODOS[c["metodo"]](c["A"],c["b"])
                self.assertEqual(r["estado"],c["esperado"])
                if c["esperado"]=="resuelto":
                    self.assertLess(r["residuo"],1e-6)
                    for v,w in zip(r["solucion"],c["referencia"]):
                        self.assertAlmostEqual(v,w,places=5)
    def test_dimensiones(self):
        with self.assertRaises(ValueError): validar([[1,2]],[1])
    def test_no_finitos(self):
        with self.assertRaises(ValueError): validar([[float("nan")]],[1])
    def test_jacobi_x0(self):
        with self.assertRaises(ValueError): jacobi([[2,0],[0,2]],[2,2],x0=[0])
    def test_residuo(self):
        self.assertEqual(residuo([[2,1],[1,3]],[4,7],[1,2]),0.0)

if __name__=="__main__":
    unittest.main()
