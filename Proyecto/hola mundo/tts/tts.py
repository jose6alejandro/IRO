# Hola mundo, text-to-speech 

import pyttsx3

engine = pyttsx3.init()

voices = engine.setProperty('voice', 'spanish-latin-am') # idioma
voices = engine.setProperty('rate', 160) # Velocidad palabras/min
voices = engine.setProperty('volume', 1) # entre 0 y 1

engine.say('Hola mundo, esto es una prueba')
engine.runAndWait()

