import Adafruit_DHT
# conectar dht22 ao gpio
sensor = Adafruit_DHT.DHT22
pin = 4  # pino GPIO conectado
umidade, temperatura = Adafruit_DHT.read_retry(sensor, pin)
