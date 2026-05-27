"""
Script Principal: mi_gestor_tareas.py
Autor: [Alan Ramos]
Fecha: 26 de Mayo, 2026
Asignatura: [Algoritmos Y Programacion]
Descripción: Programa modular para la gestión de una lista de tareas pendientes
             (To-Do List) que implementa algoritmos recursivos, manejo de
             excepciones y estándares de documentación (Docstrings).
"""

def obtener_tareas():
    """
    Inicializa y retorna una lista de ejemplo con tareas predefinidas.
    
    Parameters:
        Ninguno.
        
    Returns:
        list: Una lista de diccionarios, donde cada diccionario representa una 
              tarea con las llaves 'descripcion' (str) y 'completada' (bool).
    """
    tareas_iniciales = [
        {"descripcion": "Estudiar el capítulo 11 de Trejos", "completada": False},
        {"descripcion": "Diseñar el diagrama de flujo del proyecto", "completada": True},
        {"descripcion": "Redactar el informe de buenas prácticas", "completada": False}
    ]
    return tareas_iniciales


def mostrar_tareas(lista_tareas):
    """
    Imprime en la consola la lista de tareas con un formato visual limpio.
    
    Muestra un [X] si la tarea está completada o un [ ] si está pendiente,
    junto con un número de índice para que el usuario pueda seleccionarla.
    
    Parameters:
        lista_tareas (list): La lista de diccionarios que contiene las tareas.
        
    Returns:
        None
    """
    print("\n" + "=" * 40)
    print("           LISTA DE TAREAS")
    print("=" * 40)
    
    if not lista_tareas:
        print("No hay tareas registradas en la lista.")
    else:
        for posicion, tarea in enumerate(lista_tareas, start=1):
            marca = "[X]" if tarea["completada"] else "[ ]"
            print(f"{posicion}. {marca} {tarea['descripcion']}")
            
    print("=" * 40)


def agregar_tarea(lista_tareas, descripcion):
    """
    Agrega una nueva tarea en estado pendiente a la lista actual.
    
    Parameters:
        lista_tareas (list): La lista de diccionarios de tareas actual.
        descripcion (str): El texto descriptivo de la nueva tarea.
        
    Returns:
        list: La lista de tareas modificada con el nuevo elemento integrado.
    """
    nueva_tarea = {
        "descripcion": descripcion,
        "completada": False  
    }
    lista_tareas.append(nueva_tarea)
    return lista_tareas


def marcar_completada(lista_tareas, posicion):
    """
    Modifica el estado de una tarea específica a completada (True).
    
    Utiliza un bloque try-except para atrapar errores de índice (IndexError) 
    en caso de que el usuario elija un número fuera del rango de la lista.
    
    Parameters:
        lista_tareas (list): La lista de diccionarios de tareas.
        posicion (int): El número de tarea seleccionado por el usuario (base 1).
        
    Returns:
        None: Modifica la lista directamente por referencia.
    """
    try:
        indice_real = posicion - 1
        
        if indice_real < 0:
            raise IndexError
            
        lista_tareas[indice_real]["completada"] = True
        print(f"\n[Éxito] La tarea #{posicion} ha sido marcada como completada.")
        
    except IndexError:
        print(f"\n[ERROR] La posición '{posicion}' no existe en la lista. Intente de nuevo.")


def contar_tareas_pendientes(lista_tareas, indice=0):
    """
    Calcula de forma RECURSIVA el número total de tareas que siguen pendientes.
    
    Parameters:
        lista_tareas (list): La lista de diccionarios de tareas.
        indice (int): Posición actual del recorrido analizado (por defecto 0).
        
    Returns:
        int: El total de tareas con el estado 'completada' en False.
    """
    if indice == len(lista_tareas):
        return 0
        
    tarea_actual = lista_tareas[indice]
    
    if not tarea_actual["completada"]:
        return 1 + contar_tareas_pendientes(lista_tareas, indice + 1)
    else:
        return 0 + contar_tareas_pendientes(lista_tareas, indice + 1)


def ejecutar_menu():
    """
    Controla el flujo principal de la aplicación mediante un menú interactivo.
    """
    mis_tareas = obtener_tareas()
    
    while True:
        print("\n--- GESTOR DE TAREAS (MENÚ PRINCIPAL) ---")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Marcar tarea como completada")
        print("4. Mostrar total de tareas pendientes")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            mostrar_tareas(mis_tareas)
            
        elif opcion == "2":
            nueva_desc = input("Ingrese la descripción de la tarea: ").strip()
            if nueva_desc:
                mis_tareas = agregar_tarea(mis_tareas, nueva_desc)
                print("\n[Éxito] Tarea agregada correctamente.")
            else:
                print("\n[Advertencia] La descripción no puede estar vacía.")
                
        elif opcion == "3":
            mostrar_tareas(mis_tareas)
            try:
                pos = int(input("Ingrese el número de la tarea a completar: "))
                marcar_completada(mis_tareas, pos)
            except ValueError:
                print("\n[ERROR] Por favor, ingrese un número entero válido.")
                
        elif opcion == "4":
            pendientes = contar_tareas_pendientes(mis_tareas)
            print(f"\n--> Total de tareas pendientes (calculado recursivamente): {pendientes}")
            
        elif opcion == "5":
            print("\nGracias por utilizar el gestor de tareas. ¡Hasta pronto!")
            break
        else:
            print("\n[Opción inválida] Por favor, elija un número entre 1 y 5.")

if __name__ == "__main__":
    ejecutar_menu()
