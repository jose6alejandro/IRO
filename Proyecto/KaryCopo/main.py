from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.core.text import LabelBase
LabelBase.register(name='FontAwesome', fn_regular='fontawesome-webfont.ttf')


from kivy.clock import mainthread
from kivy.utils import platform
import threading
import sys

if platform == 'android':
    from usb4a import usb
    from usbserial4a import serial4a
else:
    from serial.tools import list_ports
    from serial import Serial
    from kivy.core.window import Window
    Window.size = (320, 1600)



from plyer import tts
import time
import random


texto_a_reproducir = [
		"voy a ejecutar los movimientos", 
		"voy a seguir las instrucciones", 
		"voy a seguir los comandos",
		"Estoy listo para empezar",
		"Empecemos a jugar",
		"Vamos a comenzar",
		"Hola soy KaryCopo, los siguientes comandos permiten controlar mis movimientos",
		"Hola, lee el significado de los comandos que pueden controlar mis movimientos",
		"Hola, voy a mostrarte que significan los comandos para controlar mis movimientos",
		"He finalizado"
		]


Builder.load_string("""
<CustomButton>
    text: self.text
    markup: True
    font_size: 60
    size_hint: (1, 1)
    background_color: (0, 0, 0, 0)
    color: self.color
    on_press: self.on_press
    fondo_color: (0,0,0,0)
    canvas.before:
        Color:
            rgba: root.fondo_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius:  [60,]


<Container>:
    orientation: 'vertical'
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle: 
            size: self.size
            pos: self.pos               

<Top_box>:
    size_hint: 1, .3
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle: 
            size: self.size
            pos: self.pos
    
    GridLayout:
        size_hint: 1, 1
        cols: 3
        padding: dp(40) 
        spacing: dp(20)
        
        CustomButton:
            text: '\uf062'  
            font_name: 'FontAwesome'
            fondo_color: (137/255, 168/255, 221/255, 0.8)
            color: (0/255, 58/255, 160/255, 0.8)
            size_hint: None, None  
            width: root.width / 5  
            height: root.width / 5 
            on_press: app.add_button(self.text)
        CustomButton:
            text: '\uf0e2' 
            font_name: 'FontAwesome'
            fondo_color: (137/255, 168/255, 221/255, 0.8)
            color: (0/255, 58/255, 160/255, 0.8)  
            size_hint: None, None  
            width: root.width / 5  
            height: root.width / 5            
            on_press: app.add_button(self.text)      
        CustomButton:
            text: '\uf01e'  
            font_name: 'FontAwesome'
            fondo_color: (137/255, 168/255, 221/255, 0.8)
            color: (0/255, 58/255, 160/255, 0.8)
            size_hint: None, None  
            width: root.width / 5  
            height: root.width / 5            
            on_press: app.add_button(self.text)
        CustomButton:
            text: '\uf063'  
            font_name: 'FontAwesome' 
            fondo_color: (137/255, 168/255, 221/255, 0.8)
            color: (0/255, 58/255, 160/255, 0.8)  
            size_hint: None, None  
            width: root.width / 5  
            height: root.width / 5            
            on_press: app.add_button(self.text)                               
        CustomButton:
            text: '\uf0da'  
            font_name: 'FontAwesome' 
            fondo_color: (137/255, 168/255, 221/255, 0.8)
            color: (0/255, 58/255, 160/255, 0.8)
            size_hint: None, None  
            width: root.width / 5  
            height: root.width / 5            
            on_press: app.add_button(self.text)
        CustomButton:
            text: '\uf0d9'  
            font_name: 'FontAwesome' 
            fondo_color: (137/255, 168/255, 221/255, 0.8)
            color: (0/255, 58/255, 160/255, 0.8)     
            size_hint: None, None  
            width: root.width / 5  
            height: root.width / 5            
            on_press: app.add_button(self.text)  
       
                                              
<Middle_box>:
    size_hint: 1, .5
    padding: dp(8)
    canvas:
        Color:
            rgb: 0.95, 0.95, 0.95
        Rectangle: 
            size: self.size
            pos: self.pos

    GridLayout:
        id: grid_layout 
        size_hint:(1, 1)
        cols: 4
        spacing: dp(25)
        padding: dp(20), 0
        
                        
<Bottom_box>:
    size_hint: 1, .2
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle: 
            size: self.size
            pos: self.pos

    GridLayout:
        id: grid_layout 
        size_hint: 1, 1
        cols: 9
        padding: dp(20) 
        spacing: dp(80)

        CustomButton:
            id: custom_button_id
            text: '\uf00c' 
            font_name: 'FontAwesome'
            fondo_color: (38/255, 213/255, 0, 0.8)
            color: (1, 1, 1, 1)   
            size_hint: None, None  
            width: root.width / 3  
            height: root.width / 3  
            font_size: 90
            on_press: app.send_button()

        CustomButton:
            text: '\uf015'  
            font_name: 'FontAwesome' 
            fondo_color: (0.8, 0.8, 0.8, 0.8)
            color: (1, 1, 1, 0.8)     
            size_hint: None, None 
            font_size: 40 
            width: root.width / 7  
            height: root.width / 7  
            on_press: app.starter_robot_screen()
            
<Connection_Screen>:
    name: 'screen_scan'
    BoxLayout:
        canvas:
            Color:
                rgb: 1, 1, 1
            Rectangle: 
                size: self.size
                pos: self.pos
        orientation: 'vertical'
        padding: [dp(0), dp(0), dp(0), 0]
        BoxLayout:
            id: box_list
            orientation: 'vertical'
            on_parent: app.uiDict['box_list'] = self
            size_hint_y: None
            height: max(self.minimum_height, self.parent.height)
        Button:
            id: btn_scan
            on_parent: app.uiDict['btn_scan'] = self
            size_hint_y: None
            height: '50dp'
            text: 'Buscar dispositivo USB'
            background_color:(38/255, 213/255, 0, 1)
            markup: True
            on_release: app.on_btn_scan_release()

<User_guide>:
    orientation: 'vertical'
    canvas:
        Color:
            rgb: 0, 0, 0
        Rectangle: 
            size: self.size
            pos: self.pos             

<Starter_top_box>:
    size_hint: 1, .2
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle: 
            size: self.size
            pos: self.pos
            
    Label:
        padding: dp(10)
        text: 'Los siguientes comandos permiten controlar mis movimientos:'
        color: 0, 0, 0
        font_size: '20sp'
        text_size: self.size
        halign:'center'
        valign:'middle'

<Starter_middle_box>:
    size_hint: 1, .7
    canvas:
        Color:
            rgb: 1,1,1
        Rectangle: 
            size: self.size
            pos: self.pos            

    GridLayout:
        size_hint: 1, 1
        cols: 1
        padding: dp(10) 
        spacing: dp(20)
        
        BoxLayout:
        
            CustomButton:
                text: '\uf062'  
                font_name: 'FontAwesome'
                fondo_color: (137/255, 168/255, 221/255, 0.8)
                color: (0/255, 58/255, 160/255, 0.8)
                size_hint: None, None  
                width: root.width / 5  
                height: root.width / 5 
            Label:
                font_size: '20sp'
                color: 0, 0, 0
                text: 'Avanzar'
        
        BoxLayout:
        
            CustomButton:
                text: '\uf0e2' 
                font_name: 'FontAwesome'
                fondo_color: (137/255, 168/255, 221/255, 0.8)
                color: (0/255, 58/255, 160/255, 0.8)  
                size_hint: None, None  
                width: root.width / 5  
                height: root.width / 5            
            Label:
                font_size: '20sp'
                color: 0, 0, 0
                text: 'Girar izquierda'
       
        BoxLayout:
        
            CustomButton:
                text: '\uf01e'  
                font_name: 'FontAwesome'
                fondo_color: (137/255, 168/255, 221/255, 0.8)
                color: (0/255, 58/255, 160/255, 0.8)
                size_hint: None, None  
                width: root.width / 5  
                height: root.width / 5            
            Label:
                font_size: '20sp'
                color: 0, 0, 0
                text: 'Girar derecha'
        
        BoxLayout:          
        
            CustomButton:
                text: '\uf063'  
                font_name: 'FontAwesome' 
                fondo_color: (137/255, 168/255, 221/255, 0.8)
                color: (0/255, 58/255, 160/255, 0.8)  
                size_hint: None, None  
                width: root.width / 5  
                height: root.width / 5            
            Label:
                font_size: '20sp'
                color: 0, 0, 0
                text: 'Retroceder'
        
        BoxLayout:    
                                                   
            CustomButton:
                text: '\uf0da'  
                font_name: 'FontAwesome' 
                fondo_color: (137/255, 168/255, 221/255, 0.8)
                color: (0/255, 58/255, 160/255, 0.8)
                size_hint: None, None  
                width: root.width / 5  
                height: root.width / 5            
            Label:
                font_size: '20sp'
                color: 0, 0, 0
                text: 'Mover brazo izquierdo'    
        
        BoxLayout:
        
            CustomButton:
                text: '\uf0d9'  
                font_name: 'FontAwesome' 
                fondo_color: (137/255, 168/255, 221/255, 0.8)
                color: (0/255, 58/255, 160/255, 0.8)     
                size_hint: None, None  
                width: root.width / 5  
                height: root.width / 5        
            Label:
                font_size: '20sp'
                color: 0, 0, 0
                text: 'Mover brazo derecho'          
        
<Starter_bottom_box>:
    size_hint: 1, .1
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle: 
            size: self.size
            pos: self.pos   
   
    GridLayout:
        size_hint: 1, 1
        cols: 1
        padding: [dp(10), dp(20), dp(10), 0]
                            
        Button:
            id: btn_start
            on_parent: app.uiDict['btn_scan'] = self
            size_hint_y: None
            height: '50dp'
            text: 'Continuar'
            background_color:(38/255, 213/255, 0, 1)
            markup: True
            on_press: app.commands_screen()
            
<Starter_robot>:
    orientation: 'vertical'
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle: 
            size: self.size
            pos: self.pos 

    GridLayout:
        size_hint: 1, 1
        cols: 1
        padding: [dp(10), dp(360), dp(10), 0]
                            
        Button:
            id: btn_start
            on_parent: app.uiDict['btn_scan'] = self
            size_hint_y: None
            height: '50dp'
            text: 'Empezar'
            background_color:(38/255, 213/255, 0, 1)
            markup: True
            on_press: app.user_guide_screen()
""")

