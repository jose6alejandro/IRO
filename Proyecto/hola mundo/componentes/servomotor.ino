// Hola mundo, servomotor

#include <Servo.h>

Servo myservo;
int pos = 0;

void setup()
{
    myservo.attach(3);
}

void loop()
{
    for(pos = 0; pos < 90; pos += 1)
    {
        myservo.write(pos);
        delay(15);
    }
    
    for(pos = 90; pos>=1; pos-=1)
    {
        myservo.write(pos);
        delay(15);
    }
}
/*
#include <Servo.h>

#define TIME 1500

Servo servo_9;  // Declaración de la variable a controlar

void setup()
{
    servo_9.attach(9); // indica el pin a usar
}

void loop()
{
    servo_9.write(0); // indica el angulo al que se de posicionar
    delay(TIME);
  
    servo_9.write(90);
    delay(TIME);
  
    servo_9.write(180);
    delay(TIME);
  
    servo_9.write(90);
    delay(TIME);
}
*/