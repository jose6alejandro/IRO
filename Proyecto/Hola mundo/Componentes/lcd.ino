// Hola mundo, LCD 2.8 ILI9341

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

LCDWIKI_SPI mylcd(MODEL,CS,CD,MISO,MOSI,RST,SCK,LED); //width,height,cs,dc,miso,mosi,reset,sck,led

#define BLACK   0x0000
#define CYAN    0x07FF

void setup() 
{
  mylcd.Init_LCD();
  mylcd.Set_Rotation(3);
  mylcd.Fill_Screen(BLACK);
}

void loop() 
{
  mylcd.Set_Text_Mode(0);
  mylcd.Fill_Screen(CYAN);
  mylcd.Set_Text_Back_colour(CYAN);
  //mylcd.Set_Text_colour(0, 250, 0);
  mylcd.Set_Text_colour(BLACK);
  mylcd.Set_Text_Size(5);
  mylcd.Print_String("Hola Mundo!", 0, 120);
  delay(5000);

}
