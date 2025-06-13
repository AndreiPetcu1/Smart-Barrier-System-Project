from machine import Pin, PWM, time_pulse_us
from time import sleep

servo = PWM(Pin(16))
servo.freq(50)

trig = Pin(17, Pin.OUT)
echo = Pin(18, Pin.IN)

def opreste():
    servo.duty_u16(4800)
    sleep(0.1)
    servo.deinit()

def misca_90_grade():
    servo.duty_u16(3000)
    sleep(0.165)
    opreste()

def revino_la_start():
    global servo
    servo = PWM(Pin(16))
    servo.freq(50)
    servo.duty_u16(7000)
    sleep(0.16)
    servo.duty_u16(4800)
    sleep(0.1)
    servo.deinit()

def masoara_distantă():
    trig.low()
    sleep(0.002)
    trig.high()
    sleep(0.00001)
    trig.low()

    durata = time_pulse_us(echo, 1, 30000)
    distanta_cm = (durata / 2) / 29.1
    return distanta_cm

while True:
    dist = masoara_distantă()
    print("Distanta:", dist, "cm")
    if dist < 10:
        print("🚗 Mașină detectată! Ridic bariera...")
        misca_90_grade()
        sleep(3)
        
        # Așteptăm până nu mai e nicio mașină sub barieră
        while True:
            dist_noua = masoara_distantă()
            print("Verific din nou distanța:", dist_noua, "cm")
            if dist_noua > 10:
                print("✅ Mașina a trecut. Cobor bariera.")
                revino_la_start()
                break
            else:
                print("⛔ Mașina încă e acolo! Aștept...")
                sleep(1)

