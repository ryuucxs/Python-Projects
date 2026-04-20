const int hallPin = 2; // Hall-Sensor an Digital-Pin 2 (Interrupt-fähig)
volatile unsigned long pulseCount = 0;
unsigned long lastTime = 0;
const unsigned long interval = 1000; // Alle 1 Sekunde senden

void hallISR() {
  pulseCount++;
}

void setup() {
  Serial.begin(9600);
  pinMode(hallPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(hallPin), hallISR, FALLING);
}

void loop() {
  unsigned long now = millis();
  if (now - lastTime >= interval) {
    noInterrupts();
    unsigned long count = pulseCount;
    pulseCount = 0;
    interrupts();

    // RPM berechnen (1 Magnet = 1 Impuls pro Umdrehung)
    float rpm = count * 60.0; // count pro Sekunde * 60

    Serial.print(now);
    Serial.print(",");
    Serial.println(rpm);

    lastTime = now;
  }
}