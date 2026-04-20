import serial
import csv
import time
from datetime import datetime

# === Konfiguration ===
PORT = "COM3"           # Windows: "COM3", Linux: "/dev/ttyUSB0", Mac: "/dev/tty.usbmodem..."
BAUD = 9600
RAD_UMFANG_M = 1.5      # Umfang des Schwungrads/Rads in Metern – anpassen!
OUTPUT_FILE = f"ergometer_{datetime.now():%Y%m%d_%H%M%S}.csv"

def main():
    ser = serial.Serial(PORT, BAUD, timeout=2)
    time.sleep(2)  # Arduino-Reset abwarten

    total_distance = 0.0

    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Zeitstempel", "Arduino_ms", "RPM", "Geschwindigkeit_kmh", "Distanz_gesamt_km"])

        print(f"Aufzeichnung gestartet → {OUTPUT_FILE}")
        print("Strg+C zum Beenden\n")

        try:
            while True:
                line = ser.readline().decode("utf-8").strip()
                if not line or "," not in line:
                    continue

                parts = line.split(",")
                arduino_ms = int(parts[0])
                rpm = float(parts[1])

                # Geschwindigkeit berechnen
                speed_ms = (rpm * RAD_UMFANG_M) / 60.0
                speed_kmh = speed_ms * 3.6

                # Distanz aufaddieren (1 Sekunde Intervall)
                total_distance += speed_ms / 1000.0  # in km

                timestamp = datetime.now().isoformat()

                writer.writerow([timestamp, arduino_ms, f"{rpm:.1f}", f"{speed_kmh:.2f}", f"{total_distance:.4f}"])
                f.flush()

                print(f"RPM: {rpm:6.1f} | {speed_kmh:5.1f} km/h | Distanz: {total_distance:.3f} km", end="\r")

        except KeyboardInterrupt:
            print(f"\n\nAufzeichnung beendet. {OUTPUT_FILE} gespeichert.")
        finally:
            ser.close()

if __name__ == "__main__":
    main()
