# IOTSL---Air-quality

 Dispositivo coleta dados da qualidade do ar, como níveis de CO₂, PM2.5, temperatura e umidade.


É recomendável uma rede de dispositivos distribuídos para capturar os dados com perímetro maior.

![radar](radar.png)


# Configurações

- Raspberry Pi Zero W

  
Ativar o SSH para acessar remotamente e instalar Raspberry Pi OS Lite para reconhecimento do dispositivo.

![image](https://github.com/user-attachments/assets/a227e28e-edc2-457a-a4ca-d7c33ee42139)

--------------------------------------------------------------------------------

**TERMINAL**

sudo apt update

sudo apt install python3 python3-pip

pip3 install paho-mqtt Adafruit_DHT pyserial

---------------------------------------------------------------------------------

# SENSORES

Sensor MQ135 (CO₂ e qualidade do ar)

![mq135](mq135.png)

Sensor SDS011 (PM2.5) - Leitura de partículas inferiores a 2,5 micrômetros.

![sds011](sds011.png)

Sensor DHT22 (Temperatura e umidade)

![dh22](dh22.png)

Sensor MQTT - Envio de dados

![mqqtt](mqtt.png)

![image](https://github.com/user-attachments/assets/7e0dd001-51df-498b-bbdd-6a974b73a845)


---------------------------------------------------------------------------------
# Interface > sem dados reais

![image](https://github.com/user-attachments/assets/9cee7216-6cff-432b-90b9-262b0cbf38fb)

---------------------------------------------------------------------------------
**Google**

![image](https://github.com/user-attachments/assets/10c79828-cedb-401e-89b5-0619a6d5795c)


**MIT LICENCE ©**
