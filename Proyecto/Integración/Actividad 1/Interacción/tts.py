import serial
ser = serial.Serial("/dev/ttyACM0",baudrate=9600,timeout=3)

import pyttsx3
import time

def reproducir_texto(texto):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'spanish-latin-am') # idioma
    engine.setProperty('rate', 160) # velocidad palabras/min
    engine.setProperty('volume', 1) # entre 0 y 1
    engine.say(texto)
    engine.runAndWait()

def obtener_duracion_estimada(texto):
    # Calcular la duración aproximada del texto basado en su longitud
    palabras = texto.split()
    palabras_por_minuto = 160  # RATE palabras/min
    duracion_minutos = len(palabras) / palabras_por_minuto
    return duracion_minutos * 60  # Convertir minutos a segundos

def hablar_robot(duracion_texto):
    tiempo_actual = 0.0
    par = 1

    while tiempo_actual < duracion_texto:
        
        if (par % 2 == 0):
            ser.write("u".encode("utf-8"))	
     
        else:
            ser.write("d".encode("utf-8"))	
    
        tiempo_actual += 0.22
        time.sleep(0.1)
        par+= 1
    
    ser.write("p".encode("utf-8"))
    
texto_a_reproducir = [
		"selecciona las instrucciones, y dale en continuar", 
		"excelente, sigue asi", 
		"vamos al siguiente nivel"]

