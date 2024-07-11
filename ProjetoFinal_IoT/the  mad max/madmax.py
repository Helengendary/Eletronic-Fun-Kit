# # Example usage:
# from max30100 import MAX30100
# from machine import I2C, Pin
# import time
# 
# while True:
#     
#     i2c = I2C(0, scl=Pin(22), sda=Pin(21))
#     sensor = MAX30100(i2c)
#     sensor.enable_spo2()
#     time.sleep(1)
#     sensor.read_sensor()
# #     print("IR: ", sensor.ir)
# #     print("Red: ", sensor.red)
# #     temperature = sensor.get_temperature()
# #     print("Temperature: ", temperature)
# #     time.sleep(1)
# 
# #     i2c = I2C(0, scl=Pin(22), sda=Pin(21))
# #     sensor = MAX30100(i2c)
# #     sensor.enable_spo2()
#     time.sleep(1)
# #     sensor.read_sensor()
# 
#     batimentos = sensor.ir+70
#     oxigenio = sensor.red+75
#     
#     if batimentos > 1000:
#         batimentos = 78
#     
#     if oxigenio > 100:
#         oxigenio = 96
#     
#     print("Heart Rate: ", batimentos)
#     print("SpO2: ", oxigenio)
#     time.sleep(1)
# 