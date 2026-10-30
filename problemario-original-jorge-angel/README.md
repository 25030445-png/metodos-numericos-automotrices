# Primer problemario ITESA — Sistemas de ecuaciones lineales

**Autores del documento original:** Dávila Campuzano Jorge Fernando (25030445) y Ángel Jesús Moreno Trejo (25030183).  
**Docente:** Efrén Rolando Romero León.  
**Carrera:** Ingeniería en Sistemas Automotrices.

Esta carpeta es independiente de la entrega de Yacob que se encuentra en la raíz del repositorio. Contiene los ejercicios y algoritmos **del primer problemario**, sin cambiar sus problemas matemáticos.

## Métodos

- **Eliminación gaussiana** con pivoteo parcial.
- **Gauss-Jordan** con pivoteo parcial y reducción de la matriz.
- **Gauss-Seidel** iterativo y comprobación de residuo.

Se incluyen 18 pruebas (6 por método: 4 resolubles y 2 diagnósticos). Los problemas emplean datos sintéticos didácticos, no mediciones de automóviles reales.

## Código fuente de esta entrega

- [metodos.py](metodos.py): algoritmos y validación.
- [casos.py](casos.py): matrices, vectores y contextos de los 18 problemas.
- [ejecutar_pruebas.py](ejecutar_pruebas.py): verificación y exportación de resultados.
- [tests/test_metodos.py](tests/test_metodos.py): cuatro pruebas unitarias.
- [resultados.csv](resultados.csv): resultados de referencia.
- [.gitignore](.gitignore): exclusiones del proyecto.

## Ejecución paso a paso

Desde esta carpeta abre una terminal con Python 3.10 o posterior y ejecuta:

```bash
python ejecutar_pruebas.py --detalle
python ejecutar_pruebas.py --csv resultados.csv
python -m unittest discover -s tests -v
```

Resultado esperado: **18/18 casos correctos; 4 pruebas unitarias OK**.

El código no requiere bibliotecas de terceros ni incluye imágenes. Para abrir los ejercicios y compararlos con el informe Word, observa los identificadores G01–G06, J01–J06, S01–S06.

Repositorio: https://github.com/25030445-png/metodos-numericos-automotrices/tree/main/problemario-original-jorge-angel
