#include <Arduino.h>

int led = 13;

void setup() 
{
    Serial.begin(9600);
    pinMode(led,OUTPUT);
}

void loop() 
{

    if(Serial.available() > 0) // existe un dato de lectura
    {
        char caracter = Serial.read();

        if(caracter == 'r')
        {
            digitalWrite(led, HIGH);
        }
        else
        {
            digitalWrite(led, LOW);
        }
    }
}
