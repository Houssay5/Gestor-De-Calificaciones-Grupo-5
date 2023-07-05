import csv

ALUMNOS_FILE = "datos/alumnos.csv"
PROFESORES_FILE = "datos/profesores.csv"
ASIGNATURAS_FILE = "datos/asignaturas.csv"
CALIFICACIONES_FILE = "datos/calificaciones.csv"

# Función para mostrar la pantalla de inicio
def pantalla_inicio():
    print("Sistema de Calificaciones")
    print("-------------------------")
    print("1. Iniciar sesión como Alumno")
    print("2. Iniciar sesión como Profesor")
    print("3. Iniciar sesión como Administrador")
    print("4. Salir")

# Función para iniciar sesión como alumno
def iniciar_sesion_alumno():
    dni = input("Ingrese el número de DNI: ")
    contraseña = input("Ingrese la contraseña: ")

    alumnos = leer_datos(ALUMNOS_FILE)
    for alumno in alumnos:
        if alumno[0] == dni and alumno[4] == contraseña:
            print(f"Bienvenido, {alumno[1]} {alumno[2]}")
            ver_calificaciones_alumno(dni)
            return

    print("Credenciales incorrectas.")

# Función para ver las calificaciones de un alumno
def ver_calificaciones_alumno(dni_alumno):
    calificaciones = leer_datos(CALIFICACIONES_FILE)
    calificaciones_alumno = []

    for calificacion in calificaciones:
        if calificacion[0] == dni_alumno:
            calificaciones_alumno.append(calificacion)

    if calificaciones_alumno:
        print("\nCalificaciones del alumno")
        print("------------------------")
        for calificacion in calificaciones_alumno:
            print(f"Asignatura: {calificacion[1]}")
            print(f"Calificación: {calificacion[2]}")
            print("----------------------")
    else:
        print("No se encontraron calificaciones para el alumno.")



# Función para obtener el nombre de una asignatura por su ID
def obtener_nombre_asignatura(id_asignatura):
    asignaturas = leer_datos(ASIGNATURAS_FILE)
    for asignatura in asignaturas:
        if asignatura[0] == id_asignatura:
            return asignatura[1]
    return "Desconocido"

# Función para iniciar sesión como profesor
def iniciar_sesion_profesor():
    dni = input("Ingrese el número de DNI: ")
    contraseña = input("Ingrese la contraseña: ")

    profesores = leer_datos(PROFESORES_FILE)
    for profesor in profesores:
        if profesor[0] == dni and profesor[3] == contraseña:
            print(f"Bienvenido, {profesor[1]} {profesor[2]}")
            menu_profesor(dni)
            return

    print("Credenciales incorrectas.")

# Función para mostrar el menú del profesor
def menu_profesor(dni):
    while True:
        print("\nMenú del Profesor")
        print("------------------")
        print("1. Ver las calificaciones de mis alumnos")
        print("2. Agregar calificaciones a un alumno")
        print("3. Modificar calificaciones de un alumno")
        print("4. Eliminar calificaciones de un alumno")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_calificaciones_profesor(dni)
        elif opcion == "2":
            agregar_calificaciones(dni)
        elif opcion == "3":
            modificar_calificaciones(dni)
        elif opcion == "4":
            eliminar_calificaciones(dni)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Función para ver las calificaciones de los alumnos asignados a un profesor
def ver_calificaciones_profesor(dni):
    calificaciones = leer_datos(CALIFICACIONES_FILE)
    print("\nCalificaciones de Mis Alumnos")
    print("-----------------------------")
    for calificacion in calificaciones:
        if calificacion[3] == dni:
            print(f"Alumno: {obtener_nombre_alumno(calificacion[0])}")
            print(f"Asignatura: {obtener_nombre_asignatura(calificacion[1])}")
            print(f"Calificación: {calificacion[2]}")
            print("----------------------")

# Función para obtener el nombre de un alumno por su DNI
def obtener_nombre_alumno(dni_alumno):
    alumnos = leer_datos(ALUMNOS_FILE)
    for alumno in alumnos:
        if alumno[0] == dni_alumno:
            return f"{alumno[1]} {alumno[2]}"
    return "Desconocido"

# Función para agregar calificaciones a un alumno
def agregar_calificaciones(dni_profesor):
    dni_alumno = input("Ingrese el número de DNI del alumno: ")
    id_asignatura = input("Ingrese el ID de la asignatura: ")
    calificacion = input("Ingrese la calificación: ")

    if not calificacion_valida(calificacion):
        print("Calificación inválida. Debe ser un número del 0 al 10.")
        return

    calificaciones = leer_datos(CALIFICACIONES_FILE)
    calificaciones.append([dni_alumno, id_asignatura, calificacion, dni_profesor])
    escribir_datos(CALIFICACIONES_FILE, calificaciones)
    print("Calificación agregada exitosamente.")

