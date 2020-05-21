import database as mp

opcion = 0
usuario = ""
contador = 1
while usuario != "":
    print('Ingresa tu usuario: ')
    usuario = input()
    
    #Se chequea que el usuario exista en la database
    if mp.usuarioexiste(usuario) == True:
            print('Ingrese la opcion de lo que desea realizar: \n')
            print("1. Explorar")
            print("2. Recomendaciones")
            opcion = input("\n")
            
            if opcion == "1":    
                print("Seleccione un video: \n")
                listaalmacenada = mp.explorarvideos(usuario)[:]    #slicing para que listaalmacenada sea independiente
                
                for element in listaalmacenada:
                    print(contador, element)
                    contador = contador + 1
                
                opcion = input("\n")
                mp.agregarvideo(usuario,listaalmacenada[opcion-1])


                
            elif opcion == "2":
                print('Seleccione un video: \n')
                
                listaalmacenada = mp.videosrecomendadosusuario(usuario)[:]    #slicing para que listaalmacenada sea independiente
                contador =0
                
                for element in listaalmacenada:
                    while contador <= len(listaalmacenada))
                        print(contador, element)                
                                
                opcion = input("\n")
                mp.agregarvideo(usuario,listaalmacenada[opcion-1])
                
        
        
        
    else:
        usuario = "":
        
        
    
        
        
        
    
    
