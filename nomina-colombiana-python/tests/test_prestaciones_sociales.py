import unittest
from nomina_colombiana_python.prestaciones_sociales import calcular_prestaciones_sociales

class TestPrestacionesSociales(unittest.TestCase):

    def test_calcular_prestaciones_sociales(self):
        # Datos de prueba
        horas_trabajadas = 160
        salario_diario_integral = 250000
        categoria_ocupacional = 'A'

        # Cálculo esperado (ejemplo, valores ficticios)
        prestaciones_sociales_esperadas = {
            'Salud': 48000,
            'Pensiones': 36000,
            'Fondo de Cesantía': 24000
        }

        # Llamada a la función a probar
        prestaciones_sociales_calculadas = calcular_prestaciones_sociales(horas_trabajadas, salario_diario_integral, categoria_ocupacional)

        # Verificación de los resultados
        self.assertEqual(prestaciones_sociales_calculadas['Salud'], prestaciones_sociales_esperadas['Salud'])
        self.assertEqual(prestaciones_sociales_calculadas['Pensiones'], prestaciones_sociales_esperadas['Pensiones'])
        self.assertEqual(prestaciones_sociales_calculadas['Fondo de Cesantía'], prestaciones_sociales_esperadas['Fondo de Cesantía'])

if __name__ == '__main__':
    unittest.main()
```

Este archivo de pruebas unitarias verifica que la función `calcular_prestaciones_sociales` en el módulo `prestaciones_sociales.py` funcione correctamente con los datos de prueba proporcionados. Los valores esperados son ficticios y deben ser ajustados según las fórmulas reales del cálculo de prestaciones sociales en Colombia.