import Adafruit_BBIO.ADC as ADC
import csv
import time

ADC.setup()
analogPin = "P9_40"
bus = "/sys/bus/w1/devices/28-00000bc43f6b/w1_slave"

# Liste med puls resultateter
pulseList = []

#Liste med temperatur resultater
tempList = []

# Uendelig løkke. Må stoppes av bruker
while True:

    #Leser inn pulsen fra P9_40
    pulse = ADC.read(analogPin) * 60

    #Leser inn temperaturen fra BUSen
    temp = open(bus, "r").read()
    celsius = float(temp.split("t=")[-1])/1000

    #Venter på at både puls og temp skal leses
    time.sleep(2)

    #Legger pulsen inn i liste
    pulseList.append(pulse)

    #Legger temperaturen inn i liste
    tempList.append(celsius)

    print(pulseList)
    #print(tempList)

    #Åpner en fil og skriver resultatene til denne
    with open("/home/jonas/pulse.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow(pulseList)
        writer.writerow(tempList)

    #Tømmer listene etter hver loop
    pulseList.clear()
    tempList.clear()

    #Skriver ut resultatene til consol
    print ("Puls: ", pulse)
    print("Temperature is {0:.2f} degrees".format(celsius))

    # Lukker filen
    file.close()










