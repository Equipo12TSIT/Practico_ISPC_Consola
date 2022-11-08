import modelo1

from tabulate import tabulate


def ListarAlbumesPorArtistas():
    con = modelo1.conectar()
    print('\n|COD. ÁLBUM|\t','| NOMBRE |\t','|       INTERPRETE       |\t','|  GENERO  |','| DISCOGRAFICA |','| PRECIO |','|CANTIDAD|','|FORMATO|')
    listado = con.ListarAlbumes()    
    print(tabulate(listado, tablefmt='fancy_grid'))
    input("Presione ENTER para continuar")

def ListarAlbumPorNombre():
    con = modelo1.conectar()
    nombre = input("\nIngrese datos del álbum que esta buscando:")
    listado = con.BuscarPorNombreDeAlbum(nombre)
    print("\n|  Álbumes Disponibles: |\n")  
    print('\n|COD. ÁLBUM|\t','| NOMBRE |\t','|       INTERPRETE       |\t','|  GENERO  |','| DISCOGRAFICA |','| PRECIO |','|CANTIDAD|','|FORMATO|')  
    print(tabulate(listado, tablefmt='fancy_grid'))
    input("\nPresione ENTER para continuar\n") 

def ListarAlbumPorGenero():
    con = modelo1.conectar()
    id_genero = input("\nIngrese ID del Género que esta buscando:")
    listado = con.BuscarPorGenero(id_genero)
    print("\n|  Álbumes Disponibles: |\n")  
    print('\n|COD. ÁLBUM|\t','| NOMBRE |\t','|       INTERPRETE       |\t','|  GENERO  |','| DISCOGRAFICA |','| PRECIO |','|CANTIDAD|','|FORMATO|')  
    print(tabulate(listado, tablefmt='fancy_grid'))
    input("\nPresione ENTER para continuar\n") 

def InsertAlbum():
    cod_album = int(input("\nIngrese el código del nuevo Álbum: "))
    nombre = input("Ingrese el nombre del álbum: ")

    con = modelo1.conectar()

    print("\n|  Intérpretes Disponibles  |")
    
    print(tabulate(con.ListarInterprete() , tablefmt='fancy_grid'))    
    id_interprete = int(input("\nIngrese el ID del Intérprete: "))
    
    print("\n|   Género  |")
    con = modelo1.conectar()     
       
    print(tabulate(con.ListarPorGenero() , tablefmt='fancy_grid'))
    id_genero = int(input("\nIngrese el ID del Género: "))

    cant_temas = int(input("\nIngrese la cantidad de temas: "))

    print("\n|  Discográfica  |")
    con = modelo1.conectar()
    print(tabulate(con.ListarDiscografica(), tablefmt='fancy_grid'))
       
    id_discografica = int(input("\nIngrese el ID de la discografica: "))

    print("\n|  Formato  |")
    con = modelo1.conectar()
    print(tabulate(con.ListarFormato(), tablefmt='fancy_grid'))
               
    id_formato = int(input("\nIngrese el ID del formato: "))
    fec_lanzamiento = input("\nIngrese la Fecha de Lanzamiento (aaaa-mm-dd): ")
    precio = float(input("\nIngrese el precio: "))
    cantidad = int(input("\nIngrese cantidad disponible de este álbum: "))
    caratula = input("\nIngrese la dirección web de la Carátula: ")

    nuevoAlbum = modelo1.album(0,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula)
    con = modelo1.conectar()
    con.InsertarAlbum(nuevoAlbum)
    input("\nPresione ENTER para continuar\n")

def BorrarALbum():
    print("\n|  Código: primer número  |\n")
    con = modelo1.conectar()
    print(tabulate(con.ListarAlbumes(), tablefmt='fancy_grid'))
       
    con = modelo1.conectar()
    cod_album = int(input("\n Elegir el código del Álbum que va a eliminar: "))    
    con.EliminarAlbum(cod_album)
    input("\nPresione ENTER para continuar\n")

