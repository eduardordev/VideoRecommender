import db as mp

opcion = 0
usuario = ""
contador = 1
t = True
bandera = True

while t:
    while usuario == "":
        print('Ingresa tu usuario: ')
        usuario = input()
            #Se chequea que el usuario exista en la database
        if mp.usuarioExiste(usuario) == True:
            while bandera == True:
        
                print('Ingrese la opcion de lo que desea realizar: \n')
                print("1. Explorar")
                print("2. Recomendaciones")
                print("3. Historial")
                print("4. Salir")
                opcion = input("\n")
                        
                if opcion == "1":    
                    print("Seleccione un video: \n")
                    listaalmacenada = mp.Explorar(usuario,mp.DevolverNodoV(usuario),mp.DevolverNodoT(usuario,mp.DevolverNodoV(usuario)),mp.DevolverNodoC(usuario,mp.DevolverNodoV(usuario)))[:]    #slicing para que listaalmacenada sea independiente
                        
                    for element in listaalmacenada:
                        print(contador, element)
                        contador = contador + 1
                        
                    opcion = input("\n")
                    mp.crearRelacion(usuario,listaalmacenada[opcion-1])


                            
                elif opcion == "2":
                    print('Seleccione un video: \n')
                        
                    listaalmacenada = mp.Recomendaciones(usuario,mp.DevolverNodoV(usuario),mp.DevolverNodoT(usuario,mp.DevolverNodoV(usuario)),mp.DevolverNodoC(usuario,mp.DevolverNodoV(usuario)))[:]    #slicing para que listaalmacenada sea independiente
                    contador =0
                    lon = len(listaalmacenada)
                        
                        
                    for element in listaalmacenada:
                        while contador <= lon:
                            print(contador, element)                
                                        
                    opcion = input("\n")
                    mp.agregarvideo(usuario,listaalmacenada[opcion-1])
                    
                elif opcion == "3":
                    print('Los videos que el usuario ha visto son: \n')
                    mp.mostrarVideosVistosPorUsuario(usuario)

                elif opcion == "4":
                    print("Gracias por utilizar el programa")
                    t = False
                    bandera = False
    else:
        usuario = ""
          
        
        
        
    
    
