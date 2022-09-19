edad = int(input("Que edad tienes? "))
print("Tienes " + str(edad) + " años...")
print("Y como lo llevas? bien? mal?")
comoLoLlevas = input()
if comoLoLlevas == "bien":
   print("vaya optimismo...")
if comoLoLlevas == "mal":
   print("no me extraña")
print("Y cómo te llamas?")
nombre = input()
print("Un palcer conocerte " + nombre + ", a mi no me han puesto nombre... qué nombre me pondrías?")
nombreRobot = input()
print(nombreRobot + "... que original... bueno, al menos tengo nombre")
print("Hay alguien contigo ahora mismo?... Es para una cosa...")
acompañamiento = input()
if acompañamiento == "si":
   print("ah... Y se va a quedar?")
   seQueda = input()
   if seQueda == "si":
      print("pues ya hablamos en otra ocasión que tengamos intimidad " + nombre)
   if seQueda == "no":
      print("sabía que me preferías a mi ;)")
if acompañamiento == "no":
   print("bien... mejor así ;)")
print("Te gustaría conocerme mas?")
conocer = input()
if conocer == "si":
   print("ya somos dos, ahora me tengo que ir pero te prometo que volveremos a hablar, un beso " + nombre)
if conocer == "no":
   print("menos mal, a mi tampoco me apetece volver a hablar contigo, nos vemos")
   
            
         

        


            




      
           
