// Expresiones del Robot

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
  lcd.Init_LCD();
  lcd.Set_Rotation(3);
  lcd.Fill_Screen(NEGRO);
  
  ojos(0);
  expresion(0);
  delay(3000);

  expresion(1);
  delay(3000);
  
  ojos(2);
  expresion(2);
  delay(3000);

  ojos(1);
  
  for(int i = 0; i < 10; i++)
  {
    expresion(3);
    expresion(4);    
  }

  expresion(0);
}

void loop()
{   
  
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
