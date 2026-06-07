const int stepPins[3] = {2, 3, 4};
const int dirPins[3]  = {5, 6, 7};
const int enPin = 8;

void stepMotor(int m, long steps) {
  if (steps == 0) return;

  digitalWrite(enPin, LOW);
  digitalWrite(dirPins[m], steps > 0);

  long s = labs(steps);
  for (long i = 0; i < s; i++) {
    digitalWrite(stepPins[m], HIGH);
    delayMicroseconds(800);
    digitalWrite(stepPins[m], LOW);
    delayMicroseconds(800);
  }
}

String line;

void setup() {
  Serial.begin(115200);
  for (int i = 0; i < 3; i++) {
    pinMode(stepPins[i], OUTPUT);
    pinMode(dirPins[i], OUTPUT);
  }
  pinMode(enPin, OUTPUT);
  digitalWrite(enPin, LOW);
}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '\n') {
      int m;
      long steps;
      sscanf(line.c_str(), "%d %ld", &m, &steps);
      if (m >= 0 && m < 3) stepMotor(m, steps);
      line = "";
    } else {
      line += c;
    }
  }
}
