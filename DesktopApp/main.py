import serial

if __name__ == '__main__':
    driver = serial.SerialDriver("serialdrv/serdrv")
    o_list = ["emo", "e", "totalen", "pederast"]
    driver.out(o_list)
