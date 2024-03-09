import flet as ft
import threading
import random
from tts import *

def main(page: ft.Page):

    c = ft.Container(
        width=100,
        height=100,
        bgcolor="green",
        border_radius=5,
        scale=ft.transform.Scale(scale=1),
        animate_scale=ft.animation.Animation(600, ft.AnimationCurve.BOUNCE_OUT),
    )
    
    button = ft.ElevatedButton(text="CONTINUAR")

    def evento_click(e):     
    
        global texto_a_reproducir
        texto = texto_a_reproducir[random.randint(0,2)]
        duracion_texto = obtener_duracion_estimada(texto)  
      
        c.scale = 2
        c.bgcolor = "red"
        button.text = "ESPERA"  
        page.update()
       
        thread_reproduccion = threading.Thread(target=reproducir_texto, args=(texto,))
        thread_reproduccion.start()

        hablar_robot(duracion_texto) 
        
        time.sleep(duracion_texto)

        c.scale = 1
        c.bgcolor = "green"
        button.text = "CONTINUAR"          
        page.update()  
        
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 30

    page.add(
        c,
        button,
    )

    button.on_click = evento_click
    
ft.app(target=main)
