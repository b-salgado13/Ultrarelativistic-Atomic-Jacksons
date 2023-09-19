# Proyecto de Física Atómica y Molecular

## Este repositorio es para subir todos los documentos que se vayan haciendo sobre el proyecto de física atómica y molecular

La estructura del programa tiene la siguiente estructura (provisional)

![Alt text](/Imagenes/Esqueletov1.png )

## Escritura de funciones, variables y nombres de archivos

### Recomendaciones generales
El nombre debe ser significativo en el sentido que debe representar aquello por lo que se definió el nombre.  Escoge los nombres cuidadosamente y cambialos en caso de encontrar uno mejor. 

Una buen nombre debe responder las siguientes prguntas 
 * ¿Qué hace?
 * ¿Por qué debe existir?
 * ¿Cómo es usada?

Como recomendación general, si un nombre requiere un comentario para especificar mejor el nombre o la función, entonces el nombre elegido no revela la intención de la variable/función. 


### Variables
Las variables se escribiran bajo el estilo de escritura *snake case* el cual simplemente se trata de escribir el nombre completamente en minúsculas y en caso de que el nombre consista de dos o más palabras serán separadas por un guión bajo "_".  

Por ejemplo, supongamos que vamos a declarar el valor de la masa del electrón, de acuerdo con este estilo de escritura podríamos escribir
> masa_electron = 393.92
> masa_del_electron = 393.93

### Funciones
Por su parte para las escritura de funciones se adoptará el estilo de escritura *camel case* el cual se basa en escribir el inicio de cada palabra con mayúsculas. En caso de que el nombre contenga dos o más palabras, no se coloca espacio, sino que cada palabra se separa escibiéndose la inicial con mayúscula.

Por ejemplo, supongamos que queremos crear una función que nos devuelva la función de onda del Hidrógeno dados los valores de *n, l* y *m*, entonces escribiríamos

> def FuncionDeOndaHidrogeno(n, l, m):





Derechos reservados
