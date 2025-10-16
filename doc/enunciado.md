# Objetivo: Implementar en Python un modelo de programación entera mixta, utilizando la librería DOCplex

## Descripción

Modificar el modelo matemático asignado, ver anexo, incluyendo nuevas variables binarias y restricciones, para
transformarlo en un problema entero mixto. Si es necesario, también pueden mejorar el modelo de la tarea 1. Resolver el
nuevo modelo utilizando la librería DOCplex desde Python, analizar los resultados y comparar con la tarea 1 respecto a
la solución en el contexto del problema y el tiempo computacional necesario para resolverlo.

A el modelo base, deben agregar nuevas restricciones, dependiendo del contexto del problema, por ejemplo:

- **Restricciones de inversión**: para producir A es necesario comprar la máquina X.
- **Costos por tramos**: si compra menos de 10 productos valen Y, pero si compra 10 o más, el costo es X.
- **Proporciones de trabajo**: si sólo fabrica A, se demora T; si sólo fabrica B, se demora W.
- **Excluyentes**: si hace A, no puede hacer B.
- **Secuencia**: el trabajo X tiene que iniciar cuando finalice el Y.
- **Otras que requieran la utilización de variables binarias.**

La tabla del anexo indica por cada estudiante, el número del grupo asignado y el nombre del autor del modelo base que
deben implementar.

Se recuerda que la entrega de archivos en blanco, corresponde a NCR. No pueden ser tareas presentadas en semestres
anteriores. Se puede utilizar inteligencia generativa pero, al entregar el trabajo, garantizan que han revisado y
validado su contenido.

## Fecha de Entrega: viernes 17 de octubre de 2025, 23:59 hrs

## Entrega

Deben subir a la plataforma Canvas dos archivos:

- informe de máximo 4 páginas con la identificación de la pareja/grupo, descripción de la situación que incluya los
  parámetros del modelo, descripción de los componentes del modelo resaltando las modificaciones; modelo matemático en
  forma algebraica, análisis y comentario de los resultados obtenidos. Formato PDF.

- Script en Python (.py o .ipynb) con la implementación en DOCplex.

## Evaluación: 7%

| Concepto | Puntaje |
|-|-|
| Coherencia de la nueva restricción en el contexto del problema | 3 |
| Originalidad de la nueva restricción en la situación propuesta | 2 |
| Definición de los componentes del modelo matemático | 4 |
| Exactitud del modelo matemático mixto respecto a la situación | 5 |
| Interpretación de los resultados | 5 |
| Correspondencia entre la implementación del modelo y el código en Python | 5 |
