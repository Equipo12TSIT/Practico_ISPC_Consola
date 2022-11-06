import mysql.connector

class conectar:
        def __init__(self):
          try:
               self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'root',
                db = 'disqueria' 
               )
        
          except mysql.connector.Error as descrpcionError:
                print('No se conecto', descrpcionError)


        def EliminarAlbum (self, cod_album):
            if self.conexion.is_connected():
                try:
                    cursor1 = self.conexion.cursor()
                    sentenciaSQL = 'DELETE from album WHERE cod_album = %s'
                    data = (cod_album,)
                    cursor1.execute(sentenciaSQL, data)
                    self.conexion.commit()
                    self.conexion.close()
                    print('\nEl Album se borro correctamente \U0001F641')

                except mysql.connector.Error as descripcionError:                   
                     print('No se conecto', descripcionError)

        def InsertarAlbum (self, album):
             if self.conexion.is_connected():
               try:
                  cursor1 = self.conexion.cursor()
                  sentenciaSQL = '''Insert into album values (null,%s,%s,%s,%s,%s,%s,%s,
                                                            %s,%s,%s,%s)'''
                  data = (album.getCod_album(),
                  album.getNombre(),
                  album.getId_interprete(),
                  album.getId_genero(),
                  album.getCant_temas(),
                  album.getId_discografica(),
                  album.getId_formato(),
                  album.getFec_lanzamiento(),
                  album.getPrecio(),
                  album.getCantidad(),
                  album.getCaratula())
                                    
                  cursor1.execute(sentenciaSQL, data)
                  self.conexion.commit()
                  self.conexion.close()
                  print('\nAlbum insertado correctamente \U00002705')

               except mysql.connector.Error as descripcionError:  
                     print('No se conecto', descripcionError) 

        def ModificarAlbum (self, album):
             if self.conexion.is_connected():
                try:
                    cursor1 = self.conexion.cursor()
                    sentenciaSQL = '''UPDATE album SET cod_album=%s,nombre=%s,id_interprete=%s, 
                             id_genero=%s,cant_temas=%s,id_discografica=%s,id_formato=%s,
                             fec_lanzamiento=%s,precio=%s,cantidad=%s,
                             caratula=%s WHERE id_album=%s'''
                
                    data = (album.getCod_album(),
                        album.getNombre(),
                        album.getId_interprete(),
                        album.getId_genero(),
                        album.getCant_temas(),
                        album.getId_discografica(),
                        album.getId_formato(),
                        album.getFec_lanzamiento(),
                        album.getPrecio(),
                        album.getCantidad(),
                        album.getCaratula(),
                        album.getId_album(),)
                                      
                    cursor1.execute(sentenciaSQL, data)
                    self.conexion.commit()
                    self.conexion.close()
                    print('\nEl Album se modifico correctamente \U0001F60E \U00002705')
                    
                except mysql.connector.Error as descripcionError:                   
                        print('No se conecto', descripcionError)

        def ListarAlbumes(self):
             if self.conexion.is_connected():
                try:
                     cursor1 = self.conexion.cursor()
                     sentenciaSQL = '''SELECT cod_album, album.nombre, interprete.nombre,
                                    interprete.apellido, genero.nombre, discografica.nombre,
                                    precio, cantidad, formato.tipo FROM album, interprete,
                                    discografica,formato,genero
                                    WHERE album.id_interprete = interprete.id_interprete
                                    AND album.id_discografica = discografica.id_discografica 
                                    AND album.id_formato = formato.id_formato 
                                    AND album.id_genero = genero.id_genero 
                                    ORDER By interprete.apellido desc'''
                     cursor1.execute(sentenciaSQL)
                     resultados = cursor1.fetchall()
                     self.conexion.close()
                     return resultados

                except mysql.connector.Error as descripcionError:                   
                     print('No se conecto', descripcionError) 

        def ListarAlbum(self):
            if self.conexion.is_connected():
                try:
                    cursor1 = self.conexion.cursor()
                    sentenciaSQL = 'SELECT * from album;'
                    cursor1.execute(sentenciaSQL)
                    resultados = cursor1.fetchall()
                    self.conexion.close()
                    return resultados
                except mysql.connector.Error as descripcionError: 
                         print('No se conecto', descripcionError) 

        def BuscarPorNombreDeAlbum(self, nombre):
            if self.conexion.is_connected():
                try:
                   cursor1 = self.conexion.cursor()
                   sentenciaSQL = """SELECT nombre FROM album WHERE nombre LIKE %s"%"; """                        
                   data = (nombre,)
                   cursor1.execute(sentenciaSQL, data)
                   resultados = cursor1.fetchall()
                   self.conexion.close()
                   return resultados

                except mysql.connector.Error as descripcionError:                   
                      print('No se conecto', descripcionError) 


        def ListarPorGenero (self):
            if self.conexion.is_connected(): 
                try:
                    cursor1 = self.conexion.cursor()
                    senteciaSQL = "SELECT * from genero"                             
                    cursor1.execute(senteciaSQL)
                    resultados = cursor1.fetchall()
                    self.conexion.close()
                    return resultados                          
                except mysql.connector.Error as descripcionError:                   
                      print('No se conecto', descripcionError)

        def InsertarGenero(self, Genero):
            if self.conexion.is_connected():
                try:
                    cursor1 = self.conexion.cursor()
                    sentenciaSQL = "INSERT into genero values(null,%s)"

                    data = (Genero.getNombre(),)
                    cursor1.execute(sentenciaSQL,data)
                    self.conexion.commit()
                    self.conexion.close()
                    print("\nGénero insertado correctamente \U0001F600 \U00002705")

                except mysql.connector.Error as descripcionError:
                    print("¡No se conectó!",descripcionError) 

        def EliminarGenero (self, Genero):
            if self.conexion.is_connected():
                try:
                    cursor1 = self.conexion.cursor()
                    sentenciaSQL = 'DELETE from genero WHERE id_genero = %s'
                    data = (Genero.getId_genero(),)
                    cursor1.execute(sentenciaSQL, data)
                    self.conexion.commit()
                    self.conexion.close()
                    print('\nEl genero se borro correctamente \U0001F641')

                except mysql.connector.Error as descripcionError:                   
                     print('No se conecto', descripcionError)  

        def ModificarGenero (self, Genero):
            if self.conexion.is_connected():
                try:
                    cursor1 = self.conexion.cursor()
                    sentenciaSQL = "UPDATE genero SET nombre=%s WHERE id_genero=%s;"
                
                    data = (Genero.getNombre(), Genero.getId_genero())
                                      
                    cursor1.execute(sentenciaSQL, data)
                    self.conexion.commit()
                    self.conexion.close()
                    print('\nEl genero se modifico correctamente \U0001F60E \U00002705')

                except mysql.connector.Error as descripcionError:                   
                        print('No se conecto', descripcionError) 

        def EliminarInterprete (self, Interprete):
            if self.conexion.is_connected():
                try:
                    cursor1 = self.conexion.cursor()
                    sentenciaSQL = 'DELETE from interprete WHERE id_interprete = %s'
                    data = (Interprete.getId_Interprete(),)
                    cursor1.execute(sentenciaSQL, data)
                    self.conexion.commit()
                    self.conexion.close()
                    print('\nEl Interprete se borro correctamente \U0001F641')

                except mysql.connector.Error as descripcionError:                   
                     print('No se conecto', descripcionError)  
        
        def InsertarInterprete(self, Interprete):
             if self.conexion.is_connected():
                try:
                    cursor1 = self.conexion.cursor()
                    sentenciaSQL = "INSERT into interprete values(null,%s,%s,%s,%s)"
                    data = (Interprete.getNombre(), Interprete.getApellido(),
                            Interprete.getNacionalidad(),Interprete.getFoto())
                    cursor1.execute(sentenciaSQL,data)
                    self.conexion.commit()
                    self.conexion.close()
                    print("\nInterprete insertado correctamente \U0001F600 \U00002705 ")
                except mysql.connector.Error as descripcionError:
                     print("¡No se conectó!",descripcionError) 
                
        def ModificarInterprete (self, Interprete):
             if self.conexion.is_connected():
                try:
                    cursor1 = self.conexion.cursor()
                    sentenciaSQL = '''UPDATE interprete SET nombre=%s,apellido=%s, 
                                   nacionalidad=%s,foto=%s WHERE id_interprete=%s'''
                
                    data = (Interprete.getNombre(), Interprete.getApellido(), Interprete.getNacionalidad(),
                            Interprete.getFoto(),Interprete.getId_Interprete(),)
                                      
                    cursor1.execute(sentenciaSQL, data)
                    self.conexion.commit()
                    self.conexion.close()
                    print('\nEl Interprete se modifico correctamente \U0001F60E')

                except mysql.connector.Error as descripcionError:                   
                        print('No se conecto', descripcionError) 

        def InsertarDiscografica(self,Discografica):
            if self.conexion.is_connected():
                try:
                    cursor1 = self.conexion.cursor()
                    sentenciaSQL = "INSERT into discografica values(null,%s)"

                    data = (Discografica.getNombre(),)

                    cursor1.execute(sentenciaSQL,data)

                    self.conexion.commit()
                    self.conexion.close()
                    print("\nDiscografica insertada correctamente \U0001F600 \U00002705")

                except mysql.connector.Error as descripcionError:
                     print("¡No se conectó!",descripcionError)  

        def EliminarDiscografica (self, Discografica):
            if self.conexion.is_connected():
                try:
                    cursor1 = self.conexion.cursor()
                    sentenciaSQL = 'DELETE from discografica WHERE id_discografica = %s'
                    data = (Discografica.getId_discografica(),)
                    cursor1.execute(sentenciaSQL, data)
                    self.conexion.commit()
                    self.conexion.close()
                    print('\nLa discografica se borro correctamente \U0001F641')

                except mysql.connector.Error as descripcionError:                   
                     print('No se conecto', descripcionError)    

        def ModificarDiscografica (self, Discografica):
             if self.conexion.is_connected():
                try:
                    cursor1 = self.conexion.cursor()
                    sentenciaSQL = 'UPDATE discografica SET nombre=%s WHERE id_discografica=%s'
                
                    data = (Discografica.getNombre(), Discografica.getId_discografica(),)
                                      
                    cursor1.execute(sentenciaSQL, data)
                    self.conexion.commit()
                    self.conexion.close()
                    print('\nSe Modifico discografica correctamente \U0001F60E \U00002705')

                except mysql.connector.Error as descripcionError:                   
                        print('No se conecto', descripcionError)

        def InsertarFormato(self, Formato):
            if self.conexion.is_connected():
                try:
                    cursor1 = self.conexion.cursor()
                    sentenciaSQL = "INSERT into formato values(null,%s)"

                    data = (Formato.getTipo(),)

                    cursor1.execute(sentenciaSQL,data)

                    self.conexion.commit()
                    self.conexion.close()
                    print("\nFormato insertado correctamente \U0001F600 \U00002705")

                except mysql.connector.Error as descripcionError:
                     print("¡No se conectó!",descripcionError) 

        def EliminarFormato (self, Formato):
            if self.conexion.is_connected():
                try:
                    cursor1 = self.conexion.cursor()
                    sentenciaSQL = 'DELETE from formato WHERE id_formato = %s'
                    data = (Formato.getId_formato(),)
                    cursor1.execute(sentenciaSQL, data)
                    self.conexion.commit()
                    self.conexion.close()
                    print('\nEl formato se elimino correctamente \U0001F641')

                except mysql.connector.Error as descripcionError:                   
                     print('No se conecto', descripcionError) 

        def ModificarFormato (self, Formato):
             if self.conexion.is_connected():
                try:
                    cursor1 = self.conexion.cursor()
                    sentenciaSQL = 'UPDATE formato SET tipo=%s WHERE id_formato=%s'
                
                    data = (Formato.getTipo(), Formato.getId_formato(),)
                                      
                    cursor1.execute(sentenciaSQL, data)
                    self.conexion.commit()
                    self.conexion.close()
                    print('\nSe Modifico formato correctamente \U0001F60E \U00002705')

                except mysql.connector.Error as descripcionError:                   
                        print('No se conecto', descripcionError)                   

        def InsertarTema(self, Tema):
            if self.conexion.is_connected():
                try:
                    cursor1 = self.conexion.cursor()
                    sentenciaSQL = "INSERT into tema values(null,%s,%s,%s,%s,%s,%s)"

                    data = (Tema.getTitulo(), Tema.getDuracion(),Tema.getAutor(),
                          Tema.getCompositor(),Tema.getCod_album(),Tema.getId_interprete())

                    cursor1.execute(sentenciaSQL,data)

                    self.conexion.commit()
                    self.conexion.close()
                    print("\nTema insertado correctamente \U0001F600 \U00002705")

                except mysql.connector.Error as descripcionError:
                     print("¡No se conectó!",descripcionError) 

        def EliminarTema (self, Tema):
            if self.conexion.is_connected():
                try:
                    cursor1 = self.conexion.cursor()
                    sentenciaSQL = 'DELETE from tema WHERE id_tema = %s'
                    data = (Tema.getId_tema(),)
                    cursor1.execute(sentenciaSQL, data)
                    self.conexion.commit()
                    self.conexion.close()
                    print('\nEl tema se elimino correctamente \U0001F641')

                except mysql.connector.Error as descripcionError:                   
                     print('No se conecto', descripcionError)  

        def ModificarTema (self, Tema):
             if self.conexion.is_connected():
                try:
                    cursor1 = self.conexion.cursor()
                    sentenciaSQL = '''UPDATE tema SET titulo=%s, duracion=%s,autor=%s,
                                    compositor=%s WHERE id_tema=%s'''
                
                    data = (Tema.getTitulo(), Tema.getDuracion(), Tema.getAutor(),  
                            Tema.getCompositor(), Tema.getId_tema())       
                    cursor1.execute(sentenciaSQL, data)
                    self.conexion.commit()
                    self.conexion.close()
                    print('\n Modifico el tema correctamente \U0001F60E \U00002705')

                except mysql.connector.Error as descripcionError:                   
                        print('No se conecto', descripcionError) 

        def ListarInterprete(self):
            if self.conexion.is_connected():
                try:
                    cursor1 = self.conexion.cursor()
                    sentenciaSQL = "SELECT * from interprete"
                    cursor1.execute(sentenciaSQL)
                    resultados = cursor1.fetchall()
                    self.conexion.close()
                    return resultados                                                                                 
                except mysql.connector.Error as descripcionError:
                    print("¡No se conectó!",descripcionError)

        def ListarDiscografica(self):
              if self.conexion.is_connected():
                try:
                    cursor1 = self.conexion.cursor()
                    sentenciaSQL = "SELECT * from discografica"
                    cursor1.execute(sentenciaSQL)
                    resultados = cursor1.fetchall()
                    self.conexion.close()
                    return resultados
                except mysql.connector.Error as descripcionError:
                    print("¡No se conectó!",descripcionError) 

        def ListarFormato(self):
            if self.conexion.is_connected():
                try:
                    cursor1 = self.conexion.cursor()
                    sentenciaSQL = "SELECT * from formato"
                    cursor1.execute(sentenciaSQL)
                    resultados = cursor1.fetchall()
                    self.conexion.close()
                    return resultados
                except mysql.connector.Error as descripcionError:
                    print("¡No se conectó!",descripcionError) 

        def ListarTema(self):
            if self.conexion.is_connected():
                try:
                    cursor1 = self.conexion.cursor()
                    sentenciaSQL = "SELECT * from tema"
                    cursor1.execute(sentenciaSQL)
                    resultados = cursor1.fetchall()
                    self.conexion.close()
                    return resultados
                except mysql.connector.Error as descripcionError:
                     print("¡No se conectó!",descripcionError)                                  




                