class Container(BoxLayout):
    def __init__(self):
        super(Container, self).__init__()
        
        self.top_box = Top_box()
        self.middle_box = Middle_box()
        self.bottom_box = Bottom_box()
        
        self.add_widget(self.top_box)        
        self.add_widget(self.middle_box)
        self.add_widget(self.bottom_box)      
        
class CustomButton(Button):
    pass
            
class Top_box(BoxLayout):
    None

class Middle_box(BoxLayout):
    None      
        
class Bottom_box(BoxLayout):
    None

class Connection_Screen(Screen):
    pass

class Commands_Screen(Screen):
    pass

class User_guide(BoxLayout):
    def __init__(self):
        super(User_guide, self).__init__()
        
        self.starter_top_box = Starter_top_box()   
        self.starter_Middle_box = Starter_Middle_box()     
        self.starter_bottom_box = Starter_bottom_box() 
         
        self.add_widget(self.starter_top_box)
        self.add_widget(self.starter_Middle_box)
        self.add_widget(self.starter_bottom_box)
               
class Starter_top_box(BoxLayout):
    None

class Starter_Middle_box(BoxLayout):
    None
    
class Starter_bottom_box(BoxLayout):
    None
    
class Starter_robot(BoxLayout):
    None
    
class MainApp(App):

    title = 'Kary-Bot'
    
    max_buttons = 20
    num_buttons = 0
    
    commands_dict = {
        '\uf0da': 'a',
        '\uf0d9': 'b',
        '\uf0e2': 'c',
        '\uf062': 'd',
        '\uf01e': 'e',
        '\uf063': 'f',                
    }
    
    commands_send = {}

    def __init__(self, *args, **kwargs):
        self.uiDict = {}
        self.device_name_list = []
        self.serial_port = None
        self.read_thread = None
        self.port_thread_lock = threading.Lock()
        super(MainApp, self).__init__(*args, **kwargs)
        
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(Connection_Screen(name='inicio'))
        
        commands_screen = Screen(name='commands')
        commands_screen.add_widget(Container())
        sm.add_widget(commands_screen)
        
        user_guide_screen = Screen(name='user_guide')
        user_guide_screen.add_widget(User_guide())
        sm.add_widget(user_guide_screen)       

        starter_robot_screen = Screen(name='starter_robot')
        starter_robot_screen.add_widget(Starter_robot())
        sm.add_widget(starter_robot_screen)         
        
        self.uiDict['sm'] = sm

        return sm
        
    def on_stop(self):
        if self.serial_port:
            with self.port_thread_lock:
                self.serial_port.close()        

    def on_btn_scan_release(self):
        #self.uiDict['sm'].current = 'starter_robot' #Debo quitar
        
        self.uiDict['box_list'].clear_widgets()
        self.device_name_list = []
        
        if platform == 'android':
            usb_device_list = usb.get_usb_device_list()
            self.device_name_list = [
                device.getDeviceName() for device in usb_device_list
            ]
        else:
            usb_device_list = list_ports.comports()
            self.device_name_list = [port.device for port in usb_device_list]
        
        for device_name in self.device_name_list:
            btnText = device_name
            button = Button(text=btnText, size_hint_y=None, height='100dp', background_color=(92/255, 96/255, 102/255, 0.5))
            button.bind(on_release=self.on_btn_device_release)
            self.uiDict['box_list'].add_widget(button)
        
    def on_btn_device_release(self, btn):
        
        device_name = btn.text
        
        if platform == 'android':
            device = usb.get_usb_device(device_name)
            if not device:
                raise SerialException(
                    "Device {} not present!".format(device_name)
                )
            if not usb.has_usb_permission(device):
                usb.request_usb_permission(device)
                return
            self.serial_port = serial4a.get_serial_port(
                device_name,
                9600,
                8,
                'N',
                1,
                timeout=1
            )
        else:
            self.serial_port = Serial(
                device_name,
                9600,
                8,
                'N',
                1,
                timeout=1
            )
        
        if self.serial_port.is_open and not self.read_thread:
            self.read_thread = threading.Thread(target = self.read_msg_thread)
            self.read_thread.start()
        
        self.uiDict['sm'].current = 'user_guide'
        
    def add_button(self, text_button):
        if self.num_buttons < self.max_buttons:
            button = CustomButton(text=text_button, 
                                    fondo_color=(92/255, 96/255, 102/255, 0.5),
                                    color=(0, 0, 0, 1), 
                                    font_size=40, 
                                    size_hint=(None, None),
                                    width=self.root.width / 7,  # Define el ancho del botón
                                    height=self.root.width / 7,  # Altura fija del botón 
                                    font_name='FontAwesome')
            
            button.bind(on_press=self.remove_button)
            
            container = self.root.get_screen('commands').children[0]
            middle_box = container.middle_box
            grid_layout = middle_box.ids.grid_layout
            
            grid_layout.add_widget(button)
            
            self.commands_send[button] = self.commands_dict[text_button]
            print(self.commands_send.values())
            self.num_buttons += 1
            

    def remove_button(self, button):
    
        container = self.root.get_screen('commands').children[0]
        middle_box = container.middle_box
        grid_layout = middle_box.ids.grid_layout
        
        grid_layout.remove_widget(button)
        
        del self.commands_send[button]
        print(self.commands_send.values()) 
        self.num_buttons -= 1
         

    def read_msg_thread(self):
        while True:
            try:
                with self.port_thread_lock:
                    if not self.serial_port.is_open:
                        break
                    received_msg = self.serial_port.read(
                        self.serial_port.in_waiting
                    )
                if received_msg:
                    msg = bytes(received_msg).decode('utf8')
                    self.display_received_msg(msg)
            except Exception as ex:
                raise ex


    def reproducir_texto(self, texto):            
        tts.speak(message=texto)

    def obtener_duracion_estimada(self, texto):
        # Calcular la duración aproximada del texto basado en su longitud
        palabras = texto.split()
        palabras_por_minuto = 160  # RATE palabras/min
        duracion_minutos = len(palabras) / palabras_por_minuto
        return duracion_minutos * 60  # Convertir minutos a segundos

    def hablar_robot(self, duracion_texto):
        tiempo_actual = 0.0
        par = 1
        
        while tiempo_actual < duracion_texto:
            
            if (par % 2 == 0):
                self.serial_port.write(bytes('3','utf8'))
         
            else:
                self.serial_port.write(bytes('4','utf8'))
        
            tiempo_actual += 0.22
            time.sleep(0.1)
            par+= 1
        
        self.serial_port.write(bytes('0','utf8'))


    def send_button(self):
        global texto_a_reproducir
        texto = texto_a_reproducir[random.randint(0,2)]
        duracion_texto = self.obtener_duracion_estimada(texto)
       
        bottom_box = self.root.get_screen('commands').children[0].bottom_box
        custom_button = bottom_box.ids.custom_button_id
        custom_button.text = '\uf04c'
        custom_button.fondo_color = (238/255, 0/255, 0, 0.8)       
        
        if self.serial_port and self.serial_port.is_open:
            def callback():
                thread_reproduccion = threading.Thread(target=self.reproducir_texto, args=(texto,))
                thread_reproduccion.start()

                self.hablar_robot(duracion_texto) 
                time.sleep(duracion_texto)    
            
                for sec in self.commands_send.values():
                   
                    if(sec == 'a'): 
                        thread_reproduccion = threading.Thread(target=self.reproducir_texto, args=("mover brazo izquierdo",))
                    
                    elif(sec == 'b'): 
                        thread_reproduccion = threading.Thread(target=self.reproducir_texto, args=("mover brazo derecho",))

                    elif(sec == 'c'): 
                        thread_reproduccion = threading.Thread(target=self.reproducir_texto, args=("girar a la izquierda",))
                    
                    elif(sec == 'd'): 
                        thread_reproduccion = threading.Thread(target=self.reproducir_texto, args=("avanzar",))
                    
                    elif(sec == 'e'): 
                        thread_reproduccion = threading.Thread(target=self.reproducir_texto, args=("girar a la derecha",))    
                    
                    else:
                        thread_reproduccion = threading.Thread(target=self.reproducir_texto, args=("retroceder",))
                                              
                        
                    thread_reproduccion.start()                        
                    self.hablar_robot(duracion_texto) 
                    time.sleep(duracion_texto)  
                    
                    self.serial_port.write(bytes(sec,'utf8')) 
                    time.sleep(2)
            
                #texto = texto_a_reproducir[random.randint(0,2)]                 
                
                custom_button.text = '\uf00c'
                custom_button.fondo_color = (38/255, 213/255, 0, 0.8)  
                self.serial_port.write(bytes('1','utf8')) 
                self.serial_port.write(bytes('-','utf8'))                 
            
            Clock.schedule_once(lambda dt: callback(), 0)
            
    def user_guide_screen(self):
           
        self.uiDict['sm'].current = 'user_guide' 
        container = self.root.get_screen('commands').children[0]
        middle_box = container.middle_box
        grid_layout = middle_box.ids.grid_layout
        grid_layout.clear_widgets()
        self.num_buttons = 0
        self.commands_send.clear()
        
        global texto_a_reproducir
        texto = texto_a_reproducir[random.randint(6,8)]
        duracion_texto = self.obtener_duracion_estimada(texto)
        thread_reproduccion = threading.Thread(target=self.reproducir_texto, args=(texto,))
        thread_reproduccion.start()

        self.hablar_robot(duracion_texto) 
        time.sleep(duracion_texto)  

    def starter_robot_screen(self):
             
        self.uiDict['sm'].current = 'starter_robot'

        global texto_a_reproducir
        texto = texto_a_reproducir[random.randint(3,5)]
        duracion_texto = self.obtener_duracion_estimada(texto)

        thread_reproduccion = threading.Thread(target=self.reproducir_texto, args=(texto,))
        thread_reproduccion.start()

        self.hablar_robot(duracion_texto) 
        time.sleep(duracion_texto)    
            
        
    def commands_screen(self):
        self.uiDict['sm'].current = 'commands'        
          
if __name__ == "__main__":
    MainApp().run()

    
    
