# Smart-Barrier-System-Project
This project simulates a smart automatic barrier system using a Raspberry Pi Pico, an ultrasonic distance sensor (HC-SR04), and a servo motor, programmed in MicroPython. The system continuously measures the distance
in front of the barrier. When an object (such as a car) is detected within 10 cm, the barrier is raised by rotating the servo motor. If no object is detected afterward, the barrier automatically returns to its
initial position after 3 seconds. If the object is still present, the system waits and rechecks until the path is clear.

The project demonstrates several key embedded systems concepts:
Reading distance via ultrasonic pulses
Generating PWM signals for servo control
Implementing event-based logic in real-time
Interfacing multiple hardware components
