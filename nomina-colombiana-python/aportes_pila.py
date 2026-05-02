# aportes_pila.py

import numpy as np
import pandas as pd
from datetime import datetime

def calcular_aportes_pila(salario_bruto, dias_trabajados):
    """
    Calcula los aportes al Plan Integral de Limpieza Ambiental (PILA)

    Args:
        salario_bruto (float): Salario bruto del empleado.
        dias_trabajados (int): Número de días trabajados en el mes.

    Returns:
        dict: Diccionario con los aportes al PILA.
    """
    # Aporte al PILA es 0.2% del salario bruto por día trabajado
    aporte_pila_diario = salario_bruto * 0.002
    aporte_pila_mensual = aporte_pila_diario * dias_trabajados

    return {
        'aporte_pila_diario': aporte_pila_diario,
        'aporte_pila_mensual': aporte_pila_mensual
    }

# Ejemplo de uso:
if __name__ == "__main__":
    salario_bruto = 1500000.0  # Salario bruto del empleado
    dias_trabajados = 30  # Número de días trabajados en el mes

    aportes_pila = calcular_aportes_pila(salario_bruto, dias_trabajados)
    print(f"Aporte al PILA diario: ${aportes_pila['aporte_pila_diario']:.2f}")
    print(f"Aporte al PILA mensual: ${aportes_pila['aporte_pila_mensual']:.2f}")