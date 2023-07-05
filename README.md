# Software de Gestión de Calificaciones y Capital Humano
## Grupo N°5 - Sistemas y Organizaciones
### Diego Piccinali ∣ Tobias Tinaro ∣ Jeremias Vergara ∣ Barbara Acuña

## Objetivo

Desarrollar, en python, un sistema para gestión de calificaciones, estudiantes, asignaturas y profesores usando la metodología de UserStories y SCRUM.

## Metas y especificaciones.

1 - Identificar los requisitos y funcionalidades clave del sistema de gestión de calificaciones. A saber:

* Como alumno quiero poder ver mis calificaciones

* Como profesor quiero poder ver y modificar las calificaciones de mis alumnos

* Como administrador quiero poder ver, crear, modificar y eliminar cualquier registro del sistema.

Por lo tanto, se debe desarrollar una pantalla de presentación en la cuál uno pueda ingresar bien como alumno, cómo profesor, o como administrador.

Apegándonos al uso que podría dársele dentro de un entorno real, tanto cada profesor individualmente, como quien sea el administrador, debería contar con una contraseña de acceso única, siendo así que nadie que utilice el programa pueda acceder a información sensible que no le corresponda. Siendo así también que las opciones disponibles para cada uno correspondan únicamente con aquellas funciones que de él se esperan.

2 - Establecer la prioridad de cada User Story, clasificándolas por importancia, en este trabajo estas implementaciones están ordenadas en los siguientes grupos:

Tiene que estar
Debería estar
Podría estar
No tiene por qué estar


3 - Crear un repositorio de GitHub y configurar sus ramas y estructura necesarias para el desarrollo.


4 - Poner las UserStories que se escogieron en el backlog y asignar a cada miembro las tareas que le correspondan en el primer y segundo sprint, estableciendo milestones para tener un proceso de desarrollo lo más ordenado y equitativo posible.

## Observaciones.

### ¿Cómo almacenamos los datos?

La implementación de una base de datos complicaría la ejecución del programa en cada computadora en la que se intente usar, por lo que reemplazarla por un método de almacenamiento y gestión de datos local parece ser lo más conveniente.
En este proyecto se utiliza la capacidad nativa de python de trabajar con archivos CSV que permiten almacenar información organizada por filas y columnas para administrar los datos de manera ordenada.

### ¿Por qué usar esa estructura de repositorio?

Parece ser la distribución más simple para poder tener una división de ficheros ordenada y al mismo tiempo evitar las división por módulos y su correspondiente importación, que, dada la poca experiencia de los miembros del equipo, complicaría en exceso el desarrollo.
Algunas modificaciones podrían ser, como ya se mencionó, la división en módulos independientes para las funciones correspondientes a la interfaz, calificaciones, asignaturas, profesores y alumnos, cómo también el uso de Tkinter o TkinterCostume para realizar una GUI más interactiva y visualmente atractiva para el programa, aunque dicha opción se descartó, puesto que el tiempo que significaría formar a los miembros del equipo en dichas librerías, además de su correspondiente implementación, excedería los plazos establecidos para la entrega que se estableció al momento del encargo del presente trabajo.

## Ideas descartadas.

Cómo se mencionó con anterioridad, el uso de una base de datos externa, o la incorporación de una GUI más elaborada e independiente del resto del código, fueron ideas que se barajaron aunque debieron ser descartadas. Pese a que dichas cosas le darían más robustez, complejidad y seguridad al sistemas, se optó por no implementarlas, dado que esto complicaría el desarrollo, lo alargaría en el tiempo, o simplemente el equipo no contaba con los conocimientos necesarios para su implementación, como también lo fueron:

* La encriptación y desencriptación de los datos almacenados en los archivos CSV, para mayor seguridad.

* Sistema de promedios, siendo que este constara de 2 notas base únicas por materia, que se procesen e informen al alumno de su condición de desaprobado, libre, regular o promocional.

* División de estudiantes de cualquier tipo, ya sea por curso, año, carrera, etc.

* Sistema de mensajería interna entre profesor y alumno.
