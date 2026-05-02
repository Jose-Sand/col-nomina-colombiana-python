import numpy as np
import pandas as pd
from datetime import datetime

def calcular_prestaciones_sociales(remuneracion_bruta_mensual, antiguedad, dias_trabajados):
    """
    Calcula las prestaciones sociales en Colombia.

    :param remuneracion_bruta_mensual: Remuneración bruta mensual del trabajador.
    :param antiguedad: Antigüedad del trabajador en años.
    :param dias_trabajados: Número de días trabajados en el periodo a calcular.
    :return: Diccionario con los valores de las prestaciones sociales calculadas.
    """
    # Cálculo de la prima
    prima = remuneracion_bruta_mensual * (antiguedad / 12)
    
    # Cálculo del auxilio de transporte
    if antiguedad < 6:
        auxilio_transporte = remuneracion_bruta_mensual * 0.06
    else:
        auxilio_transporte = remuneracion_bruta_mensual * 0.1
    
    # Cálculo del auxilio alimenticio
    if dias_trabajados >= 30:
        auxilio_alimenticio = remuneracion_bruta_mensual * 0.25
    else:
        auxilio_alimenticio = remuneracion_bruta_mensual * 0.15
    
    # Cálculo del auxilio maternidad o paternidad
    if antiguedad < 180:
        auxilio_maternidad_paternidad = remuneracion_bruta_mensual * 0.3
    else:
        auxilio_maternidad_paternidad = remuneracion_bruta_mensual * 0.2
    
    # Cálculo del bono de alimentación
    if dias_trabajados >= 60:
        bono_alimentacion = remuneracion_bruta_mensual * 0.1
    else:
        bono_alimentacion = remuneracion_bruta_mensual * 0.05
    
    # Cálculo del aporte al plan de pensiones del trabajador
    aport_trabajador_pensiones = remuneracion_bruta_mensual * 0.12
    
    # Cálculo del aporte al plan de salud del trabajador
    aport_trabajador_salud = remuneracion_bruta_mensual * 0.04
    
    return {
        'prima': prima,
        'auxilio_transporte': auxilio_transporte,
        'auxilio_alimenticio': auxilio_alimenticio,
        'auxilio_maternidad_paternidad': auxilio_maternidad_paternidad,
        'bono_alimentacion': bono_alimentacion,
        'aport_trabajador_pensiones': aport_trabajador_pensiones,
        'aport_trabajador_salud': aport_trabajador_salud
    }