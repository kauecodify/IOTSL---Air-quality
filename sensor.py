def atualizar_dados():
    # leituras reais dos sensores
    temperatura, umidade = Adafruit_DHT.read_retry(sensor, pin)
    pm2_5 = ler_sds011()
    
    if temperatura is None or umidade is None or pm2_5 is None:
        return  

    status, cor = avaliar_qualidade_ar(pm2_5)
    
    # labels
    label_temperatura.config(text=f"Temperatura: {temperatura:.1f} °C")
    label_umidade.config(text=f"Umidade: {umidade:.1f} %")
    label_pm2_5.config(text=f"PM2.5: {pm2_5} µg/m³")
    label_status.config(text=f"Qualidade do Ar: {status}", bg=cor)
    
    # envia dados via MQTT
    enviar_dados(temperatura, umidade, pm2_5)
    
    # atualização em 3seg
    root.after(3000, atualizar_dados)
