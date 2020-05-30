import db as mp

opcion = 0
usuario = ""
contador = 1
bandera = True

while usuario == "":
    print('INGRESE SU USUARIO: ')
    usuario = input()
    
    #Se chequea que el usuario unicamente contenga una cadena de letras
    if usuario.isalpha():
        
            #Se chequea que el usuario exista en la database
        if mp.usuarioExiste(usuario) == True:
            while bandera == True:
        
                print('\nINGRESE UNA OPCION: \n')
                print("1. Explorar")
                print("2. Recomendaciones")
                print("3. Historial")
                print("4. Salir")
                
                opcion = input("\n")
                
                if opcion.isdigit():
                        
                    if opcion == "1":
                        contador = 1
                        print("SELECCIONE UN VIDEO POR SU NUMERO: \n")

                        listaAllVideos = mp.allVideos()
                        listaRecomendados = mp.Recomendaciones(usuario)
                        listaHistorial = mp.Historial(usuario)
                        
                        for i in listaRecomendados:
                            if i in listaAllVideos: listaAllVideos.remove(i)
                            
                        for i in listaHistorial:
                            if i in listaAllVideos: listaAllVideos.remove(i)

                        
                        for i in listaAllVideos:
                            print(contador, i)
                            contador+=1

                        opcion = input("\n")
                        mp.crearRelacion(usuario,listaAllVideos[opcion-1])
                                
                    elif opcion == "2":
                        contador = 1
                        print("SELECCIONE UN VIDEO POR SU NUMERO: \n")
                            
                        lista = mp.Recomendaciones(usuario)
                        
                        for element in lista:
                            print(contador, element)
                            contador+=1
                 
                        opcion = input("\n")
                        mp.agregarvideo(usuario,listaalmacenada[opcion-1])
                        
                    elif opcion == "3":
                        contador = 1
                        print('HISTORIAL DEL USUARIO',usuario.upper(), ':\n')
                        lista = mp.Historial(usuario)
                        
                        for element in lista:
                            print(contador, element)
                            contador+=1

                    elif opcion == "4":
                        print("GRACIAS POR UTILIZAR EL SISTEMA DE RECOMENDACION DE VIDEOS.")
                        bandera = False
                        
                    else:
                        print("\nOPCION INVALIDA, INTENTE DE NUEVO")
                        
                        
                else:
                    print("\nOPCION INVALIDA, INTENTE DE NUEVO")
                
        else:
            usuario = ""
                    
    elif usuario == "":
        
        usuario = ""
        
        
    else:
        print("\nCARACTERES INVALIDOS, INTENTELO DE NUEVO")
        usuario = ""
          
        
        
        
    
    
