#include <Arduino.h>
#include <LCDWIKI_GUI.h>
#include <LCDWIKI_SPI.h>

#define MODEL ILI9341
#define CS   10    
#define CD   8
#define RST  9
#define MOSI  11
#define MISO  12
#define SCK   13
#define LED  -1

#define RGB_VERDE 2
#define RGB_AZUL  4
#define RGB_ROJO  3

LCDWIKI_SPI lcd(MODEL,CS,CD,MISO,MOSI,RST,SCK,LED);

#define NEGRO     0x0000
#define AZUL      0xF800
#define CIELO     0xE302 
#define ROJO      0x001F
#define VERDE     0x07E0
#define BLANCO    0xFFFF

#include <Servo.h>
Servo servo_derecha, servo_izquierda;
int angulo_izq = 0;
int angulo_der = 0;

//Motor A
int ENA = 7;
int IN1 = 15; 
int IN2 = 16;

//Motor B
int ENB = 14;
int IN3 = 17; 
int IN4 = 18;

/*
  Expresiones:
  Normal 0
  Feliz  1
  Triste 2
  Hablar 3 y 4
*/
void expresion(int);

/*
  Ojos:
  Normal n != 2
  Triste 2
*/
void ojos(int);

/*
  Movimientos de los brazos:
  Arriba
  Abajo 
  Centro
*/
void mover_arriba(Servo);

void mover_abajo(Servo);

void mover_centro(Servo);

/*
  Control de las ruedas
  Avanzar
  Girar derecha 
  Girar Izquierda
  Retroceder
*/
void avanzar();

void girar_derecha();

void girar_izquierda();

void retroceder();

void setup() 
{

  Serial.begin(9600);
  
  lcd.Init_LCD();
  lcd.Set_Rotation(3);
  lcd.Fill_Screen(0, 0, 0);
  
  ojos(0);
  expresion(0);
  
  servo_derecha.attach(5);
  servo_izquierda.attach(6);

  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  mover_centro(servo_derecha);
  mover_centro(servo_izquierda);    
  
  analogWrite(RGB_AZUL, 0);
  digitalWrite(RGB_ROJO, LOW);
  digitalWrite(RGB_VERDE, HIGH);

}

void loop() 
{

    if(Serial.available() > 0) // existe un dato de lectura
    {
        char caracter = Serial.read();

        analogWrite(RGB_AZUL, 0);
        digitalWrite(RGB_ROJO, HIGH);
        digitalWrite(RGB_VERDE, LOW);      
          
        if(caracter == '1')
        {
            expresion(1);
        }
        else if(caracter == '2')
        {
            expresion(2);
        }
        else if (caracter == '3')
        {
          expresion(3);  
        }  
        else if (caracter == '4')
        {
          expresion(4);  
        }                   
        else if(caracter == 'a')
        {
          if(angulo_izq == 1)
          {
            mover_abajo(servo_izquierda);
            angulo_izq = 0;
          }   
          else
          {
            mover_arriba(servo_izquierda);
            angulo_izq = 1;
          }   
        } 
        else if(caracter == 'b')
        {
          if(angulo_der == 1)
          {
            mover_abajo(servo_derecha);
            angulo_der = 0;
          }   
          else
          {
            mover_arriba(servo_derecha);
            angulo_der = 1;
          }
        } 
        else if (caracter == 'c')
        {
          girar_izquierda(); 
        }     
        else if (caracter == 'd')
        {
          avanzar(); 
        }   
        else if (caracter == 'e')
        {
          girar_derecha();
        } 
        else if (caracter == 'f')
        {
          retroceder();
        }                                  
        else if (caracter == '0')
        {
          expresion(0);  
        }               
        else
        {
          analogWrite(RGB_AZUL, 0);
          digitalWrite(RGB_ROJO, LOW);
          digitalWrite(RGB_VERDE, HIGH);           
        }       
    }
}

void expresion(int act)
{
  int r = 10, i = 0, j= 0, k = 0;

  unsigned long color, color2;
  
  if (act == 1)
  {
    color  = NEGRO;
    color2 = CIELO;  
  }
  else if (act == 2)
  {
    color2 = NEGRO;
    color  = CIELO;  
  }
  else if (act == 3)
  {
    color2 = AZUL;
    color  = CIELO;  
  }
  else if (act == 4)
  {
    color   = AZUL;
    color2  = CIELO;  
  }
  else
  {
    color2 = CIELO;
    color  = CIELO;   
  }
  

  for(i = r; i < lcd.Get_Display_Width() / 4; i += 2 * r)
  { 
    for(j= r; j < lcd.Get_Display_Height() / 5; j += 2 * r)
    {    
      if (k == 1 or k == 2 or k == 4 or k == 7)
      {
        lcd.Set_Draw_color(color);
      }
      else
      {
        lcd.Set_Draw_color(color2);
      }
        
      lcd.Fill_Circle(i + 120, j + 120, r);
      
      k++;
    }
  }
}

void ojos(int act)
{
  int r = 25, r2 = 15, i = 0, j= 0;

  lcd.Set_Draw_color(CIELO);
  lcd.Fill_Circle((i + r) + 80,  (j  + r) + 40, r);
  lcd.Fill_Circle((i + r) + 190, (j  + r) + 40, r);
  
  lcd.Set_Draw_color(AZUL);
  
  if (act == 2)
  {
    lcd.Fill_Circle((i + r2) + 90,  (j  + r2) + 60, r2);
    lcd.Fill_Circle((i + r2) + 200,  (j  + r2) + 60, r2);    
  }
  else
  {
    lcd.Fill_Circle((i + r2) + 90,  (j  + r2) + 50, r2);
    lcd.Fill_Circle((i + r2) + 200,  (j  + r2) + 50, r2);  
  }

}

void mover_abajo(Servo servo)
{
  servo.write(120); //160
}

void mover_arriba(Servo servo)
{
  servo.write(60); //5
}

void mover_centro(Servo servo)
{
  servo.write(93);
}


void avanzar()
{
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);

  analogWrite(ENA, 200);
  analogWrite(ENB, 200);

  delay(1000);
  
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);

}

void girar_derecha()
{
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);

  analogWrite(ENA, 200);
  analogWrite(ENB, 200);

  delay(1000);

  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);

}

void girar_izquierda()
{
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);

  analogWrite(ENA, 200);
  analogWrite(ENB, 200);

  delay(1000);

  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);

}

void retroceder()
{
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);

  analogWrite(ENA, 200);
  analogWrite(ENB, 200);

  delay(1000);

  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);

}
