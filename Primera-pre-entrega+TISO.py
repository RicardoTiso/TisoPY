#declaro las variables:
usuarios={}
usuario_nuevo=usuarios
salir = 5 #cree esta variable condicion para variar, donde el while se cumple hasta que el usuario ingrese 4.

#funciones que voy a utilizar:

def volver_menu(volver):#se va a quedar en este bucle hasta que escriba la 'n' bien.
    if  volver== "n":
        print("volviendo al menu...")
    else:
        volver=input("desea continuar? s/n: ")
        volver_menu(volver)

def  volviendo_menu(volver):#se va a quedar en este bucle hasta que escriba la 'm' bien.     
    while volver!='m':
        volver=input("Escriba 'm' para volver al menu: ")
    else:
        volver='n'
        volver_menu(volver)

def agrega_usuario(nombre,contraseña):#funcion que agrega un usuario y su contraseña al diccionario.
    usuario_nuevo[nombre]=contraseña
    volver=input("desea agregar un nuevo usuario? s/n: ")
    if volver=="n":
        volver_menu(volver)
    elif volver=="s":
        print("Ingrese un nuevo usuario")
        nombre=input("Ingrese nombre de usuario: ")
        contraseña=input("Ingrese contraseña: ")
        agrega_usuario(nombre,contraseña)
    
def comprobar_usuario(nombre_3):#funcion que comprueba si el usuario existe y si la contraseña es correcta.
    for n3 in usuarios:
        if n3 == nombre_3:
            contraseña_3=input("Ingrese contraseña: ")
            if contraseña_3 == usuarios[n3]:
                print("Usuario registrado correctamente.")
                volver='n'
                volviendo_menu(volver)
                break
            else:
                print("La contraseña es incorrecta, volviendo al menu...")  
                break 
    else:
        print("El usuario no existe.")
        nombre_3=input("ingrese un usuario existente o 'n' para no continuar: ")
        if  nombre_3== "n":
            print("volviendo al menu...")
        else:
            comprobar_usuario(nombre_3)

def menu(opcion):#funcion que muestra el menu y las opciones.
    if opcion == "1": #aca voy agregando los usuarios dentro del dic usuarios.
        print("Ingrese un nuevo usuario")
        nombre=input("Ingrese nombre de usuario: ")
        contraseña=input("Ingrese contraseña: ")
        agrega_usuario(nombre,contraseña)
    elif opcion == "2": #aca voy a mostrar solo los nombres de los usuarios registrados.
        print("Los usuarios registrados son: ")
        n=0
        for x in usuarios:
            n+=1
            print(n,"-",x)
        volver='n'
        volviendo_menu(volver)
        
    elif opcion == "3": #aca voy a comprobar si el usuario y contraseña que ingrese son correctos.
        print("Compruebe un usuario y contraseña: ")
        nombre_3=input("Ingrese nombre de usuario: ")
        while(True):
            comprobar_usuario(nombre_3)
            break       
    elif opcion == "4":
        opcion=4
    else:
        opcion=5
        print("El valor ingresado es incorrecto.")
    return opcion

#aca comienza la ejecucion de mi programa, ejecutandose hasta que salir sea distinto a '4'
while salir!=4: #aca voy a crear un menu para que el usuario pueda elegir que quiere hacer.
    opcion=input("""Bienvenido Administrador...
    Este es un programa para registrar usuarios y visualizar la base de datos de usuarios.

        1 - Ingrese un nuevo usuario.
        2 - Ver los usuarios registrados.
        3 - Compruebe su usuario y contraseña.
        4 - Salir del programa.

    Ingrese el numero de la opcion: """)
    salir = menu(opcion)
else:
    print("Gracias por utilizar el programa...")



