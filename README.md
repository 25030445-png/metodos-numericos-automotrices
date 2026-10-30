# Métodos numéricos para sistemas automotrices

**Problemario de sistemas de ecuaciones lineales — ITESA**

**Autor:** Davila Campuzano Jorge Fernando
**Matrícula:** 25030445
**Asignatura:** Métodos Numéricos

Este repositorio contiene el código fuente real en Python 3.10+ del problemario de sistemas lineales de Ingeniería en Sistemas Automotrices. Los datos son **sintéticos para fines didácticos**; no se deben utilizar para calibración o control de vehículos reales.

## Métodos implementados
- **Eliminación Gaussiana** con pivoteo parcial y sustitución regresiva.
- **Gauss-Jordan** con pivoteo parcial.
- **Jacobi** iterativo, con control de tolerancia y convergencia.

Se documentan **18 casos** (6 por método), incluidos **12 resolubles** y **6 pruebas de diagnóstico**. El código conserva la ortografía de los identificadores y la sintaxis correcta, independientemente del estilo del documento escrito.

## Archivos

- `solucionadores.py`: implementaciones matemáticas.
- `casos.py`: casos y sistemas matriciales de los 18 ejercicios.
- `ejecutar.py`: validación y exportación CSV.
- `tests/test_solucionadores.py`: pruebas automáticas.
- `resultados.csv`: resultados de las pruebas.
- `.gitignore`: exclusiones de archivos temporales.

## Cómo ejecutar

```bash
python ejecutar.py --detalle
python -m unittest discover -s tests -v
```

No requiere paquetes externos. La ejecución debe mostrar **18/18 pruebas aprobadas** y la batería unitaria debe aprobar sus cinco pruebas.

**Importante:** los casos con diagnóstico de error están diseñados para comprobar la detección de sistemas inconsistentes, indeterminados, diagonales nulas o ausencia de convergencia. No son cálculos erróneos ocultos.

**Repositorio vinculado a:** (https://github.com/25030445-png/metodos-numericos-automotrices).
