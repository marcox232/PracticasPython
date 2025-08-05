#Voy a generar un juego de adivinanza de numeros. esto para verificar lo aprendido

#Necesito un numero random para iniciar el juego vamos a importar la libreria random par esta accion
import random

def jugo_adivinansa():
    
    numero_secreto = random.randint(1,100)
    
    num_intentos = 0
    
    print("Adivina el numero, tiene 3 oportunidades para decirme cual es el numero del 1 al 100")
    while True:
        if num_intentos >= 3:
            print("Perdiste, buen intento, suerte para la pxima")
            break
        
        num_adiv = int(input("Escoje un Numero: "))
        
        if num_adiv > numero_secreto:
            print("Tu numero es mayo")
        elif num_adiv < numero_secreto:
            print("Tu numero es menor")
        else:
            print("Correcto adivinaste el numero")
            break
        
        num_intentos+=1

jugo_adivinansa()