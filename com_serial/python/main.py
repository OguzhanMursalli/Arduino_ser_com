import serial
import time

ser = serial.Serial("COM9",9600)

try:
    while True:
        if ser.in_waiting > 0:
            veri = ser.readline().decode('utf-8').strip()
            degerler = veri.split("\t")

            if len(degerler) == 2:
                print(f"sistemin çalışma zamanı: {degerler[0]}")
                print(f"girilen deger: {degerler[1]}")

        #time.sleep(0.1)
except KeyboardInterrupt:
    print("Bağlantı sonlandırılıyor.")
finally:
    ser.close()