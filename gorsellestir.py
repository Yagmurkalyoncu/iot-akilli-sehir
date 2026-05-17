import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random
from sensor_simulatoru import SENSORLAR, veri_uret

# 10 tur veri topla
trafik_yogunluk = []
cevre_sicaklik = []
cevre_gurultu = []
lamba_enerji = []
zamanlar = []

for i in range(10):
    zamanlar.append(f"T{i+1}")
    for sensor in SENSORLAR:
        veri = veri_uret(sensor)
        if sensor["tip"] == "trafik" and sensor["id"] == "trafik-001":
            trafik_yogunluk.append(veri["olcum"]["yogunluk_yuzde"])
        elif sensor["tip"] == "cevre" and sensor["id"] == "cevre-001":
            cevre_sicaklik.append(veri["olcum"]["sicaklik_c"])
            cevre_gurultu.append(veri["olcum"]["gurultu_db"])
        elif sensor["tip"] == "sokak_lambasi":
            lamba_enerji.append(veri["olcum"]["enerji_tuketim_w"])

fig, axlar = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Akıllı Şehir IoT Sensör Dashboard", fontsize=16, fontweight="bold")

# Trafik yoğunluğu
axlar[0,0].plot(zamanlar, trafik_yogunluk, color="#e74c3c", marker="o", linewidth=2)
axlar[0,0].fill_between(range(len(zamanlar)), trafik_yogunluk, alpha=0.3, color="#e74c3c")
axlar[0,0].set_title("Trafik Yoğunluğu - Atatürk Bulvarı")
axlar[0,0].set_ylabel("Yoğunluk (%)")
axlar[0,0].set_ylim(0, 100)
axlar[0,0].grid(True, alpha=0.3)

# Sıcaklık
axlar[0,1].plot(zamanlar, cevre_sicaklik, color="#3498db", marker="s", linewidth=2)
axlar[0,1].fill_between(range(len(zamanlar)), cevre_sicaklik, alpha=0.3, color="#3498db")
axlar[0,1].set_title("Sıcaklık - Merkez Park")
axlar[0,1].set_ylabel("Sıcaklık (°C)")
axlar[0,1].grid(True, alpha=0.3)

# Gürültü
axlar[1,0].bar(zamanlar, cevre_gurultu, color="#2ecc71", alpha=0.8)
axlar[1,0].axhline(y=65, color="red", linestyle="--", label="Limit (65 dB)")
axlar[1,0].set_title("Gürültü Seviyesi - Merkez Park")
axlar[1,0].set_ylabel("Gürültü (dB)")
axlar[1,0].legend()
axlar[1,0].grid(True, alpha=0.3)

# Sokak lambası enerji
axlar[1,1].bar(zamanlar, lamba_enerji, color="#f39c12", alpha=0.8)
axlar[1,1].set_title("Sokak Lambası Enerji Tüketimi")
axlar[1,1].set_ylabel("Enerji (W)")
axlar[1,1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("sensor_dashboard.png", dpi=150, bbox_inches="tight")
plt.show()
print("Dashboard kaydedildi: sensor_dashboard.png")