#Programa que realiza un sistema de recomendacion de videos en base a gustos del usuario
#Programa realizado por Gabriel Quiroz, Eduardo Ramirez, Jose Pablo Ponce y Oscar Paredez
#Algoritmos y estructuras de datos, 2020

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
                print("4. Eliminar Historial")
                print("5. Salir")
                
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

                        opcion = int(input("\n"))
                        mp.crearRelacion(usuario,listaAllVideos[opcion-1])
                        print("\nSE HA VISTO EL VIDEO *", listaAllVideos[opcion-1], "*")
                                
                    elif opcion == "2":
                        contador = 1
                            
                        lista = mp.Recomendaciones(usuario)
                        
                        if (lista != []):
                            print("SELECCIONE UN VIDEO POR SU NUMERO: \n")
                            for element in lista:
                                print(contador, element)
                                contador+=1
                            opcion = int(input("\n"))
                            mp.crearRelacion(usuario,lista[opcion-1])
                            print("\nSE HA VISTO EL VIDEO *", lista[opcion-1], "*")
                            
                        else:
                            print("\nNO SE PUEDEN MOSTRAR RECOMENDACIONES PORQUE EL HISTORIAL ESTA VACIO.")
                            
                    elif opcion == "3":
                        contador = 1
                        
                        
                        lista = mp.Historial(usuario)
                        
                        if (lista != []):
                            print('\nHISTORIAL DEL USUARIO',usuario.upper(), ':\n')
                            for element in lista:
                                print(contador, element)
                                contador+=1
                        else:
                            print("\nNO HAY HISTORIAL QUE MOSTRAR PARA EL USUARIO", usuario)
                    
                    elif opcion == "4":
                        print("\nHISTORIAL DEL USUARIO", usuario, "ELIMINADO")
                        mp.Eliminar(usuario)

                    elif opcion == "5":
                        print("\nGRACIAS POR UTILIZAR EL SISTEMA DE RECOMENDACION DE VIDEOS.")
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
          
        
        
        
    
    
