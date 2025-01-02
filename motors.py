# Klasse für die Ansteuerung beider Motoren des Rovers

# Import für Hardware Pins
from machine import Pin, PWM
# Import der sleep Funktion
from time import sleep

class Motors:
    # Konstruktor: Die beiden Pins müssen übergeben werden
    def __init__(self, left_motor_pin_nb, right_motor_pin_nb):
        self.left_motor_pin_nb = left_motor_pin_nb
        self.right_motor_pin_nb = right_motor_pin_nb
        # Für jeden Motor muss ein PWM Objekt instantiiert werden
        self.pwmLeft = PWM(Pin(self.left_motor_pin_nb), duty_u16=0)
        self.pwmRight = PWM(Pin(self.right_motor_pin_nb), duty_u16=0)
        print("Motor initialized")

    # Hilfsfunktion für die Limitierung eines PWM Wertes auf 0...65535
    @staticmethod
    def limit_value(raw_value):
        return max(min(raw_value, 65535), 0)

    # Geradeausfahrt mit bestimmter PWM (0...100) und Dauer
    def drive_straight(self, pwm, duration):
        self.pwmLeft.duty_u16(Motors.limit_value(int(pwm*65535/100)))
        self.pwmRight.duty_u16(Motors.limit_value(int(pwm*65535/100)))
        sleep(duration)
        

    # Linksdrehung mit bestimmter PWM (0...100) und Dauer
    def turn_left(self, pwm, duration):
        self.pwmLeft.duty_u16(40)
        self.pwmRight.duty_u16(Motors.limit_value(int(pwm*65535/100)))
        sleep(duration)

    # Rechtsdrehung mit bestimmter PWM (0...100) und Dauer
    def turn_right(self, pwm, duration):
        self.pwmLeft.duty_u16(Motors.limit_value(int(pwm*65535/100)))
        self.pwmRight.duty_u16(40)
        sleep(duration)
        
