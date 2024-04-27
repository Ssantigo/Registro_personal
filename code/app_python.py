import os
list_personal =[]

def fnt_limpiar():
    os.system('cls')
    print('Autor: Santiago Salas')
    print('Politecnico Jaime Isaza Cadavid\n')
    
def fnt_agregar():
    fnt_limpiar
    print('\n<<< REGISTRAR PERSONA >>>\n')
    id = input('ID: ')
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    contacto = input('Contacto: ')
    correo = input('Correo: ')
    r = id + ' ' + nombre + ' ' +apellido + ' ' + contacto + ' ' + correo
    list_personal.append(r)
    input('Persona registrada con exito, <ENTER> para continuar') 
    
def fnt_menu(m):
    while m== True:
        opcion = input('<<Menu Principal>>\n1. AGREGAR\n2. MOSTRAR\n3. SALIR\n-> ')
        if opcion == '3':
            m = False  
        elif opcion == '1':
            fnt_agregar()
                 
fnt_menu(True)
    