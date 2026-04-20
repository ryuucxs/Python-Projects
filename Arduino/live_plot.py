import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

PORT = "COM3"
BAUD = 9600

ser = serial.Serial(PORT, BAUD, timeout=2)
import time; time.sleep(2)

rpm_data = deque(maxlen=120)  # Letzte 2 Minuten

fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_ylim(0, 150)
ax.set_ylabel("RPM")
ax.set_xlabel("Sekunden")
ax.set_title("Ergometer Live")

def update(frame):
    raw = ser.readline().decode("utf-8").strip()
    if raw and "," in raw:
        rpm = float(raw.split(",")[1])
        rpm_data.append(rpm)
    line.set_data(range(len(rpm_data)), list(rpm_data))
    ax.set_xlim(0, max(len(rpm_data), 60))
    return line,

ani = animation.FuncAnimation(fig, update, interval=1000)
plt.show()
ser.close()
