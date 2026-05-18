def mostrar_menu():
    print("\n" + "="*40)
    print(" SISTEMA DE GESTIÓN DE ESTUDIANTES (SGE)")
    print("="*40)
    print("1. Agregar estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Buscar estudiante por ID")
    print("4. Salir")
    print("-" * 40)

def agregar_estudiante(lista_estudiantes, contador):
    try:
        id_estudiante = int(input("Ingrese el ID del estudiante (solo números): "))
        nombre = input("Ingrese el nombre completo del estudiante: ")
        
        for est in lista_estudiantes:
            if est['id'] == id_estudiante:
                print("Error: Ya existe un estudiante con ese ID.")
                return contador
            
        nuevo_estudiante = {"id": id_estudiante, "nombre": nombre}
        lista_estudiantes.append(nuevo_estudiante)
        
        print(f"\n[ÉXITO] Estudiante '{nombre}' agregado correctamente.")
        return contador + 1 
    except ValueError:
        print("\n[ERROR] El ID debe ser un valor numérico entero.")
        return contador

def mostrar_estudiantes(lista_estudiantes, contador):
    print("\n--- LISTA DE ESTUDIANTES ---")
    print(f"Total de registros: {contador}")

    if contador == 0:
        print("No hay estudiantes registrados en el sistema.")
    else:
        for est in lista_estudiantes:
            print(f"ID: {est['id']} | Nombre: {est['nombre']}")

def buscar_estudiante(lista_estudiantes):
    try:
        id_buscar = int(input("Ingrese el ID del estudiante a buscar: "))
        encontrado = False 
        
        for est in lista_estudiantes:
            if est['id'] == id_buscar:
                print(f"\n[ENCONTRADO] ID: {est['id']} | Nombre: {est['nombre']}")
                encontrado = True
                break
                
        if not encontrado:
            print(f"\n[NO ENCONTRADO] No existe ningún estudiante con el ID {id_buscar}.")
    except ValueError:
        print("\n[ERROR] El ID a buscar debe ser un valor numérico.")

def main():
    estudiantes = [] 
    total_estudiantes = 0 
    bandera_salir = False 
    
    
    while not bandera_salir:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")
        
        
        if opcion == '1':
            total_estudiantes = agregar_estudiante(estudiantes, total_estudiantes)
        elif opcion == '2':
            mostrar_estudiantes(estudiantes, total_estudiantes)
        elif opcion == '3':
            buscar_estudiante(estudiantes)
        elif opcion == '4':
            print("\nGuardando datos y cerrando el sistema. ¡Hasta pronto!")
            bandera_salir = True 
        else:
            print("\n[ERROR] Opción no válida. Ingrese un número del 1 al 4.")

if __name__ == "__main__":
    main()