def ModificarAbum():
    print("\n |  Lista de Álbumes para modificar  |\n")
    con = modelo1.conectar()
    print(tabulate(con.ListarAlbum(), tablefmt='fancy_grid'))
     
    Id_album = input("\nIngrese id del álbum que quiere modificar: ")
    Cod_album = int(input("Ingrese nuevo código de álbum: "))     
    Nombre = input("Ingrese nuevo nombre del álbum: ")
    con = modelo1.conectar()
    print(tabulate(con.ListarInterprete(), tablefmt='fancy_grid'))
        
    Id_interprete = int(input("\nIngrese nuevo id de interprete: "))
    con = modelo1.conectar()
    print(tabulate(con.ListarPorGenero(), tablefmt='fancy_grid'))
        
    Id_genero = int(input("\nIngrese genero del álbum: "))
    Cant_temas = int(input("Ingrese cantidad de temas del álbum: "))
    con = modelo1.conectar()
    print(tabulate(con.ListarDiscografica(), tablefmt='fancy_grid'))
        
    Id_discografica = int(input("\nIngrese nueva discografica: "))
    con = modelo1.conectar()
    print(tabulate(con.ListarFormato(), tablefmt='fancy_grid'))
       
    Id_formato = int(input("\nIngrese nuevo formato: "))
    Fec_lanzamiento = input("Ingrese fecha de lanzamiento/aaaa-mm-dd: ")
    Precio = int(input("Ingrese el precio: "))
    Cantidad = int(input("Ingrese cantidad de/u: "))
    Caratula = ''

    modi = modelo1.album(0,0,'',0,0,0,0,0,'',0,0,'')
    modi.setId_album(Id_album)
    modi.setCod_album(Cod_album)
    modi.setNombre(Nombre)
    modi.setId_interprete(Id_interprete)
    modi.setId_genero(Id_genero)
    modi.setCant_temas(Cant_temas)
    modi.setId_discografica(Id_discografica)
    modi.setId_formato(Id_formato)
    modi.setFec_lanzamiento(Fec_lanzamiento)
    modi.setPrecio(Precio)
    modi.setCantidad(Cantidad)
    modi.setCaratula(Caratula) 

    con = modelo1.conectar()
    con.ModificarAlbum(modi)
    input("\nPresione ENTER para continuar\n")

def InsertInterprete():
    nombre = input("Ingrese el nombre del interprete: ")
    apellido = input("Ingrese el apellido del interprete: ")
    nacionalidad = input("Ingrese nacionalidad: ")
    foto = ''
     
    nuevoInterprete = modelo1.Interprete(0,nombre,apellido,nacionalidad,foto) 
    con = modelo1.conectar()
    con.InsertarInterprete(nuevoInterprete)

    print("\n |  Intérpretes Disponibles  |\n")
    con=modelo1.conectar()
    print(tabulate(con.ListarInterprete(), tablefmt='fancy_grid'))   
    input("\nPresione ENTER para continuar\n")    
       
def BorrarInterprete():
    print("\n| Id.Interprete: primer número |\n")
    con = modelo1.conectar()
    print(tabulate(con.ListarInterprete(), tablefmt='fancy_grid'))         
    
    id = input("\nIngrese el id del interprete que va a eliminar:  ")
    Inter = modelo1.Interprete(id,'','','','')
    con = modelo1.conectar()   
    con.EliminarInterprete(Inter)
    con = modelo1.conectar()
    print(tabulate(con.ListarInterprete(), tablefmt='fancy_grid'))        
    input("\nPresione ENTER para continuar\n")

def ModificInterprete():
    print("\n | Lista de Interpretes para modificar. |\n")
    con = modelo1.conectar()
    print(tabulate(con.ListarInterprete(), tablefmt='fancy_grid'))       

    interp = input("\nIngrese id del interprete que quiere modificar: ")
    nombre = input("Ingrese nuevo nombre del interprete: ")    
    apellido = input("Ingrese nuevo apellido del interprete: ")
    nacionalidad = input("Ingrese nueva nacionalidad: ")
    foto = ''
   
    con = modelo1.conectar()       
    modi = modelo1.Interprete('','','','','')
    modi.setId_Interprete(interp)
    modi.setNombre(nombre)
    modi.setApellido(apellido)
    modi.setNacionalidad(nacionalidad)
    modi.setFoto(foto)
       
    con = modelo1.conectar()
    con.ModificarInterprete(modi)
    con = modelo1.conectar()
    print(tabulate(con.ListarInterprete(), tablefmt='fancy_grid'))       
    input("\nPresione ENTER para continuar\n")

def listInterprete():
    con = modelo1.conectar()    
    print("\n|  Lista de interpretes. |\n")
    print(tabulate(con.ListarInterprete(), tablefmt='fancy_grid'))
        

def InsertGenero():
    print("\n|  Generos disponibles  | \n")    
    con=modelo1.conectar()
    print(tabulate(con.ListarPorGenero(), tablefmt='fancy_grid'))
       
    nombre = input("\nIngrese el nombre del nuevo genero: ")
    nuevoGenero = modelo1.Genero(0,nombre) 
    con = modelo1.conectar()
    con.InsertarGenero(nuevoGenero)

    print("\n |  Generos Disponibles  |\n")
    con=modelo1.conectar()
    print(tabulate(con.ListarPorGenero(), tablefmt='fancy_grid'))
        
    input("\nPresione ENTER para continuar\n") 

