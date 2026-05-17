# 🏙️ IoT ve Akıllı Şehir Uygulaması

**3522 Bulut Bilişim Dersi — Proje 7**

---

## Proje Hakkında

AWS IoT Core ve MQTT protokolü kullanarak akıllı şehir sensörlerinden gerçek zamanlı veri toplayan ve analiz eden bir bulut uygulamasıdır.

## Kullanılan Teknolojiler

- **Python 3.11** — Ana programlama dili
- **AWS IoT Core** — MQTT mesajlaşma ve cihaz yönetimi
- **AWS DynamoDB** — Sensör verilerinin saklanması
- **MQTT** — IoT mesajlaşma protokolü (Port 8883)
- **Matplotlib** — Veri görselleştirme

## Sensörler

| Sensör | Konum | Ölçüm |
|--------|-------|-------|
| trafik-001 | Atatürk Bulvarı | Araç sayısı, yoğunluk |
| trafik-002 | Cumhuriyet Caddesi | Araç sayısı, yoğunluk |
| cevre-001 | Merkez Park | Sıcaklık, nem, gürültü |
| cevre-002 | Sanayi Bölgesi | Sıcaklık, nem, gürültü |
| lamba-001 | Ana Cadde | Enerji tüketimi, durum |

## Dosyalar

- `sensor_simulatoru.py` — IoT sensör simülatörü
- `iot_gonder.py` — AWS IoT Core MQTT bağlantısı
- `dynamodb_kaydet.py` — DynamoDB entegrasyonu
- `gorsellestir.py` — Dashboard görselleştirme

## Çalıştırma

```bash
pip install AWSIoTPythonSDK boto3 matplotlib

python sensor_simulatoru.py   # Sensör verisi üret
python iot_gonder.py          # AWS IoT Core'a gönder
python dynamodb_kaydet.py     # DynamoDB'ye kaydet
python gorsellestir.py        # Dashboard oluştur
```

## GitHub

https://github.com/Yagmurkalyoncu/iot-akilli-sehir

---

*Yağmur Kalyoncu — Mayıs 2026*
