import controlador1
from tabulate import tabulate
from colorama import init,Fore, Back, Style
init()

while True:
            
    print(Back.BLUE+Fore.WHITE+"""
  _____           ____                 ___             _        __  __           ____    _    ____           _     
 |  ___|   ___   |  _ \   _ __ ___    / _ \   ___     / \      |  \/  |  _   _  / ___|  (_)  / ___|   __ _  | |    
 | |_     / _ \  | |_) | | '_ ` _ \  | | | | / __|   / _ \     | |\/| | | | | | \___ \  | | | |      / _` | | |    
 |  _|   | (_) | |  _ <  | | | | | | | |_| | \__ \  / ___ \    | |  | | | |_| |  ___) | | | | |___  | (_| | | |___ 
 |_|      \___/  |_| \_\ |_| |_| |_|  \___/  |___/ /_/   \_\   |_|  |_|  \__,_| |____/  |_|  \____|  \__,_| |_____|
                                                                                                                   """+Back.RESET+Fore.RESET)
    
    print('')  
    print(Fore.BLUE+"\U0001F4FB\U0001F3B5 |  MENÚ PRINCIPAL  |\U0001F3B8\U0001F3B5\n")
    print("1 - ALTAS \U0001F4E4")            
    print("2 - BAJAS  \U0001F4E5 ")
    print("3 - MODIFICACION \U0001FA93")
    print("4 - LISTADOS \U0001F4F0")
    print("5 - BUSCAR POR INICIAL ALBUM \U0001F4D1")
    print("\n")
    
    
    try:
        opcion = int(input("Ingrese su opción:  "))
    except:
        continue
    if opcion == 1:
        print("""\n\t\t 1 - Alta de un ALBUM \U0001F4BD
                 2 - Alta de un INTERPRETE \U0001F9D1
                 3 - Alta de un GENERO \U0001F919
                 4 - Alta de una DISCOGRAFICA \U0001F3BC
                 5 - Alta de un nuevo FORMATO \U0001F4BE
                 6 - Alta de un TEMA \U0001F916 """) 
        try:                        
            opc = int(input("\nIngrese número de opción, que desea dar de ALTA: "))
        except:
            continue
        if opc == 1:
            controlador1.InsertAlbum() 
        elif opc == 2:
            controlador1.InsertInterprete()
        elif opc == 3:
            controlador1.InsertGenero()
        elif opc == 4:
            controlador1. InsertDiscografica()
        elif opc == 5:
            controlador1.InsertFormato()       
        elif opc == 6:
            controlador1.InsertTema()
        else:            
            print("¡Opción incorrecta!")
            continue
    elif opcion == 2:
        print("""\n\t\t 1 - Baja de un ALBUM \U0001F4BD
                 2 - Baja de un INTERPRETE \U0001F9D1
                 3 - Baja de un GENERO \U0001F919
                 4 - Baja de una DISCOGRAFICA \U0001F3BC
                 5 - Baja de un nuevo FORMATO \U0001F4BE
                 6 - Baja de un TEMA \U0001F916 """)
        try:
            opc = int(input("\nIngrese número de opción, que desea dar de BAJA: "))
        except:
            continue
        if opc == 1:
           controlador1.BorrarALbum()
        elif opc == 2:
            controlador1.BorrarInterprete()
        elif opc == 3:
            controlador1.BorrarGenero()
        elif opc == 4:
            controlador1.BorrarDiscografica() 
        elif opc == 5:
            controlador1.BorrarFormato()
        elif opc == 6:
            controlador1.BorrarTema()
        else:                 
            print("¡Opción incorrecta!  \U000026D4")
            continue
    elif opcion == 3:
        print("""\n\t\t 1 - Modificar un ALBUM \U0001F4BD
                 2 - Modificar un INTERPRETE \U0001F9D1
                 3 - Modificar un GENERO \U0001F919
                 4 - Modificar una DISCOGRAFICA \U0001F3BC
                 5 - Modificar un FORMATO \U0001F4BE
                 6 - Modificar un TEMA \U0001F916 """)
        try:         
            opc = int(input("\nIngrese número de opción, que desea MODIFICAR: ")) 
        except:
            continue    
        if opc == 1:
            controlador1.ModificarAbum()
        elif opc == 2:
            controlador1.ModificInterprete()
        elif opc == 3:
            controlador1.ModificGenero()
        elif opc == 4:
            controlador1.ModificDiscografica()  
        elif opc == 5:
            controlador1.ModificFormato()
        elif opc == 6:
            controlador1.ModificTema()
        else:
            print("¡Opción incorrecta!  \U000026D4")
            continue 
    elif opcion == 4:                         
        print("""\n\t\t 1 - Listado de ALBUMES por artista \U0001F4BD
                 2 - Listar INTERPRETES \U0001F9D1
                 3 - Listar GENEROS \U0001F919
                 4 - Listar DISCOGRAFICAS \U0001F3BC
                 5 - Listar FORMATOS \U0001F4BE
                 6 - Listar TEMAS \U0001F916 """)
        try:         
            opc = int(input("\nIngrese número de opción, que desea ver la LISTA:  "))
        except:
            continue
        if opc == 1:
            controlador1.ListarAlbumesPorArtistas()
        elif opc == 2:
            controlador1.listInterprete()
        elif opc == 3:
            controlador1.listGenero()
        elif opc == 4:
            controlador1.listDiscografica() 
        elif opc == 5:
            controlador1.listFormato() 
        elif opc == 6:
            controlador1.listTema()
        else:
            print("¡Opción incorrecta!  \U000026D4")
            continue
    elif opcion == 5:
        controlador1.ListarAlbumPorNombre()  
