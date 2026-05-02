import numpy as np
import pandas as pd
from datetime import datetime

def calcular_prestaciones_sociales(salario_base, dias_trabajados):
    """
    Calcula las prestaciones sociales del salario base.

    :param salario_base: Salario base mensual
    :param dias_trabajados: Número de días trabajados en el mes
    :return: Monto de las prestaciones sociales
    """
    # Prestación por Préstamo Hipotecario (PH)
    ph = salario_base * 0.025 if dias_trabajados >= 30 else 0
    
    # Prestación por Cesantía Diaria
    cesantia_diaria = salario_base / 30 * dias_trabajados
    
    # Prestación por Interés sobre el Cesantía Diaria
    interes_cesantia_diaria = cesantia_diaria * 0.12
    
    # Total de prestaciones sociales
    total_prestaciones_sociales = ph + cesantia_diaria + interes_cesantia_diaria
    
    return total_prestaciones_sociales

def calcular_aportes_pila(salario_base, dias_trabajados):
    """
    Calcula los aportes al Sistema Popular de Ahorro y Lucro (PILA).

    :param salario_base: Salario base mensual
    :param dias_trabajados: Número de días trabajados en el mes
    :return: Monto de los aportes PILA
    """
    # Aporte del empleador al PILA
    aporte_empleador = salario_base * 0.04
    
    # Aporte del empleado al PILA (2% sobre el salario base)
    aporte_empleado = salario_base * 0.02
    
    # Total de aportes PILA
    total_pila = aporte_empleador + aporte_empleado
    
    return total_pila

def calcular_retencion_en_la_fuente(salario_base, dias_trabajados):
    """
    Calcula la retención en la fuente (RETFuente).

    :param salario_base: Salario base mensual
    :param dias_trabajados: Número de días trabajados en el mes
    :return: Monto de la RETFuente
    """
    # Retención del empleador sobre la prima por ausentismo
    prima_ausentismo = salario_base * 0.1 if dias_trabajados < 30 else 0
    
    # Retención del empleador sobre el interes cesantia diaria
    interes_cesantia_diaria = calcular_prestaciones_sociales(salario_base, dias_trabajados)
    
    # Total de RETFuente
    retencion_fuente = prima_ausentismo + interes_cesantia_diaria
    
    return retencion_fuente

def calcular_nómina(salario_base, dias_trabajados):
    """
    Calcula el total de la nómina incluyendo prestaciones sociales, aportes PILA y retención en la fuente.

    :param salario_base: Salario base mensual
    :param dias_trabajados: Número de días trabajados en el mes
    :return: Total de la nómina
    """
    # Calculo de las prestaciones sociales
    prestaciones_sociales = calcular_prestaciones_sociales(salario_base, dias_trabajados)
    
    # Calculo de los aportes PILA
    aportes_pila = calcular_aportes_pila(salario_base, dias_trabajados)
    
    # Calculo de la retención en la fuente
    retencion_fuente = calcular_retencion_en_la_fuente(salario_base, dias_trabajados)
    
    # Total de la nómina
    total_nómina = salario_base + prestaciones_sociales + aportes_pila - retencion_fuente
    
    return total_nómina

# Ejemplo de uso
if __name__ == "__main__":
    salario_base = 3000000  # Salario base mensual en COP
    dias_trabajados = 25  # Número de días trabajados en el mes
    
    nómina_total = calcular_nómina(salario_base, dias_trabajados)
    print(f"Total de la nómina: {nómina_total} COP")
```

Este código proporciona funciones para calcular las prestaciones sociales, los aportes al Sistema Popular de Ahorro y Lucro (PILA) y la retención en la fuente (RETFuente). Además, incluye una función principal `calcular_nómina` que suma todas estas partes para obtener el total de la nómina del empleado.