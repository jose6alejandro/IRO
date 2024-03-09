// Hola mundo, Led RGB 

// Pines 5 y 6 se invierten aquí

#define RGB_GREEN 3
#define RGB_BLUE 6
#define RGB_RED 5

// Tiempo de espera

#define TIME 2000

void setup() 
{
  pinMode(RGB_RED, OUTPUT);
  pinMode(RGB_GREEN, OUTPUT);
  pinMode(RGB_BLUE, OUTPUT);
}


void loop() 
{

  // Verde
  digitalWrite(RGB_GREEN, HIGH); 
  delay(TIME);
  
  // Amarillo (255, 255, 0)

  digitalWrite(RGB_RED, HIGH);
  digitalWrite(RGB_BLUE, LOW);
  delay(TIME); 
  
  // Rojo
  digitalWrite(RGB_GREEN, LOW);
  digitalWrite(RGB_RED, HIGH);
  delay(TIME);
  
  /* Color especifico 
  analogWrite(RGB_RED,102);
  analogWrite(RGB_GREEN,204);
  analogWrite(RGB_BLUE,0);
  delay(TIME);
  */
  
  digitalWrite(RGB_GREEN, LOW);
  digitalWrite(RGB_BLUE, LOW);
  digitalWrite(RGB_RED, LOW);
 
 
}