import flet as ft

import serial

ser = serial.Serial("dev/ttyACM0",baudrate=9600,timeout=3)

def main(page: ft.Page):

    c = ft.Container(
        width=100,
        height=100,
        bgcolor="black",
        border_radius=5,
        scale=ft.transform.Scale(scale=1),
        animate_scale=ft.animation.Animation(600, ft.AnimationCurve.BOUNCE_OUT),
    )

    def animate(e):

        if c.scale != 2:        
            c.scale = 2
            c.bgcolor = "red"
            ser.write("r".encode("utf-8"))          
        else:
            c.scale = 1 
            c.bgcolor = "black"      
            ser.write("b".encode("utf-8"))
        print(c.scale)   
        page.update()  
        

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 30
    page.add(
        c,
        ft.ElevatedButton("Hello KaRy Copo!", on_click=animate),
    )

ft.app(target=main)
