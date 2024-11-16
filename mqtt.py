import paho.mqtt.client as mqtt

def enviar_dados(temperatura, umidade, pm2_5):
    client = mqtt.Client()
    client.connect("broker.emqx.io", 1883, 60)  # realbroker
    payload = {
        "temperatura": temperatura,
        "umidade": umidade,
        "pm2_5": pm2_5
    }
    client.publish("iot/qualidade_ar", str(payload))
    client.disconnect()
