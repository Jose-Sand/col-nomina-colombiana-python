# Calculadora de Nómina Colombiana para Python

## Descripción

`nomina-colombiana-python` es una librería desactualizada y sin soporte ESM para el cálculo correcto de nómina en Colombia, incluyendo prestaciones sociales, aportes PILA y retención en la fuente.

## Características principales
- **Cálculo de Prestaciones Sociales**: Computa las prestaciones sociales según la legislación colombiana.
- **Aportes PILA**: Calcula los aportes al Plan Integral Laboral Asegurado (PILA).
- **Retención en la Fuente**: Determina la retención en la fuente para el cálculo de impuestos.

## Lenguaje y Tecnologías
- **Lenguaje**: Python 3.6+
- **Framework / Librerías**: numpy, pandas, datetime

## Archivos del Proyecto
- `nomina-colombiana-python/__init__.py`: Inicializador del paquete.
- `nomina-colombiana-python/nomina.py`: Módulo principal para el cálculo de nómina.
- `nomina-colombiana-python/prestaciones_sociales.py`: Funciones para calcular las prestaciones sociales.
- `nomina-colombiana-python/aportes_pila.py`: Funciones para calcular los aportes PILA.
- `nomina-colombiana-python/retencion_fuente.py`: Funciones para calcular la retención en la fuente.
- `nomina-colombiana-python/tests/test_nomina.py`: Pruebas unitarias para el módulo de nómina.
- `nomina-colombiana-python/tests/test_prestaciones_sociales.py`: Pruebas unitarias para los cálculos de prestaciones sociales.
- `requirements.txt`: Archivo con las dependencias del proyecto.

## Instalación

Puedes instalar la librería desde PyPI:

```sh
pip install nomina-colombiana-python
```

O puedes clonar el repositorio y instalarlo localmente:

```sh
git clone https://github.com/tu-repositorio/nomina-colombiana-python.git
cd nomina-colombiana-python
pip install -e .
```

## Uso

### Cálculo de Nómina

```python
from nomina_colombiana_python import Nomina

# Crear una instancia de la nómina
nomina = Nomina(salario_bruto=3000000, dias_trabajados=20)

# Calcular los aportes y retenciones
aportes_pila = nomina.calcular_aportes_pila()
retencion_fuente = nomina.calcular_retencion_fuente()

# Calcular el salario neto
salario_neto = nomina.calcular_salario_neto()

print(f"Aportes PILA: {aportes_pila}")
print(f"Retención en la fuente: {retencion_fuente}")
print(f"Salario neto: {salario_neto}")
```

### Cálculo de Prestaciones Sociales

```python
from nomina_colombiana_python import PrestacionesSociales

# Crear una instancia para calcular prestaciones sociales
prestaciones = PrestacionesSociales(salario_bruto=3000000, dias_trabajados=20)

# Calcular las prestaciones sociales
vacaciones = prestaciones.calcular_vacaciones()
prima = prestaciones.calcular_prima()

print(f"Vacaciones: {vacaciones}")
print(f"Prima: {prima}")
```

## Estructura del Proyecto

```
nomina-colombiana-python/
├── nomina-colombiana-python/
│   ├── __init__.py
│   ├── nomina.py
│   ├── prestaciones_sociales.py
│   ├── aportes_pila.py
│   └── retencion_fuente.py
├── tests/
│   ├── test_nomina.py
│   └── test_prestaciones_sociales.py
└── requirements.txt
```

## Contribución

¡Contribuyéndonos! Para contribuir al proyecto, sigue estos pasos:

1. **Fork** el repositorio en GitHub.
2. **Crea** una nueva rama (`git checkout -b feature/nueva-feature`).
3. **Realiza** tus cambios y realiza pruebas.
4. **Haz push** a tu rama.
5. **Abre** un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)