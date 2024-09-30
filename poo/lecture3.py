# crear una classe de alumnos con los atributos que usted crea por conveniente.
# luego instanciara a 4 alumnos

class Alumno:
  def _init_(self, nombre, apellido, edad, promedio, telefono):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    self.promedio = promedio
    self.telefono = telefono

  def mostrar_datos(self):
    print("Nombre:", self.nombre, self.apellido)
    print("Edad:", self.edad)
    print("Promedio:", self.promedio)
    print("Teléfono:", self.telefono)

# Instanciar 4 alumnos
alumno1 = Alumno("Juan", "Pérez", 18, 8.5, "966105579")
alumno2 = Alumno("María", "González", 17, 9.2, "9876543210")
alumno3 = Alumno("Pedro", "Rodríguez", 19, 7.8, "966456321")
alumno4 = Alumno("Ana", "García", 18, 8.9, "987123692")


#ejercicio del profesor
class Alumno:
  def _init_(self, nombre,dni,edad,email,programa_estudio="APSTI"):
    self.nombre=nombre
    self.dni=dni
    self.email=email
    self.programa_estudio=programa_estudio
#metodos
 def escribir(self):
  print("estoy escribiendo")
 def tarea(self,nombre_docente):
  print("haciendo la tarea de:",nombre_docente)
 def terminar_tarea(self):
  print("terminando tarea anterior")
maricielo=Alumno("maricielo",76493681,14,"yo@gmail")
maricielo.tarea("alicia")
maricielo.terminar_tarea()
maricielo.tarea("alvarez")
print(maricielo.programa_estudio)
mercedes=Alumno("meche",62628787,15,"tu@gmail.com","enfermeria")
print(mercedes.programa_estudio)