#--------------------------------------------------------------
                     

class album:
      def __init__(self,id_album,cod_album,nombre,id_interprete,id_genero,
                  cant_temas,id_discografica,id_formato,fec_lanzamiento,
                  precio,cantidad,caratula):

          self.id_album = id_album
          self.cod_album = cod_album
          self.nombre = nombre
          self.id_interprete = id_interprete
          self.id_genero = id_genero                                                
          self.cant_temas = cant_temas
          self.id_discografica = id_discografica
          self.id_formato = id_formato
          self.fec_lanzamiento = fec_lanzamiento
          self.precio = precio
          self.cantidad = cantidad
          self.caratula = caratula

      def getId_album(self):
         return self.id_album
      def getCod_album(self):
         return self.cod_album
      def getNombre(self):
         return self.nombre
      def getId_interprete(self):
         return self.id_interprete
      def getId_genero(self):
         return self.id_genero
      def getCant_temas(self):
         return self.cant_temas
      def getId_discografica(self):
         return self.id_discografica
      def getId_formato(self):
          return self.id_formato
      def getFec_lanzamiento(self):
         return self.fec_lanzamiento
      def getPrecio(self):
         return self.precio
      def getCantidad(self):
         return self.cantidad
      def getCaratula(self):
         return self.caratula  
 
      def setId_album(self,id_album):
          self.id_album = id_album        
      def setCod_album(self,cod_album):
          self.cod_album = cod_album       
      def setNombre(self,nombre):
          self.nombre = nombre        
      def setId_interprete(self,id_interprete):
          self.id_interprete = id_interprete        
      def setId_genero(self,id_genero):
          self.id_genero = id_genero        
      def setCant_temas(self,cant_temas):
          self.cant_temas = cant_temas       
      def setId_discografica(self,id_discografica):
          self.id_discografica = id_discografica       
      def setId_formato(self,id_formato):
          self.id_formato = id_formato        
      def setFec_lanzamiento(self,fec_lanzamiento):
          self.fec_lanzamiento = fec_lanzamiento       
      def setPrecio(self,precio):
          self.precio = precio        
      def setCantidad(self,cantidad):
          self.cantidad = cantidad        
      def setCaratula(self,caratula):
          self.caratula = caratula 
       
      def __str__(self):
         return str(self.id_album) +' '+ str(self.cod_album) +'''
             '''+ self.nombre +' '+ str(self.id_interprete) +' '+ str(self.id_genero) +''' 
             '''+ str(self.cant_temas) +' '+ str(self.id_discografica) +'''
             '''+ str(self.id_formato) +' '+ self.fec_lanzamiento +'''
             '''+ str(self.precio) +' '+ str(self.cantidad) +' '+ self.caratula 


