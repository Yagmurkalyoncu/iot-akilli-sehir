import random
import json
from datetime import datetime

SENSORLAR = [
    {"id": "trafik-001", "konum": "Atatürk Bulvarı", "tip": "trafik"},
    {"id": "trafik-002", "konum": "Cumhuriyet Caddesi", "tip": "trafik"},
    {"id": "cevre-001", "konum": "Merkez Park", "tip": "cevre"},
    {"id": "cevre-002", "konum": "Sanayi Bölgesi", "tip": "cevre"},
    {"id": "lamba-001", "konum": "Ana Cadde", "tip": "sokak_lambasi"},
]

def trafik_verisi():
    yogunluk = random.randint(0, 100)
    if yogunluk < 30:
        durum = "Akıcı"
    elif yogunluk < 70:
        durum = "Orta"
    else:
        durum = "Yoğun"
    return {
        "arac_sayisi": random.randint(0, 500),
        "yogunluk_yuzde": yogunluk,
        "durum": durum,
        "ortalama_hiz_kmh": random.randint(10, 90)
    }

def cevre_verisi():
    return {
        "sicaklik_c": round(random.uniform(5, 40), 1),
        "nem_yuzde": round(random.uniform(20, 90), 1),
        "gurultu_db": round(random.uniform(30, 90), 1),
        "hava_kalitesi": random.randint(0, 300)
    }

def lamba_verisi():
    return {
        "durum": random.choice(["Açık", "Kapalı", "Arızalı"]),
        "enerji_tuketim_w": random.randint(0, 150),
        "parlaklık_yuzde": random.randint(0, 100)
    }

def veri_uret(sensor):
    if sensor["tip"] == "trafik":
        olcum = trafik_verisi()
    elif sensor["tip"] == "cevre":
        olcum = cevre_verisi()
    else:
        olcum = lamba_verisi()

    return {
        "sensor_id": sensor["id"],
        "konum": sensor["konum"],
        "tip": sensor["tip"],
        "olcum": olcum,
        "zaman": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__ == "__main__":
    print("=== Akıllı Şehir IoT Sensör Simülatörü ===\n")
    tum_veriler = []
    for sensor in SENSORLAR:
        veri = veri_uret(sensor)
        tum_veriler.append(veri)
        print(json.dumps(veri, ensure_ascii=False, indent=2))
        print("-" * 40)
    print(f"\nToplam {len(tum_veriler)} sensörden veri toplandı!")