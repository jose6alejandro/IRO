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
#define RGB_AZUL  3
#define RGB_ROJO  4

LCDWIKI_SPI lcd(MODEL,CS,CD,MISO,MOSI,RST,SCK,LED);

#define NEGRO     0x0000
#define AZUL      0xF800
#define CIELO     0xE302 
#define ROJO      0x001F
#define VERDE     0x07E0
#define BLANCO    0xFFFF

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

void setup() 
{

    Serial.begin(9600);
    
    lcd.Init_LCD();
    lcd.Set_Rotation(3);
    lcd.Fill_Screen(0, 0, 0);
    
    ojos(0);
    expresion(0);
    
    analogWrite(RGB_AZUL, 0);
    digitalWrite(RGB_ROJO, LOW);
    digitalWrite(RGB_VERDE, HIGH);

}

void loop() 
{

    if(Serial.available() > 0) // existe un dato de lectura
    {
        char caracter = Serial.read();
        
        if(caracter == 'u')
        {
            analogWrite(RGB_AZUL, 0);
            digitalWrite(RGB_ROJO, HIGH);
            digitalWrite(RGB_VERDE, LOW);
            expresion(3);

        }
        else if(caracter == 'd')
        {
            analogWrite(RGB_AZUL, 0);
            digitalWrite(RGB_ROJO, HIGH);
            digitalWrite(RGB_VERDE, LOW);
            expresion(4);

        }
        else
        {
            analogWrite(RGB_AZUL, 0);
            digitalWrite(RGB_ROJO, LOW);
            digitalWrite(RGB_VERDE, HIGH); 
            expresion(0);         
          
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
