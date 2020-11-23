import machine, time
import bme280, ssd1306

ENABLE_OLED = True

def main():
    while True:
        show()
        time.sleep_ms(1000)

def show():
    print("T=" + bme.values[0])     # temperature
    print("P=" + bme.values[1])     # pressure
    print("H=" + bme.values[2])     # humidity

    if ENABLE_OLED == True:
        oled.fill(0)
        oled.text("[air]", 0, 0)
        oled.text("T=" + bme.values[0],  0, 10)             # temperature
        oled.text("P=" + bme.values[1],  0, 20)             # pressure
        oled.text("H=" + bme.values[2], 64, 10)             # humidity
        oled.show()

if __name__ == "__main__":

    i2c = machine.I2C(scl=machine.Pin(26), sda=machine.Pin(25))
    bme = bme280.BME280(i2c=i2c)

    if ENABLE_OLED == True:
        i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
        oled = ssd1306.SSD1306_I2C(width=128, height=64, i2c=i2c)

    main()
