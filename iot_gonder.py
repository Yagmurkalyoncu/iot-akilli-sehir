
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import time
from sensor_simulatoru import SENSORLAR, veri_uret

ENDPOINT = "ancwl30g7kwdm-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "akilli-sehir-sensor"
CERT_PATH = "cd1ba05740b02aa43707494f24536cd27d72a549bb369dddde4124660d326def-certificate.pem.crt"
KEY_PATH = "cd1ba05740b02aa43707494f24536cd27d72a549bb369dddde4124660d326def-private.pem.key"
ROOT_CA = "AmazonRootCA1.pem"
TOPIC = "akilli-sehir/sensor-verisi"

client = AWSIoTMQTTClient(CLIENT_ID)
client.configureEndpoint(ENDPOINT, 8883)
client.configureCredentials(ROOT_CA, KEY_PATH, CERT_PATH)
client.configureAutoReconnectBackoffTime(1, 32, 20)
client.configureOfflinePublishQueueing(-1)
client.configureDrainingFrequency(2)
client.configureConnectDisconnectTimeout(10)
client.configureMQTTOperationTimeout(5)

print("AWS IoT Core'a bağlanılıyor...")
client.connect()
print("Bağlantı başarılı!\n")

for i in range(3):
    print(f"--- Tur {i+1} ---")
    for sensor in SENSORLAR:
        veri = veri_uret(sensor)
        mesaj = json.dumps(veri, ensure_ascii=False)
        client.publish(TOPIC, mesaj, 1)
        print(f"Gönderildi: {sensor['id']} - {sensor['konum']}")
        time.sleep(1)
    print()

client.disconnect()
print("Tüm veriler AWS IoT Core'a gönderildi!")