# Función para modificar las calificaciones de un alumno
def modificar_calificaciones(dni_profesor):
    dni_alumno = input("Ingrese el número de DNI del alumno: ")
    id_asignatura = input("Ingrese el ID de la asignatura: ")

    calificaciones = leer_datos(CALIFICACIONES_FILE)
    for calificacion in calificaciones:
        if calificacion[0] == dni_alumno and calificacion[1] == id_asignatura and calificacion[3] == dni_profesor:
            nueva_calificacion = input("Ingrese la nueva calificación: ")

            if not calificacion_valida(nueva_calificacion):
                print("Calificación inválida. Debe ser un número del 0 al 10.")
                return

            calificacion[2] = nueva_calificacion
            escribir_datos(CALIFICACIONES_FILE, calificaciones)
            print("Calificación modificada exitosamente.")
            return

    print("No se encontró la calificación.")

# Función para eliminar las calificaciones de un alumno
def eliminar_calificaciones(dni_profesor):
    dni_alumno = input("Ingrese el número de DNI del alumno: ")
    id_asignatura = input("Ingrese el ID de la asignatura: ")

    calificaciones = leer_datos(CALIFICACIONES_FILE)
    calificaciones_nuevas = []
    calificacion_eliminada = False

    for calificacion in calificaciones:
        if calificacion[0] == dni_alumno and calificacion[1] == id_asignatura and calificacion[3] == dni_profesor:
            calificacion_eliminada = True
        else:
            calificaciones_nuevas.append(calificacion)

    if calificacion_eliminada:
        escribir_datos(CALIFICACIONES_FILE, calificaciones_nuevas)
        print("Calificación eliminada exitosamente.")
    else:
        print("No se encontró la calificación.")

# Función para iniciar sesión como administrador
def iniciar_sesion_administrador():
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")

    # Verificar si las credenciales son las del administrador
    if usuario == "admin" and contraseña == "admin123":
        print("Inicio de sesión exitoso como Administrador")
        menu_administrador()
    else:
        print("Credenciales incorrectas.")

