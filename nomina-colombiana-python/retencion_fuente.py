# retencion_fuente.py

import numpy as np
import pandas as pd
from datetime import datetime

def calcular_retencion_en_la_fuente(salario_bruto, porcentaje_retencion):
    """
    Calcula la retención en la fuente basada en el salario bruto y el porcentaje de retención.

    :param salario_bruto: float - Salario bruto del empleado.
    :param porcentaje_retencion: float - Porcentaje de retención en la fuente (ej. 15 para 15%).
    :return: float - Monto de la retención en la fuente.
    """
    return salario_bruto * (porcentaje_retencion / 100)

# Ejemplo de uso
if __name__ == "__main__":
    salario_bruto = 2500000.0
    porcentaje_retencion = 15.0
    retencion = calcular_retencion_en_la_fuente(salario_bruto, porcentaje_retencion)
    print(f"Retención en la fuente: {retencion:.2f}")
```

Este módulo incluye una función `calcular_retencion_en_la_fuente` que toma como parámetros el salario bruto del empleado y el porcentaje de retención en la fuente, y devuelve el monto de la retención. El ejemplo de uso al final muestra cómo llamar a esta función con valores ficticios.