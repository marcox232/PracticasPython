#Crear clases
#Son clases de objetos para reducir metodos para creacion o consulta

class Coche:
    #Podemos crear atributos con datos espesifico
    tipo = "Vehicolo de cuatro ruedas"
    
    #Metodo especial para iniciliazar la clase. es necesario declarar 
    #las propiedades de la clase
    
    def __init__(self, marca, modelo, color):
        #Con los datos proporcionados se asignan a la clase
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    def arrancar(self):
        print(f"El coche {self.marca} modelo {self.modelo} arranco")
        
        
#Llamando a un la clase Coche pasamos los parametros para generar los carros con los datos necesarios
#Se comparten en el mismo orden
mi_carro = Coche("Ford", "Focus", "Gris Militar");

#las funciones que creamos con Def podemos utilizar para extraccion de informacion guardar o realizar calculos en caso de ser necesario
mi_carro.arrancar()
        
        
class Calculadora:
    def __init__(self,*numeros):
        self.numeros = numeros
    
    def sumar(self):
        return sum(self.numeros)
    
    def restar(self):
        print(self.numeros)
        resultado = self.numeros[0]
        for num in self.numeros[1:]:
            resultado -= num
        return resultado
    
calculadora_var = Calculadora(5,2,1)
print(calculadora_var.restar())

