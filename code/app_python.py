import os
list_personal =[]

def fnt_limpiar():
    os.system('cls')
    print('Autor: Santiago Salas')
    print('Politecnico Jaime Isaza Cadavid\n')
    
def fnt_agregar():
    fnt_limpiar()
    print('\n<<< REGISTRAR PERSONA >>>\n')
    id = input('ID: ')
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    contacto = input('Contacto: ')
    correo = input('Correo: ')
    r = id + ' ' + nombre + ' ' +apellido + ' ' + contacto + ' ' + correo
    list_personal.append(r)
    input('\nPersona registrada con exito, <ENTER> para continuar')

def fnt_mostrar():
    fnt_limpiar()
    print('\n<<< LISTA DE PERSONAS >>>\n')
    for i in list_personal:
        print(i)
        print('\n')
    input('\nFin del registro <ENTER> para continuar') 
    
def fnt_menu(m):
    while m== True:
        opcion = input('<<Menu Principal>>\n1. AGREGAR\n2. MOSTRAR\n3. SALIR\n-> ')
        if opcion == '3':
            m = False  
        elif opcion == '1':
            fnt_agregar()
        elif opcion == '2':
            fnt_mostrar()
        else:
            print('\nOpcion no valida, <ENTER> para continuar')
            input()
            fnt_limpiar()            
fnt_menu(True)
    