def BorrarGenero():
    print("\n| Generos disponibles. |\n")
    con = modelo1.conectar()
    print(tabulate(con.ListarPorGenero(), tablefmt='fancy_grid'))        
    
    id = input("\nIngrese id del genero que quiere eliminar:  ")
    gene = modelo1.Genero(id,'')
    con = modelo1.conectar()   
    con.EliminarGenero(gene)
    print("\n| Generos disponibles. |\n")
    con = modelo1.conectar()
    print(tabulate(con.ListarPorGenero(), tablefmt='fancy_grid'))
       
    input("\nPresione ENTER para continuar\n")

def ModificGenero():
    print("\n | Lista de generos para modificar. |\n")
    con = modelo1.conectar()
    print(tabulate(con.ListarPorGenero(), tablefmt='fancy_grid'))       

    idgene = input("\nIngrese id del genero que quiere modificar: ")
    nombre = input("\nIngrese nuevo nombre del genero: ")    
 
    con = modelo1.conectar()       
    modi = modelo1.Genero(idgene,'')
    modi.setId_genero(idgene)
    modi.setNombre(nombre)
          
    con = modelo1.conectar()
    con.ModificarGenero(modi)
    con = modelo1.conectar()
    print(tabulate(con.ListarPorGenero(), tablefmt='fancy_grid'))
       
    input("\nPresione ENTER para continuar\n")               
  
def listGenero():
    print("\n| Generos disponibles |\n")
    con = modelo1.conectar()
    print(tabulate(con.ListarPorGenero(), tablefmt='fancy_grid'))
        
    input("\nPresione ENTER para continuar\n")

def InsertDiscografica():
    print("\n| Discograficas disponibles | \n")    
    con=modelo1.conectar()
    print(tabulate(con.ListarDiscografica(), tablefmt='fancy_grid'))
        
    nombre = input("\nIngrese el nombre de la nueva discografica: ")
    nuevaDisc = modelo1.Discografica(0,nombre) 
    con = modelo1.conectar()
    con.InsertarDiscografica(nuevaDisc)

    print("\n |  Discograficas disponibles  |\n")
    con=modelo1.conectar()
    print(tabulate(con.ListarDiscografica(), tablefmt='fancy_grid'))
       
    input("\nPresione ENTER para continuar\n") 

def BorrarDiscografica():
    print("\n| Discograficas disponibles |\n")
    con = modelo1.conectar()
    print(tabulate(con.ListarDiscografica(), tablefmt='fancy_grid'))       
    
    id = input("\nIngrese el id de la discografica que quiere eliminar:  ")
    disco = modelo1.Discografica(id,'')
    con = modelo1.conectar()   
    con.EliminarDiscografica(disco)
    print("\n| Discograficas disponibles |\n")
    con = modelo1.conectar()
    print(tabulate(con.ListarDiscografica(), tablefmt='fancy_grid'))
        
    input("\nPresione ENTER para continuar\n") 

def ModificDiscografica():
    print("\n | Lista de discograficas para modificar |\n")
    con = modelo1.conectar()
    print(tabulate(con.ListarDiscografica(), tablefmt='fancy_grid'))       

    idisco = input("\nIngrese id del genero que quiere modificar: ")
    nombre = input("\nIngrese nuevo nombre del genero: ")    
 
    con = modelo1.conectar()       
    modi = modelo1.Discografica(idisco,'')
    modi.setId_discografica(idisco)
    modi.setNombre(nombre)
          
    con = modelo1.conectar()
    con.ModificarDiscografica(modi)
    con = modelo1.conectar()
    print(tabulate(con.ListarDiscografica(), tablefmt='fancy_grid'))
       
    input("\nPresione ENTER para continuar\n")         

def listDiscografica():
    print("\n| Discografica disponibles |\n")
    con = modelo1.conectar()
    print(tabulate(con.ListarDiscografica(), tablefmt='fancy_grid'))
        
    input("\nPresione ENTER para continuar\n")

def InsertFormato():
    print("\n| Formato disponibles | \n")    
    con=modelo1.conectar()
    print(tabulate(con.ListarFormato(), tablefmt='fancy_grid'))
        
    nombre = input("\nIngrese el nuevo tipo de formato: ")
    nuevoForma = modelo1.Formato(0,nombre) 
    con = modelo1.conectar()
    con.InsertarFormato(nuevoForma)

    print("\n |  Formatos disponibles  |\n")
    con=modelo1.conectar()
    print(tabulate(con.ListarFormato(), tablefmt='fancy_grid'))
       
    input("\nPresione ENTER para continuar\n")   

