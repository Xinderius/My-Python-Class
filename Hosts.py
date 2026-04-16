#profe, pondre comentarios para que sepas el funcionamiento del codigo porque cuando lo volvi a abrir me perdi :D
#para que sirva ponle ping [url o ip], es para darle realismo a la simulacion (me di cuenta que poner ping no es comun entonces sirve con o sin ping)
import os
import ping3 as ping
import time
Repeticiones = 0
Tabla_Tiempos = []
os.system("cls")
Host = input(r"C:\Users\User>")
Host_Limpio = Host.replace("ping ", "").replace(" ","") #me daba error con el ping
Host_Enviar = Host_Limpio.lower()
Host_Resultado = ping.ping(Host_Enviar)

#verifica el host
if Host_Resultado is None or Host_Resultado == False:
    print(f"{Host} no se reconoce como un comando interno o externo,\nprograma o archivo por lotes ejecutable.")
else:
  print(f"\nHaciendo ping a {Host} con 32 bytes de datos:")

#es mejor usar un ciclo for pero la tarea decia que usemos un while
while Host_Resultado and Repeticiones < 4:
  Host_Limpio = Host.replace("ping ", "") #me daba error con el ping
  Host_Resultado = ping.ping(Host_Limpio)
  Repeticiones += 1
  Tiempo = int(Host_Resultado * 1000)
  print(f"Respuesta desde {Host_Resultado} tiempo={Tiempo}ms")
  time.sleep(1)
  Tabla_Tiempos.append(Tiempo)

#muestra las estadisticas
if Tabla_Tiempos:
    print(f"\nEstadísticas de ping para {Host}:")
    print(f"    Paquetes: enviados = 4, recibidos = {len(Tabla_Tiempos)}, perdidos = {4 - len(Tabla_Tiempos)}")#lee la cantidad de cosas que hay en la tabla para ver si algo falta o no teniendo en cuenta que el max es 4
    print(f"Tiempos aproximados de ida y vuelta en milisegundos:")
    print(f"    Mínimo = {min(Tabla_Tiempos)}ms, Máximo = {max(Tabla_Tiempos)}ms, Media = {int(sum(Tabla_Tiempos)/len(Tabla_Tiempos))}ms")#muestra lo mismo que en el cmd