# Función para mostrar el menú del administrador
def menu_administrador():
    while True:
        print("\nMenú del Administrador")
        print("-----------------------")
        print("1. Ver las calificaciones de un alumno")
        print("2. Agregar calificaciones a un alumno")
        print("3. Modificar calificaciones de un alumno")
        print("4. Eliminar calificaciones de un alumno")
        print("5. Ver todos los alumnos")
        print("6. Crear un alumno")
        print("7. Modificar un alumno")
        print("8. Eliminar un alumno")
        print("9. Ver todos los profesores")
        print("10. Crear un profesor")
        print("11. Modificar un profesor")
        print("12. Eliminar un profesor")
        print("13. Ver todas las asignaturas")
        print("14. Crear una asignatura")
        print("15. Modificar una asignatura")
        print("16. Eliminar una asignatura")
        print("17. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_calificaciones_administrador()
        elif opcion == "2":
            agregar_calificaciones_administrador()
        elif opcion == "3":
            modificar_calificaciones_administrador()
        elif opcion == "4":
            eliminar_calificaciones_administrador()
        elif opcion == "5":
            ver_todos_los_alumnos()
        elif opcion == "6":
            crear_alumno()
        elif opcion == "7":
            modificar_alumno()
        elif opcion == "8":
            eliminar_alumno()
        elif opcion == "9":
            ver_todos_los_profesores()
        elif opcion == "10":
            crear_profesor()
        elif opcion == "11":
            modificar_profesor()
        elif opcion == "12":
            eliminar_profesor()
        elif opcion == "13":
            ver_todas_las_asignaturas()
        elif opcion == "14":
            crear_asignatura()
        elif opcion == "15":
            modificar_asignatura()
        elif opcion == "16":
            eliminar_asignatura()
        elif opcion == "17":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Función para ver las calificaciones de un alumno como administrador
def ver_calificaciones_administrador():
    dni_alumno = input("Ingrese el número de DNI del alumno: ")
    ver_calificaciones_alumno(dni_alumno)

# Función para agregar calificaciones a un alumno como administrador
def agregar_calificaciones_administrador():
    dni_alumno = input("Ingrese el número de DNI del alumno: ")
    id_asignatura = input("Ingrese el ID de la asignatura: ")
    calificacion = input("Ingrese la calificación: ")

    if not calificacion_valida(calificacion):
        print("Calificación inválida. Debe ser un número del 0 al 10.")
        return

    calificaciones = leer_datos(CALIFICACIONES_FILE)
    calificaciones.append([dni_alumno, id_asignatura, calificacion, "admin"])
    escribir_datos(CALIFICACIONES_FILE, calificaciones)
    print("Calificación agregada exitosamente.")

# Función para modificar las calificaciones de un alumno como administrador
def modificar_calificaciones_administrador():
    dni_alumno = input("Ingrese el número de DNI del alumno: ")
    id_asignatura = input("Ingrese el ID de la asignatura: ")

    calificaciones = leer_datos(CALIFICACIONES_FILE)
    for calificacion in calificaciones:
        if calificacion[0] == dni_alumno and calificacion[1] == id_asignatura:
            nueva_calificacion = input("Ingrese la nueva calificación: ")

            if not calificacion_valida(nueva_calificacion):
                print("Calificación inválida. Debe ser un número del 0 al 10.")
                return

            calificacion[2] = nueva_calificacion
            escribir_datos(CALIFICACIONES_FILE, calificaciones)
            print("Calificación modificada exitosamente.")
            return

    print("No se encontró la calificación.")

# Función para eliminar las calificaciones de un alumno como administrador
def eliminar_calificaciones_administrador():
    dni_alumno = input("Ingrese el número de DNI del alumno: ")
    id_asignatura = input("Ingrese el ID de la asignatura: ")

    calificaciones = leer_datos(CALIFICACIONES_FILE)
    calificaciones_nuevas = []
    calificacion_eliminada = False

    for calificacion in calificaciones:
        if calificacion[0] == dni_alumno and calificacion[1] == id_asignatura:
            calificacion_eliminada = True
        else:
            calificaciones_nuevas.append(calificacion)

    if calificacion_eliminada:
        escribir_datos(CALIFICACIONES_FILE, calificaciones_nuevas)
        print("Calificación eliminada exitosamente.")
    else:
        print("No se encontró la calificación.")

# Función para ver todos los alumnos
def ver_todos_los_alumnos():
    alumnos = leer_datos(ALUMNOS_FILE)
    print("\nAlumnos")
    print("-------")
    for alumno in alumnos:
        print(f"DNI: {alumno[0]}")
        print(f"Nombre: {alumno[1]} {alumno[2]}")
        print(f"Edad: {alumno[3]}")
        print("----------------------")

# Función para crear un nuevo alumno
def crear_alumno():
    dni = input("Ingrese el número de DNI: ")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = input("Ingrese la edad: ")
    contraseña = input("Ingrese una contraseña: ")

    alumnos = leer_datos(ALUMNOS_FILE)
    alumnos.append([dni, nombre, apellido, edad, contraseña])
    escribir_datos(ALUMNOS_FILE, alumnos)
    print("Alumno creado exitosamente.")

# Función para modificar un alumno existente
def modificar_alumno():
    dni = input("Ingrese el número de DNI del alumno: ")

    alumnos = leer_datos(ALUMNOS_FILE)
    for alumno in alumnos:
        if alumno[0] == dni:
            nombre = input("Ingrese el nuevo nombre: ")
            apellido = input("Ingrese el nuevo apellido: ")
            edad = input("Ingrese la nueva edad: ")
            contraseña = input("Ingrese una nueva contraseña: ")

            alumno[1] = nombre
            alumno[2] = apellido
            alumno[3] = edad
            alumno[4] = contraseña

            escribir_datos(ALUMNOS_FILE, alumnos)
            print("Alumno modificado exitosamente.")
            return

    print("No se encontró el alumno.")

# Función para eliminar un alumno existente
def eliminar_alumno():
    dni = input("Ingrese el número de DNI del alumno: ")

    alumnos = leer_datos(ALUMNOS_FILE)
    alumnos_nuevos = []
    alumno_eliminado = False

    for alumno in alumnos:
        if alumno[0] == dni:
            alumno_eliminado = True
        else:
            alumnos_nuevos.append(alumno)

    if alumno_eliminado:
        escribir_datos(ALUMNOS_FILE, alumnos_nuevos)
        print("Alumno eliminado exitosamente.")
    else:
        print("No se encontró el alumno.")

# Función para ver todos los profesores
def ver_todos_los_profesores():
    profesores = leer_datos(PROFESORES_FILE)
    print("\nProfesores")
    print("----------")
    for profesor in profesores:
        print(f"DNI: {profesor[0]}")
        print(f"Nombre: {profesor[1]} {profesor[2]}")
        print("----------------------")

# Función para crear un nuevo profesor
def crear_profesor():
    dni = input("Ingrese el número de DNI: ")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    contraseña = input("Ingrese una contraseña: ")

    profesores = leer_datos(PROFESORES_FILE)
    profesores.append([dni, nombre, apellido, contraseña])
    escribir_datos(PROFESORES_FILE, profesores)
    print("Profesor creado exitosamente.")

# Función para modificar un profesor existente
def modificar_profesor():
    dni = input("Ingrese el número de DNI del profesor: ")

    profesores = leer_datos(PROFESORES_FILE)
    for profesor in profesores:
        if profesor[0] == dni:
            nombre = input("Ingrese el nuevo nombre: ")
            apellido = input("Ingrese el nuevo apellido: ")
            contraseña = input("Ingrese una nueva contraseña: ")

            profesor[1] = nombre
            profesor[2] = apellido
            profesor[3] = contraseña

            escribir_datos(PROFESORES_FILE, profesores)
            print("Profesor modificado exitosamente.")
            return

    print("No se encontró el profesor.")

# Función para eliminar un profesor existente
def eliminar_profesor():
    dni = input("Ingrese el número de DNI del profesor: ")

    profesores = leer_datos(PROFESORES_FILE)
    profesores_nuevos = []
    profesor_eliminado = False

    for profesor in profesores:
        if profesor[0] == dni:
            profesor_eliminado = True
        else:
            profesores_nuevos.append(profesor)

    if profesor_eliminado:
        escribir_datos(PROFESORES_FILE, profesores_nuevos)
        print("Profesor eliminado exitosamente.")
    else:
        print("No se encontró el profesor.")

# Función para ver todas las asignaturas
def ver_todas_las_asignaturas():
    asignaturas = leer_datos(ASIGNATURAS_FILE)
    print("\nAsignaturas")
    print("-----------")
    for asignatura in asignaturas:
        print(f"ID: {asignatura[0]}")
        print(f"Nombre: {asignatura[1]}")
        print("----------------------")

# Función para crear una nueva asignatura
def crear_asignatura():
    id_asignatura = input("Ingrese el ID de la asignatura: ")
    nombre_asignatura = input("Ingrese el nombre de la asignatura: ")

    asignaturas = leer_datos(ASIGNATURAS_FILE)
    asignaturas.append([id_asignatura, nombre_asignatura])
    escribir_datos(ASIGNATURAS_FILE, asignaturas)
    print("Asignatura creada exitosamente.")

# Función para modificar una asignatura existente
def modificar_asignatura():
    id_asignatura = input("Ingrese el ID de la asignatura: ")

    asignaturas = leer_datos(ASIGNATURAS_FILE)
    for asignatura in asignaturas:
        if asignatura[0] == id_asignatura:
            nombre_asignatura = input("Ingrese el nuevo nombre de la asignatura: ")

            asignatura[1] = nombre_asignatura

            escribir_datos(ASIGNATURAS_FILE, asignaturas)
            print("Asignatura modificada exitosamente.")
            return

    print("No se encontró la asignatura.")

# Función para eliminar una asignatura existente
def eliminar_asignatura():
    id_asignatura = input("Ingrese el ID de la asignatura: ")

    asignaturas = leer_datos(ASIGNATURAS_FILE)
    asignaturas_nuevas = []
    asignatura_eliminada = False

    for asignatura in asignaturas:
        if asignatura[0] == id_asignatura:
            asignatura_eliminada = True
        else:
            asignaturas_nuevas.append(asignatura)

    if asignatura_eliminada:
        escribir_datos(ASIGNATURAS_FILE, asignaturas_nuevas)
        print("Asignatura eliminada exitosamente.")
    else:
        print("No se encontró la asignatura.")

# Función para leer los datos de un archivo CSV
def leer_datos(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        reader = csv.reader(archivo)
        datos = list(reader)
    return datos

# Función para escribir los datos en un archivo CSV
def escribir_datos(nombre_archivo, datos):
    with open(nombre_archivo, "w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerows(datos)

# Función para validar si una calificación es válida
def calificacion_valida(calificacion):
    try:
        calificacion = float(calificacion)
        if 0 <= calificacion <= 10:
            return True
        else:
            return False
    except ValueError:
        return False

# Función principal del programa
def main():
    while True:
        print("Sistema de Calificaciones")
        print("------------------------")
        print("1. Iniciar sesión como alumno")
        print("2. Iniciar sesión como profesor")
        print("3. Iniciar sesión como administrador")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            iniciar_sesion_alumno()
        elif opcion == "2":
            iniciar_sesion_profesor()
        elif opcion == "3":
            iniciar_sesion_administrador()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