class Genero:
    def __init__(self,id_genero,nombre):
        self.id_genero = id_genero
        self.nombre = nombre

    def __str__(self):
        return str(self.id_genero)+' '+self.nombre

    def getId_genero(self):
        return self.id_genero
    def getNombre(self):
        return self.nombre

    def setId_genero(self,id_genero):
        self.id_genero = id_genero
    def setNombre(self,nombre):
        self.nombre = nombre


class Interprete:     
    def __init__(self,id_interprete,nombre,apellido,nacionalidad,foto):
        self.id_interprete = id_interprete
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
        self.foto = foto

    def getId_Interprete(self):
        return self.id_interprete
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getNacionalidad(self):
        return self.nacionalidad
    def getFoto(self):
        return self.foto

    def setId_Interprete(self,idInterprete):
        self.id_interprete = idInterprete
    def setNombre(self,nombre):
        self.nombre = nombre
    def setApellido(self,apellido):
        self.apellido = apellido
    def setNacionalidad(self,nacionalidad):
        self.nacionalidad = nacionalidad
    def setFoto(self,foto):
        self.foto = foto

    def __str__(self) -> str:
        return str(self.id_interprete)+' '+self.nombre+' '+self.apellido+''' 
                 '''+self.nacionalidad+' '+self.foto  


