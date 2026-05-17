import boto3
import json
import uuid
from datetime import datetime
from sensor_simulatoru import SENSORLAR, veri_uret

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Tablo oluştur
try:
    tablo = dynamodb.create_table(
        TableName='iot-sensor-verileri',
        KeySchema=[{'AttributeName': 'kayit_id', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'kayit_id', 'AttributeType': 'S'}],
        BillingMode='PAY_PER_REQUEST'
    )
    tablo.wait_until_exists()
    print("DynamoDB tablosu oluşturuldu!")
except:
    tablo = dynamodb.Table('iot-sensor-verileri')
    print("Mevcut tablo kullanılıyor.")

# Sensör verilerini kaydet
print("\nSensör verileri DynamoDB'ye kaydediliyor...\n")

for sensor in SENSORLAR:
    veri = veri_uret(sensor)
    tablo.put_item(Item={
        'kayit_id': str(uuid.uuid4()),
        'sensor_id': veri['sensor_id'],
        'konum': veri['konum'],
        'tip': veri['tip'],
        'olcum': json.dumps(veri['olcum'], ensure_ascii=False),
        'zaman': veri['zaman']
    })
    print(f"Kaydedildi: {veri['sensor_id']} - {veri['konum']}")

print("\nTüm veriler DynamoDB'ye kaydedildi!")