def BorrarFormato():
    print("\n| Formatos disponibles |\n")
    con = modelo1.conectar()
    print(tabulate(con.ListarFormato(), tablefmt='fancy_grid'))      
    
    id = input("\nIngrese el id del formato que quiere eliminar:  ")
    forma = modelo1.Formato(id,'')
    con = modelo1.conectar()   
    con.EliminarFormato(forma)
    print("\n| Formatos disponibles |\n")
    con = modelo1.conectar()
    print(tabulate(con.ListarFormato(), tablefmt='fancy_grid'))
        
    input("\nPresione ENTER para continuar\n") 

def ModificFormato():
    print("\n |  Lista de formatos para modificar  |\n")
    con = modelo1.conectar()
    print(tabulate(con.ListarFormato(), tablefmt='fancy_grid'))       

    iforma = input("\nIngrese id del formato que quiere modificar: ")
    nombre = input("\nIngrese nuevo formato: ")    
 
    con = modelo1.conectar()       
    modi = modelo1.Formato(iforma,'')
    modi.setId_formato(iforma)
    modi.setTipo(nombre)
          
    con = modelo1.conectar()
    con.ModificarFormato(modi)
    con = modelo1.conectar()
    print(tabulate(con.ListarFormato(), tablefmt='fancy_grid'))
       
    input("\nPresione ENTER para continuar\n") 

def listFormato():
    print("\n| Formatos disponibles |\n")
    con = modelo1.conectar()
    print(tabulate(con.ListarFormato(), tablefmt='fancy_grid'))
        
    input("\nPresione ENTER para continuar\n")

def InsertTema():
    titulo = input("\nIngrese el nuevo tema: ")
    duracion = input("\nDuración /formato hh:mm:ss: ")
    autor = input("\n Ingresar autor: ")
    compositor = input("\n Ingresar compositor: ")
    print("\n| Lista de Albumes | \n")
    con = modelo1.conectar()
    print(tabulate(con.ListarAlbum(), tablefmt='fancy_grid'))
       
    idalbum = input("\n Ingresar id del album: ") 
    print("\n| Lista de interpretes |\n")
    con = modelo1.conectar()
    print(tabulate(con.ListarInterprete(), tablefmt='fancy_grid'))
       
    idinterprete= input("\n Insertar id interprete: ")    
        
    nuevoTema = modelo1.Tema(0,titulo,duracion,autor,compositor,idalbum,idinterprete) 
    con = modelo1.conectar()
    con.InsertarTema(nuevoTema)

    print("\n |  Temas disponibles  |\n")
    con=modelo1.conectar()
    print(tabulate(con.ListarTema(), tablefmt='fancy_grid'))
      
    input("\nPresione ENTER para continuar\n") 

def BorrarTema():
    print("\n| Temas disponibles |\n")
    con = modelo1.conectar()
    print(tabulate(con.ListarTema(), tablefmt='fancy_grid'))        
    
    id = input("\nIngrese el id del tema que quiere eliminar:  ")
    tem = modelo1.Tema(id,'','','','','','')
    con = modelo1.conectar()   
    con.EliminarTema(tem)
    print("\n| Temas disponibles |\n")
    con = modelo1.conectar()
    print(tabulate(con.ListarTema(), tablefmt='fancy_grid'))
       
    input("\nPresione ENTER para continuar\n") 

def ModificTema():
    print("\n | Lista de temas para modificar |\n")
    con = modelo1.conectar()
    print(tabulate(con.ListarTema(), tablefmt='fancy_grid'))        

    id = input("\nIngrese id del tema que quiere modificar: ")
    titulo = input("\nIngrese nuevo titulo: ")    
    duracion = input("\nIngrese duración/formato hh:mm:ss:  ")
    autor = input ("\nIngrese nuevo autor: ")
    compositor = input("\nIngresar compositor: ")
    
    con = modelo1.conectar()       
    modi = modelo1.Tema(id,'','','','','','')
    modi.setTitulo(titulo)
    modi.setDuracion(duracion)
    modi.setAutor(autor)  
    modi.setCompositor(compositor)    
    con = modelo1.conectar()
    con.ModificarTema(modi)
    con = modelo1.conectar()
    print(tabulate(con.ListarTema(), tablefmt='fancy_grid'))
        
    input("\nPresione ENTER para continuar\n") 

def listTema():
    
    con=modelo1.conectar()
    id_album = input("\nIngrese ID del Album que esta buscando:")
    listado = con.ListarTema(id_album)
    print("\n|  Álbumes Disponibles: |\n")  
    print('\n|ID|\t','|          NOMBRE           |\t','|  DURACION  |\t','|     AUTOR     |','|     COMPOSITOR     |','| ID_ALBUM |','| INTERPRETE |')  
    print(tabulate(listado, tablefmt='fancy_grid'))
    input("\nPresione ENTER para continuar\n") 



            


#--------------------------------------------------------------------------