class Discografica:
    def __init__(self,id_discografica,nombre):
        self.id_discografica = id_discografica
        self.nombre = nombre

    def __str__(self):
        return str(self.id_discografica)+' '+self.nombre

    def getId_discografica(self):
        return self.id_discografica
    def getNombre(self):
        return self.nombre
    
    def setId_discografica(self,id_discografica):
        self.id_discografica = id_discografica
    def setNombre(self,nombre):
        self.nombre = nombre


class Formato:
    def __init__(self,id_formato,tipo):
        self.id_formato = id_formato
        self.tipo = tipo

    def __str__(self):
        return str(self.id_formato)+' '+self.tipo

    def getId_formato(self):
        return self.id_formato
    def getTipo(self):
        return self.tipo

    def setId_formato(self,id_formato):
        self.id_formato = id_formato
    def setTipo(self,tipo):
        self.tipo = tipo


class Tema:
    def __init__(self,id_tema,titulo,duracion,autor,compositor,cod_album,id_interprete):
        self.id_tema = id_tema
        self.titulo = titulo
        self.duracion = duracion
        self.autor = autor
        self.compositor = compositor
        self.cod_album = cod_album
        self.id_interprete = id_interprete

    def getId_tema(self):
        return self.id_tema
    def getTitulo(self):
        return self.titulo
    def getDuracion(self):
        return self.duracion
    def getAutor(self):
        return self.autor
    def getCompositor(self):
        return self.compositor
    def getCod_album(self):
        return self.cod_album
    def getId_interprete(self):
        return self.id_interprete

    def setId_tema(self,id_tema):
        self.id_tema = id_tema
    def setTitulo(self,titulo):
        self.titulo = titulo
    def setDuracion(self,duracion):
        self.duracion = duracion
    def setAutor(self,autor):
        self.autor = autor
    def setCompositor(self,compositor):
        self.compositor = compositor
    def setCod_album(self,cod_album):
        self.cod_album = cod_album
    def setId_interprete(self,id_interprete):
        self.id_interprete = id_interprete

    def __str__(self):
        return str(self.id_tema)+' '+self.titulo+' '+str(self.duracion)+'''
        '''+self.autor+' '+self.compositor+' '+str(self.cod_album)+'''
        '''+str(self.id_interprete)                          


     
#------------------------------------------------------------------------










