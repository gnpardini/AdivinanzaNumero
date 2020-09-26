import random

#Funciones

class NumeroErroneo(Exception):
    
    pass


def verificarDato(numero):
    
    intentos = 0
    
    while True:
    
        try:
            
            adivinanza = int(input("Adivine que número se generó. Pista: es del 1 al 500"))
            
            if adivinanza == numero:
                
                print("FELICITACIONES! USTED HA ADIVINADO EL NÚMERO")
                print(f"Número secreto: {numero}")
                
                print(f"La cantidad de intentos fueron: {intentos}")
                
                break
            
            else:
                
                raise NumeroErroneo
            
        
        except(NumeroErroneo):
        
            
            if adivinanza > numero:
                
                print(f"El número que debes adivinar es menor a {adivinanza}")
            
            else:
                
                print(f"El número que debes adivinar es mayor a {adivinanza}")
                
            intentos += 1
            
            
        except(ValueError):
            
            print("Error. Solo se permite el ingreso de números enteros")
            
            
                
            
        
    
    









#Main
random.randint(1,500)
adivinanza = verificarDato(numero)
