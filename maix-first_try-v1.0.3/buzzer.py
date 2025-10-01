from maix import gpio, pinmap, time

pinmap.set_pin_function("A29", "GPIOA29")
led = gpio.GPIO("GPIOA29", gpio.Mode.OUT)
led.value(0)
# led.value(1)
# time.sleep_ms(2500)
# led.value(0)
# while 1:
#     led.toggle()
#     time.sleep_ms(500)

def open_buzzer(time):
    """Open buzzer."""
    in_time=int(time/100)
    in_time=in_time%2
    led.value(in_time)
def close_buzzer():
    """Close buzzer."""
    led.value(0)