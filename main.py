from machine import Pin, ADC
from time import sleep
import motors

#pins motoren
startbutton=17
motorlinks=14
motorrechts=27
Abstandsensor = ADC(Pin(36))
Abstandsensor.atten(ADC.ATTN_11DB)
links_helligkeit=ADC(Pin(35))
rechts_helligkeit=ADC(Pin(34))
rechtsstartbtn= 16
motors_obj = motors.Motors(motorlinks,motorrechts)
leuchte = Pin(2, Pin.OUT)

links_helligkeit.atten(ADC.ATTN_11DB)
rechts_helligkeit.atten(ADC.ATTN_11DB)
rechtsstartbtn= Pin(rechtsstartbtn,Pin.IN)
startbutton = Pin(startbutton, Pin.IN)
while True:
    if rechtsstartbtn.value():
        while True:
            linksmessung=links_helligkeit.read_uv() / 1e6
            rechtsmessung=rechts_helligkeit.read_uv() / 1e6
            summe=rechtsmessung+linksmessung
            pwm=100
            voltage = Abstandsensor.read_uv() / 1e6
            print(f"Spannung Abstandssensor: {voltage} V")
            sleep(0.0025)
            print(rechtsmessung,linksmessung)
            motors_obj.drive_straight(50,0.1)
            if voltage > 1.9:
                motors_obj.drive_straight(0,0)
                leuchte2 = not leuchte.value()
                leuchte.value(leuchte2)
                sleep(1.5)
                leuchte.value(not leuchte2)
                print('es ist ein hindernis im weg')
                break
            if rechtsmessung > 1.5 and linksmessung < 0.5:
                motors_obj.drive_straight(50,0.1)
            if linksmessung < 0.5 and rechtsmessung < 1.2 :
                motors_obj.turn_right (100,0.1)
            if linksmessung > 0.5:
                motors_obj.turn_left(100,0.1)
           
              
